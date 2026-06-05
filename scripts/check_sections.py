#!/usr/bin/env python3
"""Structure validator for Chinese official documents (公文结构校验器).

Checks Markdown documents against structure requirements defined per document type.
Pure stdlib, no dependencies beyond Python 3.11+.
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# ── Required sections per document type ──────────────────────────
# Each entry: (section_pattern, description, is_required: bool)
# Patterns are regex matched against heading text (##-level)

DOC_TYPE_RULES: dict[str, dict] = {
    "通知": {
        "required_sections": [
            (r"标题", "公文标题", True),
            (r"(正文|主体)", "正文", True),
        ],
        "common_sections": [
            (r"(主送|主送机关)", "主送机关", False),
            (r"(附件|附件说明)", "附件说明", False),
        ],
        "forbidden_patterns": [
            (r"请示", "通知中不可出现'请示'字样（该用请示的场景换文种）"),
            (r"妥否.*批复", "结尾语'妥否请批复'仅限请示使用"),
        ],
        "expected_endings": [(r"特此通知", "通知标准结尾语")],
    },
    "报告": {
        "required_sections": [
            (r"标题", "公文标题", True),
            (r"(正文|主体|基本情况|工作)", "正文", True),
        ],
        "common_sections": [
            (r"(主送|主送机关)", "主送机关", False),
        ],
        "forbidden_patterns": [
            (r"请示", "报告中不得夹带请示事项"),
            (r"妥否.*批复", "报告结尾语为'特此报告'，非'妥否请批复'"),
        ],
        "expected_endings": [(r"特此报告", "报告标准结尾语")],
    },
    "请示": {
        "required_sections": [
            (r"标题", "公文标题", True),
            (r"(正文|主体|背景|理由|申请)", "正文（含申请理由）", True),
            (r"(妥否.*批复|以上请示|恳请|拟请)", "请示结尾语", True),
        ],
        "common_sections": [
            (r"(主送|主送机关)", "主送机关", False),
            (r"(附件|附件说明|概算|测算)", "附件或经费概算", False),
        ],
        "forbidden_patterns": [
            (r"特此报告", "请示不可用'特此报告'结尾"),
            (r"特此通知", "请示不可用通知结尾语"),
        ],
        "expected_endings": [(r"妥否.*批复", "请示标准结尾语")],
    },
    "函": {
        "required_sections": [
            (r"标题", "公文标题", True),
            (r"(正文|主体|商请|商洽|函请|回复)", "正文", True),
        ],
        "forbidden_patterns": [
            (r"妥否.*批复", "函不可用请示结尾语"),
            (r"特此通知", "函不可用通知结尾语"),
            (r"请认真贯彻执行", "平级不可用指令性措辞"),
        ],
        "expected_endings": [
            (r"(请函复|特此函复|请予支持为盼|特此函告)", "函标准结尾语"),
        ],
    },
    "纪要": {
        "required_sections": [
            (r"标题", "纪要标题", True),
            (r"(会议|听取|指出|决定|议定)", "会议内容记载", True),
        ],
        "forbidden_patterns": [
            (r"妥否.*批复", "纪要不用请示结尾语"),
            (r"请认真贯彻执行", "纪要一般不发号施令（以'会议要求''会议强调'代替）"),
        ],
    },
}

# Extended rules for事务文书
MATERIAL_TYPE_RULES: dict[str, dict] = {
    "工作总结": {
        "required_sections": [
            (r"(成绩|成效|工作|进展)", "工作成绩部分", True),
            (r"(问题|不足|困难|挑战)", "存在问题部分", True),
            (r"(打算|计划|安排|思路)", "下步打算部分", True),
        ],
    },
    "工作方案": {
        "required_sections": [
            (r"(目标|总体)", "目标设定部分", True),
            (r"(任务|措施|重点)", "任务措施部分", True),
            (r"(保障|组织|考核)", "保障措施部分", True),
        ],
    },
    "讲话稿": {
        "common_sections": [
            (r"(同志们|各位|大家好)", "开场问候", False),
        ],
    },
    "简报": {
        "required_sections": [
            (r"(导语|正文|主体)", "简报正文", True),
        ],
    },
    "情况专报": {
        "required_sections": [
            (r"(基本情况|事件|概述)", "事实描述部分", True),
            (r"(研判|分析|判断|趋势)", "趋势研判部分", True),
            (r"(建议|对策|措施)", "工作建议部分", True),
        ],
    },
}


@dataclass
class ValidationIssue:
    severity: str  # "error", "warning", "info"
    section: str
    message: str


@dataclass
class ValidationReport:
    doc_type: str
    file_path: str
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def error_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "warning")

    @property
    def passed(self) -> bool:
        return self.error_count == 0


def load_markdown(filepath: str) -> str:
    """Read a Markdown file and return its content."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {filepath}")
    return path.read_text(encoding="utf-8")


def extract_headings(text: str) -> list[tuple[int, str]]:
    """Extract all headings with their levels. Returns list of (level, text)."""
    headings = []
    for line in text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if m:
            level = len(m.group(1))
            heading_text = m.group(2).strip()
            headings.append((level, heading_text))
    return headings


