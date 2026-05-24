# Example 2: IMRaD Introduction Walkthrough

> Shows Module 1 → Module 4 handoff for a short SCI-style Introduction (English).

---

## User Input

```
Draft an Introduction for a journal submission. Topic: federated learning for
hospital readmission prediction. We use a 12-hospital dataset (de-identified),
compare FedAvg vs. centralized XGBoost, primary metric AUC. APA 7. ~900 words max.
Gap: most FL readmission work uses single-disease cohorts, not multi-morbidity.
```

## Agent Process

### Step 1: Writing Gate

```
- [x] Section: Introduction
- [x] Venue: journal (generic IMRaD; user confirms word limit 900)
- [x] Language: English
- [x] User provided: RQ implied, gap, methods summary, metric — no fabricated AUC values in Intro
- [x] APA 7

Proceeding.
```

### Step 2: Introduction draft (excerpt — user must add real citations)

```markdown
## Introduction

### Territory
Hospital readmission prediction supports care management and quality reporting,
yet model development often requires pooling sensitive electronic health records
(EHR) across institutions. Privacy regulations and data governance limit centralized
learning, motivating federated approaches that train models without raw data exchange
[cite foundational FL health work — VERIFY].

### Niche
Prior federated readmission studies frequently focus on single-disease cohorts
(e.g., heart failure or COPD alone), which may underrepresent multi-morbidity
patterns common in general medical populations [VERIFY]. Centralized benchmarks
on multi-site EHR data exist, but direct comparisons between federated aggregation
(FedAvg) and strong centralized baselines (e.g., gradient-boosted trees) under
aligned feature sets remain sparse [VERIFY].

### Occupy — this study
This study evaluates federated learning with FedAvg against a centralized XGBoost
baseline for 30-day readmission prediction using de-identified EHR from 12 hospitals.
We hypothesize that FedAvg achieves competitive discrimination (AUC) to centralized
training while enabling cross-institutional collaboration without sharing patient-level
records.

**Contributions:**
1. Multi-hospital, multi-morbidity readmission cohort under a unified prediction task
2. Head-to-head FedAvg vs. centralized XGBoost with pre-specified metrics (AUC)
3. Practical discussion of federation constraints in real hospital IT environments

Methods, results, and limitations are reported in subsequent sections.
```

### Step 3: Agent reminders to user

- Replace every `[VERIFY]` with APA 7 in-text citations from user's library.
- Methods detail → Module 3; Results numbers → user-supplied only in Module 4 §4.3.
- If word count exceeds 900, trim Theme A sentences before shrinking gap statement.

---

## Chinese thesis variant

Same CARS logic; user adds `中文` → output 引言 with **研究背景、研究现状与不足、研究目的与内容、论文结构安排**; citations per GB/T 7714 (Module 5).
