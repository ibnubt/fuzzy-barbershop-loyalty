"""
Baseline: aturan diskon kaku ala loyalty program tradisional.

Dipakai sebagai pembanding visual + numerik terhadap sistem fuzzy.
Argumen utama paper: skema bertingkat punya loncatan tajam di ambang
batas, sedangkan fuzzy menghaluskannya.

Skema yang saya pakai meniru program member yang umum di Jakarta:
- Tingkatan ditentukan max() dari skor frekuensi atau skor spending
- Tiap tingkatan dikasih diskon flat
"""


def traditional_discount(frequency, spending):
    """Hitung diskon ala program member tradisional, tier-based.

    Argumen:
        frequency: kunjungan per bulan
        spending:  spending bulan berjalan dalam ribu Rupiah

    Return:
        diskon (persen, 0-20)
    """
    # Tier per dimensi
    if frequency >= 5 or spending >= 400:
        return 20
    if frequency >= 3 or spending >= 250:
        return 10
    if frequency >= 2 or spending >= 150:
        return 5
    return 0


def traditional_label(percent):
    if percent == 0:
        return "Tidak Ada"
    if percent <= 5:
        return "Bronze"
    if percent <= 10:
        return "Silver"
    return "Gold"


if __name__ == "__main__":
    cases = [
        (1, 90),
        (1, 149),
        (1, 150),     # cliff effect: 0% -> 5%
        (2, 100),
        (2, 249),
        (2, 250),     # cliff effect: 5% -> 10%
        (4, 350),
        (5, 100),     # cliff effect via frequency
        (1, 399),
        (1, 400),     # cliff effect: 5% -> 20% (loncatan ekstrim)
    ]
    for f, s in cases:
        print(f"freq={f}, spend={s}k -> {traditional_discount(f, s)}%")
