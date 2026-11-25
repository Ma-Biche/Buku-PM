#!/usr/bin/env python3
"""
Build script Lengkap (12 Modul) untuk Buku Ajar & Panduan Praktik:
Senior Project Management, Business & System Analysis (Jilid I–III: Modul 01–12)

Menghasilkan:
1. buku-lengkap-modul-01-12.md    (Naskah buku lengkap Markdown + Indeks Glosarium A-Z)
2. buku-senior-pm-modul-01-12.html (E-Book interaktif + Gambar + Mermaid + KaTeX + Kuis Auto-Koreksi + Cetak A4 PDF)
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent

CHAPTER_FILES: List[Tuple[str, str, str, str]] = [
    # (filename, slug, sidebar_label, part_group)
    ("00-studi-kasus-utama.md", "studi-kasus", "00 — Studi Kasus Utama (Proyek OMNI)", "Pendahuluan"),
    ("modul-01-advanced-project-management.md", "modul-01", "Modul 01 — Advanced Project Management", "Jilid I: Leadership & Project Delivery"),
    ("modul-02-project-planning-execution.md", "modul-02", "Modul 02 — Project Planning & Execution", "Jilid I: Leadership & Project Delivery"),
    ("modul-03-risk-issue-stakeholder-management.md", "modul-03", "Modul 03 — Risk, Issue & Stakeholder Management", "Jilid I: Leadership & Project Delivery"),
    ("modul-04-agile-scrum-hybrid-pm.md", "modul-04", "Modul 04 — Agile, Scrum & Hybrid PM", "Jilid I: Leadership & Project Delivery"),
    ("modul-05-program-management-pmo.md", "modul-05", "Modul 05 — Program Management & PMO", "Jilid I: Leadership & Project Delivery"),
    ("modul-06-advanced-business-analysis.md", "modul-06", "Modul 06 — Advanced Business Analysis", "Jilid II: Business & System Analysis"),
    ("modul-07-system-analysis-design.md", "modul-07", "Modul 07 — System Analysis & Design", "Jilid II: Business & System Analysis"),
    ("modul-08-solution-architecture-integration.md", "modul-08", "Modul 08 — Solution Architecture & Integration", "Jilid II: Business & System Analysis"),
    ("modul-09-product-management-ownership.md", "modul-09", "Modul 09 — Product Management & Ownership", "Jilid II: Business & System Analysis"),
    ("modul-10-business-strategy-financial-management.md", "modul-10", "Modul 10 — Business Strategy & Financial Management", "Jilid III: Executive & Career Advancement"),
    ("modul-11-leadership-negotiation-executive-communication.md", "modul-11", "Modul 11 — Leadership, Negotiation & Exec Comm", "Jilid III: Executive & Career Advancement"),
    ("modul-12-career-positioning-interview-simulation.md", "modul-12", "Modul 12 — Career Positioning & Interview Simulation", "Jilid III: Executive & Career Advancement"),
]

LOCAL_MD_ANCHOR_MAP = {Path(fn).stem: f"#chap-{slug}" for fn, slug, _, _ in CHAPTER_FILES}


def slugify(text: str) -> str:
    clean = re.sub(r"<[^>]+>", "", text)
    clean = re.sub(r"[`*_~]", "", clean).strip().lower()
    clean = re.sub(r"[^\w\s-]", "", clean)
    clean = re.sub(r"[\s_]+", "-", clean)
    return clean.strip("-") or "bagian"


def extract_glossary_entries(chapters: List[Tuple[str, str]]) -> List[Tuple[str, str, str]]:
    """Ekstrak entri glosarium dari sub-bab 10.2 Glosarium di setiap modul."""
    entries: List[Tuple[str, str, str]] = []
    seen = set()
    for mod_label, md in chapters:
        m = re.search(
            r"^###\s+10\.2\s+Glosarium.*?\n(.*?)(?=^###\s+10\.3|^##\s+11\.|\Z)",
            md,
            flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        if not m:
            continue
        block = m.group(1)
        for line in block.splitlines():
            s = line.strip()
            if s.startswith("|") and s.endswith("|"):
                cells = [c.strip() for c in s.strip("|").split("|")]
                if len(cells) >= 2:
                    term = re.sub(r"[*_`]", "", cells[0]).strip()
                    defn = cells[1].strip()
                    if (
                        not term
                        or set(term) <= {"-", ":", " "}
                        or term.lower() in {"istilah", "term", "istilah / konsep", "istilah teknis", "istilah (inggris)"}
                    ):
                        continue
                    key = term.lower()
                    if key not in seen:
                        seen.add(key)
                        entries.append((term, defn, mod_label))
            else:
                bm = re.match(r"^[-*]\s+\*\*(.+?)\*\*\s*[:—–-]\s*(.+)$", s)
                if bm:
                    term = bm.group(1).strip()
                    defn = bm.group(2).strip()
                    key = term.lower()
                    if key not in seen:
                        seen.add(key)
                        entries.append((term, defn, mod_label))
    entries.sort(key=lambda x: x[0].lower())
    return entries


def build_combined_markdown(chapter_contents: List[Tuple[str, str, str, str, str]]) -> str:
    """Bangun berkas Markdown gabungan buku-lengkap-modul-01-12.md."""
    glossary = extract_glossary_entries(
        [(label.split("—")[0].strip(), content) for _, _, label, _, content in chapter_contents if "Modul" in label]
    )

    parts: List[str] = []
    parts.append(
        """# Buku Ajar & Panduan Praktik Lengkap: Senior Project Management, Business & System Analysis

## Edisi Lengkap 12 Modul (Jilid I, II, dan III)

Disusun berdasarkan dokumen **"Rancangan 12 modul pembelajaran – PM"**
Studi Kasus Berkelanjutan: **PT Sinar Nusantara Retail (SNR) — Proyek OMNI & Program Nusantara 2028**

| Keterangan | Detail |
|------------|--------|
| **Cakupan Buku** | Studi Kasus Utama (00) + Modul 01 sampai Modul 12 (Lengkap 3 Jalur) |
| **Jilid I (Modul 01–05)** | Jalur Utama — *Project Management: Leadership & Project Delivery* |
| **Jilid II (Modul 06–09)** | Jalur Alternatif — *Business & System Analysis: Business & Solution Design* |
| **Jilid III (Modul 10–12)** | *Executive & Career Advancement* (untuk semua jalur, termasuk Capstone) |
| **Total Durasi Pembelajaran** | 144 jam sesi interaktif (48 sesi × 3 jam) + ±72 jam tugas mandiri |
| **Konvensi Mata Uang & Angka** | `Rp 1 M` = Rp 1 miliar; `Rp 1 jt` = Rp 1 juta; desimal memakai koma (contoh: `0,94`) |

---

## Kata Pengantar & Panduan Membaca

Buku edisi lengkap ini merangkum seluruh 12 modul kompetensi yang dibutuhkan praktisi menengah (±3 tahun pengalaman) untuk naik kelas menjadi **Senior Project Manager**, **Senior Business Analyst**, atau **System Analyst / Solution Architect**. Seluruh bab disatukan oleh satu benang merah studi kasus yang hidup dari hulu ke hilir: **Proyek OMNI di PT Sinar Nusantara Retail Tbk (SNR)** — transformasi omnichannel bagi 120 toko fisik dengan anggaran **Rp 9,20 M** dan tenggat mutlak **26 November 2027**, sebagai proyek unggulan **Program Nusantara 2028** (Rp 18,50 M).

### Cara Memaksimalkan Buku Ini
1. Mulailah dari **Bagian 00 (Studi Kasus Utama)** untuk memahami lanskap bisnis, 13 tokoh kunci, anggaran, linimasa, dan risiko proyek.
2. Gunakan **ilustrasi gambar** dan **diagram Mermaid** di setiap bab untuk menangkap pola besar konsep sebelum masuk ke detail rumus atau spesifikasi teknis.
3. Pada versi HTML E-Book ([buku-senior-pm-modul-01-12.html](buku-senior-pm-modul-01-12.html)), seluruh **120 soal kuis (Modul 01–12)** dapat langsung dijawab dengan pilihan ganda interaktif (*radio choice*) dan dikoreksi seketika lengkap dengan skor, status kelulusan (`≥ 70`), serta pembahasan detail.

---

## Peta Jalur Belajar Program (Modul 01–12)

```mermaid
flowchart LR
    subgraph U["Jilid I — Project Management (Modul 01-05)"]
        M1["01 Advanced PM"] --> M2["02 Planning & Execution"] --> M3["03 Risk, Issue & Stakeholder"] --> M4["04 Agile, Scrum & Hybrid"] --> M5["05 Program & PMO"]
    end
    subgraph A["Jilid II — Business & System Analysis (Modul 06-09)"]
        M6["06 Advanced BA"] --> M7["07 System Analysis & Design"] --> M8["08 Solution Architecture"] --> M9["09 Product Management"]
    end
    subgraph E["Jilid III — Executive & Career (Modul 10-12)"]
        M10["10 Strategy & Finance"] --> M11["11 Leadership & Exec Comm"] --> M12["12 Career & Interview"]
    end
    M5 --> M10
    M9 --> M10
```

