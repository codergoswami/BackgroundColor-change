"""
Redesign of the client-facing "Manufacturing process & supply chain map" slide.

Chart 30 — full redesign, 16:9, drop-in replacement
Chart 31 — stripped-down executive version

Run:  python3 make_slide_redesign.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np
import os

OUT = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({"font.family": "DejaVu Sans", "figure.dpi": 150})

NAVY = "#0d2b56"
MIDBLUE = "#2e6db4"
LBLUE = "#dce8f6"
GREEN = "#1a9c5b"
AMBER = "#e8a33d"
RED = "#d24545"
GREY = "#8b949e"
DGREY = "#4a5568"
PAPER = "#ffffff"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight",
                facecolor=PAPER, pad_inches=0.18)
    plt.close(fig)
    print("wrote", name)


def chevron(ax, x, y, w, h, label, fc, tc="white", fs=9.4, tip=0.30):
    """Chevron / arrow-shaped stage header."""
    pts = [(x, y), (x + w - tip, y), (x + w, y + h / 2),
           (x + w - tip, y + h), (x, y + h), (x + tip * 0.62, y + h / 2)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=fc,
                         edgecolor="none", zorder=3))
    ax.text(x + w / 2 + tip * 0.15, y + h / 2, label, ha="center", va="center",
            fontsize=fs, color=tc, fontweight="bold", zorder=4,
            linespacing=1.35)


def light(ax, cx, cy, status, r=0.145):
    cols = {"ok": GREEN, "part": AMBER, "gap": RED}
    marks = {"ok": "\u2713", "part": "!", "gap": "\u2717"}
    ax.add_patch(Circle((cx, cy), r, facecolor=cols[status],
                        edgecolor="white", linewidth=1.8, zorder=5))
    ax.text(cx, cy - 0.005, marks[status], ha="center", va="center",
            fontsize=11.5 if status != "part" else 12.5,
            color="white", fontweight="bold", zorder=6)


# ---------------------------------------------------------------- Chart 30
def chart30():
    fig, ax = plt.subplots(figsize=(13.33, 7.5))
    ax.set_xlim(0, 13.33)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # ---- title block
    ax.add_patch(Rectangle((0.32, 6.86), 0.075, 0.60,
                           facecolor=MIDBLUE, edgecolor="none"))
    ax.text(0.52, 7.30,
            "India can form the bellows — but cannot melt the alloy or certify the product",
            fontsize=15.2, fontweight="bold", color=NAVY, va="center")
    ax.text(0.52, 6.99,
            "Both ends of the 7-step chain depend on imports; the middle is already served locally",
            fontsize=10.4, color=DGREY, va="center")

    # ---- legend
    lx = 8.94
    ax.add_patch(FancyBboxPatch((lx, 6.44), 4.03, 0.48,
                                boxstyle="round,pad=0.05",
                                facecolor="#f6f8fb", edgecolor="#d6dee8",
                                linewidth=1))
    for i, (st, lab) in enumerate([("ok", "India capable"),
                                   ("part", "Partial gap"),
                                   ("gap", "Absent")]):
        light(ax, lx + 0.28 + i * 1.32, 6.68, st, r=0.112)
        ax.text(lx + 0.44 + i * 1.32, 6.68, lab, fontsize=8.0,
                color=DGREY, va="center")

    # ---- stages
    stages = [
        ("1\nMELT &\nCAST", "EAF → AOD → VOD\n→ slab. Grade\nchemistry fixed here",
         "part", "Jindal Stainless\n3.0 Mtpa",
         "AM350 / 631 not\nmelted in India"),
        ("2\nCOLD ROLL\nTO FOIL", "20-Hi mills to\n0.03–0.20 mm +\nbright annealing",
         "part", "Jindal SPD 0.076 mm\nIUP Jindal 0.03 mm\nQuality Foils 0.10 mm",
         "Tolerance ±0.020 mm\nvs ±0.001 mm best"),
        ("3\nPRECISION\nSLITTING", "Rotary knife to\nnarrow strip; deburr,\nround, chamfer edge",
         "ok", "IUP Jindal · Quality\nFoils — both name\nBELLOWS as an\napplication",
         "Capability exists —\nnot the bottleneck"),
        ("4\nFORMING &\nSTAMPING", "Seam-weld + hydro-\nform tube, or stamp\ndiaphragm leaves",
         "ok", "Flexpert · MB Metallic\nWitzenmann India\nFluidyne · Well Tech",
         "Well established"),
        ("5\nJOINING", "TIG / laser / micro-\nplasma ID+OD edge\nwelding of leaves",
         "ok", "Well Tech 0.05 mm\nFluidyne · Bhastrik\n— all in-house",
         "Capability proven,\nvolumes small"),
        ("6\nCLEAN, TEST\n& CERTIFY", "ISO Class 5/6 clean-\nroom · He leak test\n· RGA certificate",
         "gap", "No Indian bellows\ncleanroom or RGA\nfacility identified",
         "THE REAL BARRIER\nto semiconductor"),
        ("7\nEND USE", "Vacuum valves, seals,\nexpansion joints →\nfabs, refineries, H₂",
         "ok", "Micron · Tata Dholera\nIOCL · NTPC · ISRO\nNPCIL · SAIL",
         "Demand pull is real\nand policy-backed"),
    ]

    n = len(stages)
    left, right = 0.36, 12.97
    gap = 0.10
    w = (right - left - gap * (n - 1)) / n
    ytop = 5.06
    hh = 0.80

    xs = []
    for i, (hdr, proc, status, players, sowhat) in enumerate(stages):
        x = left + i * (w + gap)
        xs.append(x)
        fc = {"ok": MIDBLUE, "part": "#3d6fa8", "gap": "#7a3f52"}[status]
        chevron(ax, x, ytop, w, hh, hdr, fc, fs=8.5)

        # process
        ax.add_patch(FancyBboxPatch((x, ytop - 1.06), w * 0.965, 0.92,
                                    boxstyle="round,pad=0.035",
                                    facecolor="#f6f8fb", edgecolor="#d6dee8",
                                    linewidth=1))
        ax.text(x + w * 0.482, ytop - 0.60, proc, ha="center", va="center",
                fontsize=7.35, color="#1a1a1a", linespacing=1.5)

        # traffic light
        light(ax, x + w * 0.482, ytop - 1.32, status)

        # india players
        ax.add_patch(FancyBboxPatch((x, ytop - 2.52), w * 0.965, 0.94,
                                    boxstyle="round,pad=0.035",
                                    facecolor="#fff8ee" if status != "gap" else "#fdecec",
                                    edgecolor=AMBER if status != "gap" else RED,
                                    linewidth=1.1))
        ax.text(x + w * 0.482, ytop - 2.05, players, ha="center", va="center",
                fontsize=7.2, color="#1a1a1a", linespacing=1.5)

        # so what
        col = {"ok": GREEN, "part": AMBER, "gap": RED}[status]
        ax.text(x + w * 0.482, ytop - 2.86, sowhat, ha="center", va="center",
                fontsize=7.1, color=col, fontweight="bold", linespacing=1.5)


    # ---- import-dependency band, sitting directly above the affected stages
    ybar = ytop + hh + 0.12
    b1x, b1w = xs[0], (xs[1] + w) - xs[0]
    ax.add_patch(FancyBboxPatch((b1x, ybar), b1w, 0.40,
                                boxstyle="round,pad=0.035",
                                facecolor="#fdecec", edgecolor=RED, linewidth=1.3))
    ax.text(b1x + b1w / 2, ybar + 0.20,
            "\u25bc  IMPORTED  \u2014  Ulbrich · UPM · ATI · TOKKIN · Alleima · Matthey",
            ha="center", va="center", fontsize=7.4, color=RED, fontweight="bold")

    b2x, b2w = xs[5], w * 0.965
    ax.add_patch(FancyBboxPatch((b2x, ybar), b2w, 0.40,
                                boxstyle="round,pad=0.035",
                                facecolor="#fdecec", edgecolor=RED, linewidth=1.3))
    ax.text(b2x + b2w / 2, ybar + 0.20,
            "\u25bc  NOT DONE IN INDIA",
            ha="center", va="center", fontsize=7.4, color=RED, fontweight="bold")

    # ---- so-what band
    ax.add_patch(FancyBboxPatch((0.36, 0.46), 12.61, 1.44,
                                boxstyle="round,pad=0.06",
                                facecolor="#eef3fa", edgecolor=NAVY, linewidth=1.6))
    ax.text(0.62, 1.72, "IMPLICATIONS", fontsize=8.6,
            color=NAVY, fontweight="bold", va="center")
    pts = [
        ("1", "Precision slitting is NOT the gap.",
         "Both Indian precision-strip mills already slit and\nboth name bellows as a served application."),
        ("2", "The material gap is one step earlier.",
         "No Indian mill melts AM350 or 631, and published\ntolerance is 20x looser than global best."),
        ("3", "The capability gap is at the end.",
         "No Indian cleanroom, helium-leak or RGA facility —\nthis is what blocks semiconductor qualification."),
    ]
    for i, (num, head, body) in enumerate(pts):
        x = 0.72 + i * 4.16
        ax.add_patch(Circle((x, 1.30), 0.145, facecolor=NAVY, edgecolor="none"))
        ax.text(x, 1.295, num, ha="center", va="center", fontsize=9,
                color="white", fontweight="bold")
        ax.text(x + 0.26, 1.30, head, fontsize=9.1, color=NAVY,
                fontweight="bold", va="center")
        ax.text(x + 0.26, 0.84, body, fontsize=7.9, color=DGREY,
                va="center", linespacing=1.55)

    ax.text(0.36, 0.18,
            "Source: Company websites and brochures (Jindal Stainless, IUP Jindal, Quality Foils, Well Tech, Fluidyne, KSM, Technetics); "
            "MCA filings; NRI analysis",
            fontsize=6.6, color=GREY)
    ax.text(12.97, 0.18, "NRI", fontsize=11, color=MIDBLUE,
            fontweight="bold", ha="right")

    save(fig, "30-slide-redesign.png")


# ---------------------------------------------------------------- Chart 31
def chart31():
    """Executive version — one bar, three callouts."""
    fig, ax = plt.subplots(figsize=(13.33, 7.5))
    ax.set_xlim(0, 13.33)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    ax.add_patch(Rectangle((0.32, 6.86), 0.075, 0.66,
                           facecolor=MIDBLUE, edgecolor="none"))
    ax.text(0.52, 7.30,
            "Two of seven steps are missing in India — and neither is slitting",
            fontsize=18, fontweight="bold", color=NAVY, va="center")
    ax.text(0.52, 6.97,
            "Where India stands across the metal bellows value chain",
            fontsize=11.5, color=DGREY, va="center")

    stages = [
        ("Melt &\ncast", "part"), ("Cold roll\nto foil", "part"),
        ("Precision\nslitting", "ok"), ("Forming &\nstamping", "ok"),
        ("Joining", "ok"), ("Clean, test\n& certify", "gap"),
        ("End\nuse", "ok"),
    ]
    n = len(stages)
    left, right = 0.55, 12.78
    gap = 0.14
    w = (right - left - gap * (n - 1)) / n
    y = 4.28
    h = 1.30

    for i, (lab, st) in enumerate(stages):
        x = left + i * (w + gap)
        fc = {"ok": "#e8f4ec", "part": "#fdf3e3", "gap": "#fdeaea"}[st]
        ec = {"ok": GREEN, "part": AMBER, "gap": RED}[st]
        chevron(ax, x, y, w, h, "", fc, tip=0.26)
        pts = [(x, y), (x + w - 0.26, y), (x + w, y + h / 2),
               (x + w - 0.26, y + h), (x, y + h), (x + 0.16, y + h / 2)]
        ax.add_patch(Polygon(pts, closed=True, facecolor="none",
                             edgecolor=ec, linewidth=2.4, zorder=4))
        ax.text(x + w / 2 + 0.04, y + h * 0.60, lab, ha="center", va="center",
                fontsize=10.4, color=NAVY, fontweight="bold", linespacing=1.35)
        light(ax, x + w / 2 + 0.04, y + 0.26, st, r=0.155)

    # callouts
    calls = [
        (0.5, "MATERIAL GAP", AMBER,
         "No Indian mill melts AM350 or 631 —\nthe grades that define semiconductor\nand high-cycle bellows. 100% imported.",
         2.15),
        (2, "ALREADY SOLVED", GREEN,
         "IUP Jindal and Quality Foils both\nprecision-slit AND both list bellows\nas a served application.",
         5.86),
        (5, "QUALIFICATION GAP", RED,
         "No Indian ISO Class 5/6 cleanroom,\nhelium-leak or RGA facility for bellows.\nThis is what blocks semiconductor entry.",
         2.15),
    ]
    for idx, head, col, body, ytxt in calls:
        cx = left + idx * (w + gap) + w / 2 + 0.04
        above = ytxt > y
        ax.add_patch(FancyArrowPatch(
            (cx, ytxt + (-0.05 if above else 0.90)),
            (cx, y + h + 0.08 if above else y - 0.08),
            arrowstyle="-|>", mutation_scale=15, color=col, linewidth=2.2))
        bw = 3.62
        bx = min(max(cx - bw / 2, 0.4), 12.9 - bw)
        ax.add_patch(FancyBboxPatch((bx, ytxt), bw, 0.92,
                                    boxstyle="round,pad=0.07",
                                    facecolor="white", edgecolor=col,
                                    linewidth=2.1))
        ax.text(bx + 0.16, ytxt + 0.74, head, fontsize=9.4, color=col,
                fontweight="bold", va="center")
        ax.text(bx + 0.16, ytxt + 0.36, body, fontsize=8.4, color=DGREY,
                va="center", linespacing=1.55)

    ax.text(6.66, 1.28,
            "Iwatani's opening is the material gap, not the slitting step — and the qualification gap is where the strategy must stop.",
            fontsize=11, color=NAVY, fontweight="bold", ha="center")

    ax.text(0.55, 0.42,
            "Source: Company websites and brochures; MCA filings; NRI analysis",
            fontsize=7, color=GREY)
    ax.text(12.78, 0.42, "NRI", fontsize=11, color=MIDBLUE,
            fontweight="bold", ha="right")

    save(fig, "31-slide-exec-version.png")


if __name__ == "__main__":
    chart30(); chart31()
    print("\nSlide redesigns written to", OUT)
