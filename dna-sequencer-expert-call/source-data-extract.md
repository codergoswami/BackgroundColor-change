# Source Data Extract

The Excel model as shared, extracted from the PDF versions, so every figure quoted in the memo can be
checked. All revenue figures are **USD million** unless stated otherwise.

Files received (several were duplicates of one another): the main data sheet appeared as `data-1`,
`data-2`, `DNA_Sequencer_Market_Information_Collection_Sailesh_updated_Analysis` and
`...Analysis (1)`; the CAGR sheet appeared as `data-3` and `...Analysis (2)`. Content is identical
except that the `Analysis` versions carry the full model name for the 3500 / SeqStudio Flex rows,
which is truncated in the `data-1` / `data-2` renderings.

The **CAGR column** in the source is computed over 13 years rather than 12 intervals and is therefore
understated by roughly 0.8 percentage points throughout. The "actual" column below is our correction.

---

## Table 1 — Number of units sold

| Line | Price range | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | CAGR in sheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Total DNA sequencers** | – | 137 | 153 | 171 | 187 | 205 | 224 | 246 | 269 | 295 | 324 | 356 | 390 | 429 | – |
| NGS short read (all mfrs, all models) | 40K–800K | 65 | 72 | 79 | 87 | 95 | 105 | 115 | 127 | 139 | 153 | 169 | 185 | 204 | 10 |
| NGS long read (all mfrs, all models) | 20K–300K | 20 | 22 | 23 | 25 | 27 | 29 | 32 | 34 | 37 | 40 | 43 | 47 | 50 | 8 |
| **CE (all mfrs, all models)** | – | 52 | 60 | 69 | 75 | 82 | 90 | 99 | 108 | 119 | 131 | 144 | 158 | 174 | – |

### CE breakdown by manufacturer, model and end use — units

| Manufacturer | Model | Price range | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | CAGR | Note in sheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thermo Fisher | 3730 (96-capillary, large) — R&D / forensic identification | 250–300K | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2.5 | |
| Thermo Fisher | 3730 (96-capillary, large) — diagnostic use | 250–300K | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2.5–5 | |
| Thermo Fisher | 3500, 3500xL, SeqStudio 8 Flex, SeqStudio 24 Flex (8–24 capillary) — R&D / forensic *(inferred)* | 75–150K | 15 | 16 | 17 | 18 | 20 | 21 | 23 | 24 | 26 | 28 | 30 | 32 | 34 | 7 | |
| Thermo Fisher | 3500, 3500xL, SeqStudio 8 Flex, SeqStudio 24 Flex (8–24 capillary) — diagnostic use *(inferred)* | 75–150K | 25 | 28 | 31 | 35 | 39 | 44 | 49 | 55 | 62 | 69 | 78 | 87 | 97 | 12 | |
| Thermo Fisher | 3500 Dx, 3500xL Dx, SeqStudio 8 Flex Dx, SeqStudio 24 Flex Dx | 75–150K | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 5 | Non-regulated market |
| Promega | Spectrum CE system (mid-range) — R&D / forensics | 100–120K | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 5 | Only fragment – no marketing |
| Promega | Spectrum CE system (mid-range) — diagnostic use | 100–120K | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | No Sanger seq, only fragment |
| Thermo Fisher | SeqStudio (4-capillary, small) — R&D / forensic | 50–60K | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 5 | Not promoted by TMO |
| Thermo Fisher | SeqStudio (4-capillary, small) — diagnostic use | 50–60K | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 16 | 17 | 19 | 21 | 23 | 25 | 10 | Only standalone lab / tier-2, tier-3 labs |
| Promega | Spectrum Compact (4-capillary, small) — R&D / forensics | 50–70K | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 5 | Unless Promega focus on aggressive marketing |
| Promega | Spectrum Compact (4-channel, compact) — diagnostic use | 50–70K | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 8 | Unless Promega focus on aggressive marketing |
| Other manufacturers | – | – | | | | | | | | | | | | | | | *(blank)* |

The end-use label for the two 3500 / SeqStudio Flex rows is truncated in every file we received. We have
taken the first as R&D / forensic and the second as diagnostic use, on the basis that every other model
pair in the sheet is ordered that way and that diagnostic volumes are the larger of the two everywhere
else. **This needs confirming** — together these two rows are 48 of 69 CE units in 2025.