---
"""
    )

    for _, _, _, _, content in chapter_contents:
        parts.append(content.strip())
        parts.append("\n\n---\n\n")

    if glossary:
        lines = [
            "# Indeks Glosarium Gabungan (Modul 01–12)",
            "",
            "Daftar istilah teknis Bahasa Inggris–Indonesia yang dihimpun secara alfabetis dari seluruh 12 modul untuk memudahkan pencarian cepat.",
            "",
            "| Istilah | Penjelasan | Sumber |",
            "|---------|------------|--------|",
        ]
        for term, defn, src in glossary:
            safe_term = term.replace("|", "\\|")
            safe_defn = defn.replace("|", "\\|")
            lines.append(f"| **{safe_term}** | {safe_defn} | {src} |")
        parts.append("\n".join(lines) + "\n")

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Pure-Python Markdown -> Semantic, Accessible HTML Converter + Quiz Parser
# ---------------------------------------------------------------------------

def render_inline(text: str) -> str:
    """Konversi sintaks Markdown inline ke HTML aman sambil menjaga inline code & math KaTeX."""
    protected: List[str] = []

    def _stash(raw_html: str) -> str:
        protected.append(raw_html)
        return f"\x00TOK{len(protected) - 1}\x00"

    # 1. Protect inline code
    text = re.sub(
        r"`([^`]+)`",
        lambda m: _stash(f"<code>{html.escape(m.group(1))}</code>"),
        text,
    )
    # 2. Protect display & inline math ($P$, $n$, $\lambda$, $$...$$)
    text = re.sub(
        r"\$\$(.+?)\$\$",
        lambda m: _stash(f'<span class="math-display">$${html.escape(m.group(1))}$$</span>'),
        text,
    )
    text = re.sub(
        r"(?<!\$)\$(?!\$)(?!\s)([^$\n]+?)(?<!\s)\$(?!\$)",
        lambda m: _stash(f'<span class="math-inline">${html.escape(m.group(1))}$</span>'),
        text,
    )

    text = html.escape(text)

    # Inline images (if embedded inside paragraph)
    def _img_repl(match: re.Match[str]) -> str:
        alt = match.group(1)
        src = match.group(2).strip()
        return f'<img src="{src}" alt="{alt}" loading="lazy" decoding="async" class="inline-img">'

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _img_repl, text)

    # Links [label](url)
    def _link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        url = match.group(2).strip()
        if url.startswith(("http://", "https://")):
            return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'
        if url.endswith(".md"):
            stem = Path(url).stem
            target = LOCAL_MD_ANCHOR_MAP.get(stem, url)
            return f'<a href="{target}">{label}</a>'
        return f'<a href="{url}">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link_repl, text)
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"~~(.+?)~~", r"<del>\1</del>", text)
    text = text.replace("&lt;br/&gt;", "<br>").replace("&lt;br&gt;", "<br>")

    for idx, token in enumerate(protected):
        text = text.replace(f"\x00TOK{idx}\x00", token)
    return text


def split_table_row(line: str) -> List[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells = re.split(r"(?<!\\)\|", s)
    return [c.replace("\\|", "|").strip() for c in cells]


def is_table_separator(line: str) -> bool:
    s = line.strip()
    if "|" not in s:
        return False
    cells = split_table_row(s)
    if not cells:
        return False
    return all(bool(re.match(r"^:?-{2,}:?$", c.strip())) for c in cells if c.strip() != "")


def render_table(lines: List[str], table_idx: int) -> str:
    headers = split_table_row(lines[0])
    aligns: List[str] = []
    for sep in split_table_row(lines[1]):
        sep = sep.strip()
        if sep.startswith(":") and sep.endswith(":"):
            aligns.append("center")
        elif sep.endswith(":"):
            aligns.append("right")
        else:
            aligns.append("left")

    rows = [split_table_row(ln) for ln in lines[2:]]
    num_cols = len(headers)

    out = [
        f'<div tabindex="0" role="region" aria-label="Tabel data {table_idx}" class="table-wrapper">',
        f'<table data-cols="{num_cols}">',
        "<thead><tr>",
    ]
    for i, h in enumerate(headers):
        al = aligns[i] if i < len(aligns) else "left"
        out.append(f'<th scope="col" class="align-{al}">{render_inline(h)}</th>')
    out.append("</tr></thead><tbody>")

    for row in rows:
        out.append("<tr>")
        for i in range(num_cols):
            val = row[i] if i < len(row) else ""
            al = aligns[i] if i < len(aligns) else "left"
            label_attr = html.escape(re.sub(r"[*_`]", "", headers[i]), quote=True)
            if i == 0:
                out.append(
                    f'<th scope="row" class="align-{al}" data-label="{label_attr}">{render_inline(val)}</th>'
                )
            else:
                out.append(
                    f'<td class="align-{al}" data-label="{label_attr}">{render_inline(val)}</td>'
                )
        out.append("</tr>")

    out.append("</tbody></table></div>")
    return "\n".join(out)


def parse_quiz_keys(section_92_md: str) -> Dict[int, Tuple[str, str]]:
    """Ekstrak {no: (huruf_kunci, pembahasan_md)} dari sub-bab 9.2 (mendukung format tabel maupun daftar bernomor)."""
    keys: Dict[int, Tuple[str, str]] = {}

    # 1. Try Markdown table rows: | **1** | **B** | Explanation... |
    for line in section_92_md.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            cells = split_table_row(s)
            if len(cells) >= 3:
                num_m = re.search(r"(\d+)", cells[0])
                ans_m = re.search(r"\b([A-D])\b", re.sub(r"[*_`]", "", cells[1]).strip())
                if num_m and ans_m:
                    qnum = int(num_m.group(1))
                    if 1 <= qnum <= 20:
                        keys[qnum] = (ans_m.group(1).upper(), cells[2].strip())
    if len(keys) >= 10:
        return keys

    # 2. Try numbered list format: "1. **Jawaban: B.** ..." or "1. **Kunci: B.** ..."
    items = re.split(r"(?m)^(?=\d+\.\s+\*\*(?:Jawaban|Kunci)\s*[:.]?\s*[A-D])", section_92_md.strip())
    for item in items:
        item = item.strip()
        m = re.match(
            r"^(\d+)\.\s+\*\*(?:Jawaban|Kunci)\s*[:.]?\s*([A-D])\.?\*\*\s*(.*)$",
            item,
            flags=re.DOTALL | re.IGNORECASE,
        )
        if m:
            qnum = int(m.group(1))
            ans = m.group(2).upper()
            expl = re.sub(r"\n\s*[-*]\s+", "<br>• ", m.group(3).strip())
            expl = re.sub(r"\n+", "<br>", expl)
            keys[qnum] = (ans, expl)
    return keys


def parse_quiz_questions(section_91_md: str) -> List[Tuple[int, str, List[Tuple[str, str]]]]:
    """Ekstrak daftar (qnum, stem_md, [(letter, opt_md), ...]) dari sub-bab 9.1."""
    questions: List[Tuple[int, str, List[Tuple[str, str]]]] = []
    # Match start of each question: **1.** ... OR **Soal 1.** ... OR 1. **...**
    blocks = re.split(
        r"(?m)^(?=(?:\*\*(?:Soal\s+)?\d+\.?\*\*|\d+\.\s+\*\*))",
        section_91_md.strip(),
    )
    for blk in blocks:
        blk = blk.strip()
        if not blk:
            continue
        hm = re.match(
            r"^(?:\*\*(?:Soal\s+)?(\d+)\.?\*\*|(\d+)\.\s+)(.*)$",
            blk,
            flags=re.DOTALL,
        )
        if not hm:
            continue
        qnum = int(hm.group(1) or hm.group(2))
        rest = hm.group(3).strip()

        # Split stem vs options (- A. / A. / **A.**)
        lines = rest.splitlines()
        stem_lines: List[str] = []
        options: List[Tuple[str, str]] = []
        current_opt: Optional[Tuple[str, List[str]]] = None

        for ln in lines:
            om = re.match(r"^\s*(?:[-*]\s+)?(?:\*\*)?([A-D])[\.)](?:\*\*)?\s+(.+)$", ln)
            if om:
                if current_opt is not None:
                    options.append((current_opt[0], " ".join(current_opt[1]).strip()))
                current_opt = (om.group(1).upper(), [om.group(2).strip()])
            elif current_opt is not None:
                if ln.strip():
                    current_opt[1].append(ln.strip())
            else:
                if ln.strip():
                    stem_lines.append(ln.strip())

        if current_opt is not None:
            options.append((current_opt[0], " ".join(current_opt[1]).strip()))

        if len(options) >= 2:
            questions.append((qnum, "<br>".join(stem_lines), options))

    return questions


def render_interactive_quiz(
    chapter_slug: str,
    chapter_label: str,
    heading_id: str,
    questions: List[Tuple[int, str, List[Tuple[str, str]]]],
    keys: Dict[int, Tuple[str, str]],
) -> str:
    """Bangun form kuis pilihan ganda interaktif yang bisa langsung dikoreksi & dinilai otomatis."""
    mod_short = chapter_label.split("—")[0].strip()
    cards: List[str] = []

    for qnum, stem_md, options in questions:
        correct_letter, expl_md = keys.get(qnum, ("", ""))
        opt_html: List[str] = []
        for letter, opt_text in options:
            inp_id = f"q-{chapter_slug}-{qnum}-{letter}"
            name_attr = f"q-{chapter_slug}-{qnum}"
            opt_html.append(
                f'<label class="quiz-option" for="{inp_id}" data-option-letter="{letter}">'
                f'<input type="radio" id="{inp_id}" name="{name_attr}" value="{letter}">'
                f'<span class="opt-letter" aria-hidden="true">{letter}</span>'
                f'<span class="opt-text">{render_inline(opt_text)}</span>'
                f"</label>"
            )

        expl_rendered = render_inline(expl_md) if expl_md else "Lihat pembahasan lengkap pada bagian Kunci Jawaban di bawah."
        cards.append(
            f'<fieldset class="quiz-card" data-qnum="{qnum}" data-correct="{html.escape(correct_letter)}">'
            f'<legend class="quiz-legend">'
            f'<span class="q-badge">Soal {qnum}</span>'
            f'<span class="q-stem">{render_inline(stem_md)}</span>'
            f"</legend>"
            f'<div class="quiz-options">{"".join(opt_html)}</div>'
            f'<div class="quiz-card-actions">'
            f'<button type="button" class="btn btn-sm quiz-check-one">Periksa Soal Ini</button>'
            f"</div>"
            f'<div class="quiz-feedback" role="status" aria-live="polite" hidden>'
            f'<p class="quiz-feedback-status"></p>'
            f'<div class="quiz-feedback-expl">{expl_rendered}</div>'
            f"</div>"
            f"</fieldset>"
        )

    total_q = len(questions)
    return (
        f'<form class="quiz-form" data-quiz-module="{chapter_slug}" data-quiz-title="{html.escape(mod_short)}" '
        f'data-total="{total_q}" aria-labelledby="{heading_id}">'
        f'<div class="quiz-intro-bar">'
        f'<span><strong>Kuis Interaktif ({total_q} Pilihan Ganda):</strong> Pilih jawaban A–D pada setiap soal lalu klik <em>Periksa Soal Ini</em> atau <em>Koreksi Semua</em> untuk melihat skor dan pembahasan secara langsung.</span>'
        f"</div>"
        f'{"".join(cards)}'
        f'<div class="quiz-footer-bar">'
        f'<button type="submit" class="btn btn-primary">Koreksi Semua &amp; Hitung Skor ({total_q} Soal)</button>'
        f'<button type="button" class="btn quiz-reset-btn">Ulangi Kuis {html.escape(mod_short)}</button>'
        f"</div>"
        f'<div class="quiz-score-banner" role="status" aria-live="polite" hidden></div>'
        f"</form>"
    )


class MarkdownChapterConverter:
    """Konversi satu bab Markdown ke HTML semantik dengan gambar, Mermaid, KaTeX, TOC & kuis auto-koreksi."""

    def __init__(self, chapter_slug: str, chapter_label: str) -> None:
        self.chapter_slug = chapter_slug
        self.chapter_label = chapter_label
        self.toc_items: List[Tuple[int, str, str]] = []
        self.used_ids: set[str] = set()
        self.table_counter = 0
        self.diagram_counter = 0
        self.figure_counter = 0
        self.code_counter = 0
        self.quiz_question_count = 0

    def unique_id(self, base: str) -> str:
        candidate = f"{self.chapter_slug}-{slugify(base)}"
        if candidate not in self.used_ids:
            self.used_ids.add(candidate)
            return candidate
        n = 2
        while f"{candidate}-{n}" in self.used_ids:
            n += 1
        final = f"{candidate}-{n}"
        self.used_ids.add(final)
        return final

    def convert(self, md: str) -> str:
        # Pre-extract 9.1 and 9.2 for interactive self-grading quiz if this is a module
        quiz_keys: Dict[int, Tuple[str, str]] = {}
        quiz_questions: List[Tuple[int, str, List[Tuple[str, str]]]] = []
        m91 = re.search(r"^###\s+9\.1[^\n]*\n(.*?)(?=^###\s+9\.2)", md, flags=re.MULTILINE | re.DOTALL)
        m92 = re.search(r"^###\s+9\.2[^\n]*\n(.*?)(?=^##\s+10\.)", md, flags=re.MULTILINE | re.DOTALL)
        if m91 and m92:
            quiz_keys = parse_quiz_keys(m92.group(1))
            quiz_questions = parse_quiz_questions(m91.group(1))

        lines = md.replace("\r\n", "\n").split("\n")
        out: List[str] = []
        i = 0
        n = len(lines)
        in_disclosure = False

        def close_disclosure() -> None:
            nonlocal in_disclosure
            if in_disclosure:
                out.append("</div></details>")
                in_disclosure = False

        while i < n:
            line = lines[i]
            stripped = line.strip()

            if not stripped:
                i += 1
                continue

            if re.match(r"^(?:-{3,}|\*{3,}|_{3,})$", stripped):
                out.append("<hr>")
                i += 1
                continue

            # Standalone Markdown Image: ![Alt Caption](path/to/image.jpg)
            img_m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", stripped)
            if img_m:
                self.figure_counter += 1
                alt_txt = img_m.group(1).strip()
                src_path = img_m.group(2).strip()
                mod_short = self.chapter_label.split("—")[0].strip()
                fig_num = f"Gambar {mod_short}.{self.figure_counter}"
                out.append(
                    f'<figure class="editorial-figure">'
                    f'<button type="button" class="figure-zoom-btn" data-zoom-src="{html.escape(src_path, quote=True)}" '
                    f'data-zoom-alt="{html.escape(alt_txt, quote=True)}" '
                    f'aria-label="Perbesar {html.escape(fig_num, quote=True)}: {html.escape(alt_txt, quote=True)}">'
                    f'<img src="{html.escape(src_path, quote=True)}" alt="{html.escape(alt_txt, quote=True)}" '
                    f'loading="lazy" decoding="async" width="1280" height="720">'
                    f'<span class="zoom-hint" aria-hidden="true">Klik untuk memperbesar</span>'
                    f"</button>"
                    f"<figcaption><strong>{html.escape(fig_num)}:</strong> {render_inline(alt_txt)}</figcaption>"
                    f"</figure>"
                )
                i += 1
                continue

            # Display Math Block ($$ ... $$)
            if stripped.startswith("$$"):
                if stripped.endswith("$$") and len(stripped) > 4:
                    math_body = stripped[2:-2].strip()
                    out.append(f'<div class="math-block">$${html.escape(math_body)}$$</div>')
                    i += 1
                    continue
                math_lines: List[str] = []
                first_rem = stripped[2:].strip()
                if first_rem:
                    math_lines.append(first_rem)
                i += 1
                while i < n and not lines[i].strip().endswith("$$"):
                    math_lines.append(lines[i])
                    i += 1
                if i < n:
                    last_rem = lines[i].strip()[:-2].strip()
                    if last_rem:
                        math_lines.append(last_rem)
                    i += 1
                out.append(f'<div class="math-block">$${html.escape(chr(10).join(math_lines))}$$</div>')
                continue

            # Fenced code block or Mermaid diagram
            fence = re.match(r"^(`{3,})(.*)$", stripped)
            if fence:
                ticks = fence.group(1)
                lang = fence.group(2).strip().lower()
                code_lines: List[str] = []
                i += 1
                while i < n and not lines[i].strip().startswith(ticks):
                    code_lines.append(lines[i])
                    i += 1
                i += 1
                code_text = "\n".join(code_lines)

                if lang == "mermaid":
                    self.diagram_counter += 1
                    escaped_mermaid = html.escape(code_text)
                    mod_short = self.chapter_label.split("—")[0].strip()
                    out.append(
                        f'<figure class="mermaid-figure">'
                        f'<div class="mermaid-card">'
                        f'<div class="mermaid" data-mermaid-src="{html.escape(code_text, quote=True)}">{escaped_mermaid}</div>'
                        f"</div>"
                        f"<figcaption>Diagram {html.escape(mod_short)}.{self.diagram_counter}</figcaption>"
                        f"</figure>"
                    )
                else:
                    self.code_counter += 1
                    cls = f' class="language-{html.escape(lang)}"' if lang else ""
                    lbl = f"Blok kode atau template {self.code_counter}" + (f" ({lang})" if lang else "")
                    out.append(
                        f'<figure class="code-figure">'
                        f'<pre role="region" aria-label="{html.escape(lbl, quote=True)}" tabindex="0">'
                        f"<code{cls}>{html.escape(code_text)}</code></pre>"
                        f"</figure>"
                    )
                continue

            # Headings (# -> h2, ## -> h3, ### -> h4, #### -> h5)
            hm = re.match(r"^(#{1,5})\s+(.+)$", stripped)
            if hm:
                md_level = len(hm.group(1))
                raw_title = hm.group(2).strip()
                plain_title = re.sub(r"[*_`]", "", raw_title)

                if in_disclosure and md_level <= 3:
                    close_disclosure()

                html_level = min(md_level + 1, 6)
                hid = f"chap-{self.chapter_slug}" if md_level == 1 else self.unique_id(plain_title)

                if md_level == 1:
                    out.append(
                        f'<header class="chapter-header">'
                        f'<p class="chapter-kicker">{html.escape(self.chapter_label.split("—")[0].strip())}</p>'
                        f'<h2 id="{hid}" class="chapter-title">{render_inline(raw_title)}</h2>'
                        f"</header>"
                    )
                else:
                    out.append(f'<h{html_level} id="{hid}">{render_inline(raw_title)}</h{html_level}>')

                if md_level in (1, 2):
                    self.toc_items.append((md_level, hid, plain_title))

                # Interactive Auto-Graded Quiz for ### 9.1 Soal Kuis!
                if md_level == 3 and re.match(r"^9\.1\b", plain_title) and len(quiz_questions) >= 5 and len(quiz_keys) >= 5:
                    self.quiz_question_count = len(quiz_questions)
                    out.append(
                        render_interactive_quiz(
                            self.chapter_slug,
                            self.chapter_label,
                            hid,
                            quiz_questions,
                            quiz_keys,
                        )
                    )
                    # Skip raw Markdown lines until ### 9.2
                    i += 1
                    while i < n and not re.match(r"^###\s+9\.2\b", lines[i].strip()):
                        i += 1
                    continue

                # Wrap "7.2 Pembahasan Latihan" and "9.2 Kunci Jawaban..." in native searchable <details>
                if md_level == 3 and re.search(
                    r"(?:7\.2\s+Pembahasan|9\.2\s+Kunci\s+Jawaban|Pembahasan\s+Latihan|Kunci\s+Jawaban)",
                    plain_title,
                    flags=re.IGNORECASE,
                ):
                    summary_label = (
                        "Buka / Tutup Pembahasan Latihan"
                        if "pembahasan latihan" in plain_title.lower() or "7.2" in plain_title
                        else "Buka / Tutup Rekap Kunci Jawaban & Pembahasan Lengkap"
                    )
                    out.append(
                        f'<details class="answer-disclosure">'
                        f"<summary>{summary_label} ({html.escape(self.chapter_label.split('—')[0].strip())})</summary>"
                        f'<div class="disclosure-body">'
                    )
                    in_disclosure = True

                i += 1
                continue

            # Markdown Table
            if "|" in stripped and i + 1 < n and is_table_separator(lines[i + 1]):
                tbl_lines = [lines[i], lines[i + 1]]
                i += 2
                while i < n and lines[i].strip() and "|" in lines[i]:
                    tbl_lines.append(lines[i])
                    i += 1
                self.table_counter += 1
                out.append(render_table(tbl_lines, self.table_counter))
                continue

            # Blockquote / Callout
            if stripped.startswith(">"):
                bq_lines: List[str] = []
                while i < n and lines[i].strip().startswith(">"):
                    bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                    i += 1
                bq_text = "\n".join(bq_lines)
                callout_cls = "callout"
                if re.search(r"^\*\*Peringatan|\[!WARNING\]|\[!CAUTION\]", bq_text, re.IGNORECASE):
                    callout_cls += " callout-warn"
                elif re.search(r"^\*\*Tips|^\*\*Kiat|\[!TIP\]", bq_text, re.IGNORECASE):
                    callout_cls += " callout-tip"
                bq_text = re.sub(r"^\[!(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*", "", bq_text)
                inner_paras = [
                    f"<p>{render_inline(' '.join(p.splitlines()))}</p>"
                    for p in re.split(r"\n\s*\n", bq_text.strip())
                    if p.strip()
                ]
                out.append(f'<blockquote class="{callout_cls}">{"".join(inner_paras)}</blockquote>')
                continue

            # Lists
            if re.match(r"^(\s*)[-*+]\s+(.+)$", line) or re.match(r"^(\s*)\d+[.)]\s+(.+)$", line):
                list_html, i = self._parse_list(lines, i)
                out.append(list_html)
                continue

            # Paragraph
            para_lines = [stripped]
            i += 1
            while i < n:
                nxt = lines[i]
                ns = nxt.strip()
                if (
                    not ns
                    or re.match(r"^#{1,5}\s+", ns)
                    or re.match(r"^(`{3,})", ns)
                    or ns.startswith("$$")
                    or re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", ns)
                    or re.match(r"^(?:-{3,}|\*{3,}|_{3,})$", ns)
                    or ns.startswith(">")
                    or re.match(r"^\s*[-*+]\s+", nxt)
                    or re.match(r"^\s*\d+[.)]\s+", nxt)
                    or ("|" in ns and i + 1 < n and is_table_separator(lines[i + 1]))
                ):
                    break
                para_lines.append(ns)
                i += 1
            out.append(f"<p>{render_inline(' '.join(para_lines))}</p>")

        close_disclosure()
        return "\n".join(out)

    def _parse_list(self, lines: List[str], start: int) -> Tuple[str, int]:
        n = len(lines)
        first = lines[start]
        base_indent = len(first) - len(first.lstrip(" "))
        is_ordered = bool(re.match(r"^\s*\d+[.)]\s+", first))
        tag = "ol" if is_ordered else "ul"
        items: List[str] = []
        i = start

        while i < n:
            line = lines[i]
            if not line.strip():
                j = i + 1
                while j < n and not lines[j].strip():
                    j += 1
                if j < n:
                    nxt = lines[j]
                    nxt_indent = len(nxt) - len(nxt.lstrip(" "))
                    same_kind = (
                        bool(re.match(r"^\s*\d+[.)]\s+", nxt))
                        if is_ordered
                        else bool(re.match(r"^\s*[-*+]\s+", nxt))
                    )
                    if (nxt_indent == base_indent and same_kind) or nxt_indent > base_indent:
                        i = j
                        continue
                break

            indent = len(line) - len(line.lstrip(" "))
            if indent < base_indent:
                break

            if indent == base_indent:
                m = (
                    re.match(r"^\s*\d+[.)]\s+(.+)$", line)
                    if is_ordered
                    else re.match(r"^\s*[-*+]\s+(.+)$", line)
                )
                if not m:
                    break
                item_buf = [render_inline(m.group(1).strip())]
                i += 1
                while i < n:
                    if not lines[i].strip():
                        k = i + 1
                        while k < n and not lines[k].strip():
                            k += 1
                        if k < n and (len(lines[k]) - len(lines[k].lstrip(" "))) > base_indent:
                            i = k
                            continue
                        break
                    sub_indent = len(lines[i]) - len(lines[i].lstrip(" "))
                    if sub_indent > base_indent:
                        if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", lines[i]):
                            sub_html, i = self._parse_list(lines, i)
                            item_buf.append(sub_html)
                        else:
                            item_buf.append("<br>" + render_inline(lines[i].strip()))
                            i += 1
                    else:
                        break
                items.append(f"<li>{''.join(item_buf)}</li>")
            else:
                sub_html, i = self._parse_list(lines, i)
                if items:
                    items[-1] = items[-1][:-5] + sub_html + "</li>"
                else:
                    items.append(f"<li>{sub_html}</li>")

        return f"<{tag}>\n" + "\n".join(items) + f"\n</{tag}>", i


def build_html_ebook(chapter_contents: List[Tuple[str, str, str, str, str]]) -> Tuple[str, Dict[str, int]]:
    """Bangun berkas HTML E-Book lengkap 12 modul dengan gambar, Mermaid, KaTeX & Kuis Interaktif."""
    glossary = extract_glossary_entries(
        [(label.split("—")[0].strip(), content) for _, _, label, _, content in chapter_contents if "Modul" in label]
    )

    sections_html: List[str] = []
    toc_groups_html: List[str] = []
    quiz_pills_html: List[str] = []
    total_words = 0
    total_diagrams = 0
    total_figures = 0
    total_quiz_questions = 0
    last_part = ""

    for _, slug, label, part_group, md in chapter_contents:
        total_words += len(md.split())
        conv = MarkdownChapterConverter(slug, label)
        body_html = conv.convert(md)
        total_diagrams += conv.diagram_counter
        total_figures += conv.figure_counter
        total_quiz_questions += conv.quiz_question_count

        sections_html.append(
            f'<article class="book-chapter" id="section-{slug}">\n{body_html}\n</article>'
        )

        if part_group != last_part:
            toc_groups_html.append(f'<li class="toc-part-label">{html.escape(part_group)}</li>')
            last_part = part_group

        sub_links: List[str] = []
        chap_id = f"chap-{slug}"
        quiz_anchor = f"#{chap_id}"
        for lvl, hid, title in conv.toc_items:
            if lvl == 1:
                chap_id = hid
            else:
                sub_links.append(
                    f'<li><a href="#{hid}" class="toc-sublink">{html.escape(title)}</a></li>'
                )
                if title.startswith("9."):
                    quiz_anchor = f"#{hid}"

        toc_groups_html.append(
            f'<li class="toc-chapter">'
            f'<a href="#{chap_id}" class="toc-chaplink">{html.escape(label)}</a>'
            f'<ul class="toc-sublist">{"".join(sub_links)}</ul>'
            f"</li>"
        )

        if slug.startswith("modul-"):
            short_code = "M" + slug.split("-")[1]
            quiz_pills_html.append(
                f'<a href="{quiz_anchor}" class="quiz-pill" data-pill-module="{slug}" '
                f'title="Langsung ke Kuis {html.escape(label)}">{short_code}</a>'
            )

    # Master Glossary A-Z
    if glossary:
        gl_rows = [
            f'<tr><th scope="row" data-label="Istilah"><strong>{html.escape(t)}</strong></th>'
            f'<td data-label="Penjelasan">{render_inline(d)}</td>'
            f'<td data-label="Sumber"><span class="badge">{html.escape(s)}</span></td></tr>'
            for t, d, s in glossary
        ]
        sections_html.append(
            '<article class="book-chapter" id="section-glosarium-gabungan">\n'
            '<header class="chapter-header">'
            '<p class="chapter-kicker">Lampiran Akhir</p>'
            '<h2 id="chap-glosarium-gabungan" class="chapter-title">Indeks Glosarium Gabungan (Modul 01–12)</h2>'
            "</header>\n"
            "<p>Glosarium komprehensif istilah manajemen proyek, bisnis &amp; analisis sistem, arsitektur solusi, manajemen produk, keuangan korporat, kepemimpinan eksekutif, dan strategi karier yang dihimpun secara alfabetis dari seluruh 12 modul.</p>\n"
            '<div tabindex="0" role="region" aria-label="Indeks Glosarium Gabungan" class="table-wrapper">'
            '<table data-cols="3">'
            '<thead><tr><th scope="col">Istilah</th><th scope="col">Penjelasan</th><th scope="col">Sumber</th></tr></thead>'
            f'<tbody>{"".join(gl_rows)}</tbody></table></div>\n'
            "</article>"
        )
        toc_groups_html.append('<li class="toc-part-label">Referensi Akhir</li>')
        toc_groups_html.append(
            '<li class="toc-chapter">'
            '<a href="#chap-glosarium-gabungan" class="toc-chaplink">Indeks Glosarium Gabungan (A–Z)</a>'
            "</li>"
        )

    read_minutes = max(1, round(total_words / 200))
    mod_count = sum(1 for c in chapter_contents if c[1].startswith("modul-"))
    stats = {
        "words": total_words,
        "diagrams": total_diagrams,
        "figures": total_figures,
        "quiz_questions": total_quiz_questions,
        "glossary": len(glossary),
        "modules": mod_count,
    }

    html_doc = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="color-scheme" content="light dark">
  <script>
    try {{
      const saved = localStorage.getItem("color-scheme");
      if (saved === "light" || saved === "dark") {{
        document.querySelector('meta[name="color-scheme"]').content = saved;
      }}
    }} catch (e) {{}}
  </script>
  <title>Buku Lengkap Senior PM, BA &amp; SA (Modul 01–12) | PT Sinar Nusantara Retail — Proyek OMNI</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <style>
    /* =====================================================================
       1. Design Tokens & Color Scheme (Modern Web Guidance compliant)
       ===================================================================== */
    :root {{
      --bg-page-light: #faf8f4;
      --bg-page-dark: #10151d;
      --bg-surface-light: #ffffff;
      --bg-surface-dark: #171f2b;
      --bg-subtle-light: #f2eee6;
      --bg-subtle-dark: #1f2937;
      --ink-primary-light: #1e293b;
      --ink-primary-dark: #e6edf5;
      --ink-heading-light: #0f2540;
      --ink-heading-dark: #f8fafc;
      --ink-muted-light: #526071;
      --ink-muted-dark: #9fb0c4;
      --border-light: #dfd8cc;
      --border-dark: #2c394b;
      --accent-light: #1d4ed8;
      --accent-dark: #60a5fa;
      --brand-light: #8c2f1b;
      --brand-dark: #f59e0b;
      --ok-bg-light: #ecfdf5;
      --ok-bg-dark: #064e3b;
      --ok-border-light: #059669;
      --ok-border-dark: #34d399;
      --ok-ink-light: #065f46;
      --ok-ink-dark: #a7f3d0;
      --err-bg-light: #fef2f2;
      --err-bg-dark: #450a0a;
      --err-border-light: #dc2626;
      --err-border-dark: #f87171;
      --err-ink-light: #991b1b;
      --err-ink-dark: #fecaca;
      --callout-bg-light: #f6f3ec;
      --callout-bg-dark: #1c2533;
      --warn-border-light: #b45309;
      --warn-border-dark: #fbbf24;
      --tip-border-light: #0f766e;
      --tip-border-dark: #2dd4bf;
      --code-bg-light: #f3f1ec;
      --code-bg-dark: #0c1118;
      --scroll-track-light: #ede8df;
      --scroll-track-dark: #1a2230;
      --scroll-thumb-light: #8b8579;
      --scroll-thumb-dark: #64748b;

      /* Light defaults */
      --bg-page: var(--bg-page-light);
      --bg-surface: var(--bg-surface-light);
      --bg-subtle: var(--bg-subtle-light);
      --ink-primary: var(--ink-primary-light);
      --ink-heading: var(--ink-heading-light);
      --ink-muted: var(--ink-muted-light);
      --border: var(--border-light);
      --accent: var(--accent-light);
      --brand: var(--brand-light);
      --ok-bg: var(--ok-bg-light);
      --ok-border: var(--ok-border-light);
      --ok-ink: var(--ok-ink-light);
      --err-bg: var(--err-bg-light);
      --err-border: var(--err-border-light);
      --err-ink: var(--err-ink-light);
      --callout-bg: var(--callout-bg-light);
      --warn-border: var(--warn-border-light);
      --tip-border: var(--tip-border-light);
      --code-bg: var(--code-bg-light);
      --scroll-track: var(--scroll-track-light);
      --scroll-thumb: var(--scroll-thumb-light);

      --font-serif: Georgia, "Iowan Old Style", "Palatino Linotype", "Book Antiqua", serif;
      --font-sans: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
      --font-mono: "Cascadia Code", Consolas, "Liberation Mono", Menlo, monospace;
      --reader-scale: 1;
      --sidebar-width: 310px;
      --topbar-height: 56px;

      color-scheme: light dark;
    }}

    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg-page: var(--bg-page-dark);
        --bg-surface: var(--bg-surface-dark);
        --bg-subtle: var(--bg-subtle-dark);
        --ink-primary: var(--ink-primary-dark);
        --ink-heading: var(--ink-heading-dark);
        --ink-muted: var(--ink-muted-dark);
        --border: var(--border-dark);
        --accent: var(--accent-dark);
        --brand: var(--brand-dark);
        --ok-bg: var(--ok-bg-dark);
        --ok-border: var(--ok-border-dark);
        --ok-ink: var(--ok-ink-dark);
        --err-bg: var(--err-bg-dark);
        --err-border: var(--err-border-dark);
        --err-ink: var(--err-ink-dark);
        --callout-bg: var(--callout-bg-dark);
        --warn-border: var(--warn-border-dark);
        --tip-border: var(--tip-border-dark);
        --code-bg: var(--code-bg-dark);
        --scroll-track: var(--scroll-track-dark);
        --scroll-thumb: var(--scroll-thumb-dark);
      }}
    }}

    :root:has(> head > meta[name="color-scheme"][content="dark"]) {{
      color-scheme: dark;
      --bg-page: var(--bg-page-dark);
      --bg-surface: var(--bg-surface-dark);
      --bg-subtle: var(--bg-subtle-dark);
      --ink-primary: var(--ink-primary-dark);
      --ink-heading: var(--ink-heading-dark);
      --ink-muted: var(--ink-muted-dark);
      --border: var(--border-dark);
      --accent: var(--accent-dark);
      --brand: var(--brand-dark);
      --ok-bg: var(--ok-bg-dark);
      --ok-border: var(--ok-border-dark);
      --ok-ink: var(--ok-ink-dark);
      --err-bg: var(--err-bg-dark);
      --err-border: var(--err-border-dark);
      --err-ink: var(--err-ink-dark);
      --callout-bg: var(--callout-bg-dark);
      --warn-border: var(--warn-border-dark);
      --tip-border: var(--tip-border-dark);
      --code-bg: var(--code-bg-dark);
      --scroll-track: var(--scroll-track-dark);
      --scroll-thumb: var(--scroll-thumb-dark);
    }}

    :root:has(> head > meta[name="color-scheme"][content="light"]) {{
      color-scheme: light;
      --bg-page: var(--bg-page-light);
      --bg-surface: var(--bg-surface-light);
      --bg-subtle: var(--bg-subtle-light);
      --ink-primary: var(--ink-primary-light);
      --ink-heading: var(--ink-heading-light);
      --ink-muted: var(--ink-muted-light);
      --border: var(--border-light);
      --accent: var(--accent-light);
      --brand: var(--brand-light);
      --ok-bg: var(--ok-bg-light);
      --ok-border: var(--ok-border-light);
      --ok-ink: var(--ok-ink-light);
      --err-bg: var(--err-bg-light);
      --err-border: var(--err-border-light);
      --err-ink: var(--err-ink-light);
      --callout-bg: var(--callout-bg-light);
      --warn-border: var(--warn-border-light);
      --tip-border: var(--tip-border-light);
      --code-bg: var(--code-bg-light);
      --scroll-track: var(--scroll-track-light);
      --scroll-thumb: var(--scroll-thumb-light);
    }}

    @supports (color: light-dark(white, black)) {{
      :root {{
        --bg-page: light-dark(var(--bg-page-light), var(--bg-page-dark));
        --bg-surface: light-dark(var(--bg-surface-light), var(--bg-surface-dark));
        --bg-subtle: light-dark(var(--bg-subtle-light), var(--bg-subtle-dark));
        --ink-primary: light-dark(var(--ink-primary-light), var(--ink-primary-dark));
        --ink-heading: light-dark(var(--ink-heading-light), var(--ink-heading-dark));
        --ink-muted: light-dark(var(--ink-muted-light), var(--ink-muted-dark));
        --border: light-dark(var(--border-light), var(--border-dark));
        --accent: light-dark(var(--accent-light), var(--accent-dark));
        --brand: light-dark(var(--brand-light), var(--brand-dark));
        --ok-bg: light-dark(var(--ok-bg-light), var(--ok-bg-dark));
        --ok-border: light-dark(var(--ok-border-light), var(--ok-border-dark));
        --ok-ink: light-dark(var(--ok-ink-light), var(--ok-ink-dark));
        --err-bg: light-dark(var(--err-bg-light), var(--err-bg-dark));
        --err-border: light-dark(var(--err-border-light), var(--err-border-dark));
        --err-ink: light-dark(var(--err-ink-light), var(--err-ink-dark));
        --callout-bg: light-dark(var(--callout-bg-light), var(--callout-bg-dark));
        --warn-border: light-dark(var(--warn-border-light), var(--warn-border-dark));
        --tip-border: light-dark(var(--tip-border-light), var(--tip-border-dark));
        --code-bg: light-dark(var(--code-bg-light), var(--code-bg-dark));
        --scroll-track: light-dark(var(--scroll-track-light), var(--scroll-track-dark));
        --scroll-thumb: light-dark(var(--scroll-thumb-light), var(--scroll-thumb-dark));
      }}
    }}

    html {{
      accent-color: var(--brand);
      scrollbar-color: var(--scroll-thumb) var(--scroll-track);
      scroll-behavior: smooth;
      scroll-padding-top: calc(var(--topbar-height) + 18px);
    }}

    @media (prefers-reduced-motion: reduce) {{
      html {{ scroll-behavior: auto; }}
    }}

    *, *::before, *::after {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      font-family: var(--font-sans);
      font-size: calc(16px * var(--reader-scale));
      line-height: 1.72;
      color: var(--ink-primary);
      background-color: var(--bg-page);
      -webkit-font-smoothing: antialiased;
    }}

    .visually-hidden:where(:not(:focus-within, :active)) {{
      position: absolute !important;
      clip-path: inset(50%) !important;
      overflow: hidden !important;
      width: 1px !important;
      height: 1px !important;
      margin: -1px !important;
      padding: 0 !important;
      border: 0 !important;
      white-space: nowrap !important;
    }}

    .skip-link {{
      position: fixed;
      top: 8px;
      left: 8px;
      z-index: 2000;
      padding: 10px 16px;
      background: var(--ink-heading);
      color: var(--bg-surface);
      border-radius: 6px;
      font-weight: 600;
      text-decoration: none;
    }}

    :where(a:any-link, button, summary, input, [tabindex="0"]):focus-visible {{
      outline: 3px solid var(--brand);
      outline-offset: 2px;
    }}

    /* =====================================================================
       2. Scroll Progress Indicator
       ===================================================================== */
    #reading-progress {{
      position: fixed;
      inset-block-start: 0;
      inset-inline-start: 0;
      inline-size: 100%;
      block-size: 4px;
      background: linear-gradient(90deg, var(--brand), var(--accent));
      transform-origin: 0 50%;
      transform: scaleX(0);
      z-index: 1100;
      pointer-events: none;
    }}

    @media (prefers-reduced-motion: no-preference) {{
      @supports (animation-timeline: scroll()) {{
        @keyframes grow-reading-progress {{
          from {{ transform: scaleX(0); }}
          to {{ transform: scaleX(1); }}
        }}
        #reading-progress {{
          animation: grow-reading-progress auto linear;
          animation-timeline: scroll(root block);
        }}
      }}
    }}

    /* =====================================================================
       3. Topbar & Settings Popover
       ===================================================================== */
    .reader-topbar {{
      position: sticky;
      top: 0;
      z-index: 900;
      height: var(--topbar-height);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 0 16px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border);
    }}

    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 0;
    }}

    .brand-title {{
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: 0.96rem;
      color: var(--ink-heading);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .topbar-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      min-block-size: 38px;
      min-inline-size: 38px;
      padding: 6px 13px;
      border-radius: 7px;
      border: 1px solid var(--border);
      background: var(--bg-surface);
      color: var(--ink-primary);
      font-family: inherit;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.15s ease, border-color 0.15s ease;
    }}

    .btn-sm {{
      min-block-size: 34px;
      padding: 5px 12px;
      font-size: 0.82rem;
    }}

    .btn:hover {{
      background: var(--bg-subtle);
      border-color: var(--ink-muted);
    }}

    .btn-primary {{
      background: var(--brand);
      color: #ffffff;
      border-color: var(--brand);
    }}

    .btn-primary:hover {{
      opacity: 0.92;
      background: var(--brand);
    }}

    [data-toggle-answers][aria-expanded="true"] .label-expand,
    [data-toggle-answers][aria-expanded="false"] .label-collapse {{
      display: none;
    }}

    #reader-settings {{
      inset: unset;
      top: calc(var(--topbar-height) + 8px);
      right: 16px;
      width: min(320px, calc(100vw - 32px));
      padding: 18px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: var(--bg-surface);
      color: var(--ink-primary);
      box-shadow: 0 14px 36px rgba(0, 0, 0, 0.24);
    }}

    .settings-group {{ margin-bottom: 14px; }}
    .settings-group:last-child {{ margin-bottom: 0; }}
    .settings-group fieldset {{ border: 0; margin: 0; padding: 0; }}
    .settings-group legend {{
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--ink-muted);
      margin-bottom: 8px;
    }}
    .seg-group {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
    }}
    .seg-btn {{
      min-block-size: 36px;
      padding: 6px 8px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--bg-subtle);
      color: var(--ink-primary);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
    }}
    .seg-btn[aria-pressed="true"] {{
      background: var(--brand);
      color: #ffffff;
      border-color: var(--brand);
    }}
    .settings-hint {{
      margin: 6px 0 0;
      font-size: 0.78rem;
      color: var(--ink-muted);
    }}

    /* =====================================================================
       4. Book Shell Layout & Sidebar TOC
       ===================================================================== */
    .book-shell {{
      display: grid;
      grid-template-columns: var(--sidebar-width) minmax(0, 1fr);
      min-height: calc(100vh - var(--topbar-height));
    }}

    .book-sidebar {{
      position: sticky;
      top: var(--topbar-height);
      height: calc(100vh - var(--topbar-height));
      overflow-y: auto;
      padding: 18px 14px 36px;
      background: var(--bg-surface);
      border-right: 1px solid var(--border);
    }}

    .toc-search-box {{ margin-bottom: 14px; }}
    .toc-search-box label {{
      display: block;
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--ink-muted);
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .toc-search-box input {{
      width: 100%;
      min-block-size: 38px;
      padding: 6px 10px;
      border-radius: 7px;
      border: 1px solid var(--border);
      background: var(--bg-page);
      color: var(--ink-primary);
      font: inherit;
      font-size: max(0.9rem, 1em);
    }}

    .toc-list, .toc-sublist {{ list-style: none; margin: 0; padding: 0; }}
    .toc-part-label {{
      margin: 16px 0 6px;
      padding: 4px 8px;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--brand);
      border-bottom: 1px solid var(--border);
    }}
    .toc-chapter {{ margin-bottom: 10px; }}
    .toc-chaplink {{
      display: block;
      padding: 6px 8px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.86rem;
      color: var(--ink-heading);
      text-decoration: none;
    }}
    .toc-chaplink:hover, .toc-sublink:hover {{ background: var(--bg-subtle); }}
    .toc-sublist {{
      padding-left: 10px;
      margin-top: 2px;
      border-left: 2px solid var(--border);
      margin-left: 8px;
    }}
    .toc-sublink {{
      display: block;
      padding: 4px 8px;
      border-radius: 5px;
      font-size: 0.8rem;
      color: var(--ink-muted);
      text-decoration: none;
      line-height: 1.35;
    }}
    .toc-link-active {{
      background: var(--bg-subtle);
      color: var(--brand) !important;
      font-weight: 700;
    }}

    .sidebar-toggle-btn {{ display: none; }}
    @media (max-width: 1024px) {{
      .book-shell {{ grid-template-columns: 1fr; }}
      .sidebar-toggle-btn {{ display: inline-flex; }}
      .book-sidebar {{
        position: fixed;
        top: var(--topbar-height);
        left: 0;
        z-index: 950;
        width: min(320px, 86vw);
        transform: translateX(-105%);
        transition: transform 0.22s ease;
        box-shadow: 12px 0 32px rgba(0, 0, 0, 0.25);
      }}
      .book-sidebar.open {{ transform: translateX(0); }}
    }}

    /* =====================================================================
       5. Book Cover, Quiz Dashboard & Editorial Typography
       ===================================================================== */
    .book-main {{
      max-width: 920px;
      width: 100%;
      margin: 0 auto;
      padding: 36px clamp(18px, 4vw, 52px) 72px;
    }}

    .book-cover {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-top: 6px solid var(--brand);
      border-radius: 14px;
      padding: clamp(28px, 5vw, 48px);
      margin-bottom: 40px;
      box-shadow: 0 8px 28px rgba(0, 0, 0, 0.05);
    }}

    .cover-series {{
      margin: 0 0 10px;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--brand);
    }}

    .book-cover h1 {{
      margin: 0 0 12px;
      font-family: var(--font-serif);
      font-size: clamp(1.85rem, 3.5vw, 2.65rem);
      line-height: 1.2;
      color: var(--ink-heading);
    }}

    .cover-subtitle {{
      margin: 0 0 22px;
      font-size: 1.08rem;
      color: var(--ink-muted);
      max-width: 66ch;
    }}

    .cover-meta-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(165px, 1fr));
      gap: 12px;
      padding-top: 18px;
      border-top: 1px solid var(--border);
    }}

    .meta-card {{
      background: var(--bg-subtle);
      padding: 12px 14px;
      border-radius: 8px;
    }}
    .meta-label {{
      display: block;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
    }}
    .meta-value {{
      display: block;
      margin-top: 4px;
      font-weight: 700;
      font-size: 0.94rem;
      color: var(--ink-heading);
    }}

    .quiz-dashboard {{
      margin-top: 20px;
      padding: 16px 18px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--bg-page);
    }}
    .quiz-dashboard-head {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .quiz-dashboard-title {{
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--ink-heading);
    }}
    .quiz-dashboard-summary {{
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--ink-muted);
    }}
    .quiz-pill-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .quiz-pill {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-inline-size: 44px;
      min-block-size: 32px;
      padding: 3px 9px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--bg-surface);
      color: var(--ink-heading);
      font-size: 0.78rem;
      font-weight: 700;
      text-decoration: none;
    }}
    .quiz-pill:hover {{ border-color: var(--brand); }}
    .quiz-pill.pill-pass {{
      background: var(--ok-bg);
      border-color: var(--ok-border);
      color: var(--ok-ink);
    }}
    .quiz-pill.pill-fail {{
      background: var(--err-bg);
      border-color: var(--err-border);
      color: var(--err-ink);
    }}

    .book-chapter {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: clamp(24px, 4.2vw, 48px);
      margin-bottom: 40px;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.03);
    }}

    .chapter-header {{
      padding-bottom: 18px;
      margin-bottom: 24px;
      border-bottom: 2px solid var(--brand);
    }}
    .chapter-kicker {{
      margin: 0 0 6px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--brand);
    }}
    .chapter-title {{
      margin: 0;
      font-family: var(--font-serif);
      font-size: clamp(1.55rem, 2.6vw, 2.05rem);
      line-height: 1.25;
      color: var(--ink-heading);
    }}

    .book-chapter h3 {{
      margin-top: 2.1rem;
      margin-bottom: 0.75rem;
      padding-bottom: 0.35rem;
      border-bottom: 1px solid var(--border);
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: var(--ink-heading);
    }}
    .book-chapter h4 {{
      margin-top: 1.55rem;
      margin-bottom: 0.5rem;
      font-size: 1.08rem;
      color: var(--ink-heading);
    }}
    .book-chapter h5 {{
      margin-top: 1.2rem;
      margin-bottom: 0.4rem;
      font-size: 0.98rem;
      color: var(--brand);
    }}

    p {{ margin: 0 0 0.95rem; }}
    ul, ol {{ margin: 0 0 1rem; padding-left: 1.55rem; }}
    li {{ margin-bottom: 0.38rem; }}
    hr {{ border: 0; border-top: 1px solid var(--border); margin: 2rem 0; }}
    a {{ color: var(--accent); text-underline-offset: 2px; }}

    code {{
      font-family: var(--font-mono);
      font-size: 0.87em;
      padding: 0.12em 0.36em;
      border-radius: 4px;
      background: var(--code-bg);
    }}

    .code-figure {{ margin: 1.2rem 0; }}
    .code-figure pre {{
      margin: 0;
      padding: 16px 18px;
      overflow-x: auto;
      border-radius: 9px;
      border: 1px solid var(--border);
      background: var(--code-bg);
      font-size: 0.86rem;
      line-height: 1.55;
    }}
    .code-figure pre code {{ padding: 0; background: transparent; font-size: inherit; }}

    blockquote.callout {{
      margin: 1.25rem 0;
      padding: 14px 18px;
      border-left: 4px solid var(--brand);
      background: var(--callout-bg);
      border-radius: 0 8px 8px 0;
    }}
    blockquote.callout-warn {{ border-left-color: var(--warn-border); }}
    blockquote.callout-tip {{ border-left-color: var(--tip-border); }}
    blockquote.callout p:last-child {{ margin-bottom: 0; }}

    .badge {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 0.76rem;
      font-weight: 700;
      background: var(--bg-subtle);
      color: var(--ink-heading);
      border: 1px solid var(--border);
      white-space: nowrap;
    }}

    /* =====================================================================
       6. Editorial Illustrations & Native <dialog> Lightbox
       ===================================================================== */
    .editorial-figure {{
      margin: 1.5rem 0;
      text-align: center;
    }}
    .figure-zoom-btn {{
      position: relative;
      display: block;
      width: 100%;
      padding: 10px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: #faf8f4;
      color-scheme: light;
      cursor: zoom-in;
      overflow: hidden;
      transition: border-color 0.18s ease, box-shadow 0.18s ease;
    }}
    .figure-zoom-btn:hover {{
      border-color: var(--brand);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }}
    .figure-zoom-btn img {{
      display: block;
      width: 100%;
      height: auto;
      border-radius: 8px;
    }}
    .zoom-hint {{
      position: absolute;
      right: 16px;
      bottom: 16px;
      padding: 4px 10px;
      border-radius: 999px;
      background: rgba(15, 37, 64, 0.86);
      color: #ffffff;
      font-size: 0.74rem;
      font-weight: 600;
      opacity: 0.88;
    }}
    .editorial-figure figcaption {{
      margin-top: 8px;
      font-size: 0.85rem;
      color: var(--ink-muted);
      line-height: 1.45;
    }}

    #image-lightbox {{
      max-width: min(94vw, 1360px);
      max-height: 92vh;
      padding: 18px;
      border: 1px solid var(--border);
      border-radius: 14px;
      background: var(--bg-surface);
      color: var(--ink-primary);
      box-shadow: 0 24px 64px rgba(0, 0, 0, 0.45);
    }}
    #image-lightbox::backdrop {{
      background: rgba(10, 15, 25, 0.76);
      backdrop-filter: blur(3px);
    }}
    .lightbox-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .lightbox-title {{
      margin: 0;
      font-size: 0.96rem;
      font-weight: 700;
      color: var(--ink-heading);
    }}
    .lightbox-img-wrap {{
      background: #faf8f4;
      border-radius: 10px;
      padding: 8px;
      overflow: auto;
      max-height: 76vh;
    }}
    .lightbox-img-wrap img {{
      display: block;
      width: 100%;
      height: auto;
      border-radius: 6px;
    }}

    /* =====================================================================
       7. Responsive Tables
       ===================================================================== */
    .table-wrapper {{
      overflow: auto;
      max-inline-size: 100%;
      margin: 1.25rem 0;
      border: 1px solid var(--border);
      border-radius: 9px;
      container-type: inline-size;
    }}
    .table-wrapper table {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 0.9rem;
      line-height: 1.5;
    }}
    .table-wrapper thead {{
      position: sticky;
      inset-block-start: 0;
      z-index: 1;
    }}
    .table-wrapper thead th {{
      background: var(--bg-subtle);
      color: var(--ink-heading);
      font-weight: 700;
      text-align: left;
      padding: 10px 12px;
      border-bottom: 2px solid var(--border);
      border-right: 1px solid var(--border);
    }}
    .table-wrapper thead th:last-child {{ border-right: 0; }}
    .table-wrapper tbody th,
    .table-wrapper tbody td {{
      padding: 9px 12px;
      vertical-align: top;
      border-bottom: 1px solid var(--border);
      border-right: 1px solid var(--border);
      text-align: left;
      font-weight: 400;
    }}
    .table-wrapper tbody th {{
      font-weight: 600;
      color: var(--ink-heading);
      background: var(--bg-surface);
    }}
    .table-wrapper tbody tr:nth-child(even) td,
    .table-wrapper tbody tr:nth-child(even) th {{
      background: color-mix(in srgb, var(--bg-subtle) 42%, var(--bg-surface));
    }}
    .table-wrapper tbody tr:last-child th,
    .table-wrapper tbody tr:last-child td {{ border-bottom: 0; }}
    .table-wrapper tbody td:last-child {{ border-right: 0; }}
    .table-wrapper .align-right {{ text-align: right; }}
    .table-wrapper .align-center {{ text-align: center; }}

    @container (width < 460px) {{
      .table-wrapper table, .table-wrapper thead, .table-wrapper tbody,
      .table-wrapper tr, .table-wrapper th, .table-wrapper td {{ display: block; }}
      .table-wrapper thead {{ display: none; }}
      .table-wrapper tr {{
        margin: 10px;
        border: 1px solid var(--border);
        border-radius: 8px;
        overflow: hidden;
      }}
      .table-wrapper tbody th {{ background: var(--bg-subtle) !important; border-right: 0; }}
      .table-wrapper tbody td {{ border-right: 0; }}
      .table-wrapper tbody td::before {{
        content: attr(data-label) ": ";
        font-weight: 700;
        color: var(--ink-heading);
      }}
    }}

    /* =====================================================================
       8. Interactive Auto-Graded Multiple-Choice Quiz (Forms Guidance)
       ===================================================================== */
    .quiz-form {{
      margin: 1rem 0 1.6rem;
    }}
    .quiz-intro-bar {{
      padding: 12px 16px;
      margin-bottom: 16px;
      border-radius: 9px;
      background: var(--callout-bg);
      border-left: 4px solid var(--accent);
      font-size: 0.92rem;
    }}
    .quiz-card {{
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px 20px;
      margin: 0 0 18px;
      background: var(--bg-page);
    }}
    .quiz-card.is-correct {{
      border-color: var(--ok-border);
      box-shadow: inset 4px 0 0 var(--ok-border);
    }}
    .quiz-card.is-wrong {{
      border-color: var(--err-border);
      box-shadow: inset 4px 0 0 var(--err-border);
    }}
    .quiz-legend {{
      display: block;
      width: 100%;
      padding: 0;
      margin-bottom: 12px;
      font-weight: 600;
      color: var(--ink-heading);
      line-height: 1.55;
    }}
    .q-badge {{
      display: inline-block;
      margin-inline-end: 8px;
      padding: 2px 9px;
      border-radius: 6px;
      background: var(--ink-heading);
      color: var(--bg-surface);
      font-size: 0.78rem;
      font-weight: 800;
      vertical-align: 1px;
    }}
    .quiz-options {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .quiz-option {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      min-block-size: 48px;
      padding: 11px 14px;
      border-radius: 9px;
      border: 1.5px solid var(--border);
      background: var(--bg-surface);
      cursor: pointer;
      line-height: 1.5;
      transition: border-color 0.14s ease, background-color 0.14s ease;
    }}
    .quiz-option:hover {{
      border-color: var(--brand);
      background: var(--bg-subtle);
    }}
    .quiz-option:has(input:checked) {{
      border-color: var(--brand);
      background: color-mix(in srgb, var(--brand) 8%, var(--bg-surface));
    }}
    .quiz-option input[type="radio"] {{
      flex-shrink: 0;
      inline-size: 1.15rem;
      block-size: 1.15rem;
      margin: 3px 0 0;
      accent-color: var(--brand);
      cursor: pointer;
    }}
    .opt-letter {{
      flex-shrink: 0;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      inline-size: 24px;
      block-size: 24px;
      border-radius: 6px;
      background: var(--bg-subtle);
      color: var(--ink-heading);
      font-size: 0.8rem;
      font-weight: 800;
      margin-top: 1px;
    }}
    .opt-text {{
      flex: 1;
      min-width: 0;
    }}
    .quiz-option.opt-correct {{
      border-color: var(--ok-border) !important;
      background: var(--ok-bg) !important;
      color: var(--ok-ink);
    }}
    .quiz-option.opt-correct .opt-letter {{
      background: var(--ok-border);
      color: #ffffff;
    }}
    .quiz-option.opt-wrong {{
      border-color: var(--err-border) !important;
      background: var(--err-bg) !important;
      color: var(--err-ink);
    }}
    .quiz-option.opt-wrong .opt-letter {{
      background: var(--err-border);
      color: #ffffff;
    }}
    .quiz-card-actions {{
      margin-top: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .quiz-feedback {{
      margin-top: 12px;
      padding: 12px 15px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: var(--bg-surface);
      font-size: 0.9rem;
    }}
    .quiz-feedback.fb-ok {{
      background: var(--ok-bg);
      border-color: var(--ok-border);
      color: var(--ok-ink);
    }}
    .quiz-feedback.fb-err {{
      background: var(--err-bg);
      border-color: var(--err-border);
      color: var(--err-ink);
    }}
    .quiz-feedback-status {{
      margin: 0 0 6px;
      font-weight: 800;
    }}
    .quiz-feedback-expl {{
      color: var(--ink-primary);
      line-height: 1.58;
    }}
    .quiz-footer-bar {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      margin-top: 14px;
    }}
    .quiz-score-banner {{
      margin-top: 14px;
      padding: 16px 20px;
      border-radius: 10px;
      border: 2px solid var(--border);
      background: var(--bg-subtle);
      font-size: 0.96rem;
    }}
    .quiz-score-banner.score-pass {{
      background: var(--ok-bg);
      border-color: var(--ok-border);
      color: var(--ok-ink);
    }}
    .quiz-score-banner.score-fail {{
      background: var(--err-bg);
      border-color: var(--err-border);
      color: var(--err-ink);
    }}

    /* =====================================================================
       9. Native <details> Answer Disclosure
       ===================================================================== */
    details.answer-disclosure {{
      margin: 0.9rem 0 1.4rem;
      border: 1px solid var(--border);
      border-left: 4px solid var(--accent);
      border-radius: 8px;
      background: var(--bg-page);
    }}
    details.answer-disclosure > summary {{
      list-style: none;
      display: flex;
      align-items: center;
      gap: 0.6ch;
      padding: 12px 16px;
      font-weight: 700;
      color: var(--ink-heading);
      cursor: pointer;
      user-select: none;
    }}
    details.answer-disclosure > summary::-webkit-details-marker {{ display: none; }}
    details.answer-disclosure > summary::before {{
      content: "";
      inline-size: 0.65em;
      block-size: 0.65em;
      flex-shrink: 0;
      border-right: 2.2px solid currentColor;
      border-bottom: 2.2px solid currentColor;
      rotate: -45deg;
      margin-inline-end: 4px;
    }}
    details.answer-disclosure[open] > summary::before {{ rotate: 45deg; }}
    @media (prefers-reduced-motion: no-preference) {{
      details.answer-disclosure > summary::before {{ transition: rotate 0.2s ease; }}
      details.answer-disclosure::details-content {{
        interpolate-size: allow-keywords;
        overflow: clip;
        contain: layout;
        transition: block-size 0.28s ease-in-out, content-visibility 0.28s ease-in-out;
        transition-behavior: allow-discrete;
      }}
      details.answer-disclosure:not([open])::details-content {{ block-size: 0; }}
    }}
    .disclosure-body {{
      padding: 4px 18px 18px;
      border-top: 1px solid var(--border);
    }}

    /* =====================================================================
       10. Mermaid Cards & Math Blocks
       ===================================================================== */
    .mermaid-figure {{ margin: 1.4rem 0; }}
    .mermaid-card {{
      color-scheme: light;
      background: #ffffff;
      color: #1e293b;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px 14px;
      overflow-x: auto;
      text-align: center;
    }}
    .mermaid-card svg {{ max-width: 100%; height: auto; }}
    .mermaid-figure figcaption {{
      margin-top: 6px;
      text-align: center;
      font-size: 0.82rem;
      color: var(--ink-muted);
      font-style: italic;
    }}
    .math-block {{
      margin: 1rem 0;
      padding: 12px 16px;
      overflow-x: auto;
      text-align: center;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 8px;
    }}

    .book-footer {{
      margin-top: 24px;
      padding: 20px 16px;
      text-align: center;
      font-size: 0.84rem;
      color: var(--ink-muted);
      border-top: 1px solid var(--border);
    }}

    /* =====================================================================
       11. Print / Save-as-PDF Stylesheet (A4 Publisher Layout)
       ===================================================================== */
    @page {{
      size: A4;
      margin: 18mm 16mm 20mm 16mm;
    }}
    @media print {{
      :root {{
        color-scheme: light !important;
        --bg-page: #ffffff !important;
        --bg-surface: #ffffff !important;
        --bg-subtle: #f4f4f6 !important;
        --ink-primary: #111827 !important;
        --ink-heading: #0f172a !important;
        --ink-muted: #4b5563 !important;
        --border: #cbd5e1 !important;
        --callout-bg: #f8fafc !important;
        --code-bg: #f8fafc !important;
      }}
      body {{ font-size: 10.2pt; line-height: 1.54; background: #ffffff !important; color: #111827 !important; }}
      .reader-topbar, .book-sidebar, #reading-progress, .skip-link, #reader-settings,
      .quiz-card-actions, .quiz-footer-bar, .quiz-intro-bar, .quiz-dashboard, .zoom-hint, #image-lightbox {{
        display: none !important;
      }}
      .book-shell {{ display: block; }}
      .book-main {{ max-width: none; padding: 0; margin: 0; }}
      .book-cover {{
        box-shadow: none;
        border: 1.5pt solid #8c2f1b;
        break-after: page;
        page-break-after: always;
      }}
      .book-chapter {{
        box-shadow: none;
        border: 0;
        padding: 0;
        margin: 0 0 12mm;
        break-before: page;
        page-break-before: always;
      }}
      h2, h3, h4, h5 {{ break-after: avoid; page-break-after: avoid; }}
      blockquote, .mermaid-figure, .editorial-figure, .code-figure, .quiz-card {{
        break-inside: avoid;
        page-break-inside: avoid;
      }}
      .figure-zoom-btn {{ border: 1px solid #cbd5e1; padding: 4px; }}
      .table-wrapper {{ overflow: visible; container-type: normal; border-radius: 0; }}
      .table-wrapper thead {{ position: static; display: table-header-group; }}
      .table-wrapper tr {{ break-inside: avoid; page-break-inside: avoid; }}
      details.answer-disclosure {{ border: 1px solid #cbd5e1; border-left: 3px solid #1d4ed8; }}
      details.answer-disclosure > summary {{ background: #f1f5f9; }}
    }}
  </style>
</head>
<body>
  <a href="#main-content" class="skip-link visually-hidden">Lewati ke isi buku</a>
  <div id="reading-progress" aria-hidden="true"></div>

  <header class="reader-topbar">
    <div class="topbar-left">
      <button type="button" class="btn sidebar-toggle-btn" id="btn-sidebar" aria-expanded="false" aria-controls="toc-sidebar">
        Daftar Isi
      </button>
      <span class="brand-title">Senior PM, Business &amp; System Analysis — Edisi Lengkap (Modul 01–{mod_count:02d})</span>
    </div>

    <div class="topbar-actions">
      <button type="button" class="btn" id="btn-toggle-answers" data-toggle-answers aria-expanded="false">
        <span class="label-expand">Buka Semua Kunci</span>
        <span class="label-collapse">Tutup Semua Kunci</span>
      </button>
      <button type="button" class="btn" popovertarget="reader-settings">Tampilan</button>
      <button type="button" class="btn btn-primary" id="btn-print">Cetak / PDF</button>
    </div>
  </header>

  <div id="reader-settings" popover="auto" aria-label="Pengaturan Tampilan Buku">
    <div class="settings-group">
      <fieldset>
        <legend>Skema Warna</legend>
        <div class="seg-group" role="group" aria-label="Pilihan tema warna">
          <button type="button" class="seg-btn" data-theme-choice="system" aria-pressed="true">Sistem</button>
          <button type="button" class="seg-btn" data-theme-choice="light" aria-pressed="false">Terang</button>
          <button type="button" class="seg-btn" data-theme-choice="dark" aria-pressed="false">Gelap</button>
        </div>
        <p class="settings-hint" id="system-theme-hint">Mengikuti preferensi perangkat.</p>
      </fieldset>
    </div>
    <div class="settings-group">
      <fieldset>
        <legend>Ukuran Teks</legend>
        <div class="seg-group" role="group" aria-label="Pilihan ukuran teks">
          <button type="button" class="seg-btn" data-scale-choice="0.92" aria-pressed="false">Kecil</button>
          <button type="button" class="seg-btn" data-scale-choice="1" aria-pressed="true">Normal</button>
          <button type="button" class="seg-btn" data-scale-choice="1.12" aria-pressed="false">Besar</button>
        </div>
      </fieldset>
    </div>
  </div>

  <dialog id="image-lightbox" closedby="any" aria-labelledby="lightbox-caption">
    <div class="lightbox-head">
      <p id="lightbox-caption" class="lightbox-title">Ilustrasi Buku</p>
      <form method="dialog">
        <button type="submit" class="btn btn-sm">Tutup (Esc)</button>
      </form>
    </div>
    <div class="lightbox-img-wrap">
      <img id="lightbox-img" src="" alt="">
    </div>
  </dialog>

  <div class="book-shell">
    <aside class="book-sidebar" id="toc-sidebar">
      <search class="toc-search-box">
        <label for="toc-filter">Cari Bab atau Bagian</label>
        <input type="search" id="toc-filter" placeholder="Contoh: EVM, UML, API, RICE, NPV, STAR...">
      </search>
      <nav aria-label="Daftar Isi Buku">
        <ul class="toc-list" id="toc-list">
          {"".join(toc_groups_html)}
        </ul>
      </nav>
    </aside>

    <main id="main-content" tabindex="-1" class="book-main">
      <section class="book-cover" aria-label="Halaman Judul Buku">
        <p class="cover-series">Program Pembelajaran Senior Project Management, Business &amp; System Analysis</p>
        <h1>Senior Project Management, Business &amp; System Analysis</h1>
        <p class="cover-subtitle">
          Buku Ajar, Ilustrasi Visual &amp; Kuis Interaktif Edisi Lengkap (Modul 01–{mod_count:02d}) berbasis Studi Kasus Berkelanjutan
          <strong>PT Sinar Nusantara Retail (SNR) — Proyek OMNI &amp; Program Nusantara 2028</strong>.
        </p>
        <div class="cover-meta-grid">
          <div class="meta-card">
            <span class="meta-label">Cakupan Lengkap</span>
            <span class="meta-value">{mod_count} Modul (Jilid I, II &amp; III)</span>
          </div>
          <div class="meta-card">
            <span class="meta-label">Visual &amp; Diagram</span>
            <span class="meta-value">{total_figures} Ilustrasi + {total_diagrams} Diagram</span>
          </div>
          <div class="meta-card">
            <span class="meta-label">Bank Kuis Auto-Koreksi</span>
            <span class="meta-value">{total_quiz_questions} Soal Pilihan Ganda</span>
          </div>
          <div class="meta-card">
            <span class="meta-label">Volume Buku</span>
            <span class="meta-value">{total_words:,} Kata (±{read_minutes} Menit)</span>
          </div>
        </div>

        <div class="quiz-dashboard" aria-label="Dasbor Progres Kuis Interaktif">
          <div class="quiz-dashboard-head">
            <span class="quiz-dashboard-title">Progres Kuis Mandiri ({mod_count} Modul — Ambang Lulus ≥ 70)</span>
            <span class="quiz-dashboard-summary" id="quiz-global-summary">0 / {mod_count} modul dinilai</span>
          </div>
          <div class="quiz-pill-row">
            {"".join(quiz_pills_html)}
          </div>
        </div>
      </section>

      {"".join(sections_html)}

      <footer class="book-footer">
        <p>
          <strong>Program Pembelajaran Senior Project Management, Business &amp; System Analysis — Edisi Lengkap (Modul 01–{mod_count:02d})</strong><br>
          Seluruh nama perusahaan, tokoh, sistem, dan angka pada studi kasus PT Sinar Nusantara Retail (SNR) bersifat fiktif untuk keperluan pembelajaran.
        </p>
      </footer>
    </main>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" defer crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" defer crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js" defer></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {{
      const metaColorScheme = document.querySelector('meta[name="color-scheme"]');
      const systemDarkQuery = window.matchMedia("(prefers-color-scheme: dark)");
      const hintEl = document.getElementById("system-theme-hint");

      // 1. Theme Settings (3-state: system / light / dark)
      function getStoredTheme() {{
        try {{
          const v = localStorage.getItem("color-scheme");
          return v === "light" || v === "dark" ? v : "system";
        }} catch {{ return "system"; }}
      }}
      function updateThemeUI() {{
        const current = getStoredTheme();
        metaColorScheme.content = current === "system" ? "light dark" : current;
        document.querySelectorAll("[data-theme-choice]").forEach((btn) => {{
          btn.setAttribute("aria-pressed", String(btn.dataset.themeChoice === current));
        }});
        if (hintEl) {{
          const sysLabel = systemDarkQuery.matches ? "Gelap" : "Terang";
          hintEl.textContent = current === "system"
            ? `Sistem (saat ini: ${{sysLabel}}).`
            : `Mode dikunci ke ${{current === "dark" ? "Gelap" : "Terang"}} (Sistem: ${{sysLabel}}).`;
        }}
      }}
      document.querySelectorAll("[data-theme-choice]").forEach((btn) => {{
        btn.addEventListener("click", () => {{
          const choice = btn.dataset.themeChoice;
          try {{
            if (choice === "system") localStorage.removeItem("color-scheme");
            else localStorage.setItem("color-scheme", choice);
          }} catch {{}}
          updateThemeUI();
        }});
      }});
      systemDarkQuery.addEventListener("change", updateThemeUI);
      window.addEventListener("storage", (e) => {{ if (e.key === "color-scheme") updateThemeUI(); }});
      updateThemeUI();

      // 2. Reader Font Scale
      function applyScale(val) {{
        document.documentElement.style.setProperty("--reader-scale", val);
        document.querySelectorAll("[data-scale-choice]").forEach((btn) => {{
          btn.setAttribute("aria-pressed", String(btn.dataset.scaleChoice === String(val)));
        }});
      }}
      try {{
        const savedScale = localStorage.getItem("reader-scale");
        if (savedScale) applyScale(savedScale);
      }} catch {{}}
      document.querySelectorAll("[data-scale-choice]").forEach((btn) => {{
        btn.addEventListener("click", () => {{
          const val = btn.dataset.scaleChoice;
          applyScale(val);
          try {{ localStorage.setItem("reader-scale", val); }} catch {{}}
        }});
      }});

      // 3. Scroll Progress JS Fallback ONLY when CSS scroll-driven animations unsupported
      if (!CSS.supports("animation-timeline", "scroll()")) {{
        const bar = document.getElementById("reading-progress");
        const updateBar = () => {{
          const scrollable = document.documentElement.scrollHeight - window.innerHeight;
          const pct = scrollable > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollable)) : 0;
          bar.style.transform = `scaleX(${{pct}})`;
        }};
        window.addEventListener("scroll", updateBar, {{ passive: true }});
        updateBar();
      }}

      // 4. Native <dialog> Image Lightbox
      const lightbox = document.getElementById("image-lightbox");
      const lightboxImg = document.getElementById("lightbox-img");
      const lightboxCap = document.getElementById("lightbox-caption");
      document.querySelectorAll(".figure-zoom-btn").forEach((btn) => {{
        btn.addEventListener("click", () => {{
          lightboxImg.src = btn.dataset.zoomSrc;
          lightboxImg.alt = btn.dataset.zoomAlt || "";
          lightboxCap.textContent = btn.dataset.zoomAlt || "Ilustrasi Buku";
          if (lightbox && typeof lightbox.showModal === "function") {{
            lightbox.showModal();
          }}
        }});
      }});

      // 5. Interactive Auto-Graded Quiz Engine (All 12 Modules / 120 Questions)
      const SCORE_KEY = "snr-book-quiz-scores-v1";
      function loadScores() {{
        try {{ return JSON.parse(localStorage.getItem(SCORE_KEY) || "{{}}"); }}
        catch {{ return {{}}; }}
      }}
      function saveScore(modSlug, pct, correct, total) {{
        const scores = loadScores();
        scores[modSlug] = {{ pct, correct, total }};
        try {{ localStorage.setItem(SCORE_KEY, JSON.stringify(scores)); }} catch {{}}
        renderDashboard();
      }}
      function clearScore(modSlug) {{
        const scores = loadScores();
        delete scores[modSlug];
        try {{ localStorage.setItem(SCORE_KEY, JSON.stringify(scores)); }} catch {{}}
        renderDashboard();
      }}
      function rubricCategory(pct) {{
        if (pct >= 90) return "Sangat Baik (Skor 4)";
        if (pct >= 75) return "Baik (Skor 3)";
        if (pct >= 60) return "Cukup (Skor 2)";
        return "Perlu Perbaikan (Skor 1)";
      }}
      function renderDashboard() {{
        const scores = loadScores();
        const pills = Array.from(document.querySelectorAll(".quiz-pill[data-pill-module]"));
        let done = 0;
        let sumPct = 0;
        pills.forEach((pill) => {{
          const slug = pill.dataset.pillModule;
          const code = "M" + slug.split("-")[1];
          pill.classList.remove("pill-pass", "pill-fail");
          if (scores[slug]) {{
            done++;
            sumPct += scores[slug].pct;
            const pass = scores[slug].pct >= 70;
            pill.classList.add(pass ? "pill-pass" : "pill-fail");
            pill.textContent = `${{code}}: ${{scores[slug].pct}}%`;
          }} else {{
            pill.textContent = code;
          }}
        }});
        const summary = document.getElementById("quiz-global-summary");
        if (summary) {{
          summary.textContent = done > 0
            ? `${{done}} / ${{pills.length}} modul dinilai • Rata-rata ${{Math.round(sumPct / done)}}%`
            : `0 / ${{pills.length}} modul dinilai`;
        }}
      }}

      function gradeQuestion(card) {{
        const correct = card.dataset.correct;
        const checked = card.querySelector('input[type="radio"]:checked');
        const fb = card.querySelector(".quiz-feedback");
        const fbStatus = card.querySelector(".quiz-feedback-status");

        card.classList.remove("is-correct", "is-wrong");
        card.querySelectorAll(".quiz-option").forEach((lbl) => {{
          lbl.classList.remove("opt-correct", "opt-wrong");
        }});
        fb.classList.remove("fb-ok", "fb-err");

        if (!checked) {{
          fb.hidden = false;
          fb.classList.add("fb-err");
          fbStatus.textContent = "⚠ Belum memilih jawaban. Pilih salah satu opsi A, B, C, atau D terlebih dahulu.";
          return {{ answered: false, isCorrect: false }};
        }}

        const chosen = checked.value;
        const isCorrect = chosen === correct;
        card.querySelectorAll(".quiz-option").forEach((lbl) => {{
          const letter = lbl.dataset.optionLetter;
          if (letter === correct) lbl.classList.add("opt-correct");
          else if (letter === chosen && !isCorrect) lbl.classList.add("opt-wrong");
        }});

        fb.hidden = false;
        if (isCorrect) {{
          card.classList.add("is-correct");
          fb.classList.add("fb-ok");
          fbStatus.textContent = `✔ Benar! Jawaban Anda (${{chosen}}) tepat.`;
        }} else {{
          card.classList.add("is-wrong");
          fb.classList.add("fb-err");
          fbStatus.textContent = `✘ Kurang tepat. Anda memilih ${{chosen}}, sedangkan kunci jawaban yang benar adalah ${{correct}}.`;
        }}
        return {{ answered: true, isCorrect }};
      }}

      document.querySelectorAll(".quiz-form").forEach((form) => {{
        const modSlug = form.dataset.quizModule;
        const modTitle = form.dataset.quizTitle;
        const banner = form.querySelector(".quiz-score-banner");

        form.querySelectorAll(".quiz-check-one").forEach((btn) => {{
          btn.addEventListener("click", () => {{
            const card = btn.closest(".quiz-card");
            if (card) gradeQuestion(card);
          }});
        }});

        form.addEventListener("submit", (e) => {{
          e.preventDefault();
          const cards = Array.from(form.querySelectorAll(".quiz-card"));
          let correctCount = 0;
          let unansweredCount = 0;
          let firstUnanswered = null;

          cards.forEach((card) => {{
            const res = gradeQuestion(card);
            if (!res.answered) {{
              unansweredCount++;
              if (!firstUnanswered) firstUnanswered = card;
            }} else if (res.isCorrect) {{
              correctCount++;
            }}
          }});

          const total = cards.length;
          const pct = Math.round((correctCount / total) * 100);
          const passed = pct >= 70;
          banner.hidden = false;
          banner.classList.remove("score-pass", "score-fail");
          banner.classList.add(passed ? "score-pass" : "score-fail");
          const unansNote = unansweredCount > 0 ? ` (${{unansweredCount}} soal belum dijawab)` : "";
          banner.innerHTML =
            `<strong>Hasil ${{modTitle}}: ${{pct}} / 100</strong> (${{correctCount}} dari ${{total}} benar${{unansNote}}) — ` +
            `Kategori: <strong>${{rubricCategory(pct)}}</strong> • Status: <strong>${{passed ? "✔ LULUS (≥ 70)" : "✘ BELUM LULUS (< 70)"}}</strong>`;

          saveScore(modSlug, pct, correctCount, total);
          if (firstUnanswered) {{
            firstUnanswered.scrollIntoView({{ behavior: "smooth", block: "center" }});
          }}
        }});

        const resetBtn = form.querySelector(".quiz-reset-btn");
        if (resetBtn) {{
          resetBtn.addEventListener("click", () => {{
            form.reset();
            form.querySelectorAll(".quiz-card").forEach((card) => {{
              card.classList.remove("is-correct", "is-wrong");
              card.querySelectorAll(".quiz-option").forEach((l) => l.classList.remove("opt-correct", "opt-wrong"));
              const fb = card.querySelector(".quiz-feedback");
              if (fb) {{ fb.hidden = true; fb.classList.remove("fb-ok", "fb-err"); }}
            }});
            banner.hidden = true;
            clearScore(modSlug);
          }});
        }}
      }});
      renderDashboard();

      // 6. Expand / Collapse All Answer Disclosures + Print Auto-Expand
      const toggleAnswersBtn = document.getElementById("btn-toggle-answers");
      const allAnswers = () => Array.from(document.querySelectorAll("details.answer-disclosure"));
      function syncToggleAnswersState() {{
        const list = allAnswers();
        const allOpen = list.length > 0 && list.every((d) => d.open);
        toggleAnswersBtn.setAttribute("aria-expanded", String(allOpen));
      }}
      toggleAnswersBtn.addEventListener("click", () => {{
        const shouldOpen = toggleAnswersBtn.getAttribute("aria-expanded") !== "true";
        allAnswers().forEach((d) => {{ d.open = shouldOpen; }});
        syncToggleAnswersState();
      }});
      document.addEventListener("toggle", (e) => {{
        if (e.target && e.target.matches && e.target.matches("details.answer-disclosure")) {{
          syncToggleAnswersState();
        }}
      }}, {{ capture: true }});

      let prePrintOpenStates = [];
      window.addEventListener("beforeprint", () => {{
        const list = allAnswers();
        prePrintOpenStates = list.map((d) => d.open);
        list.forEach((d) => {{ d.open = true; }});
      }});
      window.addEventListener("afterprint", () => {{
        allAnswers().forEach((d, idx) => {{
          if (idx < prePrintOpenStates.length) d.open = prePrintOpenStates[idx];
        }});
        syncToggleAnswersState();
      }});

      // 7. Mobile Sidebar Drawer + TOC Search Filter
      const sidebar = document.getElementById("toc-sidebar");
      const sidebarBtn = document.getElementById("btn-sidebar");
      sidebarBtn.addEventListener("click", () => {{
        const isOpen = sidebar.classList.toggle("open");
        sidebarBtn.setAttribute("aria-expanded", String(isOpen));
      }});
      sidebar.addEventListener("click", (e) => {{
        if (e.target.closest("a") && window.innerWidth <= 1024) {{
          sidebar.classList.remove("open");
          sidebarBtn.setAttribute("aria-expanded", "false");
        }}
      }});

      const tocFilter = document.getElementById("toc-filter");
      tocFilter.addEventListener("input", () => {{
        const q = tocFilter.value.trim().toLowerCase();
        document.querySelectorAll("#toc-list > .toc-chapter").forEach((chap) => {{
          const chapText = chap.querySelector(".toc-chaplink").textContent.toLowerCase();
          const subs = Array.from(chap.querySelectorAll(".toc-sublist li"));
          let anySubMatch = false;
          subs.forEach((li) => {{
            const match = !q || li.textContent.toLowerCase().includes(q) || chapText.includes(q);
            li.hidden = !match;
            if (match) anySubMatch = true;
          }});
          chap.hidden = Boolean(q) && !chapText.includes(q) && !anySubMatch;
        }});
      }});

      // 8. Active Section Highlight via IntersectionObserver
      const headings = Array.from(document.querySelectorAll(".book-chapter h2[id], .book-chapter h3[id]"));
      const tocLinks = new Map(
        Array.from(document.querySelectorAll("#toc-list a[href^='#']")).map((a) => [a.getAttribute("href").slice(1), a])
      );
      if ("IntersectionObserver" in window && headings.length) {{
        const obs = new IntersectionObserver(
          (entries) => {{
            for (const entry of entries) {{
              if (entry.isIntersecting) {{
                tocLinks.forEach((a) => a.classList.remove("toc-link-active"));
                const active = tocLinks.get(entry.target.id);
                if (active) active.classList.add("toc-link-active");
              }}
            }}
          }},
          {{ rootMargin: "-12% 0px -78% 0px", threshold: 0 }}
        );
        headings.forEach((h) => obs.observe(h));
      }}

      // 9. Progressive Lazy KaTeX Rendering per Chapter (instant initial load)
      const katexOpts = {{
        delimiters: [
          {{ left: "$$", right: "$$", display: true }},
          {{ left: "$", right: "$", display: false }}
        ],
        throwOnError: false,
        ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"]
      }};
      function renderChapterMath(chap) {{
        if (!window.renderMathInElement || chap.dataset.mathDone === "1") return;
        chap.dataset.mathDone = "1";
        window.renderMathInElement(chap, katexOpts);
      }}
      const chapters = Array.from(document.querySelectorAll(".book-chapter"));
      if ("IntersectionObserver" in window && window.renderMathInElement) {{
        const mathObs = new IntersectionObserver(
          (entries) => {{
            entries.forEach((entry) => {{
              if (entry.isIntersecting) {{
                renderChapterMath(entry.target);
                mathObs.unobserve(entry.target);
              }}
            }});
          }},
          {{ rootMargin: "1200px 0px" }}
        );
        chapters.forEach((c) => mathObs.observe(c));
      }} else {{
        chapters.forEach(renderChapterMath);
      }}

      // 10. Progressive Lazy Mermaid Rendering (non-blocking UI + full render before Print)
      let mermaidQueue = Promise.resolve();
      function renderMermaidNode(el) {{
        if (!window.mermaid || el.dataset.mermaidDone === "1") return Promise.resolve();
        el.dataset.mermaidDone = "1";
        mermaidQueue = mermaidQueue.then(() =>
          window.mermaid.run({{ nodes: [el] }}).catch((err) => {{
            console.error("Mermaid render error:", err);
          }})
        );
        return mermaidQueue;
      }}
      if (window.mermaid) {{
        window.mermaid.initialize({{
          startOnLoad: false,
          theme: "default",
          securityLevel: "loose",
          flowchart: {{ useMaxWidth: true, htmlLabels: true }},
          gantt: {{ useMaxWidth: true }}
        }});
        const mermaidNodes = Array.from(document.querySelectorAll(".mermaid"));
        if ("IntersectionObserver" in window) {{
          const mObs = new IntersectionObserver(
            (entries) => {{
              entries.forEach((entry) => {{
                if (entry.isIntersecting) {{
                  renderMermaidNode(entry.target);
                  mObs.unobserve(entry.target);
                }}
              }});
            }},
            {{ rootMargin: "1200px 0px" }}
          );
          mermaidNodes.forEach((node) => mObs.observe(node));
        }} else {{
          mermaidNodes.forEach(renderMermaidNode);
        }}
      }}

      // Print button ensures all remaining math & Mermaid diagrams render before window.print()
      const printBtn = document.getElementById("btn-print");
      printBtn.addEventListener("click", async () => {{
        const origLabel = printBtn.textContent;
        printBtn.textContent = "Menyiapkan PDF…";
        printBtn.disabled = true;
        try {{
          chapters.forEach(renderChapterMath);
          const pending = Array.from(document.querySelectorAll('.mermaid:not([data-mermaid-done="1"])'));
          for (const node of pending) {{
            await renderMermaidNode(node);
          }}
        }} finally {{
          printBtn.textContent = origLabel;
          printBtn.disabled = false;
        }}
        window.print();
      }});
    }});
  </script>
</body>
</html>
"""
    return html_doc, stats


