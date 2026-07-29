"""
Charts explaining why India's share of the "expansion joints" market and the
"bellows" market are quoted differently, and reconciling the two.

Run:  python3 make_reconciliation_charts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch, FancyBboxPatch
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


# ---------------------------------------------------------------- Chart 17
def chart17():
    """The two markets overlap; neither contains the other."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.add_patch(Circle((4.5, 3.5), 2.85, facecolor=BLUE, alpha=0.17,
                        edgecolor=BLUE, linewidth=2.4, zorder=1))
    ax.add_patch(Circle((7.5, 3.5), 2.85, facecolor=AMBER, alpha=0.17,
                        edgecolor=AMBER, linewidth=2.4, zorder=1))

    ax.text(2.55, 6.35, "METAL BELLOWS MARKET", fontsize=11.5,
            fontweight="bold", color=BLUE, ha="center")
    ax.text(2.55, 6.02, "US\\$1.2 – 2.6 bn", fontsize=10.5, color=BLUE, ha="center")
    ax.text(9.45, 6.35, "EXPANSION JOINTS MARKET", fontsize=11.5,
            fontweight="bold", color="#a37411", ha="center")
    ax.text(9.45, 6.02, "US\\$3.7 – 7.2 bn", fontsize=10.5, color="#a37411", ha="center")

    ax.text(3.05, 4.55, "BELLOWS ONLY\n(not expansion joints)", fontsize=9.2,
            fontweight="bold", color=NAVY, ha="center")
    ax.text(3.05, 3.05,
            "• Mechanical seal bellows\n"
            "• Semiconductor: slit valves,\n   wafer lift, feedthroughs, MFCs\n"
            "• Aerospace actuators\n"
            "• Automotive exhaust decouplers\n"
            "• Instrument diaphragm bellows\n"
            "• Cryogenic & hydrogen bellows",
            fontsize=7.9, color=DGREY, ha="center", va="center")

    ax.text(6.0, 4.62, "BOTH", fontsize=9.6, fontweight="bold",
            color=GREEN, ha="center")
    ax.text(6.0, 3.28,
            "Metallic\npipe\nexpansion\njoints\n\n(bellows is\nthe flexing\nelement)",
            fontsize=7.6, color=DGREY, ha="center", va="center")

    ax.text(8.95, 4.55, "EXPANSION JOINTS ONLY\n(no metal bellows)", fontsize=9.2,
            fontweight="bold", color="#a37411", ha="center")
    ax.text(8.95, 3.05,
            "• Rubber expansion joints\n"
            "• Fabric / textile joints\n"
            "• PTFE-lined joints\n"
            "• Civil & structural joints\n   (bridges, buildings)\n"
            "• HVAC duct joints\n"
            "• Plus ALL non-bellows content:\n   flanges, liners, covers, tie rods",
            fontsize=7.9, color=DGREY, ha="center", va="center")

    box = FancyBboxPatch((0.35, 0.25), 11.3, 1.05,
                         boxstyle="round,pad=0.14", facecolor="#f4f7fb",
                         edgecolor=GREY, linewidth=1)
    ax.add_patch(box)
    ax.text(6.0, 0.78,
            "These are OVERLAPPING sets, not nested ones. A market share quoted against one box "
            "is not comparable to a share\nquoted against the other. That is the whole reason the two "
            "India numbers look different.",
            fontsize=9.3, color=NAVY, ha="center", va="center", fontweight="bold")

    ax.set_title(
        "Chart 17 — Why \"bellows\" and \"expansion joints\" are different markets\n"
        "Note that the expansion joints market is measured 2–3x LARGER than the bellows market",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=16)

    fig.text(0.005, 0.005,
             "Global expansion joints [S]: Dataintelo US\\$3.72bn (2024); Growth Market Reports US\\$3.87bn (2024); Marketintelo US\\$6.2bn\n"
             "(2025); Future Market Report US\\$6.2bn (2025). Metallic share of that: 38.5% (Marketintelo), 46.7% (Future Market Report),\n"
             "64.7% (Dataintelo). Global metal bellows [S]: US\\$1.2-2.6bn — see chart 1. The expansion joints figure is larger because it\n"
             "includes non-metallic joints, civil/structural joints, and all the non-bellows hardware content of a finished joint.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "17-market-overlap.png")


# ---------------------------------------------------------------- Chart 18
def chart18():
    """India's share depends entirely on which denominator you use."""
    rows = [
        ("India bellows vs global bellows\nUS\\$50–70m / US\\$1.2–2.6bn",
         1.9, 3.5, GREEN, "OUR ESTIMATE — the comparable one"),
        ("India exp. joints vs global exp. joints\nUS\\$72m / US\\$3.7–7.2bn (broad)",
         1.0, 1.9, RED, "Cross-check FAILS the 5–10% claim"),
        ("India exp. joints vs global metallic\nexp. joints  US\\$72m / US\\$1.4–4.7bn",
         1.5, 5.1, AMBER, "Partially supports it"),
        ("Research and Markets' stated claim\n\"India holds 5–10% of global\"",
         5.0, 10.0, GREY, "Denominator NOT published"),
        ("Denominator that would make 5–10% true\n⇒ global exp. joints of only US\\$0.7–1.4bn",
         5.0, 10.0, "none", "Implies a NARROW definition"),
    ]

    fig, ax = plt.subplots(figsize=(12, 6.2))
    for i, (lab, lo, hi, col, note) in enumerate(rows):
        if col == "none":
            ax.plot([lo, hi], [i, i], color=GREY, lw=11, alpha=0.35,
                    solid_capstyle="butt", zorder=3, ls="-")
            ax.plot([lo, hi], [i, i], color=DGREY, lw=1.4, ls="--", zorder=4)
        else:
            ax.plot([lo, hi], [i, i], color=col, lw=13, alpha=0.88,
                    solid_capstyle="butt", zorder=3)
        ax.text(hi + 0.35, i, f"{lo:.1f}–{hi:.1f}%", va="center",
                fontsize=10.2, fontweight="bold", color=DGREY)
        ax.text(13.2, i, note, va="center", fontsize=8.4, color=DGREY)

    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.9)
    ax.invert_yaxis()
    ax.set_xlabel("India's share of the relevant global market (%)", fontsize=10)
    ax.set_xlim(0, 23.5)
    ax.set_title(
        "Chart 18 — Same country, same year, five different answers\n"
        "India's \"share\" ranges from 1.0% to 10% depending purely on how the denominator is drawn",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.115,
             "THE KEY POINT: Research and Markets states both that India's expansion joints market was US\\$72.32m in 2024 AND that\n"
             "India holds 5-10% of the global expansion joints market. Those two statements together imply a global market of only\n"
             "US\\$0.72-1.45bn. Four other vendors put the global expansion joints market at US\\$3.7-7.2bn. So either R&M is using a\n"
             "much narrower definition (industrial metallic piping only, excluding civil, rubber and fabric joints), or the 5-10%\n"
             "figure does not hold. R&M does not publish its global denominator, so this cannot be resolved from public sources.\n"
             "RECOMMENDATION: use ~2-3% for bellows. Treat 5-10% as unverified and do not put it in a partner document.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "18-india-share-denominators.png")


# ---------------------------------------------------------------- Chart 19
def chart19():
    """The systematic pattern: share falls as value density and tech intensity rise."""
    pts = [
        ("Stainless steel\nproduction", 1, 6.2, GREY, "~US\\$2/kg\nfreight-protected"),
        ("Industrial expansion\njoints", 2, 3.0, LBLUE, "heavy, fabricated,\nfreight-protected"),
        ("Metal bellows\n(all types)", 3, 2.7, BLUE, "mixed"),
        ("Precision / edge-welded\nbellows", 4, 1.0, AMBER, "light, high-spec,\nglobally traded"),
        ("Semiconductor\nequipment", 5, 0.7, RED, "very high value,\nglobally traded"),
    ]
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    xs = [p[1] for p in pts]
    ys = [p[2] for p in pts]

    ax.plot(xs, ys, color=DGREY, lw=1.8, ls="--", zorder=1, alpha=0.7)
    for lab, x, y, col, note in pts:
        ax.scatter([x], [y], s=210, color=col, zorder=3,
                   edgecolor="white", linewidth=2)
        ax.annotate(f"{y}%", (x, y), textcoords="offset points",
                    xytext=(15, 0), ha="left", va="center",
                    fontsize=11, fontweight="bold", color=col)
        ax.annotate(lab, (x, y), textcoords="offset points",
                    xytext=(0, 26), ha="center", fontsize=9.2,
                    fontweight="bold", color=NAVY)
        ax.annotate(note, (x, y), textcoords="offset points",
                    xytext=(0, -34), ha="center", fontsize=7.8, color=DGREY)

    ax.annotate("", xy=(5.35, 5.6), xytext=(0.75, 5.6),
                arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    ax.text(3.05, 5.85, "Increasing value density, technology intensity and global tradability",
            ha="center", fontsize=9.6, color=RED, fontweight="bold")

    ax.set_ylabel("India's share of the global market (%)", fontsize=10)
    ax.set_xticks([])
    ax.set_ylim(-0.9, 7.3)
    ax.set_xlim(0.5, 5.6)
    ax.set_title(
        "Chart 19 — The pattern is systematic, and it is the actual strategic finding\n"
        "India's share collapses as products get lighter, more precise and more globally traded",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.075,
             "Stainless production ~6.2% [C, 2021]. Expansion joints ~3.0% and bellows ~2.7% are our estimates. Precision/edge-welded\n"
             "~1.0% and semiconductor equipment ~0.7% are modelled from the SEAJ 'Rest of World' bucket [P]. All points except the\n"
             "stainless figure are estimates.  WHY IT HAPPENS: heavy fabricated products are freight- and tariff-protected, so every\n"
             "industrialising economy builds domestic capacity roughly in line with its industrial capex. Light, high-specification\n"
             "products are globally traded and concentrate in whoever holds the qualification history — the US, Japan, Korea, Germany.\n"
             "IMPLICATION: enter where India is strong (left of this chart) and use that position to earn the right to move right.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "19-share-vs-value-density.png")


if __name__ == "__main__":
    chart17(); chart18(); chart19()
    print("\nReconciliation charts written to", OUT)
