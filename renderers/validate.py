#!/usr/bin/env python3
"""Structure validation semantic wrapper — delegates to scripts/check_sections.py.

Usage:
    python renderers/validate.py <doc_type> <file.md>

Examples:
    python renderers/validate.py 通知 ./drafts/notice.md
    python renderers/validate.py 请示 ./drafts/request.md
    python renderers/validate.py 简报 ./drafts/briefing.md
"""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "check_sections.py"

if __name__ == "__main__":
    if not SCRIPT.exists():
        print(f"错误: 核心脚本不存在: {SCRIPT}")
        sys.exit(1)
    result = subprocess.run(
        [sys.executable, str(SCRIPT)] + sys.argv[1:],
    )
    sys.exit(result.returncode)
