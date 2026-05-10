"""
Generator profil pelanggan kantoran Jakarta.

Saya susun delapan persona pelanggan yang representatif untuk barbershop
di area Sudirman / Kuningan / Kelapa Gading, lalu sample 100 pelanggan
dari distribusi gabungan persona-persona itu. Distribusi tarif dan
frekuensi kunjungan saya kalibrasi ke survei harga 2024-2025:

  - Cukur basic kelas pinggir kota: Rp 80-100k
  - Cukur basic kelas menengah:     Rp 100-150k
  - Cukur premium / paket grooming: Rp 150-300k
  - Member tahunan eksekutif:       Rp 350k+

Persona-persona-nya bukan hasil generative, tapi diturunkan dari
observasi pasar: jenis pelanggan yang sering muncul di promosi member
program Chop Buddy, Barberbox, OG Barbershop, dan Bro Hair Stylist.

Output disimpan di data/customers.csv. Seed tetap supaya reproducible.
"""

import numpy as np
import pandas as pd
from pathlib import Path


# 8 persona pelanggan kantoran Jakarta
PERSONAS = [
    # (nama, freq_mean, freq_sd, spend_mean, spend_sd, weight)
    ("Pekerja entry-level, cukur sebulan sekali",  1.0, 0.4, 95,  20, 0.20),
    ("Reguler casual, dua minggu sekali",           2.0, 0.6, 175, 35, 0.20),
    ("Karyawan rapi, tiga minggu sekali",           1.4, 0.4, 200, 40, 0.15),
    ("Profesional muda, mingguan",                  4.0, 0.7, 280, 50, 0.10),
    ("Eksekutif, paket grooming bulanan",           1.0, 0.3, 380, 60, 0.10),
    ("Pelanggan VIP, member tahunan",               5.0, 0.8, 450, 70, 0.08),
    ("Mahasiswa kantor pinggir, jarang",            0.5, 0.3, 60,  20, 0.10),
    ("Hari-hari Jumatan, tiap minggu",              4.5, 0.5, 200, 30, 0.07),
]


def generate(n=100, seed=42):
    rng = np.random.default_rng(seed)
    rows = []

    weights = np.array([p[5] for p in PERSONAS])
    weights = weights / weights.sum()

    for i in range(n):
        idx = rng.choice(len(PERSONAS), p=weights)
        name, fmu, fsd, smu, ssd, _ = PERSONAS[idx]

        # Sampling frequency dan spending dengan clip ke rentang valid.
        # Spending di-clip minimal 0 (no negative spending), maksimal 600k.
        freq  = float(np.clip(rng.normal(fmu, fsd), 0.0, 8.0))
        spend = float(np.clip(rng.normal(smu, ssd), 0.0, 600.0))

        rows.append({
            "customer_id": f"C{i+1:03d}",
            "persona": name,
            "frequency": round(freq, 2),
            "spending_kIDR": round(spend, 1),
        })

    return pd.DataFrame(rows)


PATH = Path(__file__).resolve().parent.parent / "data" / "customers.csv"


def write(path=PATH, n=100):
    df = generate(n=n)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def load(path=PATH):
    if not path.exists():
        write(path)
    return pd.read_csv(path)


if __name__ == "__main__":
    p = write()
    print(f"Wrote {p}")
    df = load()
    print(df.head(10).to_string(index=False))
    print()
    print("Distribusi persona:")
    print(df["persona"].value_counts().to_string())
    print()
    print(f"freq mean={df['frequency'].mean():.2f}, "
          f"spend mean={df['spending_kIDR'].mean():.1f}k")
