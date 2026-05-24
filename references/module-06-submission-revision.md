## Module 6: Submission & Revision Response

### Pre-Action Checklist

```
**Submission Gate** — Confirm before cover letter or revision response:

- [ ] Document type: initial submission / major revision / minor revision / resubmission / 修回
- [ ] Target journal or conference is named (or generic template with [JOURNAL] placeholders)
- [ ] Manuscript title and author list are provided (or placeholders marked)
- [ ] For revision: full reviewer comments pasted OR numbered list supplied by user
- [ ] For revision: user indicates what changed in the manuscript (section list or diff summary)
- [ ] Output language: English (default) or Chinese (投稿信 / 修回说明)
- [ ] User confirms they authored the scientific content (no ghostwriting HALT)

If revision response without reviewer text → request comments before point-by-point reply.
```

### 6.1 Cover letter (initial submission)

**Trigger:** "cover letter", "submission letter", "投稿信", "manuscript submission"

```markdown
[Date]

Dear Editor-in-Chief / [Editor name if known],

We submit the manuscript entitled **"[Full Title]"** for consideration as a [Article type: Original Research / Review / Short Communication] in *[Journal Name]*.

**Summary (3–5 sentences):**
- Problem/gap: [...]
- What we did: [design, n/context, key method]
- Main finding: [one sentence — from user manuscript only]
- Significance: [field/practice contribution]

**Fit with journal scope:**
[1–2 sentences linking to journal aims; cite recent journal paper if user provides — VERIFY]

**Declarations (complete all that apply):**
- [ ] Original work not published elsewhere
- [ ] All authors approved submission
- [ ] Conflicts of interest: [None / describe]
- [ ] Funding: [Grant IDs or None]
- [ ] Ethics: [IRB # / exempt / N/A]
- [ ] Data availability: [repository / on request / N/A]
- [ ] AI disclosure: [per journal/institution policy — user must confirm wording]
- [ ] Suggested reviewers (if requested): [name, email, institution, reason] — optional list from user

We believe this work will interest readers of *[Journal]* because [one sentence].

Sincerely,

[Corresponding author name]
[Affiliation]
[Email]
```

**Rules:**

- Do not exaggerate novelty ("first ever") without user evidence.
- Suggested reviewers must be real people user names — never invent experts.
- Word limit: many journals ≤ 1 page; trim Summary first if over limit.

### 6.2 Highlights / graphical abstract blurb (optional)

When journal requires **Highlights** (3–5 bullets, ≤85 characters each in some Elsevier journals):

```markdown
## Highlights

- [Finding 1 — max chars per journal guide]
- [Finding 2]
- [Finding 3]
```

User must supply facts; agent formats only.

### 6.3 Response to reviewers (point-by-point)

**Trigger:** "revision response", "rebuttal", "response to reviewers", "修回信", "逐条回复"

**Workflow:**

1. Parse each reviewer comment into a numbered item (R1-1, R1-2, R2-1…).
2. For each item output: **Comment → Response → Manuscript change**.
3. Tone: respectful, factual, concise; no defensiveness.
4. If comment is valid → thank + describe fix + cite new section/line/table.
5. If user disagrees → polite justification + evidence; offer compromise if appropriate.
6. If comment requires new analysis user has not run → mark `[ACTION REQUIRED: run analysis X]`; do not fabricate results.

**Output template:**

```markdown
# Response to Reviewers

**Manuscript ID:** [ID]
**Title:** [Title]
**Journal:** [Journal]

We thank the editor and reviewers for their constructive feedback. We have revised the manuscript accordingly. Major changes are summarized below; detailed point-by-point responses follow.

## Summary of major changes
1. [Change 1 — e.g., expanded Methods §2.3; new Table 2]
2. [Change 2]
3. [Change 3]

---

## Reviewer 1

### Comment 1.1
> [Paste reviewer text verbatim]

**Response:**
[Thank reviewer. State what was done. If applicable: "We have clarified in Lines X–Y, Page Z" or "We added Supplementary Table S1."]

**Manuscript changes:**
- Section: [§X.Y]
- Change type: [rewritten / added / deleted / new figure]

### Comment 1.2
> [...]

**Response:**
[...]

---

## Reviewer 2
[Same structure]

---

## Reviewer 3 (if applicable)
[Same structure]

---

## Additional notes to editor (optional, private tone)
[Only if user requests — e.g., disagreement with Reviewer 2 comment 3 handled as limitation paragraph]

Sincerely,
[Authors]
```

### 6.4 Response table (compact alternative)

For journals or supervisors preferring tables:

```markdown
| ID | Reviewer comment (summary) | Response | Location in revised manuscript |
|----|---------------------------|----------|--------------------------------|
| R1-1 | [short paraphrase] | [response] | p. X, Lines Y–Z / §3.2 |
```

Keep verbatim quotes in appendix if table uses paraphrase.

### 6.5 Major vs. minor revision strategy

| Revision type | Emphasis |
|---------------|----------|
| **Major** | Summary of changes up front; new analyses clearly flagged; track all R#-# |
| **Minor** | Shorter responses; copy-edits and clarifications; still point to line numbers |
| **Reject → resubmit elsewhere** | Do not reuse old reviewer IDs; write fresh cover letter (§6.1) |

### 6.6 Chinese 修回说明 (学位论文 / 中文期刊)

When output language is Chinese:

```markdown
# 审稿意见回复说明

**论文题目：** [题目]
**投稿期刊/单位：** [期刊或学位论文预答辩委员会]

感谢审稿专家提出的宝贵意见。我们已逐条修改，主要修改如下：
1. [...]
2. [...]

## 意见一
**审稿意见：** [原文]

**回复：** 感谢专家指正。我们已……（具体修改位置：第×章第×节，第×页）。

**修改情况：** [简述或“见修订稿标红处”]
```

Follow school/journal requirement for 标注修改处 / 修订模式.

### 6.7 Integrity reminders (Module 6)

- Do not fabricate "we performed additional experiments" unless user confirms.
- Do not draft fake reviewer comments to generate responses.
- If user asks to misrepresent changes → Integrity HALT.

### 6.8 Cross-module links

| Need | Module |
|------|--------|
| Rewrote Introduction per R2 | Module 4 §4.2 |
| New citations in revision | Module 5 |
| New methods paragraph | Module 3 |
| Updated PRISMA counts | Module 2 |
