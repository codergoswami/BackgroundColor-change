"""
Deck-ready numbers card + the reconciliation check behind it.

Run:  python3 make_deck_card.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch
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


# ---------------------------------------------------------------- Chart 25
def chart25():
    """Why $4.4bn by 2033 does not reconcile with 5.5-5.8% CAGR."""
    fig, ax = plt.subplots(figsize=(11.5, 6.4))

    yrs = np.arange(2025, 2034)

    def series(base, g):
        return base * (1 + g) ** (yrs - 2025)

    lo = series(1.16, 0.0519)
    mid = series(2.00, 0.0605)
    hi = series(2.55, 0.0690)

    ax.fill_between(yrs, lo, hi, color=BLUE, alpha=0.15,
                    label="Defensible range (vendor-anchored)")
    ax.plot(yrs, mid, color=NAVY, lw=2.8, label="Mid case: \\$2.0bn @ 6.05%")
    ax.plot(yrs, hi, color=GREY, lw=1.3, ls="--")
    ax.plot(yrs, lo, color=GREY, lw=1.3, ls="--")

    # the proposed deck path
    prop = 2.835 * (1.0565) ** (yrs - 2025)
    ax.plot(yrs, prop, color=RED, lw=2.6, ls="-.",
            label="Proposed deck path: \\$4.4bn by 2033 @ 5.65%")
    ax.scatter([2033], [4.4], s=170, color=RED, zorder=5,
               edgecolor="white", linewidth=2)
    ax.annotate("\\$4.4bn", (2033, 4.4), textcoords="offset points",
                xytext=(10, 4), fontsize=11.5, fontweight="bold", color=RED)
    ax.scatter([2025], [2.835], s=140, color=RED, zorder=5,
               edgecolor="white", linewidth=2)
    ax.annotate("implied 2025 base\n\\$2.83bn — ABOVE the\nentire defensible range",
                (2025, 2.835), textcoords="offset points", xytext=(14, 34),
                fontsize=9.2, fontweight="bold", color=RED)

    ax.scatter([2033], [3.20], s=150, color=NAVY, zorder=5,
               edgecolor="white", linewidth=2)
    ax.annotate("\\$3.2bn", (2033, 3.20), textcoords="offset points",
                xytext=(10, -14), fontsize=11.5, fontweight="bold", color=NAVY)
    ax.scatter([2033], [4.35], s=90, color=GREY, zorder=5,
               edgecolor="white", linewidth=1.6)
    ax.annotate("\\$4.35bn = top of range\n(needs 6.9% from \\$2.55bn)",
                (2033, 4.35), textcoords="offset points", xytext=(-172, 8),
                fontsize=8.6, color=DGREY)

    ax.axhspan(1.16, 2.55, xmin=0, xmax=0.045, color=GREEN, alpha=0.3, zorder=0)
    ax.annotate("2025 defensible\nband \\$1.2–2.6bn", (2025.05, 1.86),
                fontsize=8.8, color="#1a7f37", fontweight="bold",
                ha="left", va="center")

    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("Global metal bellows market (US\\$ bn)", fontsize=10)
    ax.set_ylim(0.6, 5.3)
    ax.set_xlim(2024.7, 2034.4)
    ax.legend(loc="upper left", frameon=False, fontsize=9.2)
    ax.set_title(
        "Chart 25 — The two proposed deck numbers do not reconcile\n"
        "\\$4.4bn by 2033 at 5.5–5.8% CAGR requires a 2025 base of \\$2.83bn, which no vendor supports",
        fontsize=12.2, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.075,
             "Defensible 2025 band is anchored on the four 'all metal bellows' vendor estimates: Zion \\$1.105bn (2024), GII/IRES \\$1.94bn\n"
             "(2025), Strategic MR \\$2.12bn (2024), Market Data Forecast \\$2.39bn (2024), each carried to 2025 at its own stated CAGR.\n"
             "TO REACH \\$4.4bn BY 2033 you need either a 2025 base of \\$2.83bn (above the whole range) or a CAGR of 7.1% from the top of\n"
             "the range / 10.4% from the midpoint — both of which contradict the 5.5-5.8% shown alongside it.\n"
             "\\$4.4bn IS defensible as the UPPER BOUND of a range. It is not defensible as a point estimate.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "25-deck-number-check.png")


# ---------------------------------------------------------------- Chart 26
def chart26():
    """Deck-ready card."""
    fig, ax = plt.subplots(figsize=(13.4, 8))
    ax.set_xlim(0, 13.4)
    ax.set_ylim(0, 8)
    ax.axis("off")

    ax.text(0.25, 7.62, "DECK-READY NUMBERS — internally consistent, each traceable to a source",
            fontsize=13, fontweight="bold", color=NAVY)
    ax.text(0.25, 7.28, "Metal bellows market · use these exact figures and phrasings",
            fontsize=9.6, color=DGREY)

    rows = [
        ("Global market size, 2025",
         "US$1.2 – 2.6 bn", "midpoint ~US$2.0 bn",
         "Range of 4 vendors; scope definitions differ", GREEN),
        ("Global forecast, 2033",
         "~US$3.2 bn", "range US$1.7 – 4.4 bn",
         "Modelled from the 2025 band at consensus CAGR", GREEN),
        ("CAGR, 2025 – 2033",
         "~6%", "range 5.2 – 6.9%",
         "Every vendor falls inside this band", GREEN),
        ("Highest SOURCED 2033 figure",
         "US$3.95 bn", "Market Data Forecast",
         "US$2.39bn (2024) at 5.74% — cite by name", BLUE),
        ("India market size, 2025",
         "US$50 – 70 m", "≈ ₹435 – 610 cr",
         "Bottom-up from MCA filings + 3 vendors", GREEN),
        ("India share of global",
         "~2 – 3%", "point estimate 2.7%",
         "MODELLED — no published figure exists", AMBER),
        ("India growth, observed",
         "+6.5%", "FY24 → FY25, revenue-weighted",
         "Measured from company filings — strongest number", GREEN),
    ]

    y = 6.78
    for lab, big, sub, note, col in rows:
        ax.add_patch(FancyBboxPatch((0.25, y - 0.62), 12.9, 0.72,
                                    boxstyle="round,pad=0.045",
                                    facecolor="#f4f7fb", edgecolor=col,
                                    linewidth=1.5))
        ax.text(0.5, y - 0.26, lab, fontsize=9.6, color=NAVY,
                fontweight="bold", va="center")
        ax.text(4.75, y - 0.26, big, fontsize=13, color=col,
                fontweight="bold", va="center")
        ax.text(6.95, y - 0.26, sub, fontsize=9, color=DGREY, va="center")
        ax.text(9.55, y - 0.26, note, fontsize=8, color=DGREY, va="center")
        y -= 0.83

    ax.add_patch(FancyBboxPatch((0.25, 0.12), 12.9, 0.70,
                                boxstyle="round,pad=0.05",
                                facecolor="#fff4ef", edgecolor=RED, linewidth=1.8))
    ax.text(6.7, 0.47,
            "DO NOT PUT \"US\\$4.4bn by 2033\" ON A SLIDE AS A POINT ESTIMATE. It implies a 2025 base of US\\$2.83bn, above every\n"
            "vendor estimate, and contradicts the 5.5–5.8% CAGR beside it. Use \"~US\\$3.2bn\" as the figure, or \"up to US\\$4.4bn\" as a range top.",
            fontsize=8.9, color=RED, ha="center", va="center", fontweight="bold")

    save(fig, "26-deck-card.png")


if __name__ == "__main__":
    chart25(); chart26()
    print("\nDeck charts written to", OUT)
