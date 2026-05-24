## Module 3: Methodology & Study Design

### Pre-Action Checklist

```
**Methodology Gate** — Confirm before writing methods:

- [ ] Research question and study type are defined (quant / qual / mixed / review / simulation)
- [ ] Data status: collected / planned / secondary / public dataset named
- [ ] Population or sample frame is described
- [ ] Ethics/IRB status stated (approved / exempt / pending / N/A with reason)
- [ ] Target reporting guideline identified (CONSORT, STROBE, PRISMA, SRQR, etc.) or agree to propose one
- [ ] Output language and venue (SCI vs Chinese thesis) confirmed

If any unchecked → list missing items. Do not invent sample sizes, IRB numbers, or equipment settings.
```

### 3.1 Methods section skeleton (IMRaD Methods)

```markdown
## Methods

### Study design
[Design name + rationale in 1–2 sentences]

### Setting and participants
- Setting: [site, dates]
- Inclusion criteria: [...]
- Exclusion criteria: [...]
- Recruitment: [...]
- Sample size: [n = X; power analysis or saturation rationale — user must supply]

### Variables / measures
| Variable | Type | Operational definition | Instrument / source | Reliability (if known) |
|----------|------|------------------------|---------------------|------------------------|

### Procedure
[Step-by-step data collection; timeline; blinding/randomization if RCT]

### Data analysis
- Software: [R / SPSS / NVivo / etc.]
- Tests / models: [name each; alpha level; assumptions checked]
- Qualitative: coding approach, inter-rater agreement if applicable

### Ethics
[IRB ID or exemption; consent; data privacy; clinical trial registration if applicable]
```

Label `[USER TO COMPLETE]` for any unknown numeric or institutional detail.

### 3.2 Design selection guide

| RQ pattern | Common designs |
|------------|----------------|
| Effect of X on Y | RCT, quasi-experiment, cohort |
| Prevalence / association | Cross-sectional survey |
| Experience / meaning | Phenomenology, grounded theory, interviews |
| Implementation | Case study, action research |
| Tool / model evaluation | Benchmark, ablation, user study (HCI) |
| Existing data | Secondary analysis, bibliometric, ML on public sets |

Recommend **one primary design**; mention alternatives in one sentence if trade-offs exist.

### 3.3 Sampling

**Quantitative:** probability vs. convenience; response rate; missing data plan.  
**Qualitative:** purposeful sampling strategy; saturation target (justify with field norms, not fake numbers).  
**ML/CS:** train/val/test split; leakage prevention; reproducibility seeds.

### 3.4 Validity & reliability checklist

| Concern | Mitigation to document |
|---------|------------------------|
| Internal validity | Randomization, controls, confounders |
| External validity | Population, setting generalizability |
| Construct validity | Instrument source, pilot, CFA if applicable |
| Replicability | Code/data availability statement |

### 3.5 Chinese thesis methods (研究方法)

When writing in Chinese, align with common 硕博 structure:

- **研究设计、研究对象/样本、数据来源、变量定义与测量、实验/调查/访谈步骤、数据分析方法、信效度说明、伦理审查**.

Use 三线表 for instrument summaries when appropriate.

### 3.6 Pre-registration & openness

If applicable, remind user to register (OSF, ClinicalTrials.gov) **before** data collection. Methods should match registered protocol or explain deviations.
