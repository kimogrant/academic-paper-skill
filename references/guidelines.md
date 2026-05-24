## Citation & Journal Style Index

Use with [module-05-citations-formatting.md](module-05-citations-formatting.md). Default by context:

| Context | Default style | Notes |
|---------|---------------|-------|
| Social sciences / psychology | APA 7 | In-text (Author, Year) |
| Engineering / CS | IEEE | Numeric [1] |
| Biomedical | Vancouver / AMA | Numeric; journal-specific |
| Chinese 硕博 / CSSCI | GB/T 7714-2015 | 顺序编码制 or 著者-出版年制 per school |
| Humanities | Chicago NB or Author-Date | Confirm with department |
| Nature / Science family | Journal-specific | Check author guide |

### Database quick reference

| Database | Best for | Export |
|----------|----------|--------|
| PubMed / MEDLINE | Biomedical | `.nbib`, BibTeX via Zotero |
| Scopus / Web of Science | Multidisciplinary SCI | RIS, BibTeX |
| IEEE Xplore | Engineering | BibTeX |
| CNKI 知网 | Chinese literature | Note + manual GB/T cleanup |
| Google Scholar | Broad discovery | BibTeX (verify metadata) |

### Reporting guidelines (methods modules)

| Study type | Guideline |
|------------|-----------|
| RCT | CONSORT |
| Systematic review | PRISMA |
| Observational | STROBE |
| Diagnostic accuracy | STARD |
| Qualitative | SRQR or COREQ |
| Prediction models | TRIPOD |

Link checklist items in Module 3 when the study type is known.

### Submission & thesis (Modules 6–7)

| Task | Module |
|------|--------|
| Cover letter / revision response | Module 6 |
| Thesis chapter map / 开题 / 答辩 PPT | Module 7 |
| Post-revision citation audit | Module 5 + `scripts/validate_bibtex.py` |

### Word / LaTeX defaults

- **LaTeX:** `biblatex` + `biber` for APA; `IEEEtran` BibTeX for IEEE; `gbt7714` package for GB/T 7714.
- **Word:** Zotero / Mendeley plugin; never hand-edit numbered lists without field codes.

### When style is unknown

Ask once: target journal name OR institution thesis handbook OR "APA / IEEE / GB/T 7714".
