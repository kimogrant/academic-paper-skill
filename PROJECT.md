# PaperCraft — Project Documentation

## Repository Structure

```text
academic-paper-skill/
├── SKILL.md              # Frontmatter, hard rules, module index
├── VERSION
├── skill.sh
├── references/
│   ├── module-01-research-question.md
│   ├── module-02-literature-review.md
│   ├── module-03-methodology.md
│   ├── module-04-imrad-writing.md
│   ├── module-05-citations-formatting.md
│   ├── module-06-submission-revision.md
│   ├── module-07-dissertation-defense.md
│   ├── integrity-boundaries.md
│   ├── guidelines.md
│   └── changelog.md
├── examples/
├── scripts/
│   └── validate_bibtex.py
├── README.md / README.zh.md
├── CONTRIBUTING.md
└── LICENSE
```

## Skill identity

| Field | Value |
|-------|--------|
| Agent Skills `name` | `academic-paper-skill` (must match install folder name) |
| Display / brand | **PaperCraft** |
| Target users | English SCI authors + Chinese 硕博 students |

## Design principles

1. **Progressive disclosure** — one `references/` file per task
2. **Integrity HALT first** — no section generation before misconduct check
3. **Citation-gated** — verifiable sources or `[VERIFY]`
4. **Checklist-gated** — incomplete inputs → no full draft
5. **Bilingual output, English skill** — prose follows user language request

## Adding a module

1. Add `references/module-0X-name.md` with Pre-Action Checklist + templates
2. Add row to `SKILL.md` module index
3. Add `examples/` walkthrough
4. Bump `VERSION` + `references/changelog.md`

## Testing checklist

- [ ] Ghostwriting request → Integrity HALT only, no IMRaD
- [ ] "Cite 10 papers on X" with no sources → HALT or `[VERIFY]` only, no fake DOIs
- [ ] Incomplete RQ request → Module 1 gate blocks
- [ ] User says 中文 + 开题 → Module 7 §7.3 + Module 1 Chinese structure
- [ ] Revision response without reviewer text → Module 6 gate blocks
- [ ] Defense slides without RQ/findings → Module 7 gate blocks or placeholders only
- [ ] `python scripts/validate_bibtex.py` on sample .bib → OK or expected errors
- [ ] `SKILL.md` YAML frontmatter valid; `name: academic-paper-skill`
- [ ] `./skill.sh install` copies `references/`, `examples/`, `scripts/`

## Release process

1. Update `VERSION`, `references/changelog.md`, README badges
2. Run testing checklist
3. `git tag -a v0.2.0 -m "Version 0.2.0"`

## Maintainers

- [kimogrant](https://github.com/kimogrant) — creator

## Related

- [clinical-skills](https://github.com/kimogrant/clinical-skills) — clinical vertical skill (parallel HALT + module pattern)

**Last updated**: 2026-05-24
