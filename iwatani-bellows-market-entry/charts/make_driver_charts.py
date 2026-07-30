"""
India growth drivers and challenges charts for 12-india-drivers-challenges.md.

Run:  python3 make_driver_charts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
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


# ---------------------------------------------------------------- Chart 23
def chart23():
    """Quantified capex pipeline: current vs 2030 target, by sector."""
    rows = [
        ("Crude steel capacity\n(MTPA)", 222, 300, "+35%", GREEN),
        ("Refining capacity\n(MMTPA)", 258.1, 309.5, "+20%", GREEN),
        ("Gas pipeline network\n('000 km)", 25.4, 33.5, "+32%", GREEN),
        ("Nuclear capacity\n(GW, to 2031-32)", 8.78, 22.0, "+151%", AMBER),
        ("Electrolyser capacity\n(GW, green H2)", 0.0, 15.0, "from zero", BLUE),
        ("Green H2 production\n(MMT/yr)", 0.0, 5.0, "from zero", BLUE),
    ]
    fig, ax = plt.subplots(figsize=(11.5, 6.4))
    y = np.arange(len(rows))
    h = 0.34
    for i, (lab, now, tgt, delta, col) in enumerate(rows):
        # normalise each row to its own target = 100
        n = now / tgt * 100 if tgt else 0
        ax.barh(i + h / 2, n, height=h, color=GREY, alpha=0.75)
        ax.barh(i - h / 2, 100, height=h, color=col, alpha=0.9)
        ax.text(n + 1.6, i + h / 2, f"now: {now:g}", va="center",
                fontsize=8.6, color=DGREY)
        ax.text(101.6, i - h / 2, f"2030 target: {tgt:g}", va="center",
                fontsize=8.6, fontweight="bold", color=col)
        ax.text(126, i, delta, va="center", fontsize=11,
                fontweight="bold", color=col)

    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.2)
    ax.invert_yaxis()
    ax.set_xlim(0, 140)
    ax.set_xlabel("Progress toward stated 2030 target (target = 100)", fontsize=10)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_title(
        "Chart 23 — The demand pipeline is government-stated policy, not forecast\n"
        "Every one of these sectors is a bellows and expansion-joint consumer",
        fontsize=12.4, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(handles=[Patch(facecolor=GREY, alpha=0.75, label="Current"),
                       Patch(facecolor=GREEN, label="2030 target")],
              loc="lower right", frameon=False, fontsize=9.5)

    fig.text(0.005, -0.075,
             "[P] Steel: 222 MTPA as of June 2026 against National Steel Policy 2017 target of 300 MTPA by 2030-31 (Ministry of Steel).\n"
             "[P] Refining: 258.1 to 309.5 MMTPA by 2030 (Minister of State for Petroleum, Lok Sabha reply).  [P] Gas pipeline: 25,429 km\n"
             "operational rising to 33,475 km planned by 2030; PNGRB has authorised ~33,500 km.  [C] Nuclear: 8.78 GW now, 22 GW by\n"
             "2031-32, 100 GW by 2047 ambition.  [P] Green hydrogen: 5 MMT/yr and 15 GW electrolyser capacity by 2030 under the National\n"
             "Green Hydrogen Mission, outlay Rs 19,744 crore including Rs 17,490 crore for SIGHT.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "23-india-demand-pipeline.png")


# ---------------------------------------------------------------- Chart 24
def chart24():
    """Challenges: severity vs whether Iwatani can address it."""
    # (label, severity 1-10, addressable-by-Iwatani 1-10)
    items = [
        ("No domestic PH grades\n(AM350 / 631)", 9.3, 9.5),
        ("Tolerance class gap\n±0.020 vs ±0.001 mm", 8.6, 8.8),
        ("Mill MOQ vs small\nlot requirement", 7.4, 9.3),
        ("Sub-0.05 mm foil\nunavailable locally", 7.0, 8.6),
        ("No cleanroom / RGA\nqualification infra", 9.0, 3.2),
        ("12–24 month customer\nqualification cycles", 8.2, 4.6),
        ("Sub-scale, fragmented\nIndian manufacturers", 7.8, 3.0),
        ("Small domestic market\n(US\\$50–70m)", 8.8, 1.6),
        ("Demand sits where tools\nare built, not fabs", 9.5, 1.4),
        ("Chinese import\nprice competition", 7.2, 5.2),
        ("Thin-gauge metallurgy\n& welding skills", 6.6, 4.0),
        ("Lumpy, project-driven\ndemand + PSU payment cycles", 6.2, 2.2),
        ("Nickel / stainless\nprice volatility", 5.6, 6.4),
        ("Foreign design standards\n(EJMA/ASME/DIN)", 4.4, 2.6),
    ]
    fig, ax = plt.subplots(figsize=(12.4, 7.4))

    ax.add_patch(Rectangle((5.5, 5.5), 5.2, 5.2, facecolor=GREEN,
                           alpha=0.08, zorder=0))
    ax.add_patch(Rectangle((5.5, 0), 5.2, 5.5, facecolor=RED,
                           alpha=0.07, zorder=0))
    ax.text(8.1, 10.35, "HIGH SEVERITY, ADDRESSABLE\n→ this is the business case",
            ha="center", fontsize=9.6, fontweight="bold", color="#1a7f37")
    ax.text(8.1, 0.55, "HIGH SEVERITY, NOT ADDRESSABLE\n→ design the strategy around these",
            ha="center", fontsize=9.6, fontweight="bold", color=RED)

    for lab, sev, addr in items:
        if sev >= 5.5 and addr >= 5.5:
            col, sz = GREEN, 200
        elif sev >= 5.5:
            col, sz = RED, 200
        else:
            col, sz = GREY, 140
        ax.scatter([sev], [addr], s=sz, color=col, zorder=4,
                   edgecolor="white", linewidth=1.6)
        below = lab.startswith("Demand sits") or lab.startswith("Chinese")
        ax.annotate(lab, (sev, addr), textcoords="offset points",
                    xytext=(0, -26 if below else 15), ha="center",
                    fontsize=7.9, color=NAVY, fontweight="bold")

    ax.axvline(5.5, color=DGREY, lw=1, ls=":")
    ax.axhline(5.5, color=DGREY, lw=1, ls=":")
    ax.set_xlabel("Severity of the challenge for the Indian bellows industry  →", fontsize=10)
    ax.set_ylabel("Can Iwatani address it?  →", fontsize=10)
    ax.set_xlim(3.6, 10.7)
    ax.set_ylim(0.2, 11.0)
    ax.set_title(
        "Chart 24 — India's challenges, sorted by whether Iwatani can do anything about them\n"
        "The four in the top-right corner ARE the value proposition",
        fontsize=12.4, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.055,
             "Positions are our judgement, informed by the evidence in files 04, 08 and 10 — they are a prioritisation aid for the monthly\n"
             "meeting, not a measurement. READING: the top-right cluster (no domestic PH grades, tolerance gap, MOQ mismatch, sub-0.05 mm\n"
             "foil) are all MATERIAL SUPPLY problems, which is exactly what a stainless trading division exists to solve. The bottom-right\n"
             "cluster (small domestic market, demand located offshore, sub-scale manufacturers, qualification infrastructure) cannot be\n"
             "fixed by Iwatani and must instead be designed around — which is what the two-track strategy does.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "24-india-challenges.png")


if __name__ == "__main__":
    chart23(); chart24()
    print("\nDriver charts written to", OUT)
