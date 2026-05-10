"""
Generator semua figure untuk laporan / proposal.

Output: PNG ke project/figures/, lalu di-copy ke proposal/figures/
supaya path \\graphicspath{} di LaTeX tinggal merujuk satu folder.
"""

import shutil
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from src.fuzzy import (
    freq_curves, spend_curves, disc_curves,
    recommend_discount,
)
from src.baseline import traditional_discount
from src.data import load


ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "figures"
PROP_DIR = ROOT.parent / "proposal" / "figures"

DPI = 200  # cukup buat IEEE format, tidak terlalu besar


def save(fig, name):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    PROP_DIR.mkdir(parents=True, exist_ok=True)
    p = FIG_DIR / name
    fig.savefig(p, dpi=DPI, bbox_inches="tight")
    shutil.copyfile(p, PROP_DIR / name)
    plt.close(fig)
    return p


# Warna konsisten untuk linguistik
FREQ_COLORS  = {"rare": "#5C6BC0", "regular": "#26A69A", "frequent": "#EF5350"}
SPEND_COLORS = {"low": "#7CB342",  "medium": "#FFA726", "high": "#8E24AA"}
DISC_COLORS  = {"none": "#90A4AE", "small": "#42A5F5",
                "medium": "#FFB300", "large": "#D32F2F"}


def plot_mf_inputs():
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))

    x, c = freq_curves()
    for term, mf in c.items():
        axes[0].plot(x, mf, lw=2, label=term, color=FREQ_COLORS[term])
        axes[0].fill_between(x, mf, alpha=0.10, color=FREQ_COLORS[term])
    axes[0].set_xlabel("Frekuensi kunjungan (per bulan)")
    axes[0].set_ylabel("Derajat keanggotaan $\\mu$")
    axes[0].set_title("Input 1: Frekuensi")
    axes[0].grid(alpha=0.3)
    axes[0].legend(loc="upper right")
    axes[0].set_ylim(-0.02, 1.05)

    x, c = spend_curves()
    for term, mf in c.items():
        axes[1].plot(x, mf, lw=2, label=term, color=SPEND_COLORS[term])
        axes[1].fill_between(x, mf, alpha=0.10, color=SPEND_COLORS[term])
    axes[1].set_xlabel("Spending bulan ini (ribu Rupiah)")
    axes[1].set_title("Input 2: Spending")
    axes[1].grid(alpha=0.3)
    axes[1].legend(loc="upper right")
    axes[1].set_ylim(-0.02, 1.05)

    fig.suptitle("Membership functions input", y=1.02)
    return save(fig, "mf_inputs.png")


def plot_mf_output():
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    x, c = disc_curves()
    for term, mf in c.items():
        ax.plot(x, mf, lw=2, label=term, color=DISC_COLORS[term])
        ax.fill_between(x, mf, alpha=0.12, color=DISC_COLORS[term])
    ax.set_xlabel("Diskon (%)")
    ax.set_ylabel("Derajat keanggotaan $\\mu$")
    ax.set_title("Output: Diskon yang direkomendasikan")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right")
    ax.set_ylim(-0.02, 1.05)
    return save(fig, "mf_output.png")


def plot_surface(grid=30):
    """3D surface diskon di sumbu (frekuensi, spending)."""
    fs = np.linspace(0, 8, grid)
    ss = np.linspace(0, 600, grid)
    F, S = np.meshgrid(fs, ss)
    Z = np.zeros_like(F)
    for i in range(grid):
        for j in range(grid):
            Z[i, j] = recommend_discount(F[i, j], S[i, j])

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(F, S, Z, cmap="viridis", edgecolor="none", alpha=0.92)
    ax.set_xlabel("Frekuensi (per bulan)")
    ax.set_ylabel("Spending (ribu Rp)")
    ax.set_zlabel("Diskon (%)")
    ax.set_title("Surface diskon fuzzy")
    ax.view_init(elev=22, azim=-120)
    return save(fig, "surface.png")