def main() -> int:
    chapter_contents: List[Tuple[str, str, str, str, str]] = []
    missing: List[str] = []
    for fname, slug, label, part_group in CHAPTER_FILES:
        fpath = ROOT / fname
        if not fpath.exists():
            missing.append(fname)
            continue
        chapter_contents.append((fname, slug, label, part_group, fpath.read_text(encoding="utf-8")))

    if missing:
        print(f"ERROR: File bab berikut belum ditemukan: {', '.join(missing)}", file=sys.stderr)
        return 1

    # 1. Write combined Markdown book (12 modules)
    combined_md = build_combined_markdown(chapter_contents)
    md_out = ROOT / "buku-lengkap-modul-01-12.md"
    md_out.write_text(combined_md, encoding="utf-8")

    # 2. Write interactive + visual + auto-graded quiz HTML e-book (12 modules)
    ebook_html, stats = build_html_ebook(chapter_contents)
    html_out = ROOT / "buku-senior-pm-modul-01-12.html"
    html_out.write_text(ebook_html, encoding="utf-8")

    print(f"OK: {md_out.name} ({md_out.stat().st_size:,} bytes)")
    print(f"OK: {html_out.name} ({html_out.stat().st_size:,} bytes)")
    print(
        f"Stats -> Modul: {stats['modules']} | Kata: {stats['words']:,} | "
        f"Ilustrasi: {stats['figures']} | Mermaid: {stats['diagrams']} | "
        f"Kuis Interaktif: {stats['quiz_questions']} soal | Glosarium: {stats['glossary']} istilah"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
