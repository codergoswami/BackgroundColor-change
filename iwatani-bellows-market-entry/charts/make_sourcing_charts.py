"""
Charts answering: where do Indian bellows makers buy their precision strip -
locally or imported?

Run:  python3 make_sourcing_charts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle, FancyArrowPatch, FancyBboxPatch
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.axisbelow": True,
    "figure.dpi": 150,
})

NAVY = "#12355b"
BLUE = "#1f6feb"
LBLUE = "#7fb3f5"
GREEN = "#2da44e"
AMBER = "#d4a017"
RED = "#cf222e"
GREY = "#8b949e"
DGREY = "#57606a"
SAFF = "#ff9933"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------- Chart 20
def chart20():
    """Minimum gauge capability: Indian mills vs global precision mills."""
    mills = [
        # (name, min thickness mm, india?, tolerance note)
        ("Alleima (Sweden)", 0.015, False, "±0.001 mm published"),
        ("Lamineries Matthey (CH)\n— makes AM350", 0.010, False, "±0.014–0.035 mm at 1.0 mm"),
        ("United Performance Metals (US)\n— makes AM350", 0.020, False, "reroll strip 0.0008\"–0.015\""),
        ("Ulbrich (US)\n— makes AM350", 0.025, False, "165+ alloys, foil"),
        ("Chinese re-rollers", 0.050, False, "±0.005–0.01 mm typical"),
        ("IUP Jindal (Ghaziabad)", 0.030, True, "AGC fitted; not published"),
        ("Jindal Stainless SPD (Hisar)", 0.076, True, "razor blade steel"),
        ("Quality Foils (Hisar)", 0.100, True, "±0.020 mm at 0.10 mm"),
    ]
    mills.sort(key=lambda m: m[1])

    fig, ax = plt.subplots(figsize=(12, 6.4))
    y = np.arange(len(mills))
    for i, (name, t, ind, note) in enumerate(mills):
        col = SAFF if ind else NAVY
        ax.barh(i, t, color=col, height=0.6, alpha=0.9)
        ax.text(t * 1.14, i, f"{t:.3f} mm", va="center", fontsize=9.6,
                fontweight="bold", color=col)
        ax.text(0.34, i, note, va="center", fontsize=8.2, color=DGREY)

    ax.set_yticks(y)
    ax.set_yticklabels([m[0] for m in mills], fontsize=9)
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlim(0.007, 1.6)
    ax.set_xlabel("Minimum rolled thickness capability (mm, log scale)", fontsize=10)

    ax.axvspan(0.05, 0.20, color=GREEN, alpha=0.13, zorder=0)
    ax.text(0.10, -0.85, "BELLOWS DIAPHRAGM BAND\n0.05 – 0.20 mm", ha="center",
            fontsize=9.4, fontweight="bold", color=GREEN)

    ax.set_ylim(7.7, -1.35)
    ax.set_title(
        "Chart 20 — Gauge is not the problem. Grade and tolerance are.\n"
        "Indian mills reach the bellows thickness band. Only one publishes a tolerance, and it is 20x looser than the best.",
        fontsize=12.3, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(handles=[Patch(facecolor=SAFF, label="Indian mill"),
                       Patch(facecolor=NAVY, label="Foreign mill / re-roller")],
              loc="lower right", frameon=False, fontsize=9.5)

    fig.text(0.005, -0.10,
             "All figures are each company's own published capability [P], except Chinese re-roller tolerances which are typical\n"
             "advertised values [U]. THE CRITICAL COMPARISON: Quality Foils publishes ±0.020 mm thickness tolerance at 0.10 mm — that\n"
             "is ±20% of gauge. Alleima publishes ±0.001 mm. IUP Jindal has automatic gauge control fitted and claims 'closest\n"
             "thickness tolerances' but publishes no number, which is itself informative. For a bellows diaphragm that must survive\n"
             "millions of flex cycles, thickness scatter drives fatigue life directly.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "20-gauge-capability.png")


# ---------------------------------------------------------------- Chart 21
def chart21():
    """Grade availability matrix: what can be bought in India vs must be imported."""
    grades = ["304 / 304L", "316 / 316L", "321 / 347", "301 spring",
              "AM350 / 633\n(S35000)", "631 / 17-7PH", "Inconel 625/718",
              "Hastelloy C-276", "Titanium"]
    mills = ["IUP Jindal\n(Ghaziabad)", "Quality Foils\n(Hisar)",
             "Jindal Stainless\nSPD (Hisar)", "Any Indian mill\nat all?"]

    # 2 = yes published, 1 = partial/unclear, 0 = no
    M = np.array([
        [2, 2, 2, 2],   # 304
        [2, 2, 2, 2],   # 316
        [2, 2, 2, 2],   # 321/347
        [1, 2, 1, 2],   # 301 spring
        [0, 0, 0, 0],   # AM350
        [0, 0, 0, 0],   # 631
        [0, 0, 0, 0],   # Inconel
        [0, 0, 0, 0],   # Hastelloy
        [0, 0, 0, 0],   # Ti
    ])

    fig, ax = plt.subplots(figsize=(9.6, 7))
    cmap = {0: "#ffd7d7", 1: "#fff4cc", 2: "#d7f5d7"}
    txt = {0: "NO", 1: "?", 2: "YES"}
    tcol = {0: RED, 1: "#a37411", 2: "#1a7f37"}

    for i in range(len(grades)):
        for j in range(len(mills)):
            v = M[i, j]
            ax.add_patch(Rectangle((j, i), 1, 1, facecolor=cmap[v],
                                   edgecolor="white", linewidth=2))
            ax.text(j + 0.5, i + 0.5, txt[v], ha="center", va="center",
                    fontsize=10, fontweight="bold", color=tcol[v])

    ax.add_patch(Rectangle((0, 4), 4, 5, facecolor="none", edgecolor=RED,
                           linewidth=3, zorder=5))
    ax.text(4.12, 6.5, "MUST BE\nIMPORTED\n\nNo Indian mill\npublishes any\nof these grades",
            fontsize=9.6, fontweight="bold", color=RED, va="center")
    ax.text(4.12, 1.9, "AVAILABLE\nLOCALLY\n\nBoth precision\nmills name\nBELLOWS as a\nserved application",
            fontsize=9.6, fontweight="bold", color="#1a7f37", va="center")

    ax.set_xlim(0, 6.9)
    ax.set_ylim(0, 9)
    ax.set_xticks(np.arange(len(mills)) + 0.5)
    ax.set_xticklabels(mills, fontsize=8.8)
    ax.set_yticks(np.arange(len(grades)) + 0.5)
    ax.set_yticklabels(grades, fontsize=9)
    ax.invert_yaxis()
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)

    ax.set_title(
        "Chart 21 — The answer, by grade\n"
        "Austenitic: buy in India. Precipitation-hardening and exotics: import, no alternative.",
        fontsize=12.3, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.055,
             "Based on each mill's own published grade list [P]. IUP Jindal: J-1, J-4, 304, 304L, 316, 316L, 317L, 321, 347 austenitic\n"
             "plus Mumetal/Permimphy magnetic alloys. Quality Foils: 301, 304/L, 316L, 321, J4 and 200 series. Jindal Stainless SPD:\n"
             "austenitic, ferritic, martensitic and duplex families — no PH grades in the published tables.\n"
             "SIGNIFICANT: both Indian precision-strip mills explicitly list bellows. IUP Jindal's application list includes 'Flexi metal\n"
             "tubes / bellows'; Quality Foils lists 'Metallic Bellows' and 'Bellows for precision measuring instruments'.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "21-grade-availability.png")


# ---------------------------------------------------------------- Chart 22
def chart22():
    """The sourcing map."""
    fig, ax = plt.subplots(figsize=(13, 7.6))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def box(x, y, w, h, label, fc, ec, fs=8.6, bold=True):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.09",
                                    facecolor=fc, edgecolor=ec, linewidth=1.7))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=fs, color=NAVY,
                fontweight="bold" if bold else "normal")

    ax.text(2.4, 7.55, "LOCAL — INDIA", fontsize=11.5, fontweight="bold",
            color="#1a7f37", ha="center")
    ax.text(9.9, 7.55, "IMPORTED", fontsize=11.5, fontweight="bold",
            color=RED, ha="center")

    # local supply
    box(0.25, 6.1, 4.3, 1.05,
        "IUP Jindal Metals & Alloys — Ghaziabad\n0.03–1.5 mm · 3.5–630 mm · 22,000 tpa\nlists \"Flexi metal tubes / bellows\"",
        "#d7f5d7", GREEN, 8.2)
    box(0.25, 4.85, 4.3, 1.05,
        "Quality Foils (India) — Hisar\n0.10–4.0 mm · 20–710 mm · since 1982\nlists \"Metallic Bellows\"",
        "#d7f5d7", GREEN, 8.2)
    box(0.25, 3.6, 4.3, 1.05,
        "Jindal Stainless SPD — Hisar\n84,000 tpa · to 0.076 mm\nmartensitic razor-blade oriented",
        "#eef4ff", BLUE, 8.2)
    box(0.25, 2.55, 4.3, 0.8,
        "Hisar Metal Industries · Singhal Strips\nregional strip mills",
        "#f4f7fb", GREY, 8.2, False)

    # imported supply
    box(8.45, 6.1, 4.3, 1.05,
        "Ulbrich (US) · UPM (US) · ATI (US)\nAM350 to AMS 5548 · \"bellows\" named\nas lead application. No India office",
        "#ffd7d7", RED, 8.2)
    box(8.45, 4.85, 4.3, 1.05,
        "Lamineries Matthey (Switzerland)\nAM350 coil 0.010–0.500 mm · 1.5–200 mm\nwidth tol +0.2/-0.0, ±0.1 on request",
        "#ffd7d7", RED, 8.2)
    box(8.45, 3.6, 4.3, 1.05,
        "TOKKIN (Japan) · Alleima (Sweden)\nTOKKIN 350 \"for bellows\" · Alleima to\n0.015 mm at ±0.001 mm. ALLEIMA IS IN INDIA",
        "#ffd7d7", RED, 8.2)
    box(8.45, 2.55, 4.3, 0.8,
        "Chinese re-rollers\n\"strip for vacuum bellows\", 3 t MOQ",
        "#fff4cc", AMBER, 8.2, False)

    # middle: the buyers
    box(5.05, 4.45, 2.9, 1.5,
        "INDIAN BELLOWS\nMAKERS\n\nWell Tech · Fluidyne\nBhastrik · Metallic Bellows\nFlexpert · Witzenmann India",
        "#eef4ff", NAVY, 8.6)

    # intermediary
    box(5.05, 2.55, 2.9, 1.15,
        "MUMBAI STOCKISTS\n& TRADERS\ne.g. Aesteiron, Sachiya,\nRiddhi Siddhi",
        "#fff4cc", AMBER, 8.2)

    # arrows
    for y0 in (6.6, 5.35, 4.1):
        ax.add_patch(FancyArrowPatch((4.6, y0), (5.0, 5.35),
                                     arrowstyle="-|>", mutation_scale=15,
                                     color=GREEN, linewidth=1.7,
                                     connectionstyle="arc3,rad=0.12"))
    for y0 in (6.6, 5.35, 4.1):
        ax.add_patch(FancyArrowPatch((8.4, y0), (8.0, 5.35),
                                     arrowstyle="-|>", mutation_scale=15,
                                     color=RED, linewidth=1.7,
                                     connectionstyle="arc3,rad=-0.12"))
    ax.add_patch(FancyArrowPatch((8.4, 2.95), (8.0, 3.05),
                                 arrowstyle="-|>", mutation_scale=15,
                                 color=AMBER, linewidth=1.7))
    ax.add_patch(FancyArrowPatch((6.5, 3.7), (6.5, 4.4),
                                 arrowstyle="-|>", mutation_scale=15,
                                 color=AMBER, linewidth=1.9))

    ax.text(4.72, 3.35, "304 / 316 / 321\naustenitic\n0.10 mm+",
            fontsize=8, color="#1a7f37", ha="center", fontweight="bold")
    ax.text(8.28, 1.95, "AM350 / 631\nInconel · Hastelloy\nsub-0.05 mm\nultra-tight tolerance",
            fontsize=8, color=RED, ha="center", fontweight="bold")

    box(0.25, 0.35, 12.5, 1.5,
        "THE ANSWER: BOTH — and the split is by GRADE, not by preference.\n\n"
        "Austenitic 304/316/321 at 0.10 mm and above is bought LOCALLY. Both Indian precision mills explicitly serve bellows.\n"
        "AM350 and 631 precipitation-hardening grades, Inconel, Hastelloy, sub-0.05 mm foil and ultra-tight tolerance work are\n"
        "IMPORTED — no Indian mill publishes any of them. Well Tech's AM350 at 0.05–0.2 mm is therefore imported, almost certainly\n"
        "through a Mumbai stockist rather than direct from the mill, because its annual requirement is far below mill MOQs.",
        "#f4f7fb", NAVY, 8.8)

    ax.set_title(
        "Chart 22 — Sourcing map for Indian bellows manufacturers",
        fontsize=13, fontweight="bold", loc="left", color=NAVY, pad=12)
    save(fig, "22-sourcing-map.png")


if __name__ == "__main__":
    chart20(); chart21(); chart22()
    print("\nSourcing charts written to", OUT)
