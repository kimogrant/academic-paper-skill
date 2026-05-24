## Module 2: Literature Search & Review

### Pre-Action Checklist

```
**Literature Gate** — Confirm before search or review writing:

- [ ] Research question or topic scope is defined (Module 1 or user-provided)
- [ ] Review type is specified (narrative / systematic / scoping / 文献综述 chapter)
- [ ] Target databases are available or named (PubMed, Scopus, WoS, CNKI, etc.)
- [ ] Date range and language filters are stated or defaulted with disclosure
- [ ] Inclusion/exclusion criteria draft exists OR user agrees to propose criteria
- [ ] Citation style for the review output is known (Module 5)

If any unchecked → request missing items. For systematic reviews, all criteria are mandatory before PRISMA flow.
```

### 2.1 Search strategy template

**Trigger:** "literature review", "systematic review", "search strategy", "PICO", "PRISMA", "文献检索"

**PICO / PICo framing (quantitative / clinical):**

| Element | Your study |
|---------|------------|
| **P**opulation | |
| **I**ntervention / exposure | |
| **C**omparison | |
| **O**utcome | |

**SPIDER (qualitative):** Sample, Phenomenon of Interest, Design, Evaluation, Research type.

**Search string builder (repeat per database):**

```markdown
## Search strategy — [Database name]

**Date run:** YYYY-MM-DD (user must execute and confirm counts)

### Concept blocks
| Concept | Keywords | Synonyms / MeSH / 主题词 |
|---------|----------|---------------------------|
| A | | |
| B | | |
| C | | |

### Boolean string
```
(Block A) AND (Block B) AND (Block C)
```

### Filters
- Years: [e.g., 2015–2026]
- Language: [English / Chinese / both]
- Document type: [peer-reviewed articles / theses excluded / etc.]

### Expected export
RIS/BibTeX → reference manager; deduplicate before screening.
```

**Never report hit counts as facts** unless the user pastes search results.

### 2.2 Screening workflow (systematic)

```text
Identify (databases + grey literature)
  → Dedupe
  → Title/abstract screen (inclusion/exclusion)
  → Full-text screen
  → Included studies → extraction table
  → Synthesis (narrative / meta-analysis if applicable)
```

Provide PRISMA 2020 checklist reference; user fills numbers.

### 2.3 Literature review outline (narrative / thesis chapter)

```markdown
## Literature review outline

### 1. Introduction to the review
- Scope and objectives
- Organization logic (chronological / thematic / methodological)

### 2. Theme A: [name]
- Key findings [Author, Year — VERIFY]
- Debates and limitations
- Link to RQ/gap

### 3. Theme B: [name]
[Same structure]

### 4. Theme C: [name]
[Same structure]

### 5. Synthesis & gap statement
- Consensus points
- Contested points
- Explicit gap motivating current study

### Reference strategy
- Seminal works: [list user must confirm]
- Recent 5 years: [search strategy from §2.1]
```

### 2.4 Evidence synthesis table

```markdown
| Author (Year) | Design | Population / context | Method | Main findings | Limitations | Relevance to RQ |
|---------------|--------|----------------------|--------|---------------|-------------|-----------------|
```

Mark cells `[VERIFY]` when not from user-provided abstracts.

### 2.5 Chinese literature (CNKI / 万方 / 维普)

- Note database access is institution-dependent.
- Search fields: 主题、关键词、摘要；combine with 同义词 and English equivalents for bilingual reviews.
- GB/T 7714 formatting deferred to Module 5.
- For 硕博 Chapter 2: typical structure **国内研究现状 → 国外研究现状 → 研究述评**, unless school template says otherwise.

### 2.6 Quality appraisal

| Design | Tool (suggest one) |
|--------|-------------------|
| RCT | Cochrane RoB 2 |
| Cohort / case-control | Newcastle-Ottawa |
| Qualitative | CASP qualitative checklist |
| Mixed | MMARS or separate tools per strand |

Appraisal is **mandatory** for systematic reviews; optional for narrative reviews unless user requests.
