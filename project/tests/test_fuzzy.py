"""
Test untuk sistem fuzzy.

Pendekatan: cek property-property kasar (rentang output, monotonisitas,
beberapa anchor case yang harus masuk akal). Bukan unit-test ketat
karena kita tidak punya ground truth eksak - sistemnya kan untuk
rekomendasi, bukan klasifikasi.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.fuzzy import recommend_discount, discount_label
from src.baseline import traditional_discount
from src.data import load


def test_pelanggan_baru_dapat_diskon_kecil():
    """Frekuensi rendah + spending rendah harus dapat diskon mendekati 0."""
    d = recommend_discount(1, 90)
    assert d <= 5, f"Expected <= 5%, got {d}"


def test_vip_dapat_diskon_besar():
    """Frekuensi tinggi + spending tinggi harus dapat diskon di atas 18%."""
    d = recommend_discount(6, 480)
    assert d >= 18, f"Expected >= 18%, got {d}"
    assert discount_label(d) == "Besar"


def test_output_selalu_dalam_range():
    """Untuk apapun input valid, output harus 0-25%."""
    cases = [(0, 0), (0, 600), (8, 0), (8, 600),
             (4, 200), (2, 350), (1, 100)]
    for f, s in cases:
        d = recommend_discount(f, s)
        assert 0 <= d <= 25, f"Out of range untuk freq={f}, spend={s}: {d}"


def test_monotonik_pada_spending():
    """Naikkan spending sambil tahan frekuensi -> diskon harus tidak turun."""
    freq = 2
    last = -1
    for s in [50, 150, 250, 350, 450, 550]:
        d = recommend_discount(freq, s)
        assert d >= last - 0.5, (
            f"Tidak monoton: spending={s}, diskon={d}, sebelumnya={last}"
        )
        last = d


def test_monotonik_pada_frekuensi():
    """Naikkan frekuensi sambil tahan spending -> diskon harus tidak turun."""
    spend = 200
    last = -1
    for f in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]:
        d = recommend_discount(f, spend)
        assert d >= last - 0.5, (
            f"Tidak monoton: freq={f}, diskon={d}, sebelumnya={last}"
        )
        last = d


def test_pelanggan_jarang_tapi_premium_dapat_diskon_menengah():
    """
    Justifikasi paper: pelanggan yang spending tinggi tapi jarang
    tetap layak dipertahankan. Rule kaku akan kasih 10% di sini
    (lewat threshold spending), fuzzy harus kasih sekitar 12-18%.
    """
    d = recommend_discount(1, 350)
    assert 10 <= d <= 20, f"Expected 10-20%, got {d}"


def test_dataset_tersedia_dan_konsisten():
    """Dataset 100 pelanggan harus ada dan kolomnya benar."""
    df = load()
    assert len(df) == 100
    assert set(df.columns) >= {
        "customer_id", "persona", "frequency", "spending_kIDR"
    }
    assert df["frequency"].between(0, 8).all()
    assert df["spending_kIDR"].between(0, 600).all()


def test_fuzzy_lebih_smooth_dari_baseline_di_threshold():
    """
    Periksa cliff effect baseline. Selisih antara s=149 dan s=150
    pada baseline harus persis 5 (cliff), tapi di fuzzy harus < 1.5.
    """
    f = 1
    base_jump  = traditional_discount(f, 150) - traditional_discount(f, 149)
    fuzzy_jump = recommend_discount(f, 150) - recommend_discount(f, 149)
    assert base_jump == 5, f"Baseline cliff di 150k seharusnya 5%, got {base_jump}"
    assert abs(fuzzy_jump) < 1.5, f"Fuzzy seharusnya halus di 150k, jump={fuzzy_jump}"
