# PaperCraft（academic-paper-skill）

<p align="center">
  <img src="https://img.shields.io/badge/version-0.2.0-blue" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/modules-7-orange" alt="modules">
</p>

面向 AI Agent 的**学术论文全流程技能包**：选题与问题界定、文献检索与综述、研究设计、IMRaD 写作、引用格式。支持 **英文 SCI** 与 **中文硕博论文** 场景。

[English](./README.md) | 简体中文

---

## 安装

```bash
git clone https://github.com/kimogrant/academic-paper-skill.git
cd academic-paper-skill
chmod +x skill.sh
./skill.sh install /path/to/your/project
```

安装路径：`your-project/.cursor/skills/academic-paper-skill/`（须包含 `references/`）。

重载 Cursor 后使用 **`/academic-paper-skill`**（显示名：**PaperCraft**）。

---

## 模块

| # | 内容 |
|---|------|
| 1 | 研究问题、创新点、开题框架 |
| 2 | 文献检索（PICO/PRISMA）、综述大纲、CNKI 场景 |
| 3 | 研究方法、样本、伦理、报告规范 |
| 4 | IMRaD 各节 + 硕博章节映射 |
| 5 | APA / IEEE / GB/T 7714、BibTeX 整理 |
| 6 | 投稿信、Highlights、审稿意见逐条回复（修回） |
| 7 | 学位论文结构、开题/中期、答辩 PPT、答辩 Q&A |

模板在 `references/module-*.md`，由 Agent **按需加载**，勿一次读入全部。

可选：`python scripts/validate_bibtex.py refs.bib` 检查 BibTeX 字段与重复 key。

---

## 学术诚信

- **HALT**：代写可提交全文、编造数据/引用、规避查重 → 仅输出拒绝说明与允许的重定向  
- **Pre-Action**：每模块先核对清单，缺信息则停止生成  
- **引用**：无 DOI/PMID 等可核实来源 → 标注 `[VERIFY]`，禁止伪造  

详见 `references/integrity-boundaries.md`

**允许：** 在你提供选题/数据/文献的前提下，做大纲、结构、语言润色、检索式、格式转换。

---

## 中英文怎么用？

| 项目 | 说明 |
|------|------|
| Skill 本体 | 英文（与 Agent 指令一致） |
| 生成正文 | 默认英文；说明「中文」「学位论文」则输出简体中文 |
| 引用格式 | 英文期刊常用 APA/IEEE；中文论文常用 GB/T 7714 |

---

## 示例

- [`examples/1-literature-review-outline.md`](examples/1-literature-review-outline.md) — 文献综述大纲  
- [`examples/2-imrad-introduction.md`](examples/2-imrad-introduction.md) — Introduction（CARS）
- [`examples/3-revision-response.md`](examples/3-revision-response.md) — 审稿意见回复
- [`examples/4-defense-slides-outline.md`](examples/4-defense-slides-outline.md) — 博士答辩 PPT 大纲

---

## 版本

当前 **0.2.0**（见 `VERSION`）：7 个模块（含投稿修回、学位论文与答辩）、诚信闸门、双语输出规则。

---

## 免责声明

仅供学术写作辅助，不能替代导师、编辑与同行评议。作者须对原创性、准确性与院校 AI 使用规定负责。

MIT · [LICENSE](LICENSE)
