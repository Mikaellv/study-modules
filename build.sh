#!/usr/bin/env bash
# Wraps the artifact page sources into standalone HTML documents in docs/
# (docs/ can be served directly with GitHub Pages).
set -euo pipefail
cd "$(dirname "$0")"
for f in git-basics.html sql-basics.html; do
  {
    printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    printf '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    printf '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%%}[hidden]{display:none!important}</style>\n'
    printf '</head>\n<body>\n'
    cat "$f"
    printf '\n</body>\n</html>\n'
  } > "docs/$f"
done
python3 scripts/build_exam.py
echo "Built docs/git-basics.html, docs/sql-basics.html and docs/exam-prep.html"
