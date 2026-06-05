# 文书（Wenshu）— 公文笔杆子

**专业中文公文写作 AI Skill** — 覆盖《党政机关公文处理工作条例》（2012）全部 15 种法定公文和 7 种常用事务文书，严格遵循 GB/T 9704-2012 格式标准，支持 Word (.docx) 导出和公文结构自动校验，兼容 Claude Code / Codex CLI / OpenClaw / OpenCode 四大 AI Agent 平台。

> **Status:** v1.1.0 Stable — 见 [CHANGELOG.md](CHANGELOG.md) 查看版本历史。

---

## 功能

- **15 种法定文种全覆盖**：决议、决定、命令(令)、公报、公告、通告、意见、通知、通报、报告、请示、批复、议案、函、纪要
- **7 种事务文书**：工作总结、工作方案、讲话稿、汇报材料、简报、情况专报、回复函
- **要素分层体系**：必备/常见/条件项/地方样式/项目自定义 — 五层分类，按需组合，避免无脑堆砌
- **GB/T 9704-2012 毫米级格式**：版头/主体/版记 18 要素、字体层级"黑一楷二仿三四"、28 磅固定行距
- **语言四准则润色**：准确、简洁、庄重、得体 — 含专用语库、数字规范、名称引用规则
- **结构方法论**：立意三层穿透法 + 总分式/并列式/递进式/对比式四种结构模式
- **错误检测**：文种混淆、格式偏差、语言失范三类自查 + 自动化结构校验脚本
- **22 篇标准范文**：15 法定公文 + 7 事务文书，均完整可用
- **Word (.docx) 导出**：Markdown → 标准 Word，自动套用字体和版式方案（A4/仿宋/小标宋/页码/版记）

---

## 架构

```
wenshu/
│
├── SKILL.md                          # 核心 — 角色定义 + 6步工作流 + 速查表
│
├── references/                       # 深度知识库（渐进式披露 Level 3）
│   ├── 01-15-document-types.md       #   15 文种逐一详解与混淆辨析
│   ├── 02-format-standards.md        #   GB/T 9704-2012 格式速查 + 要素分层
│   ├── 03-language-style.md          #   语言风格指南 + 专用语库
│   ├── 04-common-errors.md           #   三类常见错误 + 自查清单
│   ├── 05-writing-methodology.md     #   立意·结构·标题·语言写作法
│   ├── 06-history.md                 #   三千年公文简史
│   ├── 07-formal-materials.md        #   7 种事务文书详解
│   └── 08-language-taboos.md         #   公文语言禁忌清单
│
├── examples/                         # 22 篇标准范文
│   ├── 通知/报告/请示/函/纪要/       #   15 法定公文
│   ├── 决定/通报/公告/通告/意见/
│   ├── 批复/议案/决议/公报/命令/
│   └── 事务文书/                     #   7 事务文书
│       ├── 工作总结/工作方案/讲话稿/
│       ├── 汇报材料/简报/情况专报/回复函/
│
├── scripts/                          # Python 工具
│   ├── generate_docx.py              #   Word (.docx) 导出引擎
│   └── check_sections.py             #   公文结构校验引擎
│
├── prompts/                          # Prompt 模块（可拼装）
│   └── core/                         #   核心模块
│       ├── workflow.md               #   6 步写作工作流
│       ├── guardrails.md             #   硬性约束 + 语言准则 + 禁忌
│       └── output-spec.md            #   格式标准 + 文种速查表
│
├── README.md                         # 本文件
├── CHANGELOG.md                      # 版本记录
├── CONTRIBUTING.md                   # 贡献指南
└── LICENSE                           # MIT
```

---

## 快速安装

### Claude Code

```bash
# 克隆到 Claude Code skills 目录
git clone https://github.com/Aether-liusiqi/wenshu.git \
  ~/.claude/skills/wenshu/

# 或在 Claude Code 中通过 plugin 安装（如果已发布到 marketplace）
# /plugin install wenshu@claude-plugins-official
```

### Codex CLI

```bash
# 克隆到 Codex skills 目录
git clone https://github.com/Aether-liusiqi/wenshu.git \
  ~/.agents/skills/wenshu/

# 确保 skills 功能已启用
# 编辑 ~/.codex/config.toml，添加:
# [features]
# skills = true
```

### OpenClaw

```bash
# 克隆到 OpenClaw skills 目录
git clone https://github.com/Aether-liusiqi/wenshu.git \
  ~/.openclaw/skills/wenshu/

# 或放入 workspace skills 目录
git clone https://github.com/Aether-liusiqi/wenshu.git \
  <workspace>/skills/wenshu/
```

### OpenCode

```bash
# 克隆到 OpenCode skills 目录（项目级）
git clone https://github.com/Aether-liusiqi/wenshu.git \
  .opencode/skills/wenshu/

# 或全局安装
git clone https://github.com/Aether-liusiqi/wenshu.git \
  ~/.config/opencode/skills/wenshu/
```

---

## 快速使用

安装后，直接用中文描述你的公文写作需求：

```
帮我写一份关于组织年度工作会议的通知

我们单位需要向市财政局申请一笔专项经费

这份请示的格式帮我检查一下

"公告"和"通告"有什么区别？我应该用哪个？
```

Skill 会自动识别场景、选择文种、按规范撰写或检查。

---

## Word 导出与结构校验

### Markdown → Word (.docx)

```bash
# 安装依赖
pip install python-docx

# 导出为 Word（自动套用 A4/仿宋/小标宋体/页码/版记）
python scripts/generate_docx.py draft.md -o output.docx --doc-type 通知
```

### 公文结构校验

```bash
# 无外部依赖，Python 3.11+ 标准库即可
python scripts/check_sections.py 通知 draft.md
```

---

## 设计原则

- **渐进式披露。** 核心 Prompt（SKILL.md）控制在适合 Level 2 加载的长度，深度知识按需从 references/ 调取。
- **精确优先于华丽。** 公文写作的最高境界不是文采斐然，而是在有限篇幅内让所有执行者准确理解且无歧义。
- **以条例为唯一权威。** 一切写作规范以《党政机关公文处理工作条例》（中办发〔2012〕14号）和 GB/T 9704-2012 为准。
- **四平台通用。** 不依赖任何平台特有功能。SKILL.md 的 YAML frontmatter 与四大平台完全兼容。
- **范文真实可用。** 15 篇范文均基于真实公文场景撰写，可直接使用，非示意性片段。

---

## 已知限制

- **政策判断不可替代。** 本 Skill 能生成格式正确、语言得体的公文草稿，但政策分寸、多部门利益平衡、同级单位微妙措辞仍需人工判断。AI 可替代公文写作"格式层面"的 90%，剩余 10% 是人的核心价值。
- **范文中的单位名称、人名、数据均为示例**，使用时替换为真实信息。
- **不提供法律意见。** 公文内容的法律后果由起草者承担。
- **15 种文种中，命令(令)、公报、决议的使用频率较低**，对应的范文主要为格式参考。

---

## 要求

- 支持 Markdown 渲染的任何 AI Agent 平台
- 无外部依赖（纯 Markdown + YAML）

---

## 许可

MIT — 见 [LICENSE](LICENSE) 全文。

Copyright (c) 2026 Siqi Liu
