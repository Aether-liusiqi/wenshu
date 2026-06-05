# Changelog

本文件记录 文书（Wenshu）的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)，
本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)。

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

[1.0.0]: https://github.com/Aether-liusiqi/wenshu/releases/tag/v1.0.0
