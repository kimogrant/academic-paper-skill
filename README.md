# PaperCraft — Academic Paper Skill for AI Agents

<p align="center">
  <img src="https://img.shields.io/badge/version-0.2.0-blue" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/modules-7-orange" alt="modules">
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20Gemini%20CLI-purple" alt="platforms">
  <img src="https://img.shields.io/badge/skill%20language-English-red" alt="language">
</p>

> End-to-end academic writing skill — research framing, literature search, methodology, IMRaD, and citations with academic-integrity gates. Supports **English SCI** and **Chinese thesis (硕博)** workflows.

English | [简体中文](./README.zh.md)

---

## Why PaperCraft?

**PaperCraft** encodes graduate-level research writing into an [Agent Skill](https://agentskills.io/) package: `SKILL.md` + on-demand `references/` modules.

**Good for:** SCI journal authors, master's/PhD students (including 开题与文献综述), and researchers who want structured IMRaD output, search strategies, and citation cleanup — **without** fabricated references or ghostwritten submissions.

## Install

```bash
git clone https://github.com/kimogrant/academic-paper-skill.git
cd academic-paper-skill
chmod +x skill.sh
./skill.sh install /path/to/your/project
```

Installs to: `your-project/.cursor/skills/academic-paper-skill/` (includes `references/` and `examples/`).

Reload Cursor → invoke **`/academic-paper-skill`** (skill id; display name **PaperCraft**).

### Other platforms

| Platform | Path |
|----------|------|
| Cursor (manual) | `.cursor/skills/academic-paper-skill/` — copy full skill bundle |
| Claude Code | `~/.claude/skills/academic-paper-skill/SKILL.md` + `references/` |
| Codex | `~/.codex/skills/academic-paper-skill/` |

**Do not** copy only `SKILL.md` without `references/` — templates live there.

## Example

See [`examples/1-literature-review-outline.md`](examples/1-literature-review-outline.md) for Pre-Action gate → search strategy → thematic outline.

See [`examples/2-imrad-introduction.md`](examples/2-imrad-introduction.md) for CARS-style Introduction drafting.

See [`examples/3-revision-response.md`](examples/3-revision-response.md) for point-by-point reviewer responses.

See [`examples/4-defense-slides-outline.md`](examples/4-defense-slides-outline.md) for Chinese PhD defense slide planning.

## Modules

| # | Module | Reference file |
|---|--------|----------------|
| 1 | Research question & contribution | `references/module-01-research-question.md` |
| 2 | Literature search & review | `references/module-02-literature-review.md` |
| 3 | Methodology & study design | `references/module-03-methodology.md` |
| 4 | IMRaD & thesis chapter writing | `references/module-04-imrad-writing.md` |
| 5 | Citations & formatting | `references/module-05-citations-formatting.md` |
| 6 | Submission & revision response | `references/module-06-submission-revision.md` |
| 7 | Dissertation structure & defense | `references/module-07-dissertation-defense.md` |

Optional: `python scripts/validate_bibtex.py refs.bib` for BibTeX sanity checks.

## Integrity

```text
Input → Integrity HALT? → YES → HALT message first, then stop
       → NO → Pre-Action checklist → load one reference module → output
```

Details: `references/integrity-boundaries.md`

**PaperCraft refuses:** ghostwritten submissions, fabricated data/citations, plagiarism evasion.  
**PaperCraft helps:** your outlines, your drafts, search strategies, methods templates, formatting.

## Bilingual use (SCI + Chinese thesis)

| Aspect | Behavior |
|--------|----------|
| Skill instructions | English (`SKILL.md` + `references/`) |
| Prose output | English by default; Chinese when user requests 中文 / 学位论文 |
| Citations | APA / IEEE / GB/T 7714 per Module 5 |

## Repository layout

| Path | Purpose |
|------|---------|
| `SKILL.md` | Frontmatter, hard rules, module index |
| `references/` | Per-module templates |
| `examples/` | Walkthrough cases |
| `skill.sh` | Install helper |
| `VERSION` | Semver |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [PROJECT.md](PROJECT.md).

## Related skills

| Repo | Focus |
|------|--------|
| [clinical-skills](https://github.com/kimogrant/clinical-skills) | Clinical documentation & EBM |
| [kimogrant skills index](https://github.com/kimogrant) | All Agent Skills |

## License

MIT © [kimogrant](https://github.com/kimogrant/academic-paper-skill)

<p align="center"><sub><em>Verify every citation. Own your work.</em></sub></p>
