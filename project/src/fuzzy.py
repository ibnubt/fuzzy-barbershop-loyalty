"""
Sistem fuzzy untuk rekomendasi diskon loyalti barbershop.

Dua input: frekuensi kunjungan (per bulan) dan total spending bulan
berjalan (ribu rupiah). Satu output: persentase diskon untuk kunjungan
berikutnya, dibatasi 0 - 25%.

Saya pilih trapezoid di pinggir universe supaya pelanggan ekstrim
(misal hampir tidak pernah datang, atau spending sangat tinggi) tetap
kena rule dengan derajat keanggotaan penuh. Yang di tengah pakai
triangular karena overlap-nya lebih simetris.
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Universe semua variabel
FREQ_RANGE = (0, 8, 0.1)        # kunjungan per bulan
SPEND_RANGE = (0, 600, 1)       # ribu Rupiah, total spending bulan ini
DISC_RANGE = (0, 25, 0.1)       # persen diskon


# Anchor MF input - dipilih sesuai pola pekerja kantoran Jakarta:
# - Mayoritas cukur 1x sebulan -> "rare"
# - Yang care soal grooming sekitar 2-3x -> "regular"
# - Eksekutif / orang super rapi 4x+ -> "frequent"
FREQ_ANCHORS = {
    "rare":     [0.0, 0.0, 1.0, 2.5],   # trapmf
    "regular":  [1.5, 3.0, 4.5],        # trimf
    "frequent": [3.5, 5.0, 8.0, 8.0],   # trapmf
}

# Anchor spending dipilih dari survei tarif barbershop Jakarta 2024:
# - Cukur basic di pinggiran 80-100k -> 1-2x sebulan masuk "low"
# - Cukur premium 150k+ atau kombinasi service masuk "medium"
# - Paket grooming komplet beberapa kali masuk "high"
SPEND_ANCHORS = {
    "low":    [0, 0, 100, 175],
    "medium": [125, 225, 350],
    "high":   [275, 400, 600, 600],
}

# Output: 0% sampai 25%. 25% diambil sebagai cap operasional supaya
# margin bisnis (~30-40%) tetap aman.
DISC_ANCHORS = {
    "none":   [0.0, 0.0, 2.0, 5.0],
    "small":  [3.0, 8.0, 13.0],
    "medium": [10.0, 15.0, 20.0],
    "large":  [18.0, 22.0, 25.0, 25.0],
}


# Rule base 3x3. Tabel-nya bisa dibaca:
#   sumbu kiri = frequency, sumbu atas = spending, sel = output diskon.
#
#                low      medium   high
#   rare        none     small    medium
#   regular     small    medium   large
#   frequent    medium   large    large
RULE_TABLE = {
    ("rare",     "low"):    "none",
    ("rare",     "medium"): "small",
    ("rare",     "high"):   "medium",
    ("regular",  "low"):    "small",
    ("regular",  "medium"): "medium",
    ("regular",  "high"):   "large",
    ("frequent", "low"):    "medium",
    ("frequent", "medium"): "large",
    ("frequent", "high"):   "large",
}


def _build_freq(var):
    var["rare"]     = fuzz.trapmf(var.universe, FREQ_ANCHORS["rare"])
    var["regular"]  = fuzz.trimf(var.universe,  FREQ_ANCHORS["regular"])
    var["frequent"] = fuzz.trapmf(var.universe, FREQ_ANCHORS["frequent"])


def _build_spend(var):
    var["low"]    = fuzz.trapmf(var.universe, SPEND_ANCHORS["low"])
    var["medium"] = fuzz.trimf(var.universe,  SPEND_ANCHORS["medium"])
    var["high"]   = fuzz.trapmf(var.universe, SPEND_ANCHORS["high"])


def _build_disc(var):
    var["none"]   = fuzz.trapmf(var.universe, DISC_ANCHORS["none"])
    var["small"]  = fuzz.trimf(var.universe,  DISC_ANCHORS["small"])
    var["medium"] = fuzz.trimf(var.universe,  DISC_ANCHORS["medium"])
    var["large"]  = fuzz.trapmf(var.universe, DISC_ANCHORS["large"])


def build_system():
    """Bangun ControlSystem-nya. Dipanggil sekali, lalu simulator dipakai ulang."""
    freq  = ctrl.Antecedent(np.arange(*FREQ_RANGE),  "frequency")
    spend = ctrl.Antecedent(np.arange(*SPEND_RANGE), "spending")
    disc  = ctrl.Consequent(np.arange(*DISC_RANGE),  "discount",
                            defuzzify_method="centroid")

    _build_freq(freq)
    _build_spend(spend)
    _build_disc(disc)

    rules = []
    for (f_term, s_term), d_term in RULE_TABLE.items():
        rules.append(ctrl.Rule(freq[f_term] & spend[s_term], disc[d_term]))

    return ctrl.ControlSystemSimulation(ctrl.ControlSystem(rules))


# Cache simulator. Bangunan rule graph mahal, sekitar 200 ms; tanpa
# cache, tiap inference jadi lambat di Streamlit.
_simulator = None


def get_simulator():
    global _simulator
    if _simulator is None:
        _simulator = build_system()
    return _simulator


def recommend_discount(frequency, spending):
    """Return diskon yang direkomendasikan dalam persen.

    frequency: kunjungan per bulan (0-8)
    spending:  total bulan ini dalam ribu Rupiah (0-600)
    """
    sim = get_simulator()
    sim.input["frequency"] = float(np.clip(frequency, 0, 8))
    sim.input["spending"]  = float(np.clip(spending, 0, 600))
    sim.compute()
    return round(float(sim.output["discount"]), 2)


def discount_label(percent):
    """Label kategorikal untuk angka diskon, untuk ditampilkan ke UI."""
    if percent < 5:
        return "Tidak Ada"
    if percent < 12:
        return "Kecil"
    if percent < 19:
        return "Sedang"
    return "Besar"


# Helpers untuk plotting MF (dipakai di plots.py dan dashboard)
def freq_curves():
    x = np.arange(*FREQ_RANGE)
    return x, {
        "rare":     fuzz.trapmf(x, FREQ_ANCHORS["rare"]),
        "regular":  fuzz.trimf(x,  FREQ_ANCHORS["regular"]),
        "frequent": fuzz.trapmf(x, FREQ_ANCHORS["frequent"]),
    }


def spend_curves():
    x = np.arange(*SPEND_RANGE)
    return x, {
        "low":    fuzz.trapmf(x, SPEND_ANCHORS["low"]),
        "medium": fuzz.trimf(x,  SPEND_ANCHORS["medium"]),
        "high":   fuzz.trapmf(x, SPEND_ANCHORS["high"]),
    }


def disc_curves():
    x = np.arange(*DISC_RANGE)
    return x, {
        "none":   fuzz.trapmf(x, DISC_ANCHORS["none"]),
        "small":  fuzz.trimf(x,  DISC_ANCHORS["small"]),
        "medium": fuzz.trimf(x,  DISC_ANCHORS["medium"]),
        "large":  fuzz.trapmf(x, DISC_ANCHORS["large"]),
    }


if __name__ == "__main__":
    # Quick sanity check
    cases = [
        ("Pekerja baru, sekali cukur murah", 1, 90),
        ("Reguler casual, dua kali cukur",   2, 180),
        ("Eksekutif, paket grooming",        4, 350),
        ("Premium loyal",                    6, 480),
        ("Pelanggan jarang tapi premium",    1, 350),
    ]
    for name, f, s in cases:
        d = recommend_discount(f, s)
        print(f"{name:40s} freq={f}, spend={s}k -> diskon {d}% ({discount_label(d)})")
