# Example 1: Literature Review Outline

> Shows PaperCraft (`academic-paper-skill`) flow — Pre-Action gate → Module 2 templates → thematic outline (English SCI context).

---

## User Input

```
I'm writing a master's thesis on using large language models for automated code review
in open-source projects. Target: English literature review chapter (~3000 words).
I have access to Scopus and IEEE Xplore. Years 2019–2026. APA 7.
RQ: How effective are LLM-based tools compared to traditional static analyzers for
finding security-relevant bugs in OSS?
```

## Agent Process (with PaperCraft loaded)

### Step 1: Literature Gate

```
**Literature Gate** — Confirm before search or review writing:

- [x] Research question or topic scope defined
- [x] Review type: narrative thesis chapter (not full PRISMA systematic review)
- [x] Databases: Scopus, IEEE Xplore
- [x] Date range: 2019–2026; language: English (default)
- [x] Inclusion/exclusion: user agrees to proposed criteria below
- [x] Citation style: APA 7

All checks passed. Proceeding with search strategy + outline.
```

### Step 2: Proposed inclusion criteria

- Peer-reviewed articles and major conference proceedings (CORE A or IEEE/ACM).
- Studies on LLMs or neural models applied to code review, bug detection, or security analysis in OSS.
- Exclude: pure survey papers without empirical component unless seminal; non-English unless user adds later.

### Step 3: Search strategy sketch (user must run)

**Concept blocks:** (LLM OR "large language model" OR Codex OR GPT) AND ("code review" OR "static analysis" OR "vulnerability detection") AND ("open source" OR GitHub)

User runs in Scopus/IEEE → exports RIS → deduplicates before screening.

### Step 4: Output — Review outline

```markdown
## Literature review outline

### 1. Introduction to the review
- Scope: LLM-assisted code review vs. traditional static analysis for security bugs in OSS
- Organization: thematic (tool paradigms → evaluation metrics → OSS context)

### 2. Theme A: Traditional static analysis for security in OSS
- Rule-based and AST tools (e.g., Semgrep, CodeQL) — strengths/limitations [VERIFY with user sources]
- False positive burden in OSS maintenance

### 3. Theme B: LLM-based code understanding and review
- Prompt-based review vs. fine-tuned models
- Benchmarks (HumanEval-style vs. real-repo datasets)

### 4. Theme C: Comparative and hybrid approaches
- LLM + static analysis pipelines
- Human-in-the-loop and trust/security implications

### 5. Synthesis & gap
- Consensus: [to fill after user screening]
- Gap motivating RQ: rigorous OSS-scale comparisons with security-labeled ground truth remain limited

### Next steps
1. Run search strings; paste n= hits for PRISMA-style flow if upgrading to systematic review
2. Module 4 for chapter prose once extraction table has ≥15 core papers
```

---

## Notes

- No fabricated citations in the outline — `[VERIFY with user sources]` marks where user must attach papers.
- For Chinese 文献综述 chapter, same structure with GB/T 7714 and CNKI block added in Module 2 §2.5.
