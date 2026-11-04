"""Regenerate docs/glossary.md from each unit's "## Key terms" definition list.
Run from the project root: python3 planning/scripts/build_glossary.py"""
import pathlib, re

UNITS = [  # (number, file) — keep in step with mkdocs.yml
    (1, "unit-1-security-concepts.md"),
    (2, "unit-2-attacks.md"),
    (3, "unit-3-os-security.md"),
    (4, "unit-4-cryptography.md"),
    (5, "unit-5-firewalls.md"),
    (6, "unit-6-security-policy.md"),
    (7, "unit-7-wireless-mobile.md"),
    (8, "unit-8-access-control.md"),
    (9, "unit-9-malware.md"),
    (10, "unit-10-ethics-legal.md"),
    (11, "unit-11-database-security.md"),
    (12, "unit-12-idps.md"),
]

entries = []
for num, fname in UNITS:
    text = pathlib.Path("docs", fname).read_text()
    if "## Key terms" not in text:  # page mid-rewrite
        print("skipped (no Key terms):", fname)
        continue
    block = text.split("## Key terms", 1)[1].split("\n---", 1)[0]
    lines = block.strip("\n").split("\n")
    for i, line in enumerate(lines[:-1]):
        if line.strip() and not line.startswith(":") and lines[i + 1].startswith(":   "):
            entries.append((line.strip(), lines[i + 1][4:].strip(), num, fname))

key = lambda e: re.sub(r"[^a-z0-9]", "", e[0].lower())
entries.sort(key=key)
out = ["# Glossary", "", "Every key term A–Z, linked to its unit. Generated from the units' Key terms lists; do not edit by hand.", ""]
letter = None
for term, definition, num, fname in entries:
    first = key((term,))[:1].upper()
    first = "#" if not first or first.isdigit() else first
    if first != letter:
        letter = first
        out += [f"## {letter}", ""]
    out += [term, f":   {definition} — *[Unit {num}]({fname}#key-terms)*", ""]
pathlib.Path("docs/glossary.md").write_text("\n".join(out))
print(f"{len(entries)} terms written")
