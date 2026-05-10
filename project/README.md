# Fuzzy Loyalty Barbershop Jakarta

Sistem rekomendasi diskon loyalti untuk barbershop di Jakarta.
Pelanggan yang dibidik: pekerja kantoran. Ada dua input — frekuensi
kunjungan per bulan, dan total spending bulan berjalan dalam ribu
Rupiah — dan satu output, persentase diskon untuk kunjungan
berikutnya (0–25%).

## Kenapa fuzzy

Program member tradisional di banyak barbershop pakai aturan kaku:
"≥ 5 kunjungan dapat diskon 20%", "spending ≥ 250k dapat 10%". Pendekatan
ini punya cliff effect — beda Rp 1.000 di sekitar Rp 250.000 bisa
mengubah diskon dari 5% ke 10%, padahal "loyalitas" pelanggan tidak
melompat. Fuzzy logic memberi output yang halus karena membership
function tetangga overlap, dan bisa menggabungkan dua sumbu (frekuensi
dan spending) tanpa harus memilih satu sumbu yang dominan.

Konkretnya, pelanggan yang **jarang datang tapi spending besar** —
contoh: eksekutif yang sebulan sekali ambil paket grooming Rp 350.000 —
di rule kaku cuma dapat 10% (lewat threshold spending). Di fuzzy
sistem ini dia dapat sekitar 15% karena rule "rare AND high → medium"
firing penuh.

## Konteks tarif Jakarta 2024–2025

Range yang dipakai di membership function disesuaikan dengan harga
yang umum di Sudirman, Kuningan, Kelapa Gading:

| Layanan | Tarif | Linguistik di sistem |
|---|---|---|
| Cukur basic kelas pinggir kota | Rp 80–100k | low (1× kunjungan) |
| Cukur basic kelas menengah | Rp 100–150k | low (1× kunjungan) |
| Cukur premium / paket grooming | Rp 150–250k | medium |
| Member tahunan eksekutif | Rp 350k+ | high |

## Struktur folder

```
project/
├── src/
│   ├── fuzzy.py      # core: 9 rules, MFs, inference Mamdani + centroid
│   ├── baseline.py   # rule kaku tier-based untuk pembanding
│   ├── data.py       # generator 100 profil pelanggan kantoran Jakarta
│   └── plots.py      # bikin 6 figure untuk paper
├── app/
│   └── dashboard.py  # Streamlit interaktif
├── tests/
│   └── test_fuzzy.py # 8 pytest cases
├── data/
│   └── customers.csv # dataset (auto-generated, deterministic)
├── notebooks/
│   └── analysis.ipynb
└── figures/          # auto-generated PNGs
```

## Cara jalan

Saya pakai virtual environment dari project sebelumnya via symlink di
`../.venv`. Kalau install dari nol:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Lalu:

```bash
# Generate dataset (sekali)
python -m src.data

# Jalankan dashboard (akan buka browser di localhost:8501)
streamlit run app/dashboard.py

# Tests
pytest tests/

# Regenerate semua figure
python -m src.plots
```

## Rule base

Total 9 aturan, satu sel per kombinasi linguistik:

|              | low (hemat) | medium (standar) | high (premium) |
|--------------|-------------|------------------|----------------|
| **rare**     | none        | small            | medium         |
| **regular**  | small       | medium           | large          |
| **frequent** | medium      | large            | large          |

Inferensi pakai Mamdani (min t-norm, max aggregation). Defuzzifikasi
centroid of area.

## Output yang bisa dilihat

- `figures/mf_inputs.png` — bentuk MF frekuensi & spending
- `figures/mf_output.png` — MF diskon
- `figures/surface.png` — 3D surface diskon (frekuensi × spending)
- `figures/fuzzy_vs_baseline.png` — kurva fuzzy halus vs baseline tangga
- `figures/customer_scatter.png` — 100 pelanggan di plane (freq, spending)
- `figures/disc_distribution.png` — histogram diskon dua metode

## Lisensi

MIT.
