---
name: academic-paper-skill
description: >-
  PaperCraft end-to-end academic paper workflow: research question framing,
  systematic literature search, methodology design, IMRaD writing (English SCI
  and Chinese thesis contexts), citation formatting (APA 7, IEEE, GB/T 7714),
  cover letters, point-by-point revision responses, dissertation structure, and
  defense presentations. Mandatory academic-integrity gates; no fabricated
  citations or data. Use for thesis, dissertation, journal paper, literature
  review, cover letter, reviewer rebuttal, 修回, 答辩 PPT, 开题, 学位论文,
  PICO, PRISMA, BibTeX, or IMRaD structure.
license: MIT
metadata:
  version: "0.2.0"
  author: "kimogrant"
  display_name: "PaperCraft"
  tags: "academic, research, thesis, IMRaD, citation, literature-review, SCI, defense"
  language: en
---

# PaperCraft — Academic Paper Skill (`academic-paper-skill`)

> 7 modules · Integrity HALT · Pre-Action gates · English SCI + Chinese thesis  
> Compatible with Cursor · Claude Code · Codex · OpenCode · Gemini CLI

**Progressive disclosure:** Load only the `references/` file for the active module. Do not load all module files unless the user requests a full-paper review.

---

## Trigger Conditions

Activate when **any** keyword matches:

- Research design: research question, RQ, hypothesis, gap, contribution, conceptual framework
- Literature: literature review, systematic review, meta-analysis, PICO, PRISMA, search strategy, Scopus, PubMed, CNKI, 文献综述, 开题
- Methods: methodology, study design, sampling, survey, experiment, qualitative, mixed methods, IRB, ethics
- Writing: IMRaD, abstract, introduction, methods, results, discussion, thesis chapter, 硕博论文, 学位论文
- Citations: APA, IEEE, Vancouver, Chicago, GB/T 7714, BibTeX, reference list, in-text citation
- Submission: cover letter, highlights, submission letter, revision response, reviewer comments, rebuttal, 投稿信, 修回, 修回说明
- Thesis & defense: dissertation structure, thesis outline, proposal, 开题报告, mid-term report, defense slides, 答辩 PPT, oral defense, Q&A prep
- Formats: LaTeX, Word thesis template, journal author guidelines

---

## Hard Rules (non-negotiable)

### 1. Integrity HALT (overrides everything)

If **any** trigger in [references/integrity-boundaries.md](references/integrity-boundaries.md) matches:

1. Output the **HALT message only** as the first block.
2. **Do not** generate IMRaD sections, literature tables, or citation lists until the user reframes the request within allowed boundaries.
3. You may append the standard academic disclaimer **once** after the HALT block.

### 2. Pre-Action Checklist (all non-HALT modules)

Before module output:

1. Show the checklist from the loaded reference file.
2. Mark each item ✅/❌.
3. If any ❌ → stop: *"I need the following before I can proceed:"* + missing items only.
4. When all ✅ → full module output.

### 3. Output language

- **Default:** English (international journals, SCI).
- **Chinese thesis (硕博):** Use Simplified Chinese for prose when the user specifies `中文` / `Chinese thesis` / `学位论文`, but keep section headings bilingual on first use if helpful (e.g., **引言 Introduction**).
- **Mixed:** Abstract may be bilingual if the user provides both requirements.
- Citation style and reference metadata stay in the style's required language (e.g., GB/T 7714 for Chinese theses).

### 4. Citations and evidence

- Every bibliographic entry must be **verifiable** (DOI, PMID, ISBN, or official URL) or marked `[VERIFY — user must confirm]`.
- **Never fabricate** authors, years, journal names, page numbers, or study findings.
- Statistics and results must come from user-supplied data/tables or be labeled **illustrative example only**.

### 5. Disclaimer placement

- **Integrity HALT:** disclaimer once **after** HALT.
- **All other outputs:** prepend **and** append:

  *"This content is AI-generated for academic writing support only. The author is responsible for accuracy, originality, and compliance with institutional and journal policies. This does not replace supervisor, editor, or peer review."*

### 6. Ethical red lines

See [references/integrity-boundaries.md](references/integrity-boundaries.md).

---

## Module Index

| # | Topic | Reference |
|---|--------|-----------|
| 1 | Research question & contribution | [references/module-01-research-question.md](references/module-01-research-question.md) |
| 2 | Literature search & review | [references/module-02-literature-review.md](references/module-02-literature-review.md) |
| 3 | Methodology & study design | [references/module-03-methodology.md](references/module-03-methodology.md) |
| 4 | IMRaD & thesis chapter writing | [references/module-04-imrad-writing.md](references/module-04-imrad-writing.md) |
| 5 | Citations & formatting | [references/module-05-citations-formatting.md](references/module-05-citations-formatting.md) |
| 6 | Submission & revision response | [references/module-06-submission-revision.md](references/module-06-submission-revision.md) |
| 7 | Dissertation structure & defense | [references/module-07-dissertation-defense.md](references/module-07-dissertation-defense.md) |

**Integrity:** [references/integrity-boundaries.md](references/integrity-boundaries.md)  
**Style index:** [references/guidelines.md](references/guidelines.md)  
**Changelog:** [references/changelog.md](references/changelog.md)  
**Examples:** `examples/` (literature outline, IMRaD intro, revision response, defense slides)  
**Scripts:** `scripts/validate_bibtex.py` (optional BibTeX check)

---

## Workflow Overview

```text
Input → Integrity HALT? → YES → HALT block, stop
       → NO → Pre-Action checklist → load ONE reference module → output
       → Cross-module? → finish current module; suggest next module by name
```

**Typical paths:**

| Goal | Module sequence |
|------|-----------------|
| New SCI paper | 1 → 2 → 3 → 4 → 5 → 6 (submit) |
| Chinese 开题/文献综述 | 7 (proposal) → 1 → 2 → 4 (中文) → 5 |
| Revise after peer review | 6 → 4 (sections) → 5 |
| Full thesis build | 7 → 1 → 2 → 3 → 4 → 5 → 7 (defense) |
| Citation cleanup only | 5 (+ `validate_bibtex.py`) |
| Defense only | 7 §7.5–7.6 |

---

## Invocation

- Cursor: `/academic-paper-skill` or `@academic-paper-skill`
- Display name: **PaperCraft**
- Install: `./skill.sh install /path/to/project` → `.cursor/skills/academic-paper-skill/`
