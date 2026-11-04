"""Post-build audit. Run from the project root AFTER `.venv/bin/mkdocs build --strict`:
    python3 planning/scripts/audit.py [unit numbers...]
Set SITE_DIR to audit a build in another directory (e.g. `mkdocs build --strict -d $TMPDIR/site-u4`)."""
import os, pathlib, re, subprocess

PDF = "CSC 583 Note3_052848.pdf"
UNITS = [  # (site unit, courseware chapter, first PDF page, last PDF page, page file). Source has no Chapter 5 and two Chapter 8s.
    (1, "1", 2, 14, "unit-1-security-concepts.md"),
    (2, "2", 15, 19, "unit-2-attacks.md"),
    (3, "3", 20, 22, "unit-3-os-security.md"),
    (4, "4", 23, 39, "unit-4-cryptography.md"),
    (5, "6", 40, 48, "unit-5-firewalls.md"),
    (6, "7", 49, 51, "unit-6-security-policy.md"),
    (7, "8", 52, 54, "unit-7-wireless-mobile.md"),
    (8, "8", 55, 58, "unit-8-access-control.md"),
    (9, "9", 59, 65, "unit-9-malware.md"),
    (10, "10", 66, 71, "unit-10-ethics-legal.md"),
    (11, "11", 72, 75, "unit-11-database-security.md"),
    (12, "12", 76, 82, "unit-12-idps.md"),
]
DOCS, SITE = pathlib.Path("docs"), pathlib.Path(os.environ.get("SITE_DIR", "site"))

def built_page(md):
    rel = md.resolve().relative_to(DOCS.resolve())
    return SITE / (rel.with_suffix(".html") if rel.name == "index.md" else pathlib.Path(str(rel)[:-3]) / "index.html")

def pdf_text(first, last):
    out = subprocess.run(["pdftotext", "-f", str(first), "-l", str(last), PDF, "-"], capture_output=True, text=True).stdout
    return "\n".join(l for l in out.split("\n") if not re.fullmatch(r"\s*\d{1,3}\s*", l))  # drop page footers

# 1. anchors
bad = n = 0
for md in DOCS.rglob("*.md"):
    for target, frag in re.findall(r"\]\(([^)\s]+?\.md)#([^)\s]+)\)", md.read_text()):
        n += 1
        if f'id="{frag}"' not in built_page(md.parent / target).read_text():
            bad += 1
            print("MISSING ANCHOR", md, target, frag)
for md in DOCS.rglob("*.md"):  # same-page links
    for frag in re.findall(r"\]\(#([^)\s]+)\)", md.read_text()):
        n += 1
        if f'id="{frag}"' not in built_page(md).read_text():
            bad += 1
            print("MISSING ANCHOR", md, "#" + frag)
print(f"[anchors] {n} checked, {bad} missing")

import sys
ONLY = {int(x) for x in sys.argv[1:]}
for u, ch, a, b, f in UNITS:
    if ONLY and u not in ONLY:
        continue
    text, page = pdf_text(a, b), (DOCS / f).read_text()
    tags = " ".join(re.findall(r'<span class="src">(.*?)</span>', page))
    # 2. numbers in the source that never appear on the page
    nums = set(re.findall(r"\d[\d,\.]*\d%?|\d%", text))
    flat = page.replace(",", "")
    missing = sorted(x for x in nums if x.replace(",", "").rstrip(".") not in flat)
    # 3. numbered source sections not cited in any source tag
    secs = {s for pair in re.findall(rf"^\s*({ch}\.\d+(?:\.\d+)?)\.?\s*$|^\s*({ch}\.\d+(?:\.\d+)?)\s", text, re.M) for s in pair if s}
    miss_secs = sorted(s for s in secs if not re.search(rf"§{re.escape(s)}(?!\.?\d)", tags))
    # 4. source pages not cited in any source tag
    cited = set()
    for m in re.finditer(r"pp?\.\s*(\d+)(?:\s*[–-]\s*(\d+))?", tags):
        cited.update(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
    miss_pages = [p for p in range(a, b + 1) if p not in cited]
    # 5. collapsibles render; 6. each quiz has exactly one correct option
    src = len(re.findall(r"^\s*\?\?\? ", page, re.M))
    html = built_page(DOCS / f).read_text().count("<details")
    bad_quiz = [i + 1 for i, q in enumerate(page.split('<div class="quiz"')[1:]) if q.split("</ul>")[0].count("data-correct") != 1]
    print(f"[unit {u}] sections not tagged: {miss_secs}; pages not tagged: {miss_pages}; "
          f"collapsibles {src}/{html}; quizzes with != 1 correct: {bad_quiz}; numbers not found: {missing}")
