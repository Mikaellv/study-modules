#!/usr/bin/env python3
"""Merge exam-data/*.json into the exam-prep template and write docs/exam-prep.html.

Each exam-data file is one chapter:
{chapter, title, scope?, sections:[{title, keyResults:[{name, latex, note?}]}],
 questions:[{id, tier:"easy"|"hard", type:"mc"|"free", prompt, choices?, answerIndex?, solution, source?}]}
"""
import glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "exam-prep.html")
OUT = os.path.join(ROOT, "docs", "exam-prep.html")
MARK = "/*EXAM_DATA*/"

def fail(msg):
    sys.exit("ERROR: " + msg)

def check_chapter(ch, path):
    for k in ("chapter", "title", "sections", "questions"):
        if k not in ch: fail(f"{path}: missing '{k}'")
    ids = set()
    for q in ch["questions"]:
        qid = q.get("id", "?")
        if qid in ids: fail(f"{path}: duplicate id {qid}")
        ids.add(qid)
        if q.get("tier") not in ("easy", "hard"): fail(f"{path}: {qid} bad tier")
        if q.get("type") not in ("mc", "free"): fail(f"{path}: {qid} bad type")
        if not q.get("prompt") or not q.get("solution"): fail(f"{path}: {qid} missing prompt/solution")
        if q["type"] == "mc":
            c = q.get("choices") or []
            if len(c) < 2 or not isinstance(q.get("answerIndex"), int) or not 0 <= q["answerIndex"] < len(c):
                fail(f"{path}: {qid} bad mc choices/answerIndex")
    return ch

def main():
    files = sorted(glob.glob(os.path.join(ROOT, "exam-data", "*.json")))
    if not files: fail("no exam-data/*.json files")
    chapters = []
    for p in files:
        with open(p, encoding="utf-8") as f:
            chapters.append(check_chapter(json.load(f), p))
    chapters.sort(key=lambda c: int(str(c["chapter"]).split(".")[0]))
    payload = json.dumps(chapters, ensure_ascii=False).replace("</", "<\\/")
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    if MARK not in tpl: fail("template marker missing")
    page = tpl.replace(MARK, payload)
    head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(head + page + "\n</body>\n</html>\n")
    print(f"Built {os.path.relpath(OUT, ROOT)} from {len(chapters)} chapters, "
          f"{sum(len(c['questions']) for c in chapters)} questions")

if __name__ == "__main__":
    main()
