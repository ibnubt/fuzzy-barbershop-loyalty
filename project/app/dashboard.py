"""
Dashboard interaktif buat demo sistem fuzzy.

Cara jalan: streamlit run app/dashboard.py
"""

import sys
from pathlib import Path

# Supaya import src.* jalan saat dijalankan via `streamlit run`
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from src.fuzzy import (
    recommend_discount, discount_label,
    freq_curves, spend_curves, disc_curves,
)
from src.baseline import traditional_discount, traditional_label
from src.data import load


st.set_page_config(
    page_title="Fuzzy Loyalty Barbershop",
    page_icon="✂️",
    layout="wide",
)


st.title("Sistem Fuzzy Diskon Loyalti Barbershop")
st.caption(
    "Konteks: barbershop Jakarta, target pelanggan pekerja kantoran. "
    "Tarif basic Rp 80-100k, premium Rp 150k ke atas."
)

# Sidebar input
st.sidebar.header("Input pelanggan")
freq = st.sidebar.slider(
    "Frekuensi kunjungan (per bulan)",
    min_value=0.0, max_value=8.0, value=2.0, step=0.1,
)
spend = st.sidebar.slider(
    "Total spending bulan ini (ribu Rp)",
    min_value=0, max_value=600, value=200, step=10,
)
st.sidebar.divider()
st.sidebar.markdown(
    "**Acuan tarif Jakarta 2024-2025:**\n"
    "- Basic 1x: 80-100k\n"
    "- Premium 1x: 150-200k\n"
    "- Paket grooming: 250-400k"
)


# Inferensi
fuzzy_disc = recommend_discount(freq, spend)
base_disc = traditional_discount(freq, spend)


tab1, tab2, tab3 = st.tabs([
    "Inferensi",
    "Perbandingan dengan skema bertingkat",
    "Dataset 100 pelanggan",
])

with tab1:
    col1, col2 = st.columns([1, 1.5])

    with col1:
        # Big number badge
        label = discount_label(fuzzy_disc)
        color = {
            "Tidak Ada": "#90A4AE",
            "Kecil":     "#42A5F5",
            "Sedang":    "#FFA726",
            "Besar":     "#EF5350",
        }[label]
        st.markdown(
            f"""
            <div style="background:{color};padding:20px;border-radius:12px;
                        text-align:center;color:white;">
              <div style="font-size:14px;">Rekomendasi diskon (fuzzy)</div>
              <div style="font-size:50px;font-weight:700;">{fuzzy_disc:.1f}%</div>
              <div style="font-size:18px;font-weight:600;">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.metric(
            "Pembanding skema bertingkat",
            f"{base_disc}%",
            delta=f"{fuzzy_disc - base_disc:+.1f}% vs fuzzy",
            help="Tier-based: max(freq, spending) -> tier",
        )

    with col2:
        # MF input dengan crisp value vertikal
        x_f, c_f = freq_curves()
        x_s, c_s = spend_curves()
        fig, axes = plt.subplots(1, 2, figsize=(9, 3))

        for term, mf in c_f.items():
            axes[0].plot(x_f, mf, label=term)
        axes[0].axvline(freq, color="black", lw=1.5, ls="--")
        axes[0].set_title(f"Frekuensi (input: {freq:.1f})")
        axes[0].set_ylim(-0.02, 1.05)
        axes[0].grid(alpha=0.3)
        axes[0].legend(fontsize=8)

        for term, mf in c_s.items():
            axes[1].plot(x_s, mf, label=term)
        axes[1].axvline(spend, color="black", lw=1.5, ls="--")
        axes[1].set_title(f"Spending (input: {spend}k)")
        axes[1].set_ylim(-0.02, 1.05)
        axes[1].grid(alpha=0.3)
        axes[1].legend(fontsize=8)
        st.pyplot(fig)
        plt.close(fig)

    st.subheader("Output MF dengan posisi defuzzifikasi")
    x_d, c_d = disc_curves()
    fig, ax = plt.subplots(figsize=(9, 3))
    for term, mf in c_d.items():
        ax.plot(x_d, mf, lw=1.8, label=term)
    ax.axvline(fuzzy_disc, color="black", lw=2, ls="--",
               label=f"centroid = {fuzzy_disc:.1f}%")
    ax.set_xlabel("Diskon (%)")
    ax.set_ylabel("$\\mu$")
    ax.set_ylim(-0.02, 1.05)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right", fontsize=9, ncol=2)
    st.pyplot(fig)
    plt.close(fig)

    with st.expander("Rule base"):
        st.markdown(
            "| Frekuensi \\ Spending | low (hemat) | medium (standar) | high (premium) |\n"
            "|---|---|---|---|\n"
            "| **rare** (jarang)     | none   | small  | medium |\n"
            "| **regular** (sedang)  | small  | medium | large  |\n"
            "| **frequent** (sering) | medium | large  | large  |"
        )


with tab2:
    st.subheader("Sweep spending untuk frekuensi tetap")
    sweep_freq = st.slider("Frekuensi tetap untuk sweep", 0.0, 8.0, 2.0, 0.5)

    spend_grid = np.linspace(0, 500, 200)
    fz = [recommend_discount(sweep_freq, s) for s in spend_grid]
    bs = [traditional_discount(sweep_freq, s) for s in spend_grid]

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(spend_grid, fz, lw=2, label="Fuzzy", color="#1E88E5")
    ax.plot(spend_grid, bs, lw=2, label="Skema bertingkat", color="#E53935", ls="--")
    for thresh in [150, 250, 400]:
        ax.axvline(thresh, color="#999", lw=0.6, ls=":")
    ax.set_xlabel(f"Spending (ribu Rp), frekuensi = {sweep_freq}")
    ax.set_ylabel("Diskon (%)")
    ax.grid(alpha=0.3)
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

    st.markdown(
        "Garis putus-putus vertikal di **150k**, **250k**, **400k** adalah "
        "ambang batas pada skema bertingkat. Garis merah loncat tajam "
        "di tiap threshold sementara fuzzy (biru) bergerak halus."
    )


with tab3:
    st.subheader("100 profil pelanggan kantoran Jakarta")
    df = load().copy()
    df["fuzzy_disc"] = [recommend_discount(f, s)
                       for f, s in zip(df["frequency"], df["spending_kIDR"])]
    df["base_disc"] = [traditional_discount(f, s)
                      for f, s in zip(df["frequency"], df["spending_kIDR"])]
    df["selisih"] = df["fuzzy_disc"] - df["base_disc"]

    cmean = df["fuzzy_disc"].mean()
    bmean = df["base_disc"].mean()
    c1, c2, c3 = st.columns(3)
    c1.metric("Rata-rata diskon fuzzy", f"{cmean:.2f}%")
    c2.metric("Rata-rata diskon skema bertingkat", f"{bmean:.2f}%")
    c3.metric("Rata-rata selisih absolut", f"{(df['selisih']).abs().mean():.2f}%")

    st.dataframe(df, use_container_width=True, hide_index=True)

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.scatter(df["frequency"], df["spending_kIDR"],
               c=df["fuzzy_disc"], cmap="viridis",
               s=55, edgecolors="#263238", linewidth=0.5)
    ax.set_xlabel("Frekuensi (per bulan)")
    ax.set_ylabel("Spending (ribu Rp)")
    cbar = plt.colorbar(ax.collections[0], ax=ax)
    cbar.set_label("Diskon fuzzy (%)")
    st.pyplot(fig)
    plt.close(fig)
