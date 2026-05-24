## Module 5: Citations & Formatting

### Pre-Action Checklist

```
**Citation Gate** — Confirm before formatting:

- [ ] Citation style is specified (APA 7 / IEEE / Vancouver / GB/T 7714 / Chicago / journal-specific)
- [ ] Input format is known (BibTeX, RIS, DOI list, plain text references, Word doc)
- [ ] In-text vs. numbered style confirmed
- [ ] Language mix (English refs only vs. bilingual thesis) stated
- [ ] User understands unverifiable entries will be marked [VERIFY]

If formatting without sources → provide style **examples** only, not a fake bibliography.
```

### 5.1 In-text citation patterns

**APA 7:** (Author, Year) or Author (Year). Et al. rules: 3+ authors from first citation in APA 7... actually APA 7: 3+ authors use et al. from first citation.

**IEEE:** Numeric [1], sorted by order of appearance.

**GB/T 7714 顺序编码制:** 上标 [1] or [1] in brackets per school rule.

**GB/T 7714 著者-出版年制:** (作者, 年份).

When uncertain which GB/T variant → ask for thesis handbook.

### 5.2 Reference list entry templates

**Journal (APA 7):**
```
Author, A. A., & Author, B. B. (Year). Title of article. *Title of Periodical*, *volume*(issue), pages. https://doi.org/xxxxx
```

**Journal (IEEE):**
```
[1] A. Author and B. Author, "Title of paper," *Abbrev. Journal*, vol. x, no. x, pp. xx–xx, Month Year.
```

**Journal (GB/T 7714):**
```
[1] AUTHOR A, AUTHOR B. Title[J]. Journal, Year, Volume(Issue): Pages.
```

Mark `[VERIFY]` if any field missing.

### 5.3 BibTeX cleanup workflow

1. Parse user BibTeX or export from Zotero.
2. Normalize: title case per style, journal abbreviations for IEEE, DOI/URL fields.
3. Flag: missing year, duplicate keys, `@misc` without howpublished.
4. Output corrected `.bib` snippet + change log.

**Do not** add BibTeX entries from memory without DOI verification.

### 5.4 DOI / metadata verification

When user provides DOI list:

```markdown
| DOI | Status | Corrected citation |
|-----|--------|-------------------|
| 10.xxxx/yyyy | OK / [VERIFY] | [formatted entry] |
```

If DOI lookup unavailable, instruct user to confirm in Crossref or publisher site.

### 5.5 Common errors to fix

| Error | Fix |
|-------|-----|
| et al. misuse | Apply style rules for author count |
| Inconsistent year in text vs. list | Single source of truth from metadata |
| URL instead of DOI | Prefer DOI when exists |
| 中文文献作者格式混乱 | GB/T: 姓前名后 vs. 外文著者规范 |
| Secondary citation overuse | Find primary source or mark indirect |

### 5.6 LaTeX quick reference

```latex
% APA-like (biblatex)
\usepackage[style=apa,backend=biber]{biblatex}
\addbibresource{refs.bib}
\printbibliography

% IEEE
\bibliographystyle{IEEEtran}
\bibliography{refs}

% GB/T 7714
\usepackage[gb7714-2015]{gbt7714}
```

### 5.7 Word / reference managers

- Recommend Zotero with style plugin for APA/IEEE; GB/T styles available as CSL (verify version with school).
- For thesis: generate reference list last; use field codes, not manual numbering.

### 5.8 BibTeX validation (optional script)

When user provides a `.bib` file, run:

```bash
python scripts/validate_bibtex.py path/to/refs.bib
```

Reports missing required fields, duplicate keys, and suspicious `year`/`doi` values. Fix entries manually or in Zotero; re-run until `OK`.

### 5.9 Citation audit report

When user asks "check my references":

```markdown
## Citation audit

- Total references: N
- Missing DOI/URL: [list]
- Not cited in text: [list]
- Cited in text but missing from list: [list]
- Style inconsistencies: [list with line/section if provided]
- Suspected fabricated / unverifiable: [list — HALT if intentional fabrication requested]
```
