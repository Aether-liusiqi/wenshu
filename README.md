# Official Document Writer（公文笔杆子）

**专业中文公文写作 AI Skill** — 覆盖《党政机关公文处理工作条例》（2012）全部 15 种法定公文，严格遵循 GB/T 9704-2012 格式标准，兼容 Claude Code / Codex CLI / OpenClaw / OpenCode 四大 AI Agent 平台。

> **Status:** v1.0.0 Stable — 见 [CHANGELOG.md](CHANGELOG.md) 查看版本历史。

---

## 功能

- **15 种法定文种全覆盖**：决议、决定、命令(令)、公报、公告、通告、意见、通知、通报、报告、请示、批复、议案、函、纪要
- **GB/T 9704-2012 毫米级格式**：版头/主体/版记 18 要素、字体层级"黑一楷二仿三四"、28 磅固定行距
- **语言四准则润色**：准确、简洁、庄重、得体 — 含专用语库、数字规范、名称引用规则
- **结构方法论**：立意三层穿透法 + 总分式/并列式/递进式/对比式四种结构模式
- **错误检测**：文种混淆、格式偏差、语言失范三类自查
- **15 篇标准范文**：每文种一个完整可用的真实范文

---

## 架构

```
official-document-writer/
│
├── SKILL.md                          # 核心 — 角色定义 + 6步工作流 + 15文种速查表
│
├── references/                       # 深度知识库（渐进式披露 Level 3）
│   ├── 01-15-document-types.md       #   15 文种逐一详解与混淆辨析
│   ├── 02-format-standards.md        #   GB/T 9704-2012 格式速查
│   ├── 03-language-style.md          #   语言风格指南 + 专用语库
│   ├── 04-common-errors.md           #   三类常见错误 + 自查清单
│   ├── 05-writing-methodology.md     #   立意·结构·标题·语言写作法
│   └── 06-history.md                 #   三千年公文简史
│
├── examples/                         # 15 篇标准范文（每文种一篇）
│   ├── 通知-年度会议通知.md
│   ├── 报告-年度工作总结.md
│   ├── 请示-项目经费请示.md
│   ├── 函-商洽工作事项.md
│   ├── 纪要-专题会议纪要.md
│   ├── 决定-表彰决定.md
│   ├── 通报-情况通报.md
│   ├── 公告-招标公告.md
│   ├── 通告-交通管制通告.md
│   ├── 意见-指导意见.md
│   ├── 批复-事项批复.md
│   ├── 议案-法规议案.md
│   ├── 决议-会议决议.md
│   ├── 公报-统计公报.md
│   └── 命令-任免命令.md
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
git clone https://github.com/Aether-liusiqi/official-document-writer.git \
  ~/.claude/skills/official-document-writer/

# 或在 Claude Code 中通过 plugin 安装（如果已发布到 marketplace）
# /plugin install official-document-writer@claude-plugins-official
```

### Codex CLI

```bash
# 克隆到 Codex skills 目录
git clone https://github.com/Aether-liusiqi/official-document-writer.git \
  ~/.agents/skills/official-document-writer/

# 确保 skills 功能已启用
# 编辑 ~/.codex/config.toml，添加:
# [features]
# skills = true
```

### OpenClaw

```bash
# 克隆到 OpenClaw skills 目录
git clone https://github.com/Aether-liusiqi/official-document-writer.git \
  ~/.openclaw/skills/official-document-writer/

# 或放入 workspace skills 目录
git clone https://github.com/Aether-liusiqi/official-document-writer.git \
  <workspace>/skills/official-document-writer/
```

### OpenCode

```bash
# 克隆到 OpenCode skills 目录（项目级）
git clone https://github.com/Aether-liusiqi/official-document-writer.git \
  .opencode/skills/official-document-writer/

# 或全局安装
git clone https://github.com/Aether-liusiqi/official-document-writer.git \
  ~/.config/opencode/skills/official-document-writer/
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
