# CLAUDE.md — CSC 583 (Computer and Information Security) study site

Keep this file up to date whenever structure, conventions, status or commands change.

## What this is
MkDocs Material study site built from `CSC 583 Note3_052848.pdf` (82 pages, 12 units). Follows COURSE_SITE_PLAYBOOK.md, with the CSC 583 overrides in planning/STRUCTURE.md (no outcomes/self-tests in source; **mandatory Recall drill** per unit). Read `HANDOVER.md` for current state.

## Key rules
- Cover everything in the source; restructure freely; tag every section with `<span class="src">§x.y · pp.a–b</span>` (courseware section numbers; heading names where unnumbered).
- Courseware wording for definitions/lists in `>` blockquotes only; extras in "Beyond the notes"; errors in "Courseware note" + planning/ERRATA.md.
- MCQs after each major section (2–3) + mixed review; Recall drill covering every definable/listable item; exam questions per planning/QUESTION_STYLE.md.
- `mkdocs build --strict` and `planning/scripts/audit.py` must be clean.

## Page numbers and unit mapping
No printed page numbers: **all page refs are PDF page indices**. Source has no Chapter 5 and two Chapter 8s.

| Site unit | File | Courseware chapter | PDF pages |
|---|---|---|---|
| 1 | unit-1-security-concepts.md | 1 | 2–14 |
| 2 | unit-2-attacks.md | 2 | 15–19 |
| 3 | unit-3-os-security.md | 3 | 20–22 |
| 4 | unit-4-cryptography.md | 4 | 23–39 |
| 5 | unit-5-firewalls.md | 6 | 40–48 |
| 6 | unit-6-security-policy.md | 7 | 49–51 |
| 7 | unit-7-wireless-mobile.md | 8 (Wireless & Mobile) | 52–54 |
| 8 | unit-8-access-control.md | 8 (Access Control) | 55–58 |
| 9 | unit-9-malware.md | 9 | 59–65 |
| 10 | unit-10-ethics-legal.md | "Unit 10" | 66–71 |
| 11 | unit-11-database-security.md | 11 | 72–75 |
| 12 | unit-12-idps.md | 12 | 76–82 |

The unit list is already in mkdocs.yml nav, build_glossary.py and audit.py. Don't change it unless a unit is split.

## Commands
```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve | .venv/bin/mkdocs build --strict
python3 planning/scripts/build_glossary.py | python3 planning/scripts/audit.py [unit...]
# parallel-safe: build to your own dir and audit it
.venv/bin/mkdocs build --strict -d "$TMPDIR/site-u4" && SITE_DIR="$TMPDIR/site-u4" python3 planning/scripts/audit.py 4
pdftotext -layout -f <first> -l <last> "CSC 583 Note3_052848.pdf" -
```

## Status
- [x] Planning files  - [x] Scaffold  - [x] Unit 1 (reference unit)  - [x] Units 2–12 (all audited clean)
- [x] Glossary (371 terms)  - [x] Exam technique, crash course, 2 mocks  - [x] Cross-unit links upgraded  - [x] Final audit (752 anchors, all clean)  - [x] Git init + first commit  - [x] `site_url` set (https://www.josephalikah.com/security_notes/)  - [ ] Student creates GitHub repo `security_notes`, pushes, enables Pages (Source: GitHub Actions)