**Cross-checks:** the CE model rows sum to 52 in 2023 (ties exactly to the CE total) and 68 in 2025
(against a CE total of 69 — rounding). Thermo Fisher accounts for 64 of 68 units in 2025, or 94.1%,
consistent with his verbal "95 percent".

---

## Table 2 — Equipment sales revenue

| Line | Price range | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | CAGR in sheet | Actual CAGR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Total DNA sequencers** | – | 27.9 | 30.8 | 34.3 | 37.5 | 41.1 | 45.1 | 49.4 | 54.2 | 59.4 | 65.1 | 71.4 | 78.3 | 85.9 | 9.04% | **9.83%** |
| NGS short read | 40K–800K | 20.0 | 22.0 | 24.2 | 26.6 | 29.3 | 32.2 | 35.4 | 39.0 | 42.9 | 47.2 | 51.9 | 57.1 | 62.8 | 9.20% | **10.00%** |
| NGS long read | 20K–300K | 4.0 | 4.3 | 4.7 | 5.0 | 5.4 | 5.9 | 6.3 | 6.9 | 7.4 | 8.0 | 8.6 | 9.3 | 10.1 | 7.36% | **8.00%** |
| **CE** | – | 3.9 | 4.5 | 5.4 | 5.9 | 6.4 | 7.0 | 7.6 | 8.3 | 9.1 | 10.0 | 10.9 | 11.9 | 13.1 | 9.76% | **10.62%** |

### CE breakdown — equipment revenue

| Manufacturer | Model / use | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | CAGR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thermo Fisher | 3730 — R&D / forensic | 0.3 | 0.3 | 0.5 | 0.5 | 0.6 | 0.6 | 0.6 | 0.6 | 0.7 | 0.7 | 0.7 | 0.8 | 0.8 | 5 |
| Thermo Fisher | 3730 — diagnostic | 0.0 | 0.0 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.4 | 0.4 | 0.4 | 2.5–5 |
| Thermo Fisher | 3500 / SeqStudio Flex family — R&D / forensic | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8 | 1.9 | 2.1 | 2.2 | 2.4 | 2.5 | 2.7 | 7 |
| Thermo Fisher | 3500 / SeqStudio Flex family — diagnostic | 1.8 | 2.0 | 2.3 | 2.5 | 2.8 | 3.2 | 3.6 | 4.0 | 4.5 | 5.0 | 5.6 | 6.3 | 7.0 | 12 |
| Thermo Fisher | 3500 Dx / SeqStudio Flex Dx family | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.3 | 0.4 | 5 |
| Promega | Spectrum CE — R&D / forensics | 0.0 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.2 | 0.2 | 0.2 | 5 |
| Promega | Spectrum CE — diagnostic | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0 |
| Thermo Fisher | SeqStudio small — R&D / forensic | 0.0 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 5 |
| Thermo Fisher | SeqStudio small — diagnostic | 0.4 | 0.4 | 0.5 | 0.5 | 0.6 | 0.6 | 0.7 | 0.8 | 0.9 | 0.9 | 1.0 | 1.1 | 1.3 | 10 |
| Promega | Spectrum Compact — R&D / forensics | 0.0 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 5 |
| Promega | Spectrum Compact — diagnostic | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 8 |

For ten of these eleven rows the revenue CAGR equals the unit CAGR, meaning **the model holds average
selling prices flat across the whole forecast**. The only exception is the 3730 R&D row, at 2.5% units
against 5% revenue.

---

## Table 3 — Reagent sales

| Line | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | CAGR in sheet | Actual CAGR | Note in sheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Total DNA sequencers** | 50.0 | 58.9 | 69.4 | 81.9 | 96.9 | 114.6 | 135.9 | 161.2 | 191.4 | 227.5 | 270.6 | 322.1 | 383.7 | 16.97% | **18.51%** | |
| NGS short read | 40.0 | 48.0 | 57.6 | 69.1 | 82.9 | 99.5 | 119.4 | 143.3 | 172.0 | 206.4 | 247.7 | 297.2 | 356.6 | 18.33% | **20.00%** | Includes OEM assays |
| NGS long read | 3.0 | 3.3 | 3.6 | 4.0 | 4.4 | 4.8 | 5.3 | 5.8 | 6.4 | 7.1 | 7.8 | 8.6 | 9.4 | 9.20% | **10.00%** | Includes OEM assays |
| **CE** | 7.0 | 7.6 | 8.2 | 8.8 | 9.5 | 10.3 | 11.1 | 12.0 | 13.0 | 14.0 | 15.1 | 16.3 | 17.6 | 7.36% | **8.00%** | **Forensics assays — 5–8 M not included** |