def plot_fuzzy_vs_baseline_along_spending(freq_fixed=2.0):
    """Tunjukkan cliff effect baseline vs kurva fuzzy yang halus.

    Frekuensi diset 2 (regular). Spending disweep 0-500k.
    """
    spend_grid = np.linspace(0, 500, 200)
    fuzzy_y = [recommend_discount(freq_fixed, s) for s in spend_grid]
    base_y  = [traditional_discount(freq_fixed, s) for s in spend_grid]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(spend_grid, fuzzy_y, lw=2.2, label="Fuzzy (Mamdani)", color="#1E88E5")
    ax.plot(spend_grid, base_y,  lw=2.2, label="Skema bertingkat",
            color="#E53935", linestyle="--")
    ax.fill_between(spend_grid, fuzzy_y, base_y, alpha=0.10, color="#888888")

    # Tandai cliff baseline
    for thresh in [150, 250, 400]:
        ax.axvline(thresh, color="#999", lw=0.6, linestyle=":")
        ax.annotate(f"{thresh}k", xy=(thresh, 0.5), xytext=(thresh + 4, 1.5),
                    color="#666", fontsize=9)

    ax.set_xlabel(f"Spending bulan ini (ribu Rp)  [Frekuensi tetap = {freq_fixed:.0f}]")
    ax.set_ylabel("Diskon (%)")
    ax.set_title("Fuzzy vs skema bertingkat: loncatan tarif di ambang batas")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left")
    return save(fig, "fuzzy_vs_baseline.png")


def plot_customer_scatter():
    """Scatter 100 pelanggan di plane (frequency, spending), warnai dengan diskon fuzzy."""
    df = load()
    df = df.copy()
    df["fuzzy_disc"] = [recommend_discount(f, s)
                        for f, s in zip(df["frequency"], df["spending_kIDR"])]
    df["base_disc"] = [traditional_discount(f, s)
                       for f, s in zip(df["frequency"], df["spending_kIDR"])]

    fig, ax = plt.subplots(figsize=(8, 6))
    sc = ax.scatter(df["frequency"], df["spending_kIDR"],
                    c=df["fuzzy_disc"], cmap="viridis",
                    s=55, edgecolors="#263238", linewidth=0.5)
    cbar = fig.colorbar(sc, ax=ax)
    cbar.set_label("Rekomendasi diskon fuzzy (%)")
    ax.set_xlabel("Frekuensi kunjungan (per bulan)")
    ax.set_ylabel("Spending bulan ini (ribu Rp)")
    ax.set_title("100 pelanggan kantoran Jakarta - rekomendasi diskon fuzzy")
    ax.grid(alpha=0.3)
    return save(fig, "customer_scatter.png")


def plot_disc_distribution():
    df = load()
    fuzzy_disc = [recommend_discount(f, s)
                  for f, s in zip(df["frequency"], df["spending_kIDR"])]
    base_disc = [traditional_discount(f, s)
                 for f, s in zip(df["frequency"], df["spending_kIDR"])]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bins = np.arange(0, 27, 1)
    ax.hist(fuzzy_disc, bins=bins, alpha=0.65, label="Fuzzy",
            color="#1E88E5", edgecolor="white")
    ax.hist(base_disc, bins=bins, alpha=0.55, label="Skema bertingkat",
            color="#E53935", edgecolor="white")
    ax.set_xlabel("Diskon (%)")
    ax.set_ylabel("Jumlah pelanggan")
    ax.set_title("Distribusi diskon - fuzzy vs skema bertingkat (100 pelanggan)")
    ax.legend()
    ax.grid(alpha=0.3, axis="y")
    return save(fig, "disc_distribution.png")


def generate_all():
    paths = [
        plot_mf_inputs(),
        plot_mf_output(),
        plot_surface(),
        plot_fuzzy_vs_baseline_along_spending(),
        plot_customer_scatter(),
        plot_disc_distribution(),
    ]
    for p in paths:
        print(f"  {p.name}")
    print(f"\n6 figures saved to {FIG_DIR}")


if __name__ == "__main__":
    generate_all()
