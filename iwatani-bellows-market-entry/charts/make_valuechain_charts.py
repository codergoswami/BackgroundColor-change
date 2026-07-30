"""
Exhaustive metal bellows value chain maps.

Chart 27 — UPSTREAM: ore to bellows-ready precision slit strip
Chart 28 — MIDSTREAM + DOWNSTREAM: bellows manufacture to end user
Chart 29 — Value pool: where margin concentrates, and Iwatani's position

Run:  python3 make_valuechain_charts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Patch, Rectangle
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
GOLD = "#ffd24d"
RED = "#cf222e"
GREY = "#8b949e"
DGREY = "#57606a"
SAFF = "#ff9933"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def stage_column(ax, x, w, header, hcol, process, glob, india, spec,
                 top=12.50, hh=0.78, highlight=False):
    """Draw one value-chain stage column with four stacked information boxes."""
    if highlight:
        ax.add_patch(Rectangle((x - 0.09, 1.95), w + 0.18, top - 1.59,
                               facecolor=GOLD, alpha=0.20, zorder=0,
                               edgecolor=AMBER, linewidth=2.2, linestyle="--"))
    # header
    ax.add_patch(FancyBboxPatch((x, top - hh), w, hh,
                                boxstyle="round,pad=0.03",
                                facecolor=hcol, edgecolor="none", zorder=3))
    ax.text(x + w / 2, top - hh / 2, header, ha="center", va="center",
            fontsize=8.4, color="white", fontweight="bold", zorder=4)

    blocks = [
        ("PROCESS", process, "#eef4ff", NAVY, 2.45),
        ("GLOBAL PLAYERS", glob, "#f4f7fb", DGREY, 2.95),
        ("INDIA PLAYERS", india, "#fff6ec", SAFF, 2.55),
        ("KEY SPEC / GATE", spec, "#f0f8f2", GREEN, 1.15),
    ]
    y = top - hh - 0.16
    for title, body, fc, ec, h in blocks:
        ax.add_patch(FancyBboxPatch((x, y - h), w, h,
                                    boxstyle="round,pad=0.03",
                                    facecolor=fc, edgecolor=ec,
                                    linewidth=1.1, zorder=3))
        ax.text(x + 0.08, y - 0.17, title, fontsize=6.4, color=ec,
                fontweight="bold", va="center", zorder=4)
        ax.text(x + 0.08, y - 0.34, body, fontsize=6.35, color="#1a1a1a",
                va="top", ha="left", zorder=4, linespacing=1.46)
        y -= (h + 0.14)


def arrow(ax, x0, x1, y=5.0, col=NAVY):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>",
                                 mutation_scale=17, color=col,
                                 linewidth=2.1, zorder=5))


# ---------------------------------------------------------------- Chart 27
def chart27():
    stages = [
        ("1 · RAW MATERIALS", GREY,
         "Chrome ore, ferrochrome,\nnickel, molybdenum,\nstainless scrap.\nMining, beneficiation,\nsubmerged arc furnace",
         "Glencore · Vale ·\nNornickel · Eramet ·\nTsingshan · Sibanye\nSouth32 · Yildirim",
         "Jindal Stainless own\nSukinda chrome mines\n(Odisha) · 250k tpa\nferrochrome at Jajpur\nOdisha Mining Corp",
         "Cr, Ni, Mo content\nand cost basis", False),

        ("2 · MELT & CAST", GREY,
         "EAF → AOD converter →\nVOD → continuous cast\nto slab. Grade chemistry\nset here — including\nwhether PH grades are\neven possible",
         "Outokumpu · Acerinox ·\nAperam · POSCO ·\nNippon Steel Stainless ·\nNAS · Tsingshan ·\nATI · Carpenter",
         "Jindal Stainless\n— Hisar 0.8 Mtpa\n— Jajpur 2.2 Mtpa\nViraj · Mukand\n(long products only)",
         "Melt chemistry ·\ncleanliness · N control\nfor AM350 (0.07–0.13%)", False),

        ("3 · HOT ROLL", GREY,
         "Reheat → roughing →\nSteckel or tandem finishing\n→ anneal & pickle →\nHR coil. Shot blast,\nlevel, straighten",
         "Same integrated mills\nas stage 2\n\nOutokumpu · Acerinox ·\nPOSCO · Nippon Steel",
         "Jindal Stainless\n— Hisar Steckel 720k tpa\n— Hisar tandem 300k tpa\n— Jajpur 1.0 Mtpa\n  (Siemens VAI)",
         "Surface quality ·\nHR gauge uniformity", False),

        ("4 · COLD ROLL\nTO THIN GAUGE", BLUE,
         "20-Hi Sendzimir & 4-Hi\nmills with automatic gauge\ncontrol. Multi-pass\nreduction to 0.03–0.20 mm.\nBright / bell / pull-through\nannealing between passes",
         "Alleima (to 0.015 mm\nat ±0.001 mm) · Ulbrich ·\nATI · TOKKIN · Proterial ·\nAperam Imphy ·\nvoestalpine Precision Strip ·\nWaelzholz · Lamineries\nMatthey (AM350 to 0.010 mm)",
         "Jindal Stainless SPD\nHisar — 84,000 tpa,\nto 0.076 mm\nIUP Jindal — 0.03–1.5 mm,\n22,000 tpa\nQuality Foils — 0.10–4.0 mm\nHisar Metal · Singhal Strips",
         "Thickness tolerance ·\nflatness · grain structure\nfor fatigue life", False),

        ("5 · TEMPER,\nLEVEL, FINISH", BLUE,
         "Skin pass mill · tension\nleveller · strip grinding ·\nbright annealing to 2R/BA ·\ntemper to spring hardness\n(¼H to full hard, HV530+)",
         "Same precision mills\n\nAlleima · Ulbrich ·\nTOKKIN · Proterial\n\nIwatani sources\nspring & gasket tempers",
         "Jindal SPD — strip grinding,\nskin pass, tension leveller\nIUP Jindal — 2 bright\nanneal lines, Brodeur\ntension leveller",
         "Hardness · flatness ·\nsurface cleanliness\n(2R/BA for vacuum)", False),

        ("6 · PRECISION\nSLITTING", AMBER,
         "Rotary knife slitting of\nmaster coil into narrow\nstrip. Shimless tooling,\ncomputerised knife setting.\nEdge conditioning:\ndeburr · round · chamfer.\nBurr height & direction\nspecified",
         "Alleima · Ulbrich ·\nHempel Special Metals\n(serves bellows makers,\nfrom 0.05 mm) ·\nLamineries Matthey\n(±0.1 mm width on request)\n\n★ IWATANI — Suzhou &\nZhongshan (China) + Thailand",
         "IUP Jindal — 3 Brodeur\nlines, shimless tooling,\nedge rounding, slit to 3.5 mm\nQuality Foils — slit edge\nfrom 5.0 mm\nJindal SPD — precision slitters\n+ 5 slitting lines in CR complex\nStockists: Aesteiron, Sachiya",
         "Width tolerance ±0.05 mm\nBurr ≤10% of thickness\nCamber · coil set", True),
    ]

    fig, ax = plt.subplots(figsize=(21.5, 14.4))
    ax.set_xlim(0, 21.5)
    ax.set_ylim(0, 13.8)
    ax.axis("off")

    w = 3.18
    gap = 0.36
    x = 0.22
    xs = []
    for st in stages:
        stage_column(ax, x, w, st[0], st[1], st[2], st[3], st[4], st[5],
                     highlight=st[6])
        xs.append(x)
        x += w + gap

    for i in range(len(stages) - 1):
        arrow(ax, xs[i] + w + 0.02, xs[i + 1] - 0.02, y=7.45)

    ax.text(0.22, 13.48,
            "Chart 27 — UPSTREAM VALUE CHAIN:  ore  →  bellows-ready precision slit strip",
            fontsize=16, fontweight="bold", color=NAVY)
    ax.text(0.22, 13.10,
            "Six stages. Iwatani and Jindal Stainless together already cover stages 1–6 — but in different grades and different geographies. "
            "★ marks Iwatani's existing position.",
            fontsize=9.8, color=DGREY)

    ax.add_patch(FancyBboxPatch((0.22, 0.30), 21.06, 1.30,
                                boxstyle="round,pad=0.06",
                                facecolor="#fffbe8", edgecolor=AMBER,
                                linewidth=2))
    ax.text(10.75, 0.95,
            "STAGE 6 IS THE PROPOSED ENTRY POINT — and the key finding is that India already has it. Both IUP Jindal and Quality Foils precision-slit AND explicitly name bellows as a served application.\n"
            "The real gap sits UPSTREAM at stages 2 and 4: no Indian mill melts or rolls AM350 or 631, and the only published Indian thickness tolerance is ±0.020 mm at 0.10 mm gauge against Alleima's ±0.001 mm.\n"
            "So the proposition is not \"we can slit precisely\" — it is \"we can supply precipitation-hardening grades in thin gauge, at tight tolerance, in small lots, with traceability.\"",
            fontsize=8.6, color="#7a5600", ha="center", va="center",
            fontweight="bold", linespacing=1.7)

    save(fig, "27-valuechain-upstream.png")


# ---------------------------------------------------------------- Chart 28
def chart28():
    stages = [
        ("7A · FORMED BELLOWS\nMANUFACTURE", BLUE,
         "Shear strip → roll to\ncylinder → LONGITUDINAL\nSEAM WELD (TIG/plasma) →\nclean & inspect →\ntelescope plies (2–20) →\nHYDROFORM (15k–20k psi)\nor mechanical/mandrel form\n→ neck weld, rings",
         "Witzenmann (HYDRA) ·\nSenior Flexonics · BOA Group ·\nBelman · Flexider ·\nEagleBurgmann · Hyspan ·\nPenflex · Triad Bellows ·\nMacoga · Comflex",
         "Flexpert Bellows (2–20 ply)\nMB Metallic Bellows\n(100 NB to 8 m dia)\nMetallic Bellows (India)\nWitzenmann India\nFluidyne · Bhastrik\nTriveni · Scutes India",
         "Seam weld integrity ·\nthinning control ·\nEJMA / ASME VIII", False),

        ("7B · EDGE-WELDED\nBELLOWS MANUFACTURE", NAVY,
         "Blank / press diaphragm\nrings from foil → deburr →\nstack & nest → ID WELD →\nOD WELD (laser, micro-\nplasma, EB, TIG) →\nattach end pieces.\nNesting-ripple geometry\nfor max stroke",
         "KSM Corp (world's largest,\nISO 6 cleanroom) ·\nTechnetics BELFAB ·\nMW Components/Servometer ·\nMetal-Flex · Witzenmann ·\nIrie Koken · MIRAPRO ·\nEagle Industry EKK ·\nValqua · BellowsTech",
         "★ Well Tech (Vasai)\n0.05–0.2 mm, AM350,\nHe leak tested\n★ Fluidyne (Mysuru)\n0.05 mm diaphragms,\nracetrack UHV\nBhastrik 0.127–0.30 mm\nmicro-plasma",
         "Weld bead <0.1 mm ·\nspring rate · cycle life\n(3M–10M cycles)", True),

        ("8 · ASSEMBLY &\nHARDWARE", BLUE,
         "Add end plates, flanges\n(CF/KF/ISO), liners,\nexternal covers, tie rods,\ngimbal & hinge hardware,\nbraiding, reinforcing rings.\nSub-assembly into\nmanipulators & translators",
         "Same bellows makers,\nplus specialist assemblers\n\nMW Components ·\nHuntington · Nor-Cal ·\nMDC Vacuum ·\nKurt J. Lesker",
         "Fourvac (XYZ manipulators,\nUHV valves, drives)\nHHV (Bengaluru)\nAPT (UHV chambers,\nleak test to 1e-12\nTorr·l/s)\nMetallic Bellows (India)",
         "Dimensional accuracy ·\nassembly cleanliness", False),

        ("9 · CLEAN, TEST\n& CERTIFY", GREEN,
         "Ultrasonic & solvent clean →\nUHV bake → ISO Class 5/6\nCLEANROOM assembly and\npackaging → HELIUM LEAK\nTEST (<1e-9 mbar·l/s) →\nRGA certificate →\nfatigue / cycle testing →\ndouble-bag",
         "KSM — world's largest\nISO 6 cleanroom for bellows;\nISO 5 final pack\nTechnetics — Class 100/1000\nWitzenmann — UHV/UHP\nwith optional RGA cert",
         "⚠ NO Indian facility found\nwith ISO Class 5/6 bellows\ncleanroom or RGA capability.\nAPT leak-tests to\n1e-12 Torr·l/s.\nKASFAB has cleanrooms\n+ precision welding",
         "★ THE REAL BARRIER\nto semiconductor entry", False),

        ("10 · COMPONENT\nINTEGRATION", GREEN,
         "Bellows built into the\nfinished sellable component:\nvacuum valves, mechanical\nseals, feedthroughs,\nexpansion joints, dampers,\naccumulators, MFCs,\ngas panels",
         "VALVES: VAT · SMC ·\nIrie Koken · Ferrotec ·\nPfeiffer\nSEALS: EagleBurgmann ·\nJohn Crane · Flowserve ·\nEagle Industry · Chesterton\nCHAMBERS: MIRAPRO",
         "Well Tech supplies Indian\nmechanical seal makers\nFourvac — UHV valves\nHHV · APT — chambers\nEPC/piping contractors\nfor expansion joints",
         "Valve cycle life 3M+\nLeak rate · particle\ngeneration", False),

        ("11 · OEM /\nEQUIPMENT BUILD", GREEN,
         "Component goes into\ncapital equipment:\nwafer fab tools, aero\nsystems, pumps &\ncompressors, vehicles,\nelectrolysers, process plant",
         "SEMI WFE: Applied\nMaterials · Lam Research ·\nTokyo Electron · ASML ·\nKLA · Screen · Kokusai · YES\nAERO: Boeing · Airbus ·\nGE · Safran\nPUMPS: KSB · Sulzer · Grundfos",
         "★ KASFAB Tools\n(Doddaballapur) — India's\nfirst semiconductor equipment\ncontract mfr for AMAT, Lam,\nTEL, YES\nAMAT India (Bengaluru)\nHAL · BHEL · Kirloskar",
         "Tool qualification ·\nOEM AVL approval\n(12–24 months)", False),

        ("12 · END USER\n& AFTERMARKET", "#0d6b2f",
         "Installed and operated.\nBellows then RE-ORDERED\nas a consumable —\n3M cycle service life,\nuser-replaceable.\nRecurring MRO revenue\nfor decades",
         "FABS: TSMC · Samsung ·\nIntel · Micron · SK Hynix\nREFINERIES: Shell · Exxon\nSPACE: NASA · ESA · JAXA\nFUSION: ITER · accelerators",
         "FABS/OSAT: Micron Sanand ·\nTata-PSMC Dholera ·\nTSAT Assam · Kaynes · CG Semi\nREFINERY: IOCL · RIL · BPCL\nPOWER: NTPC · NPCIL\nSPACE/DEF: ISRO · BARC · DRDO\nSTEEL: SAIL · Tata · JSW",
         "★ AFTERMARKET is\nrecurring, higher margin,\nand fab-located", False),
    ]

    fig, ax = plt.subplots(figsize=(24.5, 14.4))
    ax.set_xlim(0, 24.5)
    ax.set_ylim(0, 13.8)
    ax.axis("off")

    w = 3.14
    gap = 0.30
    x = 0.22
    xs = []
    for st in stages:
        stage_column(ax, x, w, st[0], st[1], st[2], st[3], st[4], st[5],
                     highlight=st[6])
        xs.append(x)
        x += w + gap

    for i in range(len(stages) - 1):
        arrow(ax, xs[i] + w + 0.01, xs[i + 1] - 0.01, y=7.45,
              col=NAVY if i < 3 else GREEN)

    # aftermarket loop back
    ax.add_patch(FancyArrowPatch((xs[6] + w / 2, 1.30), (xs[4] + w / 2, 1.30),
                                 arrowstyle="-|>", mutation_scale=17,
                                 color=GREEN, linewidth=2.2,
                                 linestyle="--",
                                 connectionstyle="arc3,rad=0.30", zorder=6))
    ax.text((xs[4] + xs[6] + w) / 2, 0.42,
            "REPLACEMENT / MRO LOOP — bellows are a designed-in consumable,\nso demand recurs at the component stage for the life of the tool",
            fontsize=9.0, color="#0d6b2f", ha="center", fontweight="bold",
            linespacing=1.6)

    ax.text(0.22, 13.48,
            "Chart 28 — MIDSTREAM & DOWNSTREAM VALUE CHAIN:  precision strip  →  bellows  →  component  →  equipment  →  end user",
            fontsize=16, fontweight="bold", color=NAVY)
    ax.text(0.22, 13.10,
            "Two manufacturing routes diverge at stage 7. ★ marks the Indian players that matter. "
            "⚠ marks the capability India does not have.",
            fontsize=9.8, color=DGREY)

    save(fig, "28-valuechain-downstream.png")


# ---------------------------------------------------------------- Chart 29
def chart29():
    """Where value concentrates along the chain."""
    stages = [
        ("1 Raw\nmaterials", 1, 18, 60, GREY),
        ("2 Melt\n& cast", 2, 11, 120, GREY),
        ("3 Hot\nroll", 3, 10, 100, GREY),
        ("4 Cold roll\nthin gauge", 4, 20, 45, BLUE),
        ("5 Temper\n& finish", 5, 22, 25, BLUE),
        ("6 PRECISION\nSLITTING", 6, 25, 18, AMBER),
        ("7A Formed\nbellows", 7, 30, 30, BLUE),
        ("7B Edge-welded\nbellows", 8, 42, 22, NAVY),
        ("8 Assembly\n& hardware", 9, 38, 26, BLUE),
        ("9 Clean, test\n& certify", 10, 52, 14, GREEN),
        ("10 Component\nintegration", 11, 48, 60, GREEN),
        ("11 OEM\nequipment", 12, 55, 240, GREEN),
        ("12 End user\n+ aftermarket", 13, 45, 90, "#0d6b2f"),
    ]

    fig, ax = plt.subplots(figsize=(15.5, 7.8))
    xs = [s[1] for s in stages]
    ys = [s[2] for s in stages]

    ax.plot(xs[:6], ys[:6], color=GREY, lw=2, ls="--", zorder=1, alpha=0.8)
    ax.plot(xs[5:], ys[5:], color=NAVY, lw=2.4, ls="--", zorder=1, alpha=0.8)

    for lab, x, y, sz, col in stages:
        ax.scatter([x], [y], s=sz * 9, color=col, alpha=0.82, zorder=3,
                   edgecolor="white", linewidth=1.8)
        inside = sz >= 55
        ax.annotate(f"{y}%", (x, y),
                    ha="center" if inside else "left",
                    va="center",
                    textcoords="offset points" if not inside else "data",
                    xytext=(13, 0) if not inside else None,
                    fontsize=8.6, fontweight="bold",
                    color="white" if inside else col, zorder=5)
        ax.annotate(lab, (x, y), textcoords="offset points",
                    xytext=(0, -36 if x in (2, 4, 8, 11, 13) else 32),
                    ha="center", fontsize=8.1, color=NAVY,
                    fontweight="bold", zorder=4)

    # Iwatani / Jindal position bands
    ax.axvspan(0.55, 6.45, color=SAFF, alpha=0.07, zorder=0)
    ax.text(3.5, 66, "JINDAL STAINLESS plays here\nIWATANI trades and slits here",
            ha="center", fontsize=9.4, color="#a35a00", fontweight="bold")
    ax.axvspan(6.55, 9.45, color=BLUE, alpha=0.07, zorder=0)
    ax.text(8.0, 66, "TRACK B\nmanufacturing option",
            ha="center", fontsize=9.4, color=BLUE, fontweight="bold")
    ax.axvspan(9.55, 13.45, color=GREEN, alpha=0.07, zorder=0)
    ax.text(11.5, 66, "WHERE THE MARGIN IS\n— and where Iwatani will not go",
            ha="center", fontsize=9.4, color="#0d6b2f", fontweight="bold")

    ax.annotate("", xy=(6.0, 25), xytext=(6.0, 11),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=2))
    ax.text(6.30, 15.0, "moving from stage 2 to\nstage 6 roughly doubles\nindicative gross margin",
            fontsize=8.6, color=RED, fontweight="bold", va="center")

    ax.set_ylabel("Indicative gross margin (%)", fontsize=10.5)
    ax.set_xlabel("Value chain stage  →", fontsize=10.5)
    ax.set_xticks([])
    ax.set_ylim(0, 76)
    ax.set_xlim(0.3, 13.9)
    ax.set_title(
        "Chart 29 — Value pool: margin rises monotonically downstream, and so does the barrier to entry\n"
        "Bubble size ≈ relative revenue pool. INDICATIVE ESTIMATES — a prioritisation aid, not measured data.",
        fontsize=12.6, fontweight="bold", loc="left", color=NAVY, pad=14)

    fig.text(0.005, -0.075,
             "MARGIN FIGURES ARE OUR INDICATIVE ESTIMATES, not measured data, and are shown to make the shape of the chain visible. Bubble\n"
             "areas are relative revenue pools, also indicative. THE SHAPE IS THE POINT: commodity melting and hot rolling sit at 10-11%,\n"
             "precision slitting at ~25%, edge-welded bellows manufacture at ~42%, and cleanroom qualification and component integration at\n"
             "~48-52%. Every step downstream adds margin AND adds a qualification barrier. Iwatani's realistic ambition is to move from\n"
             "stage 2-3 economics to stage 5-6 economics, which roughly doubles margin without requiring a manufacturing licence, cleanroom\n"
             "or OEM approval. Stages 9-12 are where the money is and are also where a trading house cannot credibly go.",
             fontsize=7.8, color=DGREY, ha="left")
    save(fig, "29-value-pool.png")


if __name__ == "__main__":
    chart27(); chart28(); chart29()
    print("\nValue chain charts written to", OUT)
