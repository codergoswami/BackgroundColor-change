"""
Builds PDF versions of the Iwatani bellows market entry pack.

  python3 build_pdf.py            -> builds every PDF
  python3 build_pdf.py 09         -> builds just the file starting "09"

Outputs into pdf/ :
  09-market-research-bellows.pdf   the market research pack with charts
  Iwatani-Bellows-Full-Pack.pdf    all nine documents combined
"""

import os
import re
import sys
import base64
import mimetypes

import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(HERE, "pdf")
os.makedirs(PDF_DIR, exist_ok=True)

DOCS = [
    ("README.md", "Overview and Executive Summary"),
    ("01-technical-primer.md", "Technical Primer"),
    ("02-market-sizing.md", "Market Sizing"),
    ("03-india-landscape.md", "India Landscape"),
    ("04-competitive-benchmarking.md", "Competitive Benchmarking"),
    ("05-strategy-and-roadmap.md", "Strategy and Roadmap"),
    ("06-source-register.md", "Source Register"),
    ("07-research-reconciliation.md", "Research Reconciliation"),
    ("08-supply-chain-sourcing.md", "Supply Chain Sourcing"),
    ("09-market-research-bellows.md", "Bellows Market Research"),
]

CSS = """
@page {
  size: A4;
  margin: 17mm 15mm 18mm 15mm;
  @bottom-center {
    content: "Iwatani Metals Dept. / Stainless Steel Division  \\2014  Bellows & Precision-Slit Market Entry Study  \\2014  page " counter(page);
    font-family: "DejaVu Sans", sans-serif; font-size: 7.5pt; color: #8b949e;
  }
}
@page :first { @bottom-center { content: ""; } }

body { font-family: "DejaVu Sans", "Helvetica", sans-serif; font-size: 9.1pt;
       line-height: 1.48; color: #1a1a1a; }

h1 { font-size: 18pt; color: #12355b; border-bottom: 2.5px solid #12355b;
     padding-bottom: 5px; margin: 0 0 14px 0; page-break-after: avoid; }
h2 { font-size: 13pt; color: #12355b; margin: 20px 0 8px 0;
     border-bottom: 1px solid #d0d7de; padding-bottom: 3px; page-break-after: avoid; }
h3 { font-size: 10.8pt; color: #1f6feb; margin: 15px 0 6px 0; page-break-after: avoid; }
h4 { font-size: 9.6pt; color: #12355b; margin: 12px 0 5px 0; page-break-after: avoid; }

p { margin: 0 0 8px 0; text-align: left; }
ul, ol { margin: 0 0 9px 0; padding-left: 18px; }
li { margin-bottom: 3.5px; }

table { border-collapse: collapse; width: 100%; margin: 10px 0 14px 0;
        font-size: 7.6pt; page-break-inside: avoid; }
thead { background: #12355b; color: #fff; }
th { padding: 5px 6px; text-align: left; font-weight: bold; border: 1px solid #12355b; }
td { padding: 4px 6px; border: 1px solid #d0d7de; vertical-align: top; }
tbody tr:nth-child(even) { background: #f4f7fb; }

img { max-width: 100%; display: block; margin: 12px auto 6px auto;
      page-break-inside: avoid; border: 1px solid #e2e6ea; }

code { font-family: "DejaVu Sans Mono", monospace; font-size: 7.8pt;
       background: #f2f4f7; padding: 1px 3px; border-radius: 2px; color: #0b3d91; }
pre { background: #f6f8fa; border: 1px solid #d0d7de; border-left: 3px solid #1f6feb;
      padding: 8px 10px; font-size: 7.3pt; overflow-wrap: break-word;
      white-space: pre-wrap; page-break-inside: avoid; margin: 10px 0; }
pre code { background: none; padding: 0; color: #24292f; }

blockquote { border-left: 3.5px solid #d4a017; background: #fffaef;
             margin: 11px 0; padding: 8px 12px; page-break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }

a { color: #1f6feb; text-decoration: none; word-break: break-all; }
hr { border: none; border-top: 1px solid #d0d7de; margin: 16px 0; }
strong { color: #0d2b4e; }

.cover { text-align: center; padding-top: 58mm; page-break-after: always; }
.cover .eyebrow { font-size: 9.5pt; letter-spacing: 2.6px; color: #1f6feb;
                  text-transform: uppercase; margin-bottom: 14px; }
.cover h1 { font-size: 27pt; border: none; color: #12355b; margin-bottom: 8px;
            line-height: 1.2; }
.cover .sub { font-size: 12.5pt; color: #57606a; margin-bottom: 34px; }
.cover .rule { width: 92px; height: 3px; background: #d4a017; margin: 0 auto 30px auto; }
.cover .meta { font-size: 9.2pt; color: #57606a; line-height: 1.85; }
.cover .warn { margin: 34px auto 0 auto; max-width: 132mm; font-size: 8.3pt;
               color: #57606a; background: #f4f7fb; border: 1px solid #d0d7de;
               border-left: 3px solid #d4a017; padding: 11px 14px; text-align: left; }

.docsep { page-break-before: always; }
"""


