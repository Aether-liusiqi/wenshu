#!/usr/bin/env python3
"""Word export semantic wrapper — delegates to scripts/generate_docx.py.

Usage:
    python renderers/docx.py <input.md> -o <output.docx> [--doc-type <type>]

Examples:
    python renderers/docx.py draft.md -o output.docx --doc-type 通知
    python renderers/docx.py report.md -o report.docx --doc-type 报告
    python renderers/docx.py briefing.md -o briefing.docx --doc-type 简报
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "generate_docx.py"

if __name__ == "__main__":
    if not SCRIPT.exists():
        print(f"错误: 核心脚本不存在: {SCRIPT}")
        sys.exit(1)
    result = subprocess.run(
        [sys.executable, str(SCRIPT)] + sys.argv[1:],
    )
    sys.exit(result.returncode)
