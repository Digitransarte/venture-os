"""Convert Venture OS source DOCX files to conservative Markdown.

The converter is intentionally non-destructive: it only reads ``docs/_source_word``
and writes Markdown (plus embedded media, when present) under ``docs/_converted``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path

from docx import Document
from docx.document import Document as DocumentType
from docx.oxml.ns import qn
from docx.table import Table, _Cell
from docx.text.paragraph import Paragraph
from docx.text.hyperlink import Hyperlink


@dataclass
class ConversionResult:
    source: str
    output: str
    sha256: str
    title: str
    paragraphs: int
    tables: int
    images: int
    warnings: list[str]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def kebab_case(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "document"


def iter_blocks(parent: DocumentType | _Cell):
    parent_element = parent.element.body if isinstance(parent, DocumentType) else parent._tc
    for child in parent_element.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def escape_cell(text: str) -> str:
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def inline_runs(paragraph: Paragraph) -> str:
    pieces: list[str] = []
    for item in paragraph.iter_inner_content():
        if isinstance(item, Hyperlink):
            label = item.text.strip()
            if label:
                pieces.append(f"[{label}]({item.url})" if item.url else label)
            continue
        run = item
        text = run.text
        if not text:
            continue
        text = text.replace("\r", "").replace("\v", "  \n")
        if run.font.strike:
            text = f"~~{text}~~"
        if run.italic:
            text = f"*{text}*"
        if run.bold:
            text = f"**{text}**"
        pieces.append(text)
    return "".join(pieces).strip()


def list_info(paragraph: Paragraph) -> tuple[bool, int, bool]:
    p_pr = paragraph._p.pPr
    if p_pr is not None and p_pr.numPr is not None:
        level = int(p_pr.numPr.ilvl.val) if p_pr.numPr.ilvl is not None else 0
        num_id = int(p_pr.numPr.numId.val) if p_pr.numPr.numId is not None else 0
        return True, level, num_id != 0
    style = (paragraph.style.name if paragraph.style else "").lower()
    if "list" in style:
        level_match = re.search(r"(\d+)$", style)
        level = max(0, int(level_match.group(1)) - 1) if level_match else 0
        return True, level, "number" in style
    return False, 0, False


def paragraph_markdown(paragraph: Paragraph) -> str:
    text = inline_runs(paragraph)
    if not text:
        return ""
    style = (paragraph.style.name if paragraph.style else "").strip()
    style_lower = style.lower()
    heading = re.match(r"heading\s+(\d+)", style_lower)
    if style_lower in {"title", "subtitle"}:
        level = 1 if style_lower == "title" else 2
        return f"{'#' * level} {text}"
    if heading:
        return f"{'#' * min(6, int(heading.group(1)))} {text}"
    is_list, level, numbered = list_info(paragraph)
    if is_list:
        return f"{'  ' * level}{'1.' if numbered else '-'} {text}"
    if "quote" in style_lower or "citation" in style_lower:
        return "\n".join(f"> {line}" for line in text.splitlines())
    if "code" in style_lower or "source" in style_lower:
        return f"```\n{text}\n```"
    return text


def table_markdown(table: Table) -> str:
    rows = [[escape_cell("\n".join(p.text for p in cell.paragraphs).strip()) for cell in row.cells]
            for row in table.rows]
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    header = rows[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * width) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return "\n".join(lines)


def archive_features(path: Path) -> list[str]:
    warnings: list[str] = []
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        document_xml = archive.read("word/document.xml")
        if b"<w:txbxContent" in document_xml:
            warnings.append("Contém caixas de texto; a posição visual pode não ser preservada.")
        if b"<w:footnoteReference" in document_xml:
            warnings.append("Contém notas de rodapé; requer revisão da conversão.")
        if b"<w:endnoteReference" in document_xml:
            warnings.append("Contém notas finais; requer revisão da conversão.")
        if "word/comments.xml" in names:
            comments_xml = archive.read("word/comments.xml")
            if b"<w:comment " in comments_xml:
                warnings.append("Contém comentários de revisão, não incorporados no Markdown.")
        if b"<w:ins" in document_xml or b"<w:del" in document_xml:
            warnings.append("Contém alterações controladas; requer revisão humana.")
        if b"<m:oMath" in document_xml:
            warnings.append("Contém equações Word; a formatação pode perder-se.")
        if b"<w:smartTag" in document_xml or b"<w:sdt" in document_xml:
            warnings.append("Contém elementos Word estruturados; a semântica visual pode perder-se.")
    return warnings


def extract_images(document: DocumentType, output_dir: Path, stem: str) -> list[str]:
    image_rels = [rel for rel in document.part.rels.values() if "image" in rel.reltype]
    if not image_rels:
        return []
    asset_dir = output_dir / "assets" / stem
    asset_dir.mkdir(parents=True, exist_ok=True)
    links: list[str] = []
    for index, rel in enumerate(image_rels, 1):
        part = rel.target_part
        suffix = Path(str(part.partname)).suffix or ".bin"
        filename = f"image-{index}{suffix.lower()}"
        (asset_dir / filename).write_bytes(part.blob)
        links.append(f"![Imagem extraída {index}](assets/{stem}/{filename})")
    return links


def convert(source: Path, output_dir: Path) -> ConversionResult:
    document = Document(source)
    stem = kebab_case(source.stem)
    output = output_dir / f"{stem}.md"
    warnings = archive_features(source)
    blocks: list[str] = []
    paragraph_count = 0
    table_count = 0
    title = ""
    for block in iter_blocks(document):
        if isinstance(block, Paragraph):
            paragraph_count += 1
            markdown = paragraph_markdown(block)
            if markdown:
                if not title:
                    title = re.sub(r"^#{1,6}\s+", "", markdown).strip()
                blocks.append(markdown)
        else:
            table_count += 1
            markdown = table_markdown(block)
            if markdown:
                blocks.append(markdown)
    supplementary: list[str] = []
    seen_parts: set[str] = set()
    for section in document.sections:
        for label, part in (("Cabeçalho", section.header), ("Rodapé", section.footer)):
            key = str(part.part.partname)
            if key in seen_parts:
                continue
            seen_parts.add(key)
            content = [paragraph_markdown(p) for p in part.paragraphs]
            content = [item for item in content if item]
            if content:
                supplementary.extend([f"### {label}", *content])
    if supplementary:
        blocks.extend(["## Conteúdo de cabeçalhos e rodapés", *supplementary])
        warnings.append("Cabeçalhos/rodapés foram preservados no final, sem posicionamento de página.")
    image_links = extract_images(document, output_dir, stem)
    if image_links:
        warnings.append("Imagens extraídas no final; a posição original deve ser revista.")
        blocks.extend(["## Imagens extraídas", *image_links])
    output.write_text("\n\n".join(blocks).rstrip() + "\n", encoding="utf-8")
    return ConversionResult(
        source=source.name,
        output=output.name,
        sha256=sha256(source),
        title=title or source.stem,
        paragraphs=paragraph_count,
        tables=table_count,
        images=len(image_links),
        warnings=warnings,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("docs/_source_word"))
    parser.add_argument("--output", type=Path, default=Path("docs/_converted"))
    parser.add_argument("--metadata", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    results = [convert(path, args.output) for path in sorted(args.source.rglob("*.docx"), key=lambda p: p.name.lower())]
    payload = [asdict(result) for result in results]
    if args.metadata:
        args.metadata.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