def get_rules_for_doc_type(doc_type: str) -> dict:
    """Get validation rules for a given document type."""
    # Check exact match first
    if doc_type in DOC_TYPE_RULES:
        return DOC_TYPE_RULES[doc_type]
    if doc_type in MATERIAL_TYPE_RULES:
        return MATERIAL_TYPE_RULES[doc_type]

    # Fuzzy match
    for key in {**DOC_TYPE_RULES, **MATERIAL_TYPE_RULES}:
        if key in doc_type or doc_type in key:
            return {**DOC_TYPE_RULES, **MATERIAL_TYPE_RULES}[key]

    return {}


def validate(text: str, doc_type: str) -> ValidationReport:
    """Validate a document's structure against rules for its type."""
    report = ValidationReport(doc_type=doc_type, file_path="")
    rules = get_rules_for_doc_type(doc_type)
    headings = extract_headings(text)
    heading_texts = [h[1] for h in headings]
    full_text_lower = text.lower()

    if not rules:
        report.issues.append(ValidationIssue(
            "warning", "文种识别",
            f"未找到'{doc_type}'的校验规则，仅做基础检查"
        ))

    # Check if there's at least one heading (acts as title)
    has_any_heading = len(headings) > 0

    # Check required sections
    for pattern, description, required in rules.get("required_sections", []):
        found = any(re.search(pattern, h) for h in heading_texts)
        if not found:
            # Also search in full text
            found = bool(re.search(pattern, text))
        # Special case: "标题" requirement is satisfied by any h1 heading
        if not found and pattern == r"标题" and has_any_heading and any(h[0] == 1 for h in headings):
            found = True
        if not found and required:
            report.issues.append(ValidationIssue(
                "error", description,
                f"缺少必备章节: {description}"
            ))
        elif not found and not required:
            report.issues.append(ValidationIssue(
                "info", description,
                f"建议补充常见章节: {description}"
            ))

    # Check forbidden patterns
    for pattern, reason in rules.get("forbidden_patterns", []):
        if re.search(pattern, text):
            report.issues.append(ValidationIssue(
                "error", "内容检查",
                f"发现禁止内容: {reason}"
            ))

    # Check expected endings
    for pattern, description in rules.get("expected_endings", []):
        # Search last 200 chars
        tail = text[-300:] if len(text) > 300 else text
        if not re.search(pattern, tail):
            report.issues.append(ValidationIssue(
                "warning", "结尾检查",
                f"未检测到标准结尾语: {description}"
            ))

    # ── Universal checks ──
    # Heading level continuity
    prev_level = 0
    for level, h_text in headings:
        if level > prev_level + 1:
            report.issues.append(ValidationIssue(
                "warning", "标题层级",
                f"标题层级跳跃: 从 H{prev_level} 跳至 H{level}（'{h_text}'）"
            ))
        prev_level = level

    # Check for six-angle bracket in document number patterns
    doc_num_pattern = r"[〔［\[](\d{4})[〕］\]]"
    doc_nums = re.findall(doc_num_pattern, text)
    if doc_nums:
        # Check if they use proper six-angle brackets
        bad_brackets = re.findall(r"[［\[]\d{4}[］\]]", text)
        if bad_brackets:
            report.issues.append(ValidationIssue(
                "error", "发文字号",
                "发文字号年份必须使用六角括号〔〕，当前使用了错误括号"
            ))

    # Check for "请示报告" hybrid
    if "请示报告" in text:
        report.issues.append(ValidationIssue(
            "error", "文种标识",
            "标题中出现'请示报告'这一杂交名称——请示和报告是两种不同文种，不可混用"
        ))

    return report


def format_report(report: ValidationReport) -> str:
    """Format a validation report for terminal output."""
    lines = []
    lines.append(f"\n{'='*60}")
    lines.append(f"  公文结构校验报告")
    lines.append(f"  文种: {report.doc_type}")
    lines.append(f"  文件: {report.file_path}")
    lines.append(f"{'='*60}")

    if not report.issues:
        lines.append("  [OK] 未发现问题")
    else:
        for issue in report.issues:
            icon = {"error": "[ERR]", "warning": "[WARN]", "info": "[INFO]"}.get(issue.severity, "[?]")
            lines.append(f"  {icon} [{issue.severity.upper()}] {issue.section}")
            lines.append(f"    {issue.message}")

    lines.append(f"{'='*60}")
    lines.append(f"  结果: {report.error_count} 个错误, {report.warning_count} 个警告")
    lines.append(f"  判定: {'[OK] 通过' if report.passed else '[FAIL] 不通过'}")
    lines.append(f"{'='*60}\n")
    return "\n".join(lines)


def main():
    # Force UTF-8 output on Windows
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if len(sys.argv) < 2:
        print("用法: python check_sections.py <文种> <文件路径>")
        print("示例: python check_sections.py 通知 ./drafts/notice.md")
        print()
        print("支持的文种:")
        for k in {**DOC_TYPE_RULES, **MATERIAL_TYPE_RULES}:
            print(f"  - {k}")
        sys.exit(1)

    doc_type = sys.argv[1]
    filepath = sys.argv[2] if len(sys.argv) > 2 else None

    if not filepath:
        print("请指定要校验的文件路径")
        sys.exit(1)

    try:
        text = load_markdown(filepath)
    except FileNotFoundError as e:
        print(f"错误: {e}")
        sys.exit(1)

    report = validate(text, doc_type)
    report.file_path = filepath
    print(format_report(report))
    sys.exit(0 if report.passed else 1)


if __name__ == "__main__":
    main()