### CE breakdown — reagent sales by supplier

| Supplier | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | Share 2023 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thermo Fisher Scientific | 5.00 | 5.4 | 5.8 | 6.3 | 6.8 | 7.3 | 7.9 | 8.6 | 9.3 | 10.0 | 10.8 | 11.7 | 12.6 | 71.4% |
| Promega | 1.00 | 1.08 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.9 | 2.0 | 2.2 | 2.3 | 2.5 | 14.3% |
| **Company A** *(unnamed; Nimagen per our open question)* | 1.00 | 1.08 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.9 | 2.0 | 2.2 | 2.3 | 2.5 | 14.3% |
| Company B | 0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Company C | 0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Other manufacturers | 0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

Promega and Company A are modelled as exactly equal, at the same growth rate, for all thirteen years.
The three named suppliers sum exactly to the CE total, so the sheet assumes a three-supplier CE reagent
market with no residual.

**Definition confirmed on the call:** the CE reagent line is running reagents only and **excludes assay
kits**. The NGS reagent lines **include** OEM assays plus running cost. This asymmetry is the main
definitional problem in the model.

---

## Table 4 — Software, parts and other sales

| Line | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | CAGR in sheet | Actual CAGR | Note in sheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Total DNA sequencers** | 5.5 | 6.2 | 7.1 | 8.0 | 9.1 | 10.3 | 11.7 | 13.3 | 15.2 | 17.2 | 19.6 | 22.4 | 25.5 | 12.52% | **13.63%** | |
| NGS short read | 4.0 | 4.6 | 5.3 | 6.1 | 7.0 | 8.0 | 9.3 | 10.6 | 12.2 | 14.1 | 16.2 | 18.6 | 21.4 | 13.77% | **15.00%** | Only the maintenance for NGS; softwares FOC from OEM; 3rd party reporting softwares not included |
| NGS long read | 0.5 | 0.55 | 0.6 | 0.7 | 0.7 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.6 | 9.20% | **10.00%** | Same note as above |
| **CE** | 1.0 | 1.08 | 1.17 | 1.26 | 1.36 | 1.47 | 1.59 | 1.71 | 1.85 | 2.00 | 2.16 | 2.33 | 2.52 | 7.36% | **8.00%** | **Software and maintenance included** |
| — of which Thermo Fisher | 0.95 | 1.03 | 1.11 | 1.20 | 1.29 | 1.40 | 1.51 | 1.63 | 1.76 | 1.90 | 2.05 | 2.22 | 2.39 | 7.36% | 8.00% | |
| — of which Promega | 0.05 | 0.05 | 0.06 | 0.06 | 0.07 | 0.07 | 0.08 | 0.09 | 0.09 | 0.10 | 0.11 | 0.12 | 0.13 | 7.36% | 8.00% | |
| — Company A / B / C, other | *(blank)* | | | | | | | | | | | | | | | |

NGS short read rises from 72.7% of this line in 2023 to 84.0% in 2035, entirely because it is assumed
to grow at 15% against CE at 8% and NGS long read at 10%. Company A has reagent revenue but nothing
here, consistent with a reagent-only supplier.

---

## Table 5 — Diagnostic assay reagents using CE

Header in the source: *"Diagnostic assay reagents using CE (refers to assay reagent kits specialized for
specific diagnostics, excluding electrophoresis reagents (polymer and buffer), STR reagents for personal
identification, and fluorescent sequencing reagents)"*

The column below is headed "Annual Kit Sales Volume – Million $" in the source. **Sailesh confirmed on
the call that it is annual kit sales *revenue* in USD million, not volume**, and that the header is
wrong: "I should have mentioned revenues in itself directly."

