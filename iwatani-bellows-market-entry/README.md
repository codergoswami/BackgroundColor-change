# Iwatani Metals Dept. / Stainless Steel Division — Bellows & Precision-Slit Market Entry Study

**Client:** Iwatani Corporation — Metals Department → Stainless Steel Division
**Subject:** Evaluating a new business beyond stainless trading, leveraging the Jindal Stainless relationship, centred on bellows tube (precision-slit material) for semiconductor manufacturing equipment in India
**Status:** Working document — to be updated at monthly internal meetings
**Last updated:** July 2026

---

## How to read this pack

| File | Contents | Use it for |
| --- | --- | --- |
| [`01-technical-primer.md`](01-technical-primer.md) | What bellows are, every bellows type, what precision slitting actually is, where each sits in the value chain, materials and grades | Getting everyone in the room to the same technical baseline |
| [`02-market-sizing.md`](02-market-sizing.md) | Market size and growth for metal bellows and the semiconductor equipment demand driver, with source-quality warnings | Numbers for the business case — read the caveats before quoting any figure |
| [`03-india-landscape.md`](03-india-landscape.md) | India's semiconductor programme, stainless industry position, precision-strip supply base, and vacuum-component ecosystem | Testing the "Make in India" leg of the hypothesis |
| [`04-competitive-benchmarking.md`](04-competitive-benchmarking.md) | Indian bellows manufacturers plus the global incumbents you would be competing with or selling to | Competitive positioning and partner shortlisting |
| [`05-strategy-and-roadmap.md`](05-strategy-and-roadmap.md) | Verdict on the hypothesis, strategic options, the recommended two-track plan, stage-gated roadmap, KPIs, and the monthly meeting agenda | The actual consulting output — start here if you only read one file |
| [`06-source-register.md`](06-source-register.md) | Every source with a URL and a verification grade | Checking any claim in this pack |
| [`07-research-reconciliation.md`](07-research-reconciliation.md) | Merge of the second research pass: where both passes agree, errors to fix before external use, two newly-found Indian manufacturers, segment-by-segment purchasing logic, the hydrogen insight, and the revised three-rung entry ladder | Read alongside 04 and 05 — it revises conclusions in both |
| [`08-supply-chain-sourcing.md`](08-supply-chain-sourcing.md) | Where Indian bellows makers buy their precision strip today: grade-tier logic, the domestic mill list, named likely import sources, the Alleima India finding, customs-data method with HS codes, price anchors, and the procurement questions to ask | Displacement planning — who you actually have to beat, and how to confirm it |
| [`09-market-research-bellows.md`](09-market-research-bellows.md) | **World market research pack, 10 charts**: global size and the vendor spread, five-year history and projections to 2035, CAGR, segmentation by industry/type/material, regional structure, and growth drivers ranked by evidence | Numbers and visuals for slides. Includes a "what to quote / never quote" table |
| [`10-india-market-data.md`](10-india-market-data.md) | **India market data, 6 charts**: market size triangulated top-down and bottom-up from MCA company filings, CAGR, share of world, and addressable market by entry-ladder rung | The India numbers. Answers "how big is India and how fast is it growing" |
| [`11-share-reconciliation.md`](11-share-reconciliation.md) | **3 charts.** Why India's expansion-joints share and bellows share differ: the two markets overlap rather than nest, the structural reason India indexes higher in heavy products, and a **correction** withdrawing the 5–10% expansion joints figure | Read before quoting any market share. Contains the denominator test to apply to all share claims |

| [`12-india-drivers-challenges.md`](12-india-drivers-challenges.md) | **2 charts.** India's demand drivers ranked by evidence strength — refining, steel, gas, hydrogen, semiconductors, with government targets — and challenges sorted by whether Iwatani can address them | Building the "why India, why now" case, and knowing which obstacles are yours to solve |

| [`13-deck-number-check.md`](13-deck-number-check.md) | **2 charts.** Verification of figures proposed for a client deck, an internally consistent replacement set, suggested slide wording, and the list of withdrawn figures | **Read before any number goes on a slide** |

| [`14-value-chain-map.md`](14-value-chain-map.md) | **3 large landscape charts + full reference table.** Twelve stages from chrome ore to replacement bellows, naming global and Indian players at every stage, with the technical gate at each, plus an indicative margin-by-stage view | The industry structure reference. Use chart 29 for internal approval, 27 with Jindal, 28 with bellows makers |

**PDF versions** are in [`pdf/`](pdf/) — `09-market-research-bellows.pdf`, `10-india-market-data.pdf`, and `Iwatani-Bellows-Full-Pack.pdf` (everything combined). Regenerate with `python3 build_pdf.py`.

---

## The short version

