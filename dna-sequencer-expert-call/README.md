# DNA Sequencer Expert Call — Memo Pack

Memo prepared from the clarification call with **Sailesh** (former Thermo Fisher Scientific, India) on the
India DNA sequencer market model, with focus on **CE (capillary electrophoresis) sequencers**.

## Contents

| File | What it is |
|---|---|
| `expert-call-memo.md` | The memo. Ten MECE subject segments, each mapped to the questions we sent, plus five appendices |
| `source-data-extract.md` | The Excel data as extracted from the shared PDFs, so every figure in the memo is auditable |
| `build_docx.py` | Generates `Expert-Call-Memo-DNA-Sequencer.docx` from the memo for circulation |

## Structure of the memo

Segments 1–10 cover subject matter. Each of the 13 questions we sent is assigned to exactly one
segment, so the segmentation is MECE. Within each segment three things are kept separate on purpose:
**what the expert said**, **what the data shows**, and **our read** — so his statements are never blended
with our interpretation.

| Segment | Subject | Questions covered |
|---|---|---|
| 1 | Data provenance and forecast methodology | Q1 |
| 2 | CE growth structure: equipment vs consumables | Q2 |
| 3 | CE volume trajectory and durability of demand to 2035 | Q3 |
| 4 | CE vs NGS short read: units vs revenue | Q4 |
| 5 | End-use segment economics: forensics vs clinical diagnostics | Q5 |
| 6 | Pricing: level, direction and basis | Q6, Q8 |
| 7 | Scope of "reagents" and "assays"; total market reconciliation | Q7 |
| 8 | Supplier attribution within the CE reagent line | Q9, Q10 |
| 9 | Software, parts, service and other revenue | Q11 |
| 10 | Segment classification and test-volume flow | F1, F2 |
| 11 | Commitments the expert made | — |
| 12 | Open items to go back to him with | — |

Appendices: **A** question coverage table · **B** additional facts captured beyond the questionnaire ·
**C** data quality flags from our own review · **D** transcript reliability and corrections ·
**E** all key figures in one place.

## Headline points

1. **Six of the 13 questions were fully answered, two partly, and five were never reached** — the
   transcription cut off at 30 minutes and the recording runs longer. The full audio should be
   re-transcribed before the memo is treated as final.
2. **The biggest substantive problem is definitional.** Within the same reagent table the CE row
   excludes assay kits while the NGS rows include them. The "Total DNA Sequencers" reagent line is a
   mixed-definition sum and should not be quoted until he delivers the split he agreed to provide.
3. **A USD 104M error was caught and closed.** The assay table column headed "Annual Kit Sales Volume –
   Million $" actually contains revenue. Reading it as volume and multiplying by price gives USD 104.5M
   instead of the correct USD 4.5M. He confirmed the header is wrong.
4. **His verbal NGS numbers do not tie to his own sheet** — USD 85–90M for NGS reagents plus assays
   against USD 61.2M in the file, a gap of roughly a quarter of the total market. This is the top item
   to resolve, in writing.
5. **The sheet's printed CAGR column is mis-computed**, dividing by 13 years instead of 12 intervals, so
   every CAGR is understated by about 0.8 percentage points. The forecast values themselves are correct.
6. **The CE growth story is credible but carries a hidden assumption.** Government funding places
   instruments regardless of workload and those machines are underused, while private labs run theirs
   flat out. That explains equipment growing at 10.6% against reagents at 8.0% — but it means the model
   implicitly assumes reagent consumption per installed CE instrument falls about 25% by 2035.

## Reproducing the Word version

```bash
pip install python-docx
python3 build_docx.py
```
