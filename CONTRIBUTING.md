# Contributing to PaperCraft

We welcome contributions — especially from researchers, librarians, graduate advisors, and journal editors.

## How to Contribute

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/kimogrant/academic-paper-skill.git
   ```
3. **Create a branch**:
   ```bash
   git checkout -b feature/your-module-name
   ```
4. **Make your changes**:
   - Templates → edit the relevant `references/module-*.md`
   - Triggers / hard rules / index → edit `SKILL.md` only
   - New module: add `references/module-0X-*.md`, index row in `SKILL.md`, example in `examples/`
   - Bump `VERSION` and `references/changelog.md`
5. **Commit** with a descriptive message:
   ```bash
   git commit -m "[Module] Brief description of change"
   ```
6. **Push** and open a Pull Request

## Standards

- **Citation examples must be labeled** as illustrative or `[VERIFY]` — never present invented DOIs as real
- **Integrity rules are non-negotiable**: PRs that weaken HALT or enable misconduct will not be merged
- **Pre-Action Checklists are mandatory** for all modules
- **Keep SKILL.md under ~500 lines**; put detail in `references/`
- **English only** in `SKILL.md` and `references/` (README.zh.md is for human docs)

## Review Process

- PRs affecting `integrity-boundaries.md` or `SKILL.md` hard rules need maintainer review
- Style-guide updates should cite official manual (APA, IEEE, GB/T) or journal author instructions
- All PRs should pass the testing checklist in `PROJECT.md`

## Code of Conduct

- Be respectful and constructive
- Debate on evidence and clarity, not authority
- Academic integrity is the highest priority

## Questions?

Open an Issue with tag `question` or start a Discussion.
