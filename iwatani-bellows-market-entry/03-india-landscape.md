# 03 — India Landscape: Semiconductor Programme, Stainless Position, Component Ecosystem

## 1. India Semiconductor Mission — where it actually stands

### Phase 1 (Semicon 1.0), ₹76,000 crore

As of mid-2026, the Government of India reports **12 approved semiconductor manufacturing projects** with cumulative committed investment of approximately **₹1.64 lakh crore**, spread across Gujarat, Assam, Andhra Pradesh, Uttar Pradesh and Odisha. The composition is **one silicon fab, one silicon carbide fab, one integrated GaN micro-LED display facility, and nine packaging units** **[C]** ([Outlook Business](https://www.outlookbusiness.com/deeptech/cabinet-outlays-127-lakh-cr-for-india-semiconductor-mission-20-to-boost-chip-design-manufacturing); [New Indian Express](https://www.newindianexpress.com/business/2026/Jul/15/cabinet-approves-rs-127-lakh-crore-for-semicon-india-20-to-boost-domestic-chip-ecosystem)).

| Project | Location | Investment | Type & status |
| --- | --- | --- | --- |
| **Micron Technology** | Sanand, Gujarat | US$2.75 bn / ₹22,516 cr | ATMP for DRAM, NAND, SSD. **Inaugurated 28 Feb 2026; in commercial production** **[C]** ([Indian Express](https://indianexpress.com/article/cities/ahmedabad/pm-to-inaugurate-indias-first-semiconductor-fabrication-plant-worth-over-rs-20000-crore-in-sanand-10554477/)) |
| **Tata Electronics + PSMC** | Dholera, Gujarat | ~₹91,000 cr | India's first commercial wafer fab, 28 nm and above, **50,000 wafers/month** planned. Under construction; first silicon targeted late 2026 **[C]** |
| **Tata Semiconductor Assembly & Test (TSAT)** | Jagiroad / Morigaon, Assam | ₹27,000 cr | Assembly & test, up to **48 million chips/day** at capacity, flip-chip and ISIP packaging. 15,000 direct jobs. Phase-1 commissioning through 2026 **[C]** ([Economic Times](https://economictimes.indiatimes.com/industry/cons-products/electronics/semiconductor-plant-in-assam-likely-to-start-production-this-fiscal-union-minister-ashwini-vaishnaw-says/articleshow/131421750.cms)) |
| **Kaynes Semicon** | Sanand, Gujarat | ~₹3,300 cr | OSAT. **Commercial production from March 2026** **[C]** |
| **CG Semi** (CG Power) | Sanand, Gujarat | ~₹7,600 cr | Power-management IC assembly & test. **In commercial production** **[C]** |
| CG Power–Renesas JV | Sanand | — | Packaging **[C]** |
| Crystal / additional OSAT | Dholera | ~US$355 m | Newly approved 2026 **[C]** |
| Others incl. SiC fab, GaN micro-LED display, Odisha projects | AP, UP, Odisha | — | Various stages **[C]** |

**Three facilities are in commercial production**: Micron (Feb 2026), Kaynes Semicon (Mar 2026), and CG Semi.

### Phase 2 (Semicon 2.0) — approved 15 July 2026, ₹1,27,500 crore

This is the decisive policy development for this business case. Approved by the Union Cabinet on **15 July 2026**, six-year duration **[C]** ([Cyril Amarchand Mangaldas analysis](https://corporate.cyrilamarchandblogs.com/2026/07/semicon-2-0-the-next-phase-of-indias-semiconductor-ambitions/); [Business Standard](https://www.business-standard.com/industry/news/cabinet-clears-rs-1-28-trillion-for-ism-2-0-rs-62-500-crore-for-mobile-scheme-126071500711_1.html); [Economic Times](https://economictimes.indiatimes.com/industry/cons-products/electronics/cabinet-approves-india-semiconductor-mission-2-0-earmarks-rs-1-27-lakh-crore-for-the-project/articleshow/132412149.cms)).

Six pillars:

1. Chip design, IP and system design (grant-plus-equity for startups; co-investment or royalty-linked for larger firms)
2. **Semiconductor equipment, machines, materials, specialty chemicals and industrial gases** ← *this is the relevant one*
3. Additional fabs — silicon, compound semiconductor, discrete, display
4. ATMP/OSAT expansion, with emphasis on advanced packaging
5. R&D including advanced process nodes
6. Talent development

Revised incentive rates:

| Category | Semicon 1.0 | Semicon 2.0 |
| --- | --- | --- |
| Silicon fabs | 50% flat | **40%** |
| Display / compound semiconductor fabs | 50% | **35%** |
| Advanced packaging | 50% | **35%** |
| Conventional ATMP/OSAT | 50% | **25%** |
| **Equipment, materials, chemicals, gases** | *not covered* | **up to 30% of project cost** |
| R&D | — | up to 75% (Centre + State) |
| Talent development | — | up to 75% |

The government's own framing of pillar 2 is unusually direct about the gap it is trying to close: India "relies on imports for specialty chemicals, ultra-pure gases, and photomasks needed for semiconductor manufacturing" and "lacks the capability to manufacture equipment required for use within cleanrooms" **[C]** ([Cyril Amarchand](https://corporate.cyrilamarchandblogs.com/2026/07/semicon-2-0-the-next-phase-of-indias-semiconductor-ambitions/)).

> **Implication for Iwatani.** A precision-slit or bellows-manufacturing facility in India plausibly qualifies under pillar 2 as a semiconductor *materials* or *equipment sub-system* supplier. A 30% capex subsidy materially changes the economics of Track B. **The scheme guidelines and eligibility definitions had not been published in detail at the time of writing — obtaining them and testing eligibility is a Gate 1 action.**

---

## 2. The structural problem with the original hypothesis

The hypothesis assumes that because India is building semiconductor capacity, India will need locally-made semiconductor bellows. That inference does not hold cleanly, for one reason:

**Bellows are consumed by whoever builds the tool, not whoever runs the fab.**

A slit-valve bellows is bought by SMC or VAT, who sell the valve to Applied Materials, Lam Research or Tokyo Electron, who sell the tool to the fab. India is acquiring **fabs and packaging plants**. It is not acquiring **wafer-fab-equipment OEMs**. So the new-build bellows demand created by Dholera is captured in Japan, Korea, the US and Taiwan — not in India.

What India *does* create is:

- **Spare-parts and MRO demand** at the fabs and OSATs themselves, which is real, recurring and reasonably high-margin, but small in absolute tonnage and slow to arrive (a fab's bellows replacement cycle only begins after several years of operation).
- **Contract-manufacturing demand**, if global OEMs localise sub-assembly work in India. This is the more interesting channel and it has just started to become real — see section 4.

This is not a reason to abandon the idea. It is a reason to **sequence it correctly**: earn revenue from the global supply chain first, and treat India as the option, not the anchor. That is the core of the recommendation in [`05-strategy-and-roadmap.md`](05-strategy-and-roadmap.md).

---

## 3. Testing the two stated hypotheses

### Hypothesis A: "There may be few companies in India that can produce high-quality precision slits made of stainless steel."

**Verdict: not accurate as stated. India has real precision-slit capability. The gap is grade and qualification, not slitting.**

| Indian supplier | Capability | Note |
| --- | --- | --- |
| **Jindal Stainless — Hisar SPD** | 84,000 tpa precision cold-rolled strip; **dedicated precision slitters**; strip to **0.076 mm**; up to 650 mm width | Your own partner. Focus is martensitic razor-blade steel **[P]** ([brochure](https://www.jindalstainless.com/product-brochure/)) |
| **IUP Jindal Metals & Alloys** (Jindal SAW group — *a different Jindal company*) | Thickness **1.5 mm to 0.03 mm**; width **620 mm to 3.5 mm**; edge conditions: mill, slit, **deburred, deburred+round, deburred+chamfered**; 200/300/400 series; 2D/2B/BA/2R/2H and quarter-to-full hard; 20-Hi mill with AGC. Explicitly lists **"flexible tubes & capillary tubes"** among served applications | **The most directly comparable Indian competitor for bellows-grade slit strip.** First to make precision stainless in India (1980, as Swastik Foils) **[P]** ([IUP brochure](https://jindalmetal.com/images/iup-brochure.pdf), [slitting page](https://jindalmetal.com/page/cold-rolled-precision-stainless-steel-strips-manufacturers-in-india-3)) |
| Sachiya Steel International (Mumbai) | 0.02–4.0 mm, width 3–650 mm, slit/deburred/round edge, ISO 9001/14001/45001 | Stockist-processor rather than mill **[U]** |
| Various regional processors | 0.05 mm and up | Long tail, unverified |

**Two consequences.** First, do not present "India cannot precision-slit" to Jindal — they can, and IUP Jindal already sells into flexible tube applications. Second, and more important commercially: **IUP Jindal is a competitor operating under a confusingly similar name.** Iwatani should be explicit internally that Jindal Stainless (Ratan Jindal) and Jindal SAW / IUP Jindal Metals & Alloys (a separate O.P. Jindal group company) are different entities. Confusing them in a partner conversation would be damaging.

The genuine gaps, restated precisely:

- **Precipitation-hardening grades.** AM350/AISI 633 and 631/17-7PH do not appear in Jindal Stainless's published grade tables. These are the defining grades for semiconductor bellows.
- **Fatigue-qualified microstructure.** Bellows strip needs controlled fine grain for cyclic life — this is the property Iwatani already markets in its "stainless steel for gaskets" line ("finer crystalline structure to maintain high spring performance and fatigue characteristics") **[P]**.
- **Cleanliness and traceability regime** appropriate to semiconductor supply.
- **Customer approvals.** No evidence of any Indian mill being an approved bellows-strip source for a semiconductor-grade bellows maker.

### Hypothesis B: "Make in India policy makes local manufacture of semiconductor materials and equipment advantageous."

**Verdict: correct, and substantially stronger than when the hypothesis was written.** Semicon 2.0's pillar 2 puts a flat capex incentive of up to 30% behind exactly this layer, and the government has publicly identified equipment and materials as the structural gap. This is the strongest external tailwind in the whole analysis. The caveat is timing: scheme guidelines were not yet detailed at the time of writing, and incentive schemes in India typically take time to convert into disbursement.

---

## 4. India's vacuum and semiconductor-equipment component ecosystem

This is where the near-term Indian customers actually are, and it is more developed than expected.

| Company | What they do | Relevance |
| --- | --- | --- |
| **KASFAB Tools Pvt Ltd** (KAS Group, with UHP Technologies and KASTECH Equipment), Doddaballapur, Bengaluru | Opened what is described as **India's first semiconductor equipment manufacturing facility for global clients**. Contract manufacturing aimed at **Applied Materials, Lam Research, Tokyo Electron and Yield Engineering Systems**. Facility includes **precision welding, cleanrooms, test and validation tools, safety simulation bench**. Launch attended by Applied Materials India's Head of Semiconductor Products Group | **The single most important potential Indian customer/partner identified in this study.** A contract manufacturer building sub-assemblies for WFE OEMs is exactly who buys bellows in India **[C]** ([Machine Maker](https://themachinemaker.com/news/kasfab-tools-opens-indias-first-semiconductor-equipment-manufacturing-facility-for-global-clients/)) |
| **Applied Materials India**, Bengaluru | One of AMAT's largest R&D centres outside the US. Designs high-precision vacuum chambers, thermal distribution systems, robotic wafer transfer handlers. Operates an **India Validation Center** giving local access to 300 mm wafers in cleanroom conditions, so Indian-designed hardware can be validated locally instead of being shipped abroad. Reported to be encouraging "domestic machine shops, specialty metal fabricators, and cleanroom vendors to achieve the precision tolerances required for global fab equipment" | Demand creator and qualification gatekeeper **[C]** ([report](https://matribhumisamachar.com/en/2026/07/20/beyond-design-assembly-how-applied-materials-india-is-driving-the-nations-upstream-semiconductor-manufacturing-equipment-leap/)) |
| **Hind High Vacuum (HHV) Group**, Bengaluru | 61 years in vacuum technology. Thin-film deposition systems, vacuum furnaces, precision optics. Aerospace, automotive, defence | Established buyer of vacuum hardware incl. bellows **[P]** ([hhv.in](https://hhv.in/)) |
| **Fourvac Technologies** | UHV components, vacuum chambers, **UHV valves, XYZ manipulators, drives and motions**. Exports to 18+ countries. Built the complete six-chamber UHV system for IIT Kanpur's HeNDI spectrometer | **XYZ manipulators and drives are bellows-containing assemblies** — a direct, immediate prospect **[P]** ([fourvac.com](https://fourvac.com/)) |
| **Advanced Process Technology (APT)** | Custom HV/UHV chambers, SS304/304L/316/316L and aluminium, UHV-compatible welding, leak tested to 1×10⁻¹² Torr·l/s | Demonstrates that UHV-grade welding and leak testing competence exists in India **[P]** ([aptglobal.com](https://aptglobal.com/vacuum-chambers/)) |

**Read across these five.** India already has companies doing UHV welding, leak testing to 10⁻¹² Torr·l/s, cleanroom assembly, and manipulator/drive assembly. What is missing is specifically the **bellows** element — the thin-foil stamping, precision edge welding and fatigue qualification. That is a narrow, identifiable gap rather than a general absence of capability, which makes it a more tractable entry point than it first appears.

---

## 5. India stainless steel context for a Japanese trading company

- India: **2nd largest consumer, 3rd largest producer** of stainless; installed capacity 6.6–6.8 Mt; finished production 3.2–3.7 Mt. Indonesia displaced India and Japan for the number-two production slot in 2021 **[C]** ([Indian stainless industry report](https://www.rajputanastainless.com/public/frontend/assets/pdf/Report%20on%20Indian%20Stainless%20Steel%20Industry.pdf)).
- **Jindal Stainless is India's largest stainless producer**, with 16 manufacturing and processing facilities across India, Spain and Indonesia and a network spanning 12 countries; Hisar 0.8 Mtpa and Jajpur 2.2 Mtpa **[P]** ([Annual Report FY24](https://www.jindalstainless.com/annualreport/2023-2024/corporate-overview/manufacturing-strengths)).
- Jindal has stated plans for a **Stainless Steel Industrial Park of about 300 acres** adjacent to the Odisha plant, including SEZ and non-SEZ areas, with a large service centre, and an explicit invitation to investors to site downstream units there with "long term Stainless Steel availability at concessional rates" plus land, power and water **[P]** ([product brochure](https://www.jindalstainless.com/product-brochure/)).

> **That industrial park is a concrete, pre-existing vehicle for Track B.** If a bellows or precision-slitting converter is to be built in India with Jindal, Jindal has already published the mechanism and the incentive. This should be tested directly with them. Note the caveat that the brochure text is undated, so the park's current status needs confirmation.

---

## 6. Open questions on India — to close before Gate 1

1. Semicon 2.0 pillar-2 scheme guidelines: exact eligibility definitions, whether a component or materials converter qualifies, application windows, minimum investment thresholds.
2. Status and terms of Jindal's Odisha Stainless Steel Industrial Park.
3. Whether KASFAB, Fourvac, HHV or APT currently import bellows, from whom, at what volume and lead time.
4. Whether Applied Materials India's supplier-development programme has a formal vendor onboarding route Iwatani could enter.
5. Indian import duty and any anti-dumping duty position on thin-gauge stainless flat products, since it affects whether a Track A trading flow or a Track B local conversion is more economic. *Not yet researched — carried as a gap.*
6. Whether Tata Electronics' Dholera fab has a published local-content or vendor-localisation target.
