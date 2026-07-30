"""
Charts for the reframed Aerospace, Space & Defence growth driver.

Run:  python3 make_defence_charts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, FancyBboxPatch, FancyArrowPatch
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


# ---------------------------------------------------------------- Chart 32
def chart32():
    """Defence production and exports trajectory, actual to target."""
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13.5, 6))

    yrs = ["FY15", "FY21", "FY24", "FY25", "FY26", "FY29 (target)"]
    prod = [46429/1e5, 84643/1e5, 127434/1e5, 154000/1e5, 178000/1e5, 300000/1e5]
    actual = [True, True, True, True, True, False]
    bars = ax.bar(yrs, prod, color=[NAVY if a else LBLUE for a in actual],
                  hatch=["" if a else "//" for a in actual],
                  edgecolor=["none" if a else BLUE for a in actual], width=0.62)
    for b, v in zip(bars, prod):
        ax.text(b.get_x() + b.get_width()/2, v + 0.05, f"{v:.2f}",
                ha="center", fontsize=9.5, fontweight="bold", color=NAVY)
    ax.set_ylabel("Defence production (₹ lakh crore)", fontsize=10)
    ax.set_ylim(0, 3.4)
    ax.set_title("Defence production: already past\nhalfway to the FY29 target",
                 fontsize=11.5, fontweight="bold", color=NAVY, pad=8)
    ax.legend(handles=[Patch(facecolor=NAVY, label="Actual"),
                       Patch(facecolor=LBLUE, hatch="//", edgecolor=BLUE, label="Target")],
              loc="upper left", frameon=False, fontsize=8.8)
    ax.tick_params(axis="x", labelsize=8.6, rotation=15)

    yrs2 = ["FY14", "FY26", "FY29\n(target)"]
    exp = [686/1e4, 38424/1e4, 50000/1e4]
    actual2 = [True, True, False]
    bars2 = ax2.bar(yrs2, exp, color=[GREEN if a else "#a8dbb8" for a in actual2],
                    hatch=["" if a else "//" for a in actual2],
                    edgecolor=["none" if a else "#1a7f37" for a in actual2], width=0.55)
    for b, v in zip(bars2, exp):
        ax2.text(b.get_x() + b.get_width()/2, v + 0.15, f"₹{v:.2f} lakh cr" if v > 1 else f"₹{v*1e4:.0f} cr",
                 ha="center", fontsize=9.5, fontweight="bold", color="#1a7f37")
    ax2.set_ylabel("Defence exports (₹ lakh crore)", fontsize=10)
    ax2.set_ylim(0, 6.2)
    ax2.set_title("Defence exports: 56x growth in\na decade, private share rising",
                  fontsize=11.5, fontweight="bold", color="#1a7f37", pad=8)
    ax2.legend(handles=[Patch(facecolor=GREEN, label="Actual"),
                        Patch(facecolor="#a8dbb8", hatch="//", edgecolor="#1a7f37", label="Target")],
               loc="upper left", frameon=False, fontsize=8.8)

    fig.suptitle("Chart 32 — India's defence industrial base: government targets, not analyst forecasts",
                 fontsize=13, fontweight="bold", color=NAVY, x=0.055, ha="left", y=1.02)
    fig.text(0.005, -0.09,
             "[P/C] Ministry of Defence / PIB / Rajnath Singh statements, FY2025-26 review. Production: ₹46,429 cr (FY15) -> ₹84,643 cr\n"
             "(FY21) -> ₹1,27,434 cr (FY24) -> ~₹1.54 lakh cr (FY25) -> ₹1.78 lakh cr (FY26, +15.6% y/y) -> ₹3 lakh cr target (FY29).\n"
             "Private sector share of production reached an all-time high of 24% (~₹42,000 cr) in FY26, up from 22% in FY25, and has\n"
             "nearly tripled since FY17. Exports: ₹686 cr (FY14) -> ₹38,424 cr (FY26, +63% y/y) -> ₹50,000 cr target (FY29).",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "32-defence-production-exports.png")


# ---------------------------------------------------------------- Chart 33
def chart33():
    """Space budget growth and composition."""
    fig, ax = plt.subplots(figsize=(11.5, 6.2))

    heads = ["Space\nTechnology", "Space\nApplications", "Space\nSciences",
             "INSAT\nSystems", "IN-SPACe", "NSIL\n(commercial)"]
    fy26 = [9602, 1600, 480, 140, 175, 900]
    fy27 = [10397.06, 1725.06, 569.76, 130.93, 194.57, 1403]

    x = np.arange(len(heads))
    w = 0.36
    ax.bar(x - w/2, fy26, w, color=GREY, alpha=0.75, label="FY2025-26 (RE)")
    ax.bar(x + w/2, fy27, w, color=BLUE, label="FY2026-27 (BE)")
    for i, (a, b) in enumerate(zip(fy26, fy27)):
        ax.text(i - w/2, a + 120, f"{a:,.0f}", ha="center", fontsize=7.6, color=DGREY)
        ax.text(i + w/2, b + 120, f"{b:,.0f}", ha="center", fontsize=7.6,
                color=BLUE, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(heads, fontsize=9)
    ax.set_ylabel("Allocation (₹ crore)", fontsize=10)
    ax.set_title(
        "Chart 33 — India's space budget: ₹13,705.63 crore for 2026-27,\n"
        "capital spend up as Gaganyaan and NGLV move to hardware realisation",
        fontsize=12.2, fontweight="bold", loc="left", color=NAVY, pad=14)
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
    ax.set_ylim(0, 11800)

    fig.text(0.005, -0.08,
             "[P] Union Budget 2026-27, Department of Space. Total outlay ₹13,705.63 crore (+2% over FY26 BE), of which capital\n"
             "expenditure ₹6,375.92 crore (+20% over FY26 RE) — signalling the shift from preparatory work to hardware for Gaganyaan,\n"
             "the Next Generation Launch Vehicle, and planetary missions (Chandrayaan-4, LUPEX, Venus Orbiter). NSIL budgetary support\n"
             "rises to ₹1,403 crore to drive commercial revenue through private-sector production and technology transfer.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "33-space-budget.png")


# ---------------------------------------------------------------- Chart 34
def chart34():
    """Proof point: Fluidyne's documented strategic sector footprint."""
    fig, ax = plt.subplots(figsize=(13, 7.4))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7.4)
    ax.axis("off")

    ax.text(0.3, 7.05,
            "Chart 34 — This is not hypothetical: an Indian bellows maker already supplies India's fighter jet programme",
            fontsize=13.6, fontweight="bold", color=NAVY)
    ax.text(0.3, 6.68,
            "Fluidyne Engineers (India) Pvt Ltd, Mysuru — registrations, recognitions and named programme deliveries, from the company's own site",
            fontsize=9.6, color=DGREY)

    # left: registrations
    ax.add_patch(FancyBboxPatch((0.3, 0.9), 5.9, 5.5, boxstyle="round,pad=0.08",
                                facecolor="#eef4ff", edgecolor=BLUE, linewidth=1.6))
    ax.text(0.62, 6.10, "REGISTERED VENDOR TO", fontsize=10.5, fontweight="bold",
            color=BLUE)
    regs = ["DGQA — Directorate General of Quality Assurance",
            "ISRO — Indian Space Research Organisation",
            "HAL — Hindustan Aeronautics Limited",
            "BARC — Bhabha Atomic Research Centre",
            "NPCIL — Nuclear Power Corporation of India",
            "BEL — Bharat Electronics Limited",
            "BHEL — Bharat Heavy Electricals Limited",
            "MDL — Mazagon Dock Shipbuilders Limited",
            "IRS — Indian Register of Shipping",
            "EIL, PDIL, ILP, Indian Coast Guard, Ship Building Centre"]
    yy = 5.72
    for r in regs:
        ax.text(0.66, yy, "\u2022  " + r, fontsize=9.2, color="#1a1a1a", va="center")
        yy -= 0.45

    # right: named deliveries
    ax.add_patch(FancyBboxPatch((6.5, 0.9), 6.2, 5.5, boxstyle="round,pad=0.08",
                                facecolor="#eefaf0", edgecolor=GREEN, linewidth=1.6))
    ax.text(6.82, 6.10, "NAMED PROGRAMME DELIVERIES", fontsize=10.5,
            fontweight="bold", color="#1a7f37")

    items = [
        ("HAL Nasik honour",
         "Precision pipe bending for LCA Mk1A\n(Tejas) and HTT-40 trainer aircraft"),
        ("SIATI award",
         "Indigenous development of metallic\nbellows for frontline trainer aircraft"),
        ("IDEMI recognition",
         "Precision welding, Inconel to SS304,\nfor BARC"),
        ("Materials qualified",
         "Titanium bellows supplied to valve\nmanufacturers and atomic energy\nresearch organisations"),
        ("Industry ranking",
         "Top 10 Expansion Joint Manufacturers,\nIndustry Outlook"),
    ]
    yy = 5.62
    for head, body in items:
        ax.add_patch(FancyBboxPatch((6.78, yy - 0.72), 5.62, 0.86,
                                    boxstyle="round,pad=0.04",
                                    facecolor="white", edgecolor="#bfe5c8",
                                    linewidth=1.1))
        ax.text(6.94, yy - 0.10, head, fontsize=9.4, fontweight="bold",
                color="#1a7f37", va="center")
        ax.text(6.94, yy - 0.44, body, fontsize=8.3, color=DGREY,
                va="center", linespacing=1.4)
        yy -= 1.00

    ax.text(6.5, 0.55,
            "Source: fluidyneengineers.com/certification.php, fluidyneengineers.com/about.php — company's own published record [P]",
            fontsize=7.4, color=GREY)

    save(fig, "34-fluidyne-proof-point.png")


