# 02 — Market Size and Trends

## Read this warning before quoting any number in this file

The commercial market-research reports on metal bellows **disagree with each other by more than a factor of six for the same segment in the same year**. This is not a rounding difference; it means at least some of them are not measuring what they claim to measure. Two examples that cannot both be true:

| Claim | Segment | Value | Source |
| --- | --- | --- | --- |
| Global **welded** metal bellows market, 2025 | welded | **US$1.8 bn** | Dataintelo **[S]** |
| Global **welded** metal bellows market, 2024 | welded | **US$0.291 bn** | Expert Market Research **[S]** |

The same vendor set also reports the **total** metal bellows market at US$1.94 bn in 2025 (GII/IRES **[S]**), which is *smaller* than Dataintelo's figure for the welded sub-segment alone. These are mutually inconsistent.

**Practical guidance for the monthly meeting:** use the authoritative upstream indicators (SEMI equipment forecasts, worldstainless production data) as the real demand signals, and treat the bellows-specific vendor numbers as directional colour only. Do not put a vendor bellows number in a board paper or a partner discussion without labelling it as a third-party estimate with a wide range.

---

## 1. Global metal bellows market — the range, honestly

| Scope | Base value | Forecast | CAGR | Source | Grade |
| --- | --- | --- | --- | --- | --- |
| Total metal bellows | US$1.94 bn (2025) | US$2.88 bn by 2032 | 5.79% | [GII / IRES report page](https://www.giiresearch.com/report/ires1948584-metal-bellows-market-by-type-material.html) | **[S]** |
| Welded metal bellows | US$1.8 bn (2025) | US$3.1 bn by 2034 | 6.2% | [Dataintelo](https://dataintelo.com/report/global-welded-metal-bellow-market) | **[S]** |
| Welded metal bellows | US$291.33 m (2024) | US$488.03 m by 2034 | 5.9% | [Expert Market Research](https://www.expertmarketresearch.com/reports/welded-metal-bellows-market) | **[S]** |
| Edge-welded metal bellows | US$409 m (2025) | US$706.2 m by 2034 | 6.2% | [Dataintelo](https://dataintelo.com/report/global-edge-welded-metal-bellow-market) | **[S]** |
| Hydroformed metal bellows | US$920 m (2025) | US$1,675 m by 2034 | 6.8% | [Dataintelo](https://dataintelo.com/report/global-hydroformed-metal-bellows-market) | **[S]** |

**What survives cross-checking.** Three qualitative conclusions are consistent across all the vendors and are also consistent with what the manufacturers themselves say, so they are usable:

1. **The market grows mid-single-digit to high-single-digit**, roughly 5–7% CAGR. No source claims explosive growth, and none claims decline.
2. **Edge-welded is the premium sub-segment and grows faster than the average**, on the strength of semiconductor and aerospace demand. Dataintelo puts edge-welded at 62.4% of the welded market and growing at ~6.5%.
3. **Stainless steel is the dominant material**, put at 54.3% of the welded market by Dataintelo — consistent with the material lists published by Valqua, KSM and Technetics.

Useful segmentation logic, again from vendor material but structurally sensible: by type into convoluted / edge-welded / hydroformed, with edge-welded sub-split by joining method into electron-beam, laser and TIG welded; by material into stainless steel, high-nickel alloys (Hastelloy, Inconel, Monel) and titanium ([GII/IRES](https://www.giiresearch.com/report/ires1948584-metal-bellows-market-by-type-material.html)) **[S]**.

One vendor claim worth flagging *because it is checkable and matters operationally*: Dataintelo reports order books for aerospace-grade bellows with delivery timelines extending 16–20 weeks **[S]**. If true, long lead times are a genuine opening for a new qualified source. **Action: verify this directly with two or three bellows makers rather than relying on the report.**

---

## 2. The real demand driver: semiconductor equipment spending (authoritative)

This is the number to build the business case on, because it comes from the industry's own association and is measured, not modelled.

SEMI's Mid-Year Total Semiconductor Equipment Forecast, published **14 July 2026** **[P]** ([SEMI press release](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports)):

| Metric | 2025 (actual) | 2026 (f) | 2027 (f) | 2028 (f) |
| --- | --- | --- | --- | --- |
| **Total semiconductor equipment sales** | — | **US$165.9 bn** (+23.2%) | — | **US$229.5 bn** |
| Wafer Fab Equipment (WFE) | US$116.9 bn (record) | US$143.9 bn (+23.1%) | +21.8% | +14.1%, reaching ~US$200 bn |
| Foundry & logic | — | US$78.0 bn (+18.9%) | +18.1% | US$104.7 bn (+13.6%) |
| DRAM | — | US$38.8 bn (+39.0%) | +27.4% | US$56.9 bn (+15.0%) |
| NAND | — | US$13.9 bn (+30.7%) | +31.1% | US$20.8 bn (+14.5%) |

2028 would mark **five consecutive years of growth**, driven by AI infrastructure, high-bandwidth memory, and leading-edge logic. SEMI describes its 2026 WFE number as a *significant upward revision* from its own 2025 year-end forecast.

**Why this matters for bellows.** Bellows are consumed per-tool and per-motion-axis. Etch, CVD, implant and wafer-handling tools are bellows-dense, and these are precisely the segments SEMI shows expanding fastest. A WFE market compounding at roughly 20% for two years and reaching US$200 bn means the installed base of bellows-consuming tools — and therefore the replacement stream — grows on a lag behind it.

**Also note where that spending goes.** SEMI's regional data has consistently placed China, Taiwan and Korea as the top three equipment markets. India does not appear in the top tier. This is the single most important qualification on the original hypothesis and is treated fully in [`03-india-landscape.md`](03-india-landscape.md).

---

## 3. Bellows demand sizing — an explicit, checkable model

No credible public source gives semiconductor bellows demand directly. Rather than quote a vendor number, here is a transparent order-of-magnitude frame. **Every input below is an assumption to be validated, not a finding.** It is included so the monthly meeting can argue about the inputs rather than about a black box.

```
Semiconductor bellows demand  =  (A) new-build demand  +  (B) replacement demand

(A) new-build   = WFE spend  ×  bellows content as % of tool BOM value
(B) replacement = installed tool base  ×  bellows per tool  ×  (1 / service interval in years)  ×  unit price
```

Anchors that *are* verified and can constrain the model:

- **WFE spend 2026: US$143.9 bn** — SEMI **[P]**.
- **Service interval: ~3 million cycles to first service** for slit valves and transfer valves — SMC and VAT **[P]**. Converting cycles to years requires the customer's wafer throughput, which is fab-specific.
- **Bellows are explicitly customer-replaceable** on both SMC and VAT valve families **[P]**, confirming a genuine aftermarket exists rather than whole-valve replacement.
- **Valve-level population per tool** must come from teardown knowledge or OEM discussion. A 300 mm cluster tool has multiple slit valves plus wafer-lift, pin-lift and pedestal-lift bellows per process module.

**Recommended action instead of modelling in the dark:** the fastest route to a defensible number is two or three structured conversations with vacuum-valve makers and bellows makers (see the shortlist in [`04-competitive-benchmarking.md`](04-competitive-benchmarking.md)). One hour with a valve engineer replaces a month of desk estimation. This is listed as a Gate 1 deliverable in the roadmap.

---

## 4. Stainless steel context

### Global production

World Stainless Association full-year 2025 data, released 27 February 2026 **[P]** ([worldstainless](https://worldstainless.org/media/press-releases/stainless-steel-melt-shop-production-increases-by-2-1-in-2025/)):

| Region | 2024 (kt) | 2025 (kt) | Change |
| --- | --- | --- | --- |
| Asia | 53,876 | 55,313 | +2.7% |
| — of which China | 39,441 | 40,868 | +3.6% |
| European Union | 5,770 | 5,659 | −1.9% |
| United States | 1,950 | 2,099 | +7.6% |
| Others | 1,225 | 1,086 | −11.3% |
| **Total** | **62,821** | **64,157** | **+2.1%** |

Q1 2026 total was 15,774 kt, up 2.5% year on year **[P]** ([worldstainless data](https://worldstainless.org/data/stainless-steel-meltshop-production/)).

The signal here is stark: **the commodity stainless market grows at ~2%, while semiconductor equipment grows at ~23%.** That gap is the entire economic rationale for the Stainless Steel Division moving up the value chain. It is the strongest single argument in this pack for doing something.

### India's position — correcting a common error

India is the **second-largest consumer** and the **third-largest producer** of stainless steel globally, with installed capacity estimated at 6.6–6.8 Mt. India was the second-largest producer behind China until 2020, but **Indonesia overtook both Japan and India in 2021**, and India's share of world output fell from 7.3% in 2016 to about 6.2% in 2021. India's finished stainless production has run in the 3.2–3.7 Mt range **[C]** ([Industry Report on Indian Stainless Steel, Nov 2025](https://www.rajputanastainless.com/public/frontend/assets/pdf/Report%20on%20Indian%20Stainless%20Steel%20Industry.pdf)).

**Please do not use "India is the world's number two stainless producer" in any Iwatani material.** It was true through 2020 and is now wrong. India is number two in *consumption*, which is actually the more useful fact for a market-entry argument anyway.

### Precision strip — where the real capacity numbers are

| Facility | Capability | Grade |
| --- | --- | --- |
| **Jindal Stainless, Hisar Specialty Products Division** | **84,000 tpa** precision cold-rolled strip; primarily **martensitic** for razor blades; 4-Hi and 20-Hi mills; strip grinding, skin pass, tension leveller; **dedicated precision slitters**; razor-blade strip **to 0.076 mm**; coin blanks 9,125 tpa | **[P]** [Jindal product brochure](https://www.jindalstainless.com/product-brochure/) |
| Jindal Stainless, Hisar cold rolling complex | 375,000 tpa CR flats; four 20-Hi Sendzimir mills; **five slitting lines**; No.1, 2D, 2B, BA, N3, No.4 finishes | **[P]** same |
| Jindal Stainless, Hisar melt | 800,000 tpa | **[P]** same |
| Jindal Stainless, Jajpur | 2.2 Mtpa | **[P]** [Annual Report FY24](https://www.jindalstainless.com/annualreport/2023-2024/corporate-overview/manufacturing-strengths) |

Expansion history, which shows sustained management commitment to this segment: JSHL commissioned a 26,000 tpa precision strip mill in October 2021, taking capacity from 22,000 to 48,000 tpa, with a stated plan to reach **60,000 tpa** and to raise blade steel from 14,000 to 24,000 tpa, at a combined brownfield capex of about ₹450 crore. Post-expansion the plant could produce **up to 650 mm width**, and the blade steel line goes **as low as 0.07 mm** **[P]** ([Jindal press release](https://www.jindalstainless.com/press-releases/jindal-stainless-hisar-limited-commissions-phase-i-of-brownfield-expansion-at-specialty-products-division/); corroborated **[C]** [Business Standard](https://www.business-standard.com/article/news-cm/jindal-stainless-hisar-commissions-26-000-tpa-capacity-precision-strip-mill-121102100487_1.html), [Hindu BusinessLine](https://www.thehindubusinessline.com/companies/jindal-stainless-eyes-2600-cr-capex-to-double-melting-capacity/article66226105.ece)).

> **The most important number in this pack.** Jindal already rolls and precision-slits stainless at **0.07–0.076 mm** — squarely inside the 0.03–0.15 mm band that bellows diaphragms and bellows tube stock occupy. The capability constraint is therefore **metallurgical and qualification-related, not dimensional.** Jindal has the mills. What is unproven is the grade (AM350/631), the fatigue-controlled grain structure, the cleanliness regime, and the customer approvals.

---

## 5. Trends to track monthly

| Trend | Why it matters here | Where to watch |
| --- | --- | --- |
| AI/HBM-driven WFE capex | Directly sets new-build bellows demand | SEMI monthly billings; SEMI Total Equipment Forecast (bi-annual) |
| Supply-chain regionalisation | The reason a non-China, non-Korea second source has strategic value to OEMs | SEMI, OEM investor calls |
| India Semicon 2.0 pillar-2 rulemaking | Determines whether a components plant in India is subsidised at 30% | MeitY / ISM notifications |
| Vendor lead times for bellows | A capacity-constrained incumbent set is the entry window | Direct conversations, not reports |
| Indonesian and Chinese stainless oversupply | Pressures commodity trading margin, strengthening the case to move upmarket | worldstainless quarterly |
| Witzenmann's India build-out | The most credible competitor path to localised bellows in India | Witzenmann press releases |