**The original hypothesis is directionally interesting but mis-locates the customer.** Semiconductor bellows are consumed where *tools are built* (United States, Japan, Korea, Taiwan, China), not where *wafers are made*. India is building fabs and packaging plants, not wafer-fab-equipment factories. So Indian demand for slit-valve and wafer-lift bellows in the near term is spare-parts-scale, not new-build-scale.

**Three findings change the shape of the opportunity:**

1. **India already has genuine precision-slit capability**, so "few Indian companies can do precision slitting" is not accurate as stated. Jindal Stainless's own Hisar Specialty Products Division rolls precision strip down to **0.076 mm** and runs dedicated precision slitters, and IUP Jindal Metals & Alloys (a *different* Jindal group company) rolls **0.03–1.5 mm** and slits to **3.5 mm** width with deburred, rounded and chamfered edge options. The real gap is not slitting — it is **bellows-grade qualification**: precipitation-hardening grades such as AM350, fatigue-controlled fine grain structure, burr and edge specification, cleanliness, and lot traceability.

2. **The binding constraint in India is the absence of a qualified bellows manufacturer**, not the absence of material. India has competent hydroformed-bellows and expansion-joint makers, and at least one company claiming edge-welded capability, but no evidence of a semiconductor-qualified edge-welded bellows supplier operating at volume with cleanroom assembly and helium leak certification.

3. **Policy just moved in your favour, hard.** India's Semicon 2.0, approved 15 July 2026 with a ₹1,27,500 crore outlay, has a dedicated pillar for semiconductor **equipment, materials, chemicals and gases**, offering a flat incentive of **up to 30% of project cost**. That is the first time India has put capital subsidy behind exactly the layer of the chain this business would occupy.

**Recommended reframe:** run two tracks in parallel rather than betting on Indian semiconductor bellows demand.

- **Track A (revenue engine, near term):** qualify Jindal as a second-source mill for **bellows-grade precision-slit strip**, and sell it into the *existing global* bellows and vacuum-valve supply chain in Korea, Japan, Taiwan and Europe. Iwatani already slits precision stainless in Suzhou and Zhongshan and already handles stainless foil down to 8 µm, so this uses capability you have rather than capability you would have to build.
- **Track B (option value, medium term):** build a position in India — fab spares and MRO first, then a converter partnership or joint venture for bellows manufacture, timed to Semicon 2.0 incentives and to Dholera and the OSAT cluster reaching steady-state volume.

Full reasoning, risks and the stage-gated plan are in [`05-strategy-and-roadmap.md`](05-strategy-and-roadmap.md).

**Two updates from the second research pass** (detail in [`07-research-reconciliation.md`](07-research-reconciliation.md)):

- **Don't enter at semiconductor. Enter at mechanical seal bellows, then hydrogen and cryogenic, then semiconductor.** Mechanical seals is the segment where Indian sourcing is already strongest — large installed base in refineries, petrochemicals, fertiliser and power, with shutdown economics that make long import lead times unacceptable. And **hydrogen is where Iwatani has its strongest credibility of all**: its stainless line already carries hydrogen-resistant stainless steel and hydrogen-refuelling-station materials, and hydrogen is the group's flagship business. Each rung earns the credibility needed for the next.
- **Two Indian manufacturers already work at the target specification.** Well Tech Metal Bellows (Vasai) claims 0.05–0.2 mm diaphragms in AM350, helium leak tested, for high-purity gas delivery and mass flow controllers; Fluidyne Engineers India (Mysuru) claims 0.05 mm diaphragms and UHV racetrack bellows. Both claims are directory-sourced and need auditing — but if they hold, **Indian demand for exactly this material already exists and is being met by imports.** They are now the top two customer-discovery targets.

---

## Evidence standard used in this pack

Every factual claim carries an inline source link. Sources are graded, because the quality range here is extreme — primary industry and government sources are solid, while the commercial market-research reports on bellows disagree with each other by more than 6x and should not be quoted externally without qualification.

| Grade | Meaning |
| --- | --- |
| **[P] Primary** | Company's own website, brochure, annual report, investor deck, regulatory filing, or industry association / government publication |
| **[C] Credible press** | Established business or trade press reporting a verifiable, attributable fact |
| **[S] Secondary / commercial** | Paid market-research vendor press pages. Indicative direction only. Treated as unreliable for absolute values |
| **[U] Unverified** | Trade directory or aggregator listing not confirmed by the company itself |

Two things are explicitly **not** verified and are carried as assumptions from the client brief:

- Iwatani's role as the Japan-market window for Jindal Stainless. No public documentation of this arrangement was found; it is taken as given from the brief.
- Any statement about Jindal's willingness or internal roadmap to enter precipitation-hardening or bellows-grade strip. This must come from Jindal directly and is listed as an open question.
