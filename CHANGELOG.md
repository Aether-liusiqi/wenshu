# Changelog

本文件记录 文书（Wenshu）的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)，
本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

---

## [1.1.1] — 2026-06-06

### Changed
- **SKILL.md 瘦身**：13KB → ~5KB。详细内容按职责拆分为 `prompts/core/` 三个可拼装模块（workflow/guardrails/output-spec），SKILL.md 保留角色定义、底线约束、流程概述和模块指针
- **renderers/ 合并到 scripts/**：删除 renderers/ 薄封装层，Word 导出和结构校验直接调用 scripts/
- **第四步正文撰写约束精确化**：新增 `references/08-language-taboos.md`，定义六类语言禁忌（主观评价词/模糊时间词/绝对化用语/措辞力度错配/事实与研判混淆/自查流程）。workflow.md 的 Step 4 同步更新

### Added
- **`prompts/core/workflow.md`**：6 步完整工作流（含决策树、场景识别路线、语言禁忌引用）
- **`prompts/core/guardrails.md`**：硬性约束 + 语言准则 + 六类语言禁忌三大类红线
- **`prompts/core/output-spec.md`**：格式标准 + 数字规范 + 名称引用 + 22 文种速查表 + 混淆辨析
- **范文写作要点注释**：通知/报告/请示/函/纪要/公告/命令 7 篇范文新增详细写作要点注释段（为什么这样写、哪些地方容易出错、措辞的语境考量）

### Fixed
- **公告范文**信息密度提升：从 1.6KB 扩至含完整写作要点注释
- **命令范文**信息密度提升：从 1.9KB 扩至含完整写作要点注释

---

## [1.1.0] — 2026-06-05

### Added
- **要素分层体系** — 引入五层分类法（必备/常见/条件项/地方或系统样式/项目自定义），替换 v1.0 的平铺式规则罗列。AI 生成公文时按文种和场景按需组合要素，避免"无脑堆砌"所有可能元素。应用于 `references/02-format-standards.md` 全部版头/主体/版记要素
- **7 种事务文书** — 新增 `references/07-formal-materials.md`，覆盖：工作总结、工作方案/实施方案、讲话稿/发言稿、汇报材料、简报/信息简报/新闻简报、情况专报/信息专报/舆情专报、回复函（事务）。每种文种含核心结构、要素分层速查和写作要点
- **事务文书范文（7 篇）** — `examples/事务文书/`：工作总结（年度总结）、工作方案（营商环境方案）、讲话稿（部署讲话）、汇报材料（项目进展）、简报（工作简报）、情况专报（市场供应）、回复函（征求意见回复）
- **Word (.docx) 导出** — `scripts/generate_docx.py` + `renderers/docx.py`：将 Markdown 公文导出为标准 Word 文件。支持双套字体方案（standard/compact）、双套版式方案、A4 页面、仿宋/小标宋/黑体/楷体自动套用、页码/版记/首行缩进/落款格式。依赖 python-docx
- **公文结构自动校验** — `scripts/check_sections.py` + `renderers/validate.py`：按文种自动校验必备章节、标题层级、禁止用语、标准结尾语、发文字号格式、"请示报告"等杂交名称。支持 15 法定公文 + 7 事务文书。纯标准库，零外部依赖
- SKILL.md 能力范围扩展至 9 项，新增工具使用说明
- README 架构图更新至 v1.1，新增 Word 导出与结构校验使用说明

### Changed
- `references/02-format-standards.md` 全部要素表格增加"层级"列
- SKILL.md description 增加事务文书和导出/校验功能
- 范文总数从 15 篇增至 22 篇

---

## [1.0.0] — 2026-06-05

### 首次发布

#### Added
- **SKILL.md** — 核心 Skill 文件，包含完整的角色定义、8 项能力范围、6 步写作流程、输出规范、15 文种速查表、易混淆文种辨析
- **references/ 深度知识库**（6 个文件）：
  - `01-15-document-types.md` — 15 种法定公文按行文方向和功能定位的完整分类，五对经典混淆辨析，文种选择流程图
  - `02-format-standards.md` — GB/T 9704-2012 格式标准速查：三大板块 18 要素、字体层级规则、核心参数表
  - `03-language-style.md` — 语言风格四准则 + 专用语库（开端语/表态语/结尾语）+ 数字使用规范 + 名称引用规范
  - `04-common-errors.md` — 文种/格式/语言三类常见错误 + 15 项自查清单
  - `05-writing-methodology.md` — 立意三层穿透法 + 结构四种模式 + 标题提炼公式 + 五个写作技巧
  - `06-history.md` — 三千年公文简史（甲骨→秦汉→隋唐→明清→民国→建国→2012统一→AI时代）
- **examples/ 范文模板**（15 篇，每文种一篇）：
  - 通知（年度工作会议通知）、报告（年度工作总结）、请示（项目经费请示）
  - 函（商洽工作事项）、纪要（专题会议纪要）、决定（表彰决定）
  - 通报（情况通报）、公告（招标公告）、通告（交通管制通告）
  - 意见（指导意见）、批复（事项批复）、议案（法规议案）
  - 决议（会议决议）、公报（统计公报）、命令（任免命令/法规颁布）
- **README.md** — 项目着陆页：功能列表、架构图、四平台安装指南、设计原则、已知限制
- **CONTRIBUTING.md** — 贡献指南：开发环境搭建、范文贡献规范、PR 流程
- **LICENSE** — MIT 许可，署名 Siqi Liu
- **.gitignore** — 标准排除规则
- **.github/CODEOWNERS** — 代码所有者配置

### Design Decisions
- 采用所有平台的统一标准 `SKILL.md`（YAML frontmatter + Markdown body）
- 遵循渐进式披露架构：Level 1 元数据 → Level 2 SKILL.md → Level 3 references/
- 范文篇幅设计为"可直接复制使用"的完整公文，非示意片段
- 语言风格兼顾 ima 笔记的文学性要求（排比、比喻、古诗词融入）和研究报告的严谨性

---

[1.1.1]: https://github.com/Aether-liusiqi/wenshu/releases/tag/v1.1.1
[1.1.0]: https://github.com/Aether-liusiqi/wenshu/releases/tag/v1.1.0
[1.0.0]: https://github.com/Aether-liusiqi/wenshu/releases/tag/v1.0.0
