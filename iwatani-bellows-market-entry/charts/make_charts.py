"""
Generates the chart set for 09-market-research-bellows.md.

Every data point traces to a source listed in 06-source-register.md or in the
markdown chart captions. Modelled figures are labelled as such on the chart
itself so they cannot be mistaken for sourced data when the image is reused
in a slide deck.

Run:  python3 make_charts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "-",
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


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------- Chart 1
# Vendor disagreement on market level
def chart1():
    data = [
        ("Expert Market Research", 0.291, "Welded only", 2024),
        ("Dataintelo", 0.409, "Edge-welded only", 2025),
        ("Dataintelo", 0.920, "Hydroformed only", 2025),
        ("Zion Market Research", 1.105, "All metal bellows", 2024),
        ("Dataintelo", 1.800, "Welded only", 2025),
        ("GII / IRES", 1.940, "All metal bellows", 2025),
        ("Strategic Market Research", 2.120, "All metal bellows", 2024),
        ("Market Data Forecast", 2.390, "All metal bellows", 2024),
        ("SkyQuest / GII", 5.400, "Welded only", 2024),
        ("Market Research Future", 5.638, "Welded only", 2024),
    ]
    colours = {
        "All metal bellows": NAVY,
        "Welded only": RED,
        "Edge-welded only": BLUE,
        "Hydroformed only": LBLUE,
    }

    fig, ax = plt.subplots(figsize=(10.5, 6.2))
    y = np.arange(len(data))
    vals = [d[1] for d in data]
    cols = [colours[d[2]] for d in data]
    ax.barh(y, vals, color=cols, height=0.66)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{d[0]}  ({d[3]})" for d in data], fontsize=9.5)
    ax.invert_yaxis()

    for i, v in enumerate(vals):
        ax.text(v + 0.08, i, f"\\${v:.3f}bn".replace("$0.", "$0."),
                va="center", fontsize=9, color=DGREY)

    # highlight the contradiction
    ax.annotate(
        "These two measure a SUB-SET of the market\nyet report 2–5x the ALL-market estimates",
        xy=(5.4, 8.5), xytext=(3.15, 6.15),
        fontsize=9, color=RED, ha="left",
        arrowprops=dict(arrowstyle="->", color=RED, lw=1.2,
                        connectionstyle="arc3,rad=-0.25"))

    ax.set_xlabel("Reported market size (US\$ bn)", fontsize=10)
    ax.set_xlim(0, 6.9)
    ax.set_title(
        "Chart 1 — The commercial estimates do not agree, and cannot all be right\n"
        "Global metal bellows market, base-year values as published",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    handles = [Patch(facecolor=c, label=k) for k, c in colours.items()]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.115),
              ncol=4, frameon=False, fontsize=9)

    fig.text(0.005, -0.175,
             "Spread across 'welded only' estimates alone: \$0.291bn to \$5.638bn — a factor of 19.\n"
             "Sources: Expert Market Research; Dataintelo; Zion Market Research; GII/IRES; Strategic Market Research;\n"
             "Market Data Forecast; SkyQuest via GII; Market Research Future. All [S] grade — commercial vendor pages.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "01-vendor-disagreement.png")


# ---------------------------------------------------------------- Chart 2
# Level vs CAGR: they disagree on size, agree on growth
def chart2():
    pts = [
        ("Zion", 1.105, 5.19, "All"),
        ("GII / IRES", 1.940, 5.79, "All"),
        ("Strategic MR", 2.120, 6.90, "All"),
        ("Market Data Fcst", 2.390, 5.74, "All"),
        ("Mkt Research Future", 5.638, 5.60, "Welded"),
        ("SkyQuest", 5.400, 6.90, "Welded"),
        ("Dataintelo", 1.800, 6.20, "Welded"),
        ("Expert MR", 0.291, 5.90, "Welded"),
        ("Dataintelo", 0.409, 6.20, "Edge-welded"),
        ("Dataintelo", 0.920, 6.80, "Hydroformed"),
    ]
    cmap = {"All": NAVY, "Welded": RED, "Edge-welded": BLUE, "Hydroformed": LBLUE}

    fig, ax = plt.subplots(figsize=(10, 5.8))
    ax.axhspan(5.19, 6.90, color=GREEN, alpha=0.09, zorder=0)
    ax.axhline(6.05, color=GREEN, lw=1.1, ls="--", zorder=1)
    ax.text(6.55, 6.12, "CAGR consensus band 5.2 – 6.9%",
            color=GREEN, fontsize=9.5, fontweight="bold", ha="right")

    for name, lvl, cagr, scope in pts:
        ax.scatter(lvl, cagr, s=135, color=cmap[scope], zorder=3,
                   edgecolor="white", linewidth=1.2)
        ax.annotate(name, (lvl, cagr), textcoords="offset points",
                    xytext=(0, 11), ha="center", fontsize=8.2, color=DGREY)

    ax.annotate("", xy=(0.291, 4.72), xytext=(5.638, 4.72),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
    ax.text(2.96, 4.58, "Level disagreement: 19x", color=RED,
            fontsize=10, fontweight="bold", ha="center")

    ax.set_xlabel("Reported market size (US\$ bn)", fontsize=10)
    ax.set_ylabel("Reported CAGR (%)", fontsize=10)
    ax.set_ylim(4.35, 7.6)
    ax.set_xlim(-0.25, 6.6)
    ax.set_title(
        "Chart 2 — Vendors agree on the growth rate and disagree on the size\n"
        "Use the CAGR. Do not use the absolute values.",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)
    handles = [Patch(facecolor=c, label=k) for k, c in cmap.items()]
    ax.legend(handles=handles, loc="upper right", frameon=False, fontsize=9,
              title="Scope", title_fontsize=9)
    fig.text(0.005, -0.055,
             "Every vendor lands between 5.2% and 6.9% CAGR while disagreeing on level by a factor of 19.\n"
             "Reading: growth rate is the only reliable output of this literature. Sources as Chart 1, all [S] grade.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "02-level-vs-cagr.png")


# ---------------------------------------------------------------- Chart 3
# Modelled consensus band 2020-2035
def chart3():
    yrs = np.arange(2020, 2036)
    # Anchored on the three "all metal bellows" estimates, grown at the
    # consensus CAGR band. 2025 anchors: low 1.16, mid 2.00, high 2.55
    lo25, mid25, hi25 = 1.16, 2.00, 2.55
    g_lo, g_mid, g_hi = 0.0519, 0.0605, 0.0690

    def series(a25, g):
        return np.array([a25 * (1 + g) ** (y - 2025) for y in yrs])

    lo, mid, hi = series(lo25, g_lo), series(mid25, g_mid), series(hi25, g_hi)

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.fill_between(yrs, lo, hi, color=BLUE, alpha=0.16, label="Plausible range")
    ax.plot(yrs, mid, color=NAVY, lw=2.6, label="Mid case (6.05% CAGR)")
    ax.plot(yrs, lo, color=GREY, lw=1.2, ls="--")
    ax.plot(yrs, hi, color=GREY, lw=1.2, ls="--")

    ax.axvline(2025.5, color=DGREY, lw=1, ls=":")
    ax.text(2025.2, hi.max() * 0.97, "actual/base", ha="right", fontsize=9, color=DGREY)
    ax.text(2025.8, hi.max() * 0.97, "forecast", ha="left", fontsize=9, color=DGREY)

    for yr in (2020, 2025, 2030, 2035):
        i = list(yrs).index(yr)
        ax.scatter([yr], [mid[i]], s=52, color=NAVY, zorder=4, edgecolor="white")
        ax.annotate(f"\\${mid[i]:.2f}bn", (yr, mid[i]), textcoords="offset points",
                    xytext=(0, 13), ha="center", fontsize=9.5,
                    fontweight="bold", color=NAVY)

    ax.set_ylabel("Global metal bellows market (US\$ bn)", fontsize=10)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_title(
        "Chart 3 — Modelled consensus view, 2020–2035\n"
        "MODELLED, not sourced: consensus CAGR band applied to the three 'all metal bellows' estimates",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax.set_xticks(np.arange(2020, 2036, 3))

    fig.text(0.005, -0.05,
             "MODEL, NOT A SOURCE. Built by applying the 5.19%–6.90% vendor CAGR band to 2024–25 'all metal bellows'\n"
             "anchors (Zion \$1.105bn, GII/IRES \$1.94bn, Strategic MR \$2.12bn, Market Data Forecast \$2.39bn). Shown because\n"
             "no single vendor series is trustworthy on its own. Treat the band width as the real answer, not the mid line.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "03-consensus-band.png")


# ---------------------------------------------------------------- Chart 4
# SEMI actuals + forecast
def chart4():
    yrs = ["2021", "2022", "2023", "2024", "2025", "2026f", "2027f*", "2028f"]
    vals = [102.64, 107.64, 106.30, 117.14, 135.06, 165.90, 195.10, 229.50]
    actual = [True, True, True, True, True, False, False, False]

    fig, ax = plt.subplots(figsize=(11, 6))
    bars = ax.bar(yrs, vals,
                  color=[NAVY if a else LBLUE for a in actual],
                  hatch=["" if a else "//" for a in actual],
                  edgecolor=["none" if a else BLUE for a in actual],
                  width=0.66)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 3.5, f"{v:.1f}",
                ha="center", fontsize=10, fontweight="bold", color=NAVY)

    yoy = ["", "+4.9%", "-1.3%", "+10.2%", "+15.0%", "+23.2%", "", ""]
    for b, t in zip(bars, yoy):
        if t:
            ax.text(b.get_x() + b.get_width() / 2, 6, t, ha="center",
                    fontsize=9, color="white", fontweight="bold")

    ax.set_ylabel("Total semiconductor equipment billings (US\$ bn)", fontsize=10)
    ax.set_ylim(0, 258)
    ax.set_title(
        "Chart 4 — The actual demand driver, from the industry's own association\n"
        "Global semiconductor manufacturing equipment: SEMI / SEAJ actuals and SEMI forecast",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(handles=[Patch(facecolor=NAVY, label="Actual (SEMI/SEAJ WWSEMS)"),
                       Patch(facecolor=LBLUE, hatch="//", edgecolor=BLUE,
                             label="Forecast (SEMI Mid-Year, 14 Jul 2026)")],
              loc="upper left", frameon=False, fontsize=9.5)

    fig.text(0.005, -0.05,
             "[P] PRIMARY DATA. Actuals: SEMI/SEAJ Worldwide Semiconductor Equipment Market Statistics — 2021 \$102.6bn,\n"
             "2022 \$107.6bn, 2023 \$106.3bn, 2024 \$117.1bn, 2025 \$135.1bn. Forecast: SEMI Mid-Year Total Equipment Forecast,\n"
             "14 Jul 2026 — 2026 \$165.9bn, 2028 \$229.5bn.  *2027 is geometrically interpolated between the two published\n"
             "forecast points and is NOT a SEMI figure.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "04-semi-equipment.png")


# ---------------------------------------------------------------- Chart 5
# Growth rate ladder
def chart5():
    items = [
        ("Global stainless steel production\n(worldstainless, 2025 actual)", 2.1, GREY, "[P]"),
        ("Global metal bellows market\n(vendor consensus mid)", 6.05, BLUE, "[S]"),
        ("Edge-welded bellows sub-segment\n(Dataintelo)", 6.50, BLUE, "[S]"),
        ("Semiconductor equipment\n(SEMI, 2025 actual)", 15.0, GREEN, "[P]"),
        ("Semiconductor equipment\n(SEMI, 2026 forecast)", 23.2, GREEN, "[P]"),
    ]
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    y = np.arange(len(items))
    ax.barh(y, [i[1] for i in items], color=[i[2] for i in items], height=0.62)
    ax.set_yticks(y)
    ax.set_yticklabels([i[0] for i in items], fontsize=9.5)
    ax.invert_yaxis()
    for i, it in enumerate(items):
        ax.text(it[1] + 0.4, i, f"{it[1]:.1f}%  {it[3]}", va="center",
                fontsize=10, fontweight="bold", color=DGREY)

    ax.set_xlabel("Annual growth rate (%)", fontsize=10)
    ax.set_xlim(0, 28)
    ax.set_title(
        "Chart 5 — Why the Stainless Steel Division should move up the value chain\n"
        "Commodity stainless grows at 2%. The market it feeds grows at 23%.",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    ax.annotate("", xy=(2.1, 4.62), xytext=(23.2, 4.62),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
    ax.text(12.6, 4.85, "11x growth differential", color=RED, fontsize=10.5,
            fontweight="bold", ha="center")
    ax.set_ylim(4.95, -0.6)

    fig.text(0.005, -0.055,
             "[P] worldstainless full-year 2025 melt shop production +2.1%.  [P] SEMI: equipment billings +15.0% in 2025 actual,\n"
             "+23.2% forecast for 2026.  [S] bellows CAGRs are the commercial vendor consensus band midpoint — indicative only.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "05-growth-ladder.png")


# ---------------------------------------------------------------- Chart 6
# Indexed comparison
def chart6():
    yrs = np.arange(2021, 2029)
    semi = np.array([102.64, 107.64, 106.30, 117.14, 135.06, 165.90, 195.10, 229.50])
    semi_i = semi / semi[0] * 100
    bell_i = np.array([100 * (1.0605) ** (y - 2021) for y in yrs])
    # worldstainless: 2024 62.821 Mt, 2025 64.157 Mt; ~2% trend applied
    ss_i = np.array([100 * (1.021) ** (y - 2021) for y in yrs])

    fig, ax = plt.subplots(figsize=(10.5, 6))
    ax.plot(yrs, semi_i, color=GREEN, lw=3, marker="o", ms=6,
            label="Semiconductor equipment  [P] SEMI")
    ax.plot(yrs, bell_i, color=BLUE, lw=2.4, marker="s", ms=5,
            label="Metal bellows market  [S] vendor consensus")
    ax.plot(yrs, ss_i, color=GREY, lw=2.4, marker="^", ms=5,
            label="Stainless steel production  [P] worldstainless")
    ax.axvline(2025.5, color=DGREY, lw=1, ls=":")
    ax.text(2025.42, 232, "actual", ha="right", fontsize=9, color=DGREY)
    ax.text(2025.6, 232, "forecast", ha="left", fontsize=9, color=DGREY)

    for arr, col in ((semi_i, GREEN), (bell_i, BLUE), (ss_i, GREY)):
        ax.annotate(f"{arr[-1]:.0f}", (yrs[-1], arr[-1]),
                    textcoords="offset points", xytext=(9, -3),
                    fontsize=10.5, fontweight="bold", color=col)

    ax.set_ylabel("Index, 2021 = 100", fontsize=10)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_title(
        "Chart 6 — Three markets, indexed to 2021\n"
        "The divergence is the entire strategic argument",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax.set_xlim(2020.7, 2028.9)

    fig.text(0.005, -0.05,
             "Semiconductor equipment line is SEMI/SEAJ actuals to 2025 and SEMI forecast thereafter (2027 interpolated).\n"
             "Bellows and stainless lines are trend lines at 6.05% and 2.1% respectively, not year-by-year observations.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "06-indexed-growth.png")


# ---------------------------------------------------------------- Chart 7
# End-use split
def chart7():
    labels = ["Aerospace &\ndefence", "Oil, gas &\npetrochemical",
              "Industrial, power\n& process", "Semiconductor\n& electronics",
              "Automotive", "Medical", "Other"]
    vals = [29, 18, 17, 15, 12, 5, 4]
    cols = [NAVY, "#2b5d8a", "#4a83b4", GREEN, AMBER, "#c084c0", GREY]

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13, 6),
                                  gridspec_kw={"width_ratios": [1.05, 1]})
    wedges, _, autotexts = ax.pie(
        vals, labels=None, colors=cols, startangle=90, counterclock=False,
        autopct=lambda p: f"{p:.0f}%", pctdistance=0.78,
        wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2),
        textprops=dict(fontsize=10, fontweight="bold", color="white"))
    ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(-0.28, 0.5),
              frameon=False, fontsize=9.5)
    ax.set_title("By end-use industry", fontsize=11.5, fontweight="bold",
                 color=NAVY, pad=6)
    ax.text(0, 0, "INDICATIVE\nsynthesis", ha="center", va="center",
            fontsize=10, color=DGREY, fontweight="bold")

    # right: type + material stacked
    ax2.barh([1.0], [62.4], color=BLUE, height=0.42, label="Edge-welded")
    ax2.barh([1.0], [37.6], left=[62.4], color=LBLUE, height=0.42,
             label="Seam-welded / other welded")
    ax2.text(31, 1.0, "62.4%", ha="center", va="center", color="white",
             fontweight="bold", fontsize=10.5)
    ax2.text(81, 1.0, "37.6%", ha="center", va="center", color=NAVY,
             fontweight="bold", fontsize=10.5)

    ax2.barh([0.4], [54.3], color=NAVY, height=0.42, label="Stainless steel")
    ax2.barh([0.4], [45.7], left=[54.3], color=GREY, height=0.42,
             label="Ni alloys, Ti, other")
    ax2.text(27, 0.4, "54.3%", ha="center", va="center", color="white",
             fontweight="bold", fontsize=10.5)
    ax2.text(77, 0.4, "45.7%", ha="center", va="center", color="white",
             fontweight="bold", fontsize=10.5)

    ax2.set_yticks([1.0, 0.4])
    ax2.set_yticklabels(["Welded market\nby TYPE", "Welded market\nby MATERIAL"],
                        fontsize=9.5)
    ax2.set_xlim(0, 100)
    ax2.set_xlabel("Share of welded metal bellows market (%)", fontsize=10)
    ax2.set_ylim(0.05, 1.45)
    ax2.legend(loc="upper center", bbox_to_anchor=(0.5, 1.02), ncol=2,
               frameon=False, fontsize=8.6)
    ax2.set_title("By type and material", fontsize=11.5, fontweight="bold",
                  color=NAVY, pad=6)

    fig.suptitle(
        "Chart 7 — Market segmentation: where the value sits",
        fontsize=13, fontweight="bold", color=NAVY, x=0.055, ha="left", y=1.02)

    fig.text(0.005, -0.03,
             "LEFT PANEL IS AN INDICATIVE SYNTHESIS, NOT A SINGLE SOURCE. Anchored on the points vendors do agree on:\n"
             "aerospace 27.8% (Dataintelo, welded) and 32.5% (Dataintelo, hydroformed); aerospace/defence 25–35% (SkyQuest).\n"
             "Remaining shares are apportioned judgementally. Treat as +/- 8pp. Note one vendor claim was DISCARDED as impossible:\n"
             "Market Growth Reports gives US semiconductor+electronics 48% AND aerospace+defence 56%, which sums to 104%.\n"
             "RIGHT PANEL is single-source: Dataintelo welded metal bellows — edge-welded 62.4% of type, stainless 54.3% of material. [S]",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "07-segmentation.png")


# ---------------------------------------------------------------- Chart 8
# Regional: bellows vendor disagreement + SEMI hard data
def chart8():
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13.2, 6),
                                  gridspec_kw={"width_ratios": [1, 1]})

    regions = ["Asia Pacific", "North America", "Europe", "LatAm", "MEA"]
    marketintelo = [42.8, 28.3, 19.4, 5.2, 4.3]
    zion = [41.0, 37.0, np.nan, np.nan, np.nan]
    mrfr = [20.0, 45.0, np.nan, np.nan, np.nan]

    x = np.arange(len(regions))
    w = 0.26
    ax.bar(x - w, marketintelo, w, color=NAVY, label="Marketintelo (all bellows)")
    ax.bar(x, zion, w, color=BLUE, label="Zion (all bellows)")
    ax.bar(x + w, mrfr, w, color=RED, label="Mkt Research Future (welded)")
    ax.set_xticks(x)
    ax.set_xticklabels(regions, fontsize=9, rotation=18, ha="right")
    ax.set_ylabel("Share of global market (%)", fontsize=10)
    ax.legend(frameon=False, fontsize=8.6, loc="upper right")
    ax.set_title("Bellows regional share — vendors contradict each other",
                 fontsize=11.5, fontweight="bold", color=NAVY, pad=6)
    ax.annotate("APAC: 20% or 43%?\nNA: 28% or 45%?", xy=(0.35, 46),
                fontsize=9.5, color=RED, fontweight="bold")
    ax.set_ylim(0, 56)

    # SEAJ hard regional data
    seaj_lab = ["China", "Taiwan", "S. Korea", "N. America", "Japan",
                "Rest of\nWorld*", "Europe"]
    seaj_val = [49.31, 31.50, 25.75, 10.89, 9.52, 5.23, 2.86]
    cols = [DGREY] * 5 + [GREEN, DGREY]
    bars = ax2.bar(seaj_lab, seaj_val, color=cols, width=0.66)
    for b, v in zip(bars, seaj_val):
        ax2.text(b.get_x() + b.get_width() / 2, v + 1.1, f"{v:.1f}",
                 ha="center", fontsize=9.5, fontweight="bold", color=NAVY)
    ax2.set_ylabel("2025 semiconductor equipment billings (US\$ bn)", fontsize=10)
    ax2.set_title("Semiconductor equipment by region, 2025 — hard data",
                  fontsize=11.5, fontweight="bold", color=NAVY, pad=6)
    ax2.tick_params(axis="x", labelsize=8.6)
    ax2.set_ylim(0, 58)
    ax2.annotate("*India sits inside this\n\$5.23bn bucket — 3.9% of\nglobal, shared with Singapore,\nIsrael and others",
                 xy=(5, 5.23), xytext=(3.05, 26),
                 fontsize=8.8, color=GREEN, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.3,
                                 connectionstyle="arc3,rad=0.25"))

    fig.suptitle("Chart 8 — Regional structure: unreliable for bellows, precise for equipment",
                 fontsize=13, fontweight="bold", color=NAVY, x=0.055, ha="left", y=1.02)
    fig.text(0.005, -0.045,
             "LEFT: [S] Marketintelo, Zion Market Research, Market Research Future. Blank bars = not published by that vendor.\n"
             "Data Bridge Market Research was EXCLUDED: its page states both APAC and North America 'dominated' at 38.7% in 2024.\n"
             "RIGHT: [P] SEAJ/SEMI WWSEMS, 8 Apr 2026 — 2025 billings by region, total \$135.06bn.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "08-regional.png")


# ---------------------------------------------------------------- Chart 9
# India share triangulation
def chart9():
    items = [
        ("Global stainless steel output\n(India, 2021)", 6.2, GREY, "[C]"),
        ("Asia-Pacific share of global\nbellows market", 42.8, LBLUE, "[S]"),
        ("India share of global semiconductor\nequipment spend", 0.7, GREEN, "modelled"),
        ("INDIA SHARE OF GLOBAL\nBELLOWS MARKET (estimate)", 3.0, NAVY, "MODELLED"),
    ]
    fig, ax = plt.subplots(figsize=(10.8, 5.4))
    y = np.arange(len(items))
    bars = ax.barh(y, [i[1] for i in items], color=[i[2] for i in items],
                   height=0.6)
    bars[3].set_hatch("//")
    bars[3].set_edgecolor(BLUE)
    ax.set_yticks(y)
    ax.set_yticklabels([i[0] for i in items], fontsize=9.5)
    ax.invert_yaxis()

    ann = ["6.2%", "42.8%", "<1%", "2 – 4%"]
    for i, (it, a) in enumerate(zip(items, ann)):
        ax.text(it[1] + 0.7, i, f"{a}   {it[3]}", va="center", fontsize=10,
                fontweight="bold", color=DGREY)

    ax.set_xlabel("Share of global total (%)", fontsize=10)
    ax.set_xlim(0, 52)
    ax.set_title(
        "Chart 9 — India's share of the world bellows market: roughly 2–4%\n"
        "No published source exists. This is triangulated from proxies and is a MODEL.",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.16,
             "NO VENDOR PUBLISHES AN INDIA BELLOWS NUMBER. Triangulation logic: India is ~6% of world stainless output [C, 2021];\n"
             "Asia-Pacific is 41–43% of the bellows market [S] but is dominated by China, Japan and Korea; India's semiconductor\n"
             "equipment spend is a fraction of the \$5.23bn 'Rest of World' bucket [P, SEAJ 2025], so well under 1% of global.\n"
             "India's bellows industry is weighted to expansion joints, mechanical seals and automotive decouplers — not the\n"
             "high-value semiconductor segment. Estimate: 2–4% of global by value, i.e. roughly US\$45-90m at a \$2.2bn global mid.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "09-india-share.png")


# ---------------------------------------------------------------- Chart 10
# Growth drivers waterfall-ish
def chart10():
    drivers = [
        ("AI / HBM-driven fab capex", 9.2, GREEN, "[P] SEMI: WFE \$116.9bn 2025 -> ~\$200bn 2028"),
        ("Bellows as designed-in\nconsumable (replacement)", 7.5, GREEN, "[P] SMC & VAT: 3m cycle life, user-replaceable"),
        ("Aerospace build rates &\nlong lead times", 6.5, BLUE, "[S] 16–20 wk aerospace bellows lead times"),
        ("Supply-chain regionalisation\n(non-China sourcing)", 6.0, BLUE, "[C] geopolitical de-risking"),
        ("Hydrogen economy &\nelectrolyser buildout", 5.8, BLUE, "Iwatani H2-resistant SS line [P]"),
        ("India Semicon 2.0\n(30% capex incentive)", 5.0, AMBER, "[C] ₹1,27,500cr, approved 15 Jul 2026"),
        ("Automotive: exhaust\ndecouplers & EV thermal", 4.0, AMBER, "[C] Witzenmann India: 10m+ decouplers"),
        ("Commodity stainless\nvolume growth", 2.1, GREY, "[P] worldstainless 2025: +2.1%"),
    ]
    fig, ax = plt.subplots(figsize=(12.2, 6.4))
    y = np.arange(len(drivers))
    ax.barh(y, [d[1] for d in drivers], color=[d[2] for d in drivers], height=0.62)
    ax.set_yticks(y)
    ax.set_yticklabels([d[0] for d in drivers], fontsize=9.3)
    ax.invert_yaxis()
    for i, d in enumerate(drivers):
        ax.text(d[1] + 0.18, i, d[3], va="center", fontsize=8.2, color=DGREY)
    ax.set_xlabel("Relative strength of driver  (1 = weak, 10 = strong)", fontsize=10)
    ax.set_xlim(0, 21)
    ax.set_title(
        "Chart 10 — Growth drivers ranked by strength of supporting evidence\n"
        "Green = backed by primary data · Blue = credible but unquantified · Amber = policy-dependent · Grey = weak",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)
    fig.text(0.005, -0.045,
             "Scoring is a judgement call combining market impact with the quality of available evidence. It is a prioritisation\n"
             "aid for the monthly meeting, not a measurement. The citations shown are the basis for each score.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "10-growth-drivers.png")


if __name__ == "__main__":
    chart1(); chart2(); chart3(); chart4(); chart5()
    chart6(); chart7(); chart8(); chart9(); chart10()
    print("\nAll charts written to", OUT)
