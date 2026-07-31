#!/usr/bin/env python3
"""Render the markdown memo into a Word document for circulation.

Handles the subset of markdown used in the memo: ATX headings, pipe tables,
bullet and numbered lists, block quotes, horizontal rules, and inline bold,
italic and code spans.

    pip install python-docx && python3 build_docx.py
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Inches

HERE = Path(__file__).parent
SOURCES = [
    ("expert-call-memo.md", "Expert-Call-Memo-DNA-Sequencer.docx"),
    ("source-data-extract.md", "Source-Data-Extract-DNA-Sequencer.docx"),
]

ACCENT = RGBColor(0x1F, 0x3A, 0x5F)
MUTED = RGBColor(0x55, 0x55, 0x55)

# Bold, italic and code spans, in one pass so nesting order does not matter.
INLINE = re.compile(r"(\*\*.+?\*\*|(?<!\*)\*(?!\*).+?(?<!\*)\*(?!\*)|`[^`]+`)")


def add_runs(paragraph, text):
    """Write text into a paragraph, honouring inline markdown."""
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


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_divider(line):
    return bool(re.fullmatch(r"\|[\s:\-|]+\|", line.strip()))


def shade(cell, colour):
    el = cell._tc.get_or_add_tcPr().makeelement(qn("w:shd"), {})
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), colour)
    cell._tc.get_or_add_tcPr().append(el)


def add_table(doc, rows):
    header, body = rows[0], rows[1:]
    table = doc.add_table(rows=1, cols=len(header))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    for cell, text in zip(table.rows[0].cells, header):
        cell.paragraphs[0].clear() if hasattr(cell.paragraphs[0], "clear") else None
        add_runs(cell.paragraphs[0], text)
        for run in cell.paragraphs[0].runs:
            run.bold = True
            run.font.size = Pt(8.5)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade(cell, "1F3A5F")

    for r in body:
        cells = table.add_row().cells
        # Tolerate ragged rows rather than failing the whole build.
        for cell, text in zip(cells, r + [""] * (len(header) - len(r))):
            add_runs(cell.paragraphs[0], text)
            for run in cell.paragraphs[0].runs:
                run.font.size = Pt(8.5)

    doc.add_paragraph()
    return table


def build(md_path: Path, out_path: Path):
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)

    for section in doc.sections:
        section.left_margin = section.right_margin = Inches(0.7)
        section.top_margin = section.bottom_margin = Inches(0.7)

    lines = md_path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Horizontal rule
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            border = p._p.get_or_add_pPr().makeelement(qn("w:pBdr"), {})
            bottom = border.makeelement(qn("w:bottom"), {})
            bottom.set(qn("w:val"), "single")
            bottom.set(qn("w:sz"), "6")
            bottom.set(qn("w:color"), "BBBBBB")
            border.append(bottom)
            p._p.get_or_add_pPr().append(border)
            i += 1
            continue

        # Table: a pipe row followed by a divider row
        if stripped.startswith("|") and i + 1 < len(lines) and is_divider(lines[i + 1]):
            rows = [split_row(stripped)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            add_table(doc, rows)
            continue

        # Headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level, text = len(m.group(1)), m.group(2)
            if level == 1:
                p = doc.add_paragraph()
                add_runs(p, text)
                for run in p.runs:
                    run.bold = True
                    run.font.size = Pt(18)
                    run.font.color.rgb = ACCENT
                p.paragraph_format.space_after = Pt(12)
            else:
                h = doc.add_heading(level=min(level, 4))
                h.text = ""
                add_runs(h, text)
                for run in h.runs:
                    run.font.color.rgb = ACCENT
                    run.font.size = Pt({2: 14, 3: 12, 4: 11}.get(level, 11))
            i += 1
            continue

        # Block quote
        if stripped.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            add_runs(p, stripped.lstrip("> ").strip())
            for run in p.runs:
                run.italic = True
                run.font.color.rgb = MUTED
            i += 1
            continue

        # Numbered list
        m = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if m:
            p = doc.add_paragraph(style="List Number")
            add_runs(p, m.group(2))
            i += 1
            continue

        # Bullet list, including one level of nesting
        m = re.match(r"^([-*+])\s+(.*)$", stripped)
        if m:
            indent = len(line) - len(line.lstrip())
            p = doc.add_paragraph(style="List Bullet 2" if indent >= 2 else "List Bullet")
            add_runs(p, m.group(2))
            i += 1
            continue

        # Paragraph, joining soft-wrapped lines
        buf = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", "|", ">", "-", "*", "+")) or re.match(r"^\d+\.\s", nxt):
                break
            buf.append(nxt)
            i += 1
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_runs(p, " ".join(buf))

    doc.save(out_path)
    return out_path


if __name__ == "__main__":
    for src, dst in SOURCES:
        path = HERE / src
        if not path.exists():
            sys.exit(f"missing source: {path}")
        out = build(path, HERE / dst)
        print(f"wrote {out.name} ({out.stat().st_size // 1024} KB)")
