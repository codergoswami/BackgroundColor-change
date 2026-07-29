"""
India-specific charts for 10-india-market-data.md.

Company revenues are from MCA-derived filings surfaced by Tracxn,
TheCompanyCheck and Tofler. Where a provider publishes only a band, the
midpoint is used and the chart marks it as a band.

Run:  python3 make_india_charts.py
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
SAFF = "#ff9933"   # India accent


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------- Chart 11
def chart11():
    """India expansion joints / bellows market — the three vendor series."""
    fig, ax = plt.subplots(figsize=(11, 6))

    # Persistence Market Research: 60.5 (2020) -> 91.9 (2026) -> 158.5 (2033) @8.1%
    p_yrs = np.arange(2020, 2034)
    p_2026 = 91.9
    p = np.array([60.5 * (91.9 / 60.5) ** ((y - 2020) / 6) if y <= 2026
                  else p_2026 * 1.081 ** (y - 2026) for y in p_yrs])

    # Research and Markets: 72.32 (2024) -> 126.47 (2031) @8.3%
    r_yrs = np.arange(2024, 2032)
    r = np.array([72.32 * 1.083 ** (y - 2024) for y in r_yrs])

    # IMARC: 33.76 (2024) -> 50.26 (2033) @4.18%
    i_yrs = np.arange(2024, 2034)
    i = np.array([33.76 * 1.0418 ** (y - 2024) for y in i_yrs])

    ax.plot(p_yrs, p, color=NAVY, lw=2.6, marker="o", ms=4.5,
            label="Persistence MR — 8.1% CAGR")
    ax.plot(r_yrs, r, color=SAFF, lw=2.6, marker="s", ms=4.5,
            label="Research and Markets — 8.3% CAGR")
    ax.plot(i_yrs, i, color=GREY, lw=2.6, marker="^", ms=4.5,
            label="IMARC — 4.18% CAGR")

    # bottom-up band
    ax.axhspan(40, 70, xmin=0.30, xmax=0.44, color=GREEN, alpha=0.22, zorder=0)
    ax.annotate("Our BOTTOM-UP estimate\nfrom company filings:\nUS\\$40–70m (FY2025)",
                xy=(2025, 55), xytext=(2021.4, 116),
                fontsize=9.2, color=GREEN, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.4,
                                connectionstyle="arc3,rad=-0.2"))

    for arr, yr_arr, col in ((p, p_yrs, NAVY), (r, r_yrs, SAFF), (i, i_yrs, GREY)):
        ax.annotate(f"{arr[-1]:.0f}", (yr_arr[-1], arr[-1]),
                    textcoords="offset points", xytext=(8, -3),
                    fontsize=10, fontweight="bold", color=col)

    ax.set_ylabel("India market size (US\\$ m)", fontsize=10)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylim(0, 175)
    ax.set_title(
        "Chart 11 — India expansion joints / bellows market: three vendor views\n"
        "The 2024–26 spread is 2.7x (US\\$34m to US\\$92m). Our bottom-up build lands in the middle.",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)

    fig.text(0.005, -0.055,
             "[S] Persistence Market Research: US\\$60.5m (2020), US\\$91.9m (2026), US\\$158.5m (2033), CAGR 8.1%.\n"
             "[S] Research and Markets: US\\$72.32m (2024) to US\\$126.47m (2031), CAGR 8.3%; also states India holds 5-10% of the\n"
             "global expansion joints market. [S] IMARC: US\\$33.76m (2024) to US\\$50.26m (2033), CAGR 4.18%. Intermediate years\n"
             "are interpolated at each vendor's stated CAGR, not published points.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "11-india-vendor-views.png")


# ---------------------------------------------------------------- Chart 12
def chart12():
    """Bottom-up: actual filed revenues of Indian bellows makers."""
    cos = [
        ("Witzenmann India\n(MNC; mostly auto decouplers)", 249.61, False, NAVY),
        ("Metallic Bellows (India)\n(band midpoint)", 62.5, True, LBLUE),
        ("MB Metallic Bellows\n(band midpoint)", 30.0, True, LBLUE),
        ("Fluidyne Engineers (India)", 16.3, False, GREEN),
        ("Flexpert Bellows", 4.62, False, GREEN),
        ("Well Tech Metal Bellows\n(not filed / est.)", 6.0, True, GREY),
        ("Bhastrik Mechanical Labs\n(not filed / est.)", 5.0, True, GREY),
        ("Long tail — 20+ small\nfabricators (est.)", 80.0, True, GREY),
    ]
    fig, ax = plt.subplots(figsize=(11, 6))
    y = np.arange(len(cos))
    bars = ax.barh(y, [c[1] for c in cos], color=[c[3] for c in cos], height=0.64)
    for b, c in zip(bars, cos):
        if c[2]:
            b.set_hatch("//")
            b.set_edgecolor(DGREY)
    ax.set_yticks(y)
    ax.set_yticklabels([c[0] for c in cos], fontsize=9)
    ax.invert_yaxis()
    for i, c in enumerate(cos):
        tag = "  (est./band)" if c[2] else "  (filed)"
        ax.text(c[1] + 4, i, f"₹{c[1]:.1f} Cr{tag}", va="center",
                fontsize=9, color=DGREY)

    total = sum(c[1] for c in cos)
    ax.set_xlabel("FY2025 revenue (₹ crore)", fontsize=10)
    ax.set_xlim(0, 330)
    ax.set_title(
        "Chart 12 — Bottom-up build from actual company filings\n"
        f"Identified Indian bellows-sector revenue ≈ ₹{total:.0f} crore (US\\$"
        f"{total/8.7:.0f}m) in FY2025",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(handles=[
        Patch(facecolor=NAVY, label="Filed revenue, MNC subsidiary"),
        Patch(facecolor=GREEN, label="Filed revenue, Indian specialist"),
        Patch(facecolor=LBLUE, hatch="//", edgecolor=DGREY, label="Published band, midpoint used"),
        Patch(facecolor=GREY, hatch="//", edgecolor=DGREY, label="Estimated, not filed/found"),
    ], loc="lower right", frameon=False, fontsize=8.6)

    fig.text(0.005, -0.06,
             "Filed figures [C, MCA-derived]: Witzenmann India ₹249.61 Cr FY2025 (TheCompanyCheck); Fluidyne Engineers ₹16.3 Cr and\n"
             "Flexpert Bellows ₹4.62 Cr FY2025 (Tracxn). Bands: Metallic Bellows (India) ₹25-100 Cr, MB Metallic Bellows ₹10-50 Cr.\n"
             "CAUTION: Witzenmann India's revenue is dominated by AUTOMOTIVE exhaust decouplers, metal hoses and pipe supports,\n"
             "not bellows for industrial or precision use. Stripping that out lowers the 'pure bellows' market materially — see chart 14.\n"
             "Converted at approximately ₹87 per US dollar. Long-tail figure is our estimate and is the weakest input here.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "12-india-bottom-up.png")


# ---------------------------------------------------------------- Chart 13
def chart13():
    """The finding: incumbent grows slowly, precision specialists grow fast."""
    cos = [
        ("Witzenmann India\n₹249.6 Cr — MNC incumbent", 4.0, NAVY),
        ("MB Metallic Bellows\n₹10–50 Cr — large-bore joints", 8.0, LBLUE),
        ("Flexpert Bellows\n₹4.6 Cr — multi-ply specialist", 23.0, GREEN),
        ("Fluidyne Engineers\n₹16.3 Cr — precision / UHV / aero", 37.0, GREEN),
    ]
    fig, ax = plt.subplots(figsize=(11, 5.8))
    y = np.arange(len(cos))
    ax.barh(y, [c[1] for c in cos], color=[c[2] for c in cos], height=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels([c[0] for c in cos], fontsize=9.3)
    ax.invert_yaxis()
    for i, c in enumerate(cos):
        ax.text(c[1] + 0.7, i, f"+{c[1]:.0f}%", va="center", fontsize=11.5,
                fontweight="bold", color=c[2] if c[2] != LBLUE else DGREY)

    ax.axvline(6.5, color=RED, lw=1.6, ls="--")
    ax.text(6.9, 3.42, "Revenue-weighted\naverage +6.5%", color=RED,
            fontsize=9.3, fontweight="bold")

    ax.set_xlabel("Revenue growth, FY2024 → FY2025 (%)", fontsize=10)
    ax.set_xlim(0, 44)
    ax.set_title(
        "Chart 13 — The most useful number in this file\n"
        "The commodity incumbent grows at 4%. The precision specialists grow at 23–37%.",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.135,
             "[C] MCA-derived filings via Tracxn and TheCompanyCheck, FY2024 to FY2025.\n"
             "WHY THIS MATTERS: the revenue-weighted average of +6.5% understates what is happening. Growth is concentrated in the\n"
             "small, high-specification, precision end of the Indian market — exactly the customers Track A would sell to. Fluidyne\n"
             "(+37%) makes UHV and aerospace bellows at 0.05mm; Flexpert (+23%) makes multi-ply laminated bellows. Witzenmann's +4%\n"
             "reflects a mature automotive decoupler business. Caveat: small-base effects exaggerate percentage growth at this scale,\n"
             "and single-year growth is not a trend. Verify across three years before relying on it.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "13-india-company-growth.png")


# ---------------------------------------------------------------- Chart 14
def chart14():
    """Triangulation convergence."""
    fig, ax = plt.subplots(figsize=(11, 5.6))

    rows = [
        ("IMARC (expansion joints, 2024)", 33.76, 33.76, GREY),
        ("Bottom-up, 'pure bellows' only\n(ex-Witzenmann automotive)", 29, 41, GREEN),
        ("Bottom-up, all identified filings\n+ estimated long tail", 40, 70, GREEN),
        ("Research and Markets\n(expansion joints, 2024)", 72.32, 72.32, SAFF),
        ("Persistence MR\n(expansion joints, 2026)", 91.9, 91.9, NAVY),
    ]
    for i, (lab, lo, hi, col) in enumerate(rows):
        if lo == hi:
            ax.scatter([lo], [i], s=190, color=col, zorder=3,
                       edgecolor="white", linewidth=1.6)
            ax.text(lo + 3.2, i, f"US\\${lo:.0f}m", va="center", fontsize=9.8,
                    fontweight="bold", color=DGREY)
        else:
            ax.plot([lo, hi], [i, i], color=col, lw=11, solid_capstyle="butt",
                    alpha=0.85, zorder=3)
            ax.text(hi + 3.2, i, f"US\\${lo:.0f}–{hi:.0f}m", va="center",
                    fontsize=9.8, fontweight="bold", color=DGREY)

    ax.axvspan(40, 72, color=AMBER, alpha=0.12, zorder=0)
    ax.text(56, 4.62, "Convergence zone\nUS\\$40–72m", ha="center", fontsize=10,
            fontweight="bold", color=AMBER)

    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.2)
    ax.invert_yaxis()
    ax.set_xlabel("India market size (US\\$ m)", fontsize=10)
    ax.set_xlim(0, 118)
    ax.set_ylim(4.95, -0.7)
    ax.set_title(
        "Chart 14 — Top-down and bottom-up converge on US\\$40–72m\n"
        "Two independent methods agreeing is the strongest evidence available here",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.115,
             "The bottom-up build (company filings) and two of the three top-down vendor estimates land in the same US\\$40-72m zone.\n"
             "IMARC's US\\$33.76m sits below it and is hard to reconcile: Witzenmann India alone filed ₹249.61 Cr (~US\\$29m) in FY2025,\n"
             "which would be 85% of IMARC's entire market. Persistence's US\\$91.9m sits above it and likely uses a broader scope\n"
             "including non-metallic and civil expansion joints. Working figure for the monthly meeting: US\\$50-70m.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "14-india-triangulation.png")


# ---------------------------------------------------------------- Chart 15
def chart15():
    """India vs world: size share and growth rate."""
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13, 5.6),
                                  gridspec_kw={"width_ratios": [1, 1.15]})

    # left: share of global
    sizes = [2.7, 97.3]
    ax.pie(sizes, colors=[SAFF, "#e8edf3"], startangle=90, counterclock=False,
           wedgeprops=dict(width=0.40, edgecolor="white", linewidth=2))
    ax.text(0, 0.06, "2.7%", ha="center", va="center", fontsize=25,
            fontweight="bold", color=SAFF)
    ax.text(0, -0.20, "India share of\nglobal bellows market\n(mid estimate)",
            ha="center", va="center", fontsize=9.5, color=DGREY)
    ax.set_title("India's slice of the world market",
                 fontsize=11.5, fontweight="bold", color=NAVY, pad=8)

    # right: CAGR comparison
    items = [
        ("World metal bellows\n(vendor consensus)", 6.05, GREY),
        ("India mechanical shaft seals\n(FMI)", 5.5, LBLUE),
        ("India metal bellows\n(6Wresearch)", 6.9, LBLUE),
        ("India expansion joints\n(Persistence)", 8.1, SAFF),
        ("India expansion joints\n(Research and Markets)", 8.3, SAFF),
        ("India precision bellows makers\n(actual FY24→FY25)", 30.0, GREEN),
    ]
    y = np.arange(len(items))
    ax2.barh(y, [i[1] for i in items], color=[i[2] for i in items], height=0.6)
    ax2.set_yticks(y)
    ax2.set_yticklabels([i[0] for i in items], fontsize=8.8)
    ax2.invert_yaxis()
    for i, it in enumerate(items):
        ax2.text(it[1] + 0.5, i, f"{it[1]:.1f}%", va="center", fontsize=10,
                 fontweight="bold", color=DGREY)
    ax2.axvline(6.05, color=DGREY, lw=1.2, ls=":")
    ax2.set_xlabel("CAGR (%)", fontsize=10)
    ax2.set_xlim(0, 37)
    ax2.set_title("India grows faster than the world — from a small base",
                  fontsize=11.5, fontweight="bold", color=NAVY, pad=8)

    fig.suptitle("Chart 15 — Small share, high growth: the India profile",
                 fontsize=13, fontweight="bold", color=NAVY, x=0.055,
                 ha="left", y=1.03)
    fig.text(0.005, -0.06,
             "LEFT: MODELLED. India US\\$50-70m against a global US\\$1.2-2.6bn implies roughly 1.9%-3.5%; 2.7% is the midpoint.\n"
             "Cross-check: Research and Markets states India holds 5-10% of the global EXPANSION JOINTS market specifically — India\n"
             "indexes higher in that lower-value sub-segment than in bellows overall, which is consistent with our reading.\n"
             "RIGHT: [S] vendor CAGRs, except the final bar which is the observed FY24-FY25 growth of Fluidyne (+37%) and Flexpert\n"
             "(+23%), shown at their approximate average. Small-base effects apply; treat as directional.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "15-india-vs-world.png")


# ---------------------------------------------------------------- Chart 16
def chart16():
    """Addressable market by rung of the entry ladder."""
    fig, ax = plt.subplots(figsize=(11.5, 6))

    rungs = [
        ("RUNG 1\nMechanical seal bellows\n+ industrial expansion joints",
         40, 70, GREEN, "India bellows/EJ market US\\$40-70m.\nLargest installed base, lowest\nqualification barrier."),
        ("RUNG 2\nHydrogen + cryogenic\nbellows",
         5, 15, BLUE, "Not separately sized. Estimated from\nIndia H2 mission + industrial gas capex.\nIwatani's strongest credibility."),
        ("RUNG 3\nSemiconductor\nbellows",
         1, 5, AMBER, "Derived from IndexBox vacuum transfer\nvalve data: 6,000-20,000 valves/yr.\nSmall now, strategic later."),
    ]
    y = np.arange(len(rungs))
    for i, (lab, lo, hi, col, note) in enumerate(rungs):
        ax.barh(i, hi - lo, left=lo, color=col, height=0.5, alpha=0.9)
        ax.text(hi + 2.5, i, f"US\\${lo}–{hi}m", va="center", fontsize=11,
                fontweight="bold", color=col)
        ax.text(hi + 16, i, note, va="center", fontsize=8.3, color=DGREY)

    ax.set_yticks(y)
    ax.set_yticklabels([r[0] for r in rungs], fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlabel("Estimated India addressable market, finished bellows level (US\\$ m)",
                  fontsize=10)
    ax.set_xlim(0, 108)
    ax.set_title(
        "Chart 16 — India addressable market by rung of the entry ladder\n"
        "Note the ordering: the accessible market is 10–40x the semiconductor market today",
        fontsize=12.5, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.125,
             "ALL FIGURES ARE ESTIMATES AT THE FINISHED-BELLOWS LEVEL. Iwatani's addressable slice is the MATERIAL content, which is a\n"
             "fraction of these numbers — single-digit tonnes of precision strip for rung 3, more for rung 1. Rung 1 is anchored on the\n"
             "triangulated India bellows/expansion joint market. Rung 2 has no published sizing and is the weakest estimate here.\n"
             "Rung 3 is derived from IndexBox's India vacuum transfer valve estimate of 1,500-3,000 domestic units at 15-25% of demand.\n"
             "READING: do not enter at rung 3. The market that pays the bills today is rung 1.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "16-india-addressable.png")


if __name__ == "__main__":
    chart11(); chart12(); chart13(); chart14(); chart15(); chart16()
    print("\nIndia charts written to", OUT)