def embed_images(html: str, base_dir: str) -> str:
    """Inline local images as data URIs so the PDF is self-contained."""
    def repl(m):
        src = m.group(1)
        if src.startswith(("http://", "https://", "data:")):
            return m.group(0)
        path = os.path.normpath(os.path.join(base_dir, src))
        if not os.path.exists(path):
            return m.group(0)
        mime = mimetypes.guess_type(path)[0] or "image/png"
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode()
        return f'src="data:{mime};base64,{b64}"'
    return re.sub(r'src="([^"]+)"', repl, html)


def md_to_html(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    # Mermaid blocks cannot render in print; show as a labelled diagram listing.
    text = re.sub(
        r"```mermaid\n(.*?)```",
        lambda m: "**[Diagram — rendered in the web version. Source below.]**\n\n```\n"
                  + m.group(1) + "```",
        text, flags=re.S)
    html = markdown.markdown(
        text, extensions=["tables", "fenced_code", "attr_list", "sane_lists"])
    return embed_images(html, os.path.dirname(path))


def cover(title, subtitle, contents_note):
    return f"""
    <div class="cover">
      <div class="eyebrow">Iwatani Corporation &nbsp;&middot;&nbsp; Confidential Working Draft</div>
      <h1>{title}</h1>
      <div class="sub">{subtitle}</div>
      <div class="rule"></div>
      <div class="meta">
        <strong>Client</strong><br>Iwatani Corporation &mdash; Metals Department &rarr; Stainless Steel Division<br><br>
        <strong>Subject</strong><br>Bellows tube (precision-slit material) market entry,<br>
        leveraging the Jindal Stainless relationship<br><br>
        <strong>Status</strong><br>Working document &mdash; updated at monthly internal meetings<br><br>
        <strong>Prepared</strong><br>July 2026
      </div>
      <div class="warn">
        <strong>Evidence standard.</strong> Every factual claim in this document carries an inline
        source link and a verification grade: <strong>[P]</strong> primary (company, association or
        government publication), <strong>[C]</strong> credible press, <strong>[S]</strong> commercial
        market-research vendor (indicative only), <strong>[U]</strong> unverified directory listing.
        Commercial estimates for the bellows market disagree with one another by up to a factor of 19;
        figures marked <strong>[S]</strong> must not be quoted externally without stating the range.
        {contents_note}
      </div>
    </div>
    """


def build(doc_files, out_name, title, subtitle, contents_note=""):
    parts = [cover(title, subtitle, contents_note)]
    for i, (fname, label) in enumerate(doc_files):
        path = os.path.join(HERE, fname)
        if not os.path.exists(path):
            print("  skip (missing):", fname)
            continue
        sep = ' class="docsep"' if i > 0 else ""
        parts.append(f"<div{sep}>{md_to_html(path)}</div>")
    html = ("<!doctype html><html><head><meta charset='utf-8'>"
            f"<style>{CSS}</style></head><body>" + "".join(parts) + "</body></html>")
    out = os.path.join(PDF_DIR, out_name)
    HTML(string=html, base_url=HERE).write_pdf(out)
    size = os.path.getsize(out) / 1_000_000
    print(f"  wrote pdf/{out_name}  ({size:.1f} MB)")


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None

    if only in (None, "09"):
        build([("09-market-research-bellows.md", "Bellows Market Research")],
              "09-market-research-bellows.pdf",
              "Bellows Market Research",
              "Global market size, five-year history, projections to 2035,<br>"
              "CAGR, segmentation, regional structure and India&rsquo;s share",
              " This document closes with a &ldquo;what to quote / never quote&rdquo; table.")

    if only is None:
        build(DOCS, "Iwatani-Bellows-Full-Pack.pdf",
              "Bellows &amp; Precision-Slit<br>Market Entry Study",
              "Complete pack &mdash; technical primer, market sizing, India landscape,<br>"
              "competitive benchmarking, strategy, roadmap and sourcing",
              " This combined pack contains all nine documents in sequence.")

    print("\nDone. Output in", PDF_DIR)
