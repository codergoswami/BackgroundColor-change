#!/usr/bin/env python3
"""Build the circulation copies of the memo, in Word and PDF.

Both outputs are a single self-contained document: the memo followed by the
source data extract as Appendix F, so there is one file to hand over.

    pip install python-docx fpdf2 && python3 build_documents.py
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from fpdf import FPDF
from fpdf.enums import TableCellFillMode, XPos, YPos
from fpdf.fonts import FontFace

HERE = Path(__file__).parent
MEMO = HERE / "expert-call-memo.md"
DATA = HERE / "source-data-extract.md"
STEM = "Expert-Call-Memo-DNA-Sequencer"

ACCENT_RGB = RGBColor(0x1F, 0x3A, 0x5F)
ACCENT_HEX = "1F3A5F"
ACCENT_PDF = (0x1F, 0x3A, 0x5F)
MUTED_RGB = RGBColor(0x55, 0x55, 0x55)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

# Bold, italic and code spans in one pass, so nesting order does not matter.
INLINE = re.compile(r"(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*)|`[^`]+`)")


# --------------------------------------------------------------------------- #
# Markdown -> blocks
# --------------------------------------------------------------------------- #

def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_divider(line):
    return bool(re.fullmatch(r"\|[\s:\-|]+\|", line.strip()))


def parse(md, demote=0):
    """Turn markdown into a flat list of blocks.

    demote raises every heading by that many levels, so a second document can
    be folded in underneath an appendix heading.
    """
    blocks = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            blocks.append(("hr",))
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and is_divider(lines[i + 1]):
            rows = [split_row(stripped)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            width = max(len(r) for r in rows)
            rows = [r + [""] * (width - len(r)) for r in rows]
            blocks.append(("table", rows))
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            blocks.append(("h", min(len(m.group(1)) + demote, 6), m.group(2)))
            i += 1
            continue

        if stripped.startswith(">"):
            blocks.append(("quote", stripped.lstrip("> ").strip()))
            i += 1
            continue

        m = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if m:
            blocks.append(("ol", m.group(2)))
            i += 1
            continue

        m = re.match(r"^([-*+])\s+(.*)$", stripped)
        if m:
            indent = len(line) - len(line.lstrip())
            blocks.append(("ul", m.group(2), 1 if indent >= 2 else 0))
            i += 1
            continue

        buf = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", "|", ">", "-", "*", "+")) or re.match(r"^\d+\.\s", nxt):
                break
            buf.append(nxt)
            i += 1
        blocks.append(("p", " ".join(buf)))

    return blocks


def build_blocks():
    memo = parse(MEMO.read_text(encoding="utf-8"))

    extract = parse(DATA.read_text(encoding="utf-8"), demote=1)
    # Drop the extract's own title; it becomes the appendix heading instead.
    if extract and extract[0][0] == "h":
        extract = extract[1:]

    return memo + [("hr",), ("h", 2, "Appendix F — Source data extract")] + extract


# --------------------------------------------------------------------------- #
# Word
# --------------------------------------------------------------------------- #

def docx_runs(paragraph, text):
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            paragraph.add_run(piece[2:-2]).bold = True
        elif piece.startswith("`") and piece.endswith("`"):
            run = paragraph.add_run(piece[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(9)
        elif piece.startswith("*") and piece.endswith("*"):
            paragraph.add_run(piece[1:-1]).italic = True
        else:
            paragraph.add_run(piece)


def shade(cell, colour):
    pr = cell._tc.get_or_add_tcPr()
    el = pr.makeelement(qn("w:shd"), {})
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), colour)
    pr.append(el)


def render_docx(blocks, out):
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)

    for section in doc.sections:
        section.left_margin = section.right_margin = Inches(0.6)
        section.top_margin = section.bottom_margin = Inches(0.6)

    for block in blocks:
        kind = block[0]

        if kind == "hr":
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            pr = p._p.get_or_add_pPr()
            border = pr.makeelement(qn("w:pBdr"), {})
            bottom = border.makeelement(qn("w:bottom"), {})
            bottom.set(qn("w:val"), "single")
            bottom.set(qn("w:sz"), "6")
            bottom.set(qn("w:color"), "BBBBBB")
            border.append(bottom)
            pr.append(border)

        elif kind == "h":
            level, text = block[1], block[2]
            if level == 1:
                p = doc.add_paragraph()
                docx_runs(p, text)
                for run in p.runs:
                    run.bold = True
                    run.font.size = Pt(17)
                    run.font.color.rgb = ACCENT_RGB
                p.paragraph_format.space_after = Pt(12)
            else:
                h = doc.add_heading(level=min(level, 4))
                h.text = ""
                docx_runs(h, text)
                for run in h.runs:
                    run.font.color.rgb = ACCENT_RGB
                    run.font.size = Pt({2: 14, 3: 12, 4: 11}.get(level, 11))

        elif kind == "quote":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            docx_runs(p, block[1])
            for run in p.runs:
                run.italic = True
                run.font.color.rgb = MUTED_RGB

        elif kind == "ol":
            docx_runs(doc.add_paragraph(style="List Number"), block[1])

        elif kind == "ul":
            style = "List Bullet 2" if block[2] else "List Bullet"
            docx_runs(doc.add_paragraph(style=style), block[1])

        elif kind == "table":
            rows = block[1]
            size = Pt(8.5 if len(rows[0]) <= 8 else 6.5)
            table = doc.add_table(rows=1, cols=len(rows[0]))
            table.style = "Table Grid"
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            for cell, text in zip(table.rows[0].cells, rows[0]):
                docx_runs(cell.paragraphs[0], text)
                for run in cell.paragraphs[0].runs:
                    run.bold = True
                    run.font.size = size
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                shade(cell, ACCENT_HEX)
            for r in rows[1:]:
                cells = table.add_row().cells
                for cell, text in zip(cells, r):
                    docx_runs(cell.paragraphs[0], text)
                    for run in cell.paragraphs[0].runs:
                        run.font.size = size
            doc.add_paragraph()

        else:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            docx_runs(p, block[1])

    doc.save(out)
    return out


# --------------------------------------------------------------------------- #
# PDF
# --------------------------------------------------------------------------- #

def pdf_markdown(text):
    """fpdf2 markdown understands **bold** and __italic__, not *italic*."""
    out = []
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            out.append(piece)
        elif piece.startswith("`") and piece.endswith("`"):
            out.append(piece[1:-1])
        elif piece.startswith("*") and piece.endswith("*"):
            out.append("__" + piece[1:-1] + "__")
        else:
            out.append(piece)
    return "".join(out)


def column_weights(rows):
    """Relative column widths, so label columns are not squeezed by year columns.

    Weighted towards the longest cell in each column but clamped at both ends,
    which keeps a 17-column table legible without starving the first column.
    """
    weights = []
    for col in range(len(rows[0])):
        longest = max(len(re.sub(r"[*`]", "", r[col])) for r in rows)
        weights.append(min(max(longest, 6), 30))
    return tuple(weights)


class Memo(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("DejaVu", "", 7)
        self.set_text_color(0x77, 0x77, 0x77)
        self.cell(0, 6, f"{self.page_no()}", align="C")


def render_pdf(blocks, out):
    pdf = Memo(orientation="P", unit="mm", format="A4")
    pdf.set_margins(12, 12, 12)
    pdf.set_auto_page_break(True, margin=15)

    pdf.add_font("DejaVu", "", FONT_DIR / "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "B", FONT_DIR / "DejaVuSans-Bold.ttf")
    # No oblique face ships with this family; regular stands in for italic.
    pdf.add_font("DejaVu", "I", FONT_DIR / "DejaVuSans.ttf")
    pdf.add_font("DejaVu", "BI", FONT_DIR / "DejaVuSans-Bold.ttf")
    pdf.set_font("DejaVu", "", 9)

    pdf.add_page()

    for block in blocks:
        kind = block[0]

        if kind == "hr":
            pdf.ln(1.5)
            pdf.set_draw_color(0xBB, 0xBB, 0xBB)
            pdf.set_line_width(0.2)
            y = pdf.get_y()
            pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
            pdf.ln(2.5)

        elif kind == "h":
            level, text = block[1], block[2]
            size = {1: 16, 2: 12.5, 3: 10.5, 4: 9.5}.get(level, 9)
            pdf.ln(2 if level > 2 else 3)
            pdf.set_font("DejaVu", "B", size)
            pdf.set_text_color(*ACCENT_PDF)
            pdf.multi_cell(0, size * 0.48, pdf_markdown(text), markdown=True,
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("DejaVu", "", 9)
            pdf.ln(1.2)

        elif kind == "quote":
            pdf.set_font("DejaVu", "I", 8.5)
            pdf.set_text_color(0x55, 0x55, 0x55)
            pdf.set_x(pdf.l_margin + 6)
            pdf.multi_cell(pdf.epw - 6, 4.2, pdf_markdown(block[1]), markdown=True,
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font("DejaVu", "", 9)
            pdf.ln(1)

        elif kind in ("ul", "ol"):
            indent = 6 + (4 if kind == "ul" and block[2] else 0)
            bullet = "\u2022  " if kind == "ul" else "\u2013  "
            pdf.set_x(pdf.l_margin + indent)
            pdf.multi_cell(pdf.epw - indent, 4.3, bullet + pdf_markdown(block[1]),
                           markdown=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(0.8)

        elif kind == "table":
            rows = block[1]
            ncols = len(rows[0])
            size = 7.5 if ncols <= 5 else 6.5 if ncols <= 8 else 5.2 if ncols <= 12 else 4.3
            pdf.set_font("DejaVu", "", size)
            with pdf.table(
                col_widths=column_weights(rows),
                borders_layout="ALL",
                cell_fill_color=(0xF2, 0xF5, 0xF8),
                cell_fill_mode=TableCellFillMode.ROWS,
                headings_style=FontFace(
                    emphasis="BOLD",
                    color=(0xFF, 0xFF, 0xFF),
                    fill_color=ACCENT_PDF,
                ),
                line_height=size * 0.62,
                markdown=True,
                first_row_as_headings=True,
            ) as table:
                for r in rows:
                    row = table.row()
                    for datum in r:
                        row.cell(pdf_markdown(datum))
            pdf.set_font("DejaVu", "", 9)
            pdf.ln(3)

        else:
            pdf.set_font("DejaVu", "", 9)
            pdf.multi_cell(0, 4.4, pdf_markdown(block[1]), markdown=True,
                           new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(1.6)

    pdf.output(str(out))
    return out


if __name__ == "__main__":
    for path in (MEMO, DATA):
        if not path.exists():
            sys.exit(f"missing source: {path}")

    blocks = build_blocks()
    for out in (render_docx(blocks, HERE / f"{STEM}.docx"),
                render_pdf(blocks, HERE / f"{STEM}.pdf")):
        print(f"wrote {out.name} ({out.stat().st_size // 1024} KB)")