# ---------------------------------------------------------------- Chart 35
def chart35():
    """AMCA / engine programme timeline showing the qualification window."""
    fig, ax = plt.subplots(figsize=(13, 5.6))

    events = [
        (2025, "AMCA execution model\ncleared (May 2025)", NAVY),
        (2026, "Vendor/partner\nselection underway", BLUE),
        (2028, "AMCA prototype\nrollout targeted", BLUE),
        (2030, "Indigenous 120kN engine\ncore test (Safran/RR bid)", AMBER),
        (2034, "AMCA first flight\n/ engine flight test", AMBER),
        (2036, "AMCA serial production\n+ indigenous engine\nenters production", GREEN),
    ]
    yrs = [e[0] for e in events]
    ax.hlines(0, 2024, 2037, color=GREY, lw=2, zorder=1)
    for i, (yr, lab, col) in enumerate(events):
        ax.scatter([yr], [0], s=170, color=col, zorder=3, edgecolor="white", linewidth=2)
        ax.annotate(lab, (yr, 0), textcoords="offset points",
                    xytext=(0, 32 if i % 2 == 0 else -46), ha="center",
                    fontsize=8.6, color=col, fontweight="bold", linespacing=1.4)
        ax.plot([yr, yr], [0, 0.28 if i % 2 == 0 else -0.28], color=col, lw=1.2, alpha=0.5)

    ax.axvspan(2025, 2036, color=GREEN, alpha=0.06, zorder=0)
    ax.text(2030.5, -0.85, "an 11-YEAR SUPPLIER-QUALIFICATION WINDOW is now open —\nvendor base for the AMCA private-industry supply chain is being built now",
            ha="center", fontsize=9.6, color="#1a7f37", fontweight="bold", linespacing=1.5)

    ax.set_ylim(-1.1, 0.75)
    ax.set_xlim(2024, 2037)
    ax.set_yticks([])
    ax.set_xticks(range(2025, 2038, 2))
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_title(
        "Chart 35 — India's fighter engine programme opens an 11-year supplier qualification window\n"
        "AMCA private-sector supply chain (Godrej Aerospace, Tata Advanced Systems, Bharat Forge) is being assembled now",
        fontsize=12, fontweight="bold", loc="left", color=NAVY, pad=16)

    fig.text(0.005, -0.05,
             "[C] Ministry of Defence approved the AMCA execution model in May 2025 (~₹15,000 crore development cost), opening the\n"
             "programme to private and state industry. AMCA Mk1 uses the imported GE F414; the AMCA Mk2 indigenous 120kN-class engine\n"
             "is being co-developed with Safran or Rolls-Royce, targeting a core test by 2030, first flight 2034, production 2036.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "35-amca-timeline.png")


if __name__ == "__main__":
    chart32(); chart33(); chart34(); chart35()
    print("\nDefence/space/aerospace charts written to", OUT)