| Manufacturer | Product name | Approval status (Indian medical device authorities) | Target disease | Target gene | Annual kit sales **revenue**, USD M | Price range, USD |
|---|---|---|---|---|---|---|
| Thermo Fisher | MSI | *(blank)* | Cancer | Multiple MS | 0.1 | 25 |
| Thermo Fisher | FGA+SMA | *(blank)* | Fragile X and SMA | Fragile X and SMA | 0.1 | 25 |
| Thermo Fisher | Identifiler | *(blank)* | Chimerism, MCC | Multiple STR | 0.8 | 20 |
| Promega | Forensic kit | *(blank)* | Chimerism, MCC | Multiple STR | 0.8 | 20 |
| Promega | MSI | *(blank)* | Cancer | Multiple MS | 0.2 | 25 |
| MRC Holland | MLPA | *(blank)* | Multiple diseases | Multiple loci | 1.0 | 25 |
| Asuragen | FGA+SMA | *(blank)* | FGA+SMA | FGA+SMA | 0.5 | 25 |
| Devyser | QF-PCR | *(blank)* | Pre-natal testing | Multiple loci | 1.0 | 25 |
| **Total** | | | | | **4.5** | |

Reading the column as volume and multiplying by the price range gives **USD 104.5M**, which is the
figure computed live on the call and then corrected. The approval status column is blank for every
product. Identifiler and the Promega Forensic kit are both multiplex STR products, which the table
header says are excluded, yet both are recorded against clinical applications (chimerism monitoring and
maternal cell contamination).

---

## Table 6 — Tests performed, from the second follow-up questionnaire

Supplied by Sailesh before the call. The "tests originated" column was what we asked him to fill in and
is still outstanding.

| Provider type | Tests originated | Tests performed |
|---|---|---|
| Specialised genomics labs | *(requested)* | ~40% (~200K–240K) |
| National chain labs | *(requested)* | ~20% (~100K–120K) |
| Regional chain labs | *(requested)* | Negligible |
| Standalone labs | *(requested)* | Negligible |
| Specialty treatment hospitals | *(requested)* | ~10% (~50K–60K) |
| Large private hospitals | *(requested)* | ~10–15% (~50K–90K) |
| Small and medium private hospitals | *(requested)* | Negligible |
| Government tertiary hospitals / public medical colleges / programme-linked centres | *(requested)* | ~15–20% (~75K–120K) |

Note in the source: total CE-relevant genetic tests done in India ~500K–600K.

**Cross-check:** the shares sum to 95–105% and the absolute volumes to 475K–630K, against a stated
total of 500K–600K. Internally consistent.

---

## Derived figures used in the memo

All computed from the tables above.

| Figure | Value | How derived |
|---|---|---|
| Total market 2025, sheet lines only | USD 110.7M | 34.3 equipment + 69.4 reagents + 7.1 software |
| Total market 2025, adjusted | USD 126–134M | 110.7 + 10–15 third-party NGS assays + 5–8 CE forensics assays |
| CE implied price per unit, 2025 | ~USD 78,000 | 5.3963M ÷ 69 units |
| NGS short-read implied price per unit, 2025 | ~USD 306,000 | 24.2M ÷ 79 units |
| NGS long-read implied price per unit, 2025 | ~USD 203,000 | 4.6656M ÷ 23 units |
| CE reagent revenue per unit shipped, 2023 → 2035 | USD 134,600 → USD 101,300 (−25%) | CE reagents ÷ CE units, each year |
| CE end-use split 2025 | 22 R&D/forensic, 46 diagnostic | Sum of the model rows by end use |
| CE end-use split 2023 | 16 R&D/forensic, 36 diagnostic | Sum of the model rows by end use |
| Thermo Fisher share of CE units, 2025 | 94.1% | 64 of 68 model-level units |
| Thermo Fisher share of CE equipment revenue, 2025 | 94.6% | 5.3M of 5.6M |
| CE units 2035 with a 1 pp CAGR cut | 156 | 52 × 1.0959¹² |
| CE units 2035 with a 2 pp CAGR cut | 140 | 52 × 1.0859¹² |
| CE revenue mix 2025 incl. diagnostic assays | 28.1% equipment / 65.9% reagents+assays / 6.1% software | (5.40, 8.16+4.5, 1.17) ÷ 19.23 |
| NGS software/service gap, verbal vs sheet | +USD 4.1M | 10.0 verbal − 5.9 sheet |
| NGS reagents+assays gap, verbal vs sheet | +USD 23.8M to +28.8M | 85–90 verbal − 61.2 sheet |
