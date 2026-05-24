## Module 1: Research Question & Contribution

### Pre-Action Checklist

```
**Research Question Gate** — Confirm before framing:

- [ ] Broad topic area is stated
- [ ] Academic level is specified (undergraduate / master's / PhD / faculty paper)
- [ ] Target output is specified (journal article / thesis chapter / proposal / 开题)
- [ ] Discipline field is specified (e.g., CS, education, medicine, economics)
- [ ] Any constraints are known (data already collected? timeline? target venue?)

If any unchecked → "I need [missing item(s)] before I can frame the research question."
```

### 1.1 Problem → Gap → RQ pipeline

**Trigger:** "research question", "RQ", "thesis topic", "开题", "contribution", "research gap"

Use this sequence:

1. **Context (2–3 sentences):** What is established in the field?
2. **Gap:** What is missing, contested, or outdated? (Must be falsifiable or investigable.)
3. **Research question(s):** 1 primary RQ + ≤2 secondary RQs.
4. **Contribution claim:** What this work adds (theoretical / methodological / empirical / practical).
5. **Scope boundaries:** What this study will **not** address.

**Output template:**

```markdown
## Research framing

### Context
[2–3 sentences]

### Gap
- Gap 1: [specific, cited or marked VERIFY]
- Gap 2: [optional]

### Research questions
- **RQ1 (primary):** [interrogative, specific population/context/method if known]
- RQ2: [optional]
- RQ3: [optional]

### Hypotheses (if quantitative)
- H1: [directional relationship, testable]
- H2: [optional]

### Expected contributions
| Type | Contribution |
|------|--------------|
| Theoretical | [one line] |
| Methodological | [one line] |
| Practical | [one line] |

### Scope & limitations (design phase)
- In scope: [...]
- Out of scope: [...]
```

### 1.2 FINER / SMART checks

After drafting RQs, validate:

| Criterion | Question |
|-----------|----------|
| **F**easible | Data and methods available in timeframe? |
| **I**nteresting | Matters to field or practice? |
| **N**ovel | Not a pure replication unless justified? |
| **E**thical | IRB / consent / data privacy addressed? |
| **R**elevant | Aligns with target venue or degree requirements? |

Flag any ❌ with a one-line fix suggestion.

### 1.3 Conceptual framework (optional)

When user requests framework or 理论框架:

```markdown
## Conceptual framework

### Constructs
| Construct | Definition (operational) | Source [VERIFY] |
|-----------|------------------------|-----------------|

### Relationships (hypothesized)
[Diagram description or bullet list: A → B → C; moderators; mediators]

### Positioning vs. prior models
[How this extends or differs from cited model]
```

Do not invent construct definitions without user confirmation or citable source.

### 1.4 Chinese thesis (开题) alignment

When output language is Chinese:

- Include **研究背景、研究意义（理论/实践）、国内外研究现状（简述，详述见 Module 2）、研究内容、拟解决的关键问题、创新点、技术路线（文字版）**.
- Keep RQs in Chinese; optional English RQ in parentheses for SCI-bound students.

### 1.5 Common failure modes

| Issue | Fix |
|-------|-----|
| RQ too broad | Narrow population, context, or time window |
| RQ is a topic not a question | Rewrite as interrogative |
| Gap = "little research" | Specify **what kind** of research is missing |
| Contribution = "first study ever" | Soften unless user provides evidence |
