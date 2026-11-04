# Course study-site playbook

A brief for a Claude session that turns a course's lecture material into a study website. It was distilled from building the CSC 584 (ICT for Development) site, and it is written for **essay/theory courses**: definitions, lists, cases and scenario questions.

**How to use it:** put this file in an empty project folder next to the course material, and tell Claude: *"Read COURSE_SITE_PLAYBOOK.md and build the study site for this course."* Claude should follow it from Phase 0.

---

## 1. Goal and non-negotiables

Build a MkDocs Material site that lets the student learn the **whole** course and prepare for its essay exam.

1. **Cover everything in the source.** Every heading, list item, example, statistic, case, person, figure and table must appear somewhere on the site. Lists keep their **full count**. Summaries are extra, never a replacement. Coverage is proven by the coverage map and the audit script (§7).
2. **Restructure freely for understanding.** Within a unit you may reorder, merge or split sections, put a concept before the case that uses it, and write your own explanations. The courseware's order is not sacred; its **content** is.
3. **Keep the examinable wording.** Definitions, named lists and anything the examiner is likely to quote stay in the **courseware's exact words** in a `>` blockquote. Everything else can be your own explanation.
4. **Tag every block of content with its source** (§4.3), so restructuring never loses traceability.
5. **Mix the MCQs through the unit**, after each major section, plus a short mixed review at the end (§5.1).
6. **Clearly separate what is not from the courseware.** Extras go only in `!!! info "Beyond the notes"`, examples in `!!! example`. Courseware errors are flagged, never silently fixed (§4.4).
7. **Put answers on the same page**, in collapsed `??? success "Model answer"` boxes.
8. **`mkdocs build --strict` must pass** with no warnings, and the audit must be clean before a unit counts as done.
9. **Keep `CLAUDE.md` and `HANDOVER.md` current**, so any session (or one starting after a context reset) can pick up where the last one left off.

---

## 2. Workflow

### Phase 0: intake (ask the student before writing anything)

Ask these in one batch, and record the answers in `planning/PLAN.md`:

1. **Source files:** which files are the course material? Are there past papers or sample questions? Ask for photos of real exam papers; they set the question style.
2. **Exam format:** duration, how many questions to attempt, marks per question, part structure (a/b/c), and whether there is a scenario part. Defaults from CSC 584 (University of Ibadan): 2 hours, attempt any 3 of about 6, parts a/b/c totalling about 20 marks, part (c) a scenario needing justification.
3. **Difficulty:** recall, or application and justification? (CSC 584's student wanted "a bit challenging": scenarios and justification.)
4. **Local context:** a country or region for examples (CSC 584 used Nigerian examples, always inside Example or Beyond boxes).
5. **Hosting:** GitHub Pages? Repo name and custom domain? Should the course material be kept out of the public repo? (Default: yes.)
6. **Anything to do differently** from this playbook.

### Phase 1: read the source and plan

1. Extract the text: `pdftotext -f <first> -l <last> "<course>.pdf" -`. Check that the printed page number matches the PDF page index; if it doesn't, record the offset in `CLAUDE.md`.
2. Find the figures: `pdfimages -list -f <first> -l <last> "<course>.pdf"`. Then view figure pages as images with the Read tool and its `pages` parameter. Don't trust a table of contents to say which figures exist.
3. Write the planning files in `planning/` (§3). The most important is **`CONTENT_MAP.md`**: one checkbox row per source section, listing every item with its count and page.
4. While reading, log every courseware error or inconsistency in `ERRATA.md` (§4.4). In particular, compare **learning outcomes vs section contents vs self-test questions**: their counts often disagree ("six challenges" when five are listed).

### Phase 2: scaffold

Create the files in §8: `mkdocs.yml`, `requirements.txt`, the quiz JS/CSS, `extra.css`, the scripts, the deploy workflow and `.gitignore`. Write `docs/index.md` from the course's general introduction, which is content too and must be covered. Set up the venv and check that the strict build passes.

### Phase 3: write units, one at a time

For each unit:

1. Re-read the unit's source pages in full. Don't rely on the content map alone.
2. Design the unit's structure: the order that makes the ideas easiest to learn (§4.1). Note in the content map where each source section now lives.
3. Write the page (§4), with MCQs after each major section (§5.1).
4. Draw the diagrams (§6).
5. Run `mkdocs build --strict`, then the audit (`python3 planning/scripts/audit.py`). Fix everything it reports, or confirm each leftover by hand.
6. Visually check the built page (§7.3), especially scenario questions, nested lists, Mermaid diagrams and SVGs.
7. Tick the content map, update the status in `CLAUDE.md`, and update `HANDOVER.md`.

**After Unit 1, stop and ask the student to review** its depth, tone, MCQ density and question difficulty before writing the rest. Unit 1 becomes the reference unit.

### Phase 4: course-wide pages

1. **Glossary:** generated from every unit's Key terms by `build_glossary.py`. Never edit it by hand.
2. **Exam technique:** the paper format and time plan; what each command word asks for; the scenario method (I-A-J-A, §5.4); diagrams worth practising (with links); a table of questions whose counts don't match the courseware; high-yield lists with their counts; memory aids; common mistakes; a 7-day revision plan.
3. **Two mock exams:** full papers in the real format, mixing units, with model answers and marking points.
4. **Crash course:** a one-page cheatsheet, described in §5.5.

### Phase 5: final audit and hosting

1. Run the audit over all units. Every section and every page must be cited, all anchors must resolve, and all collapsibles must render (§7).
2. `git init`, commit, push; the workflow deploys to GitHub Pages (§8.7).

### Working across sessions

A long course won't fit in one context window. Before stopping, or when context is getting long, update `HANDOVER.md` with:
- what is done;
- what is next;
- the exact workflow;
- the lessons learned so far.

A fresh session should be able to continue from `CLAUDE.md` and `HANDOVER.md` alone.

---

## 3. Project layout

```
<project>/
  CLAUDE.md                 # rules, commands, gotchas, status (kept current)
  HANDOVER.md               # state of work, next steps, lessons learned
  README.md                 # minimal: what it is, live URL, how to run
  <course>.pdf              # source (git-ignored if the repo is public)
  pq*.jpg                   # past papers (git-ignored)
  mkdocs.yml
  requirements.txt
  .github/workflows/deploy.yml
  planning/                 # not built into the site
    PLAN.md                 # goal, intake answers, decisions
    STRUCTURE.md            # page template and markup conventions (copy §4–§6)
    CONTENT_MAP.md          # coverage checklist: every source item → where it lives
    QUESTION_STYLE.md       # the real exam's format + how site questions are written
    ERRATA.md               # courseware errors and how the site handles them
    scripts/build_glossary.py
    scripts/audit.py
  docs/
    index.md                # course introduction + unit table + how to use the site
    unit-N-<slug>.md        # one page per unit
    glossary.md             # generated
    exam/exam-technique.md
    exam/crash-course.md
    exam/mock-exam-1.md
    exam/mock-exam-2.md
    assets/diagrams/uN-<name>.svg
    javascripts/quiz.js
    stylesheets/extra.css
    stylesheets/quiz.css
```

**`CONTENT_MAP.md` row format.** Add a "lives in" note once the unit is written:

```markdown
- [x] 3.4 How to use the model (4 steps): thematic analysis; rate each dimension 0–10; add up; interpret with Table 3.1 (5 bands) (pp.36–37) → "Scoring a project" section
```

**`ERRATA.md` format:** `| # | Where | Issue | How the site handles it |`.

---

## 4. Unit page template

### 4.1 Order of a unit page

1. `# Unit N: <title>`, then a one-line italic source note: `*Courseware pages 31–38.*`
2. **At a glance:** what the unit answers, in 3–6 lines, plus a small concept map (Mermaid, branch names only) or a table.
3. **Learning outcomes:** verbatim from the courseware, with a source tag. If they don't match the content or the self-test, add a Courseware note directly below.
4. **The teaching sections**, ordered for understanding. You may:
    - put foundational definitions first, and cases after the concepts they illustrate;
    - merge a short section into a related one, or split a long one;
    - group parallel items (e.g. the four e-government types) into one comparison table;
    - add bridging paragraphs that connect sections, or link to other units.

    Each section contains:
    - a **source tag** (§4.3);
    - the **courseware wording** for definitions and lists, in `>` blockquotes, complete;
    - an **explanation** in plain language, with an analogy or a local example where it helps;
    - a **diagram or table** where a picture helps (§6);
    - `!!! tip "Exam angle"`: how the point is likely to be examined;
    - **Check your understanding:** 2–3 MCQs on that section (§5.1).
5. **Key terms:** a definition list (`Term` / `:   definition`) ending with `---`. The glossary script reads it, so keep that exact format.
6. **Unit summary:** a dense recap, *after* the full content.
7. **Mixed review:** 3–5 MCQs that connect sections or contrast neighbouring concepts.
8. **Self-test assessment (from the courseware):** the courseware's questions verbatim, each with a model answer.
9. **Practice exercises:** short tasks (classify these, fill a comparison table, draw and label, a mini-calculation), with reveal answers.
10. **Sample exam questions:** 3–4 full questions in the real exam's format, with model answers and marking points (§5.2).

A very long unit may be split into sub-pages (`docs/unit-6/e-health.md`, …). Update the nav and the audit's unit list if so.

### 4.2 Admonitions

| Purpose | Syntax |
|---|---|
| Plain explanation | `!!! note "In plain terms"` |
| Example (local examples go here) | `!!! example "Example"` |
| Likely exam point | `!!! tip "Exam angle"` |
| Not from the courseware | `!!! info "Beyond the notes"` |
| Courseware error | `!!! warning "Courseware note"` |
| Revealed answer | `??? success "Model answer"` (collapsed) |
| Cheatsheet traps | `!!! danger "Traps"` |

**Blockquotes (`>`) are reserved for courseware wording.** Never put a paraphrase in one.

### 4.3 Source tags

Put a source tag on its own line directly under each section heading, and under any block whose content comes from elsewhere in the source:

```markdown
## Scoring a project with the DRG model

<span class="src">§3.4 · pp.36–37</span>
```

Formats:

- several sections: `§3.1, §3.3 · pp.32–35`;
- a figure or table: `§3.4 · Table 3.1 · p.37`;
- an unnumbered part of the source: `Introduction · p.31`.

The audit uses these tags to prove that every numbered source section and every page appears on the unit's page. Tags are small and grey (`.src` in `extra.css`).

### 4.4 Courseware errors

Teach the courseware's version, because it is what the examiner set and marks against. Add a `!!! warning "Courseware note"` that explains the problem and gives the clearer version, and log it in `ERRATA.md`. Common kinds of error:

- count mismatches (an outcome asks for "ten" but nine are listed);
- garbled or pasted-in text;
- sentences that are cut off;
- empty headings or outcomes;
- references to figures that don't exist;
- typos in names.

When you complete a cut-off thought, say it is an inference.

---

## 5. Questions

### 5.1 MCQs, mixed through the unit

- **Purpose:** point out key facts and catch misunderstandings. They are not a mock exam.
- **Placement:** after each major teaching section, add **2–3 MCQs** under a bold label line, `**Check your understanding**`. Don't use a heading: it would clutter the table of contents.
- At the end of the unit, add a **Mixed review** of 3–5 MCQs that cross sections, e.g. "which of these is G2G, not G2B?"
- **Total:** roughly 15–20 per unit.
- Each MCQ has one correct option and **plausible distractors** taken from neighbouring concepts.
- The explanation says **why the right answer is right and why the tempting wrong one is wrong**, and names the section.
- The quiz script numbers the quizzes on a page automatically, so they can be placed anywhere.

```html
<div class="quiz" markdown>
<p class="quiz-q">Which statement best describes the relationship between IT and ICT?</p>
<ul class="quiz-options">
  <li>ICT is a subset of IT</li>
  <li data-correct>IT is a subset of ICT</li>
  <li>They are unrelated</li>
  <li>They mean exactly the same thing</li>
</ul>
<div class="quiz-explain" markdown>
IT manages information technologies (hardware, software, networking) and excludes telecommunications; ICT includes telecommunications too. So IT is a subset of ICT (§1.2).
</div>
</div>
```

### 5.2 Exam questions

Write them in the real exam's shape (record it in `QUESTION_STYLE.md` from the past papers). For a UI-style essay paper, that means:

- Parts **a, b, c** (optionally d), with marks shown as `<span class="marks">(6 marks)</span>`, totalling about **20 marks**.
- **At least half the marks need application, comparison or justification**, not just recall.
- A comparison names its criteria ("differentiate X and Y in terms of A, B and C").
- "Explain" rather than "list".
- **A scenario part in every question**, usually (c): a believable local case where the student must identify, classify, rate, recommend and **justify**, including why not the alternatives.
- Use the course's numbers, tables and scoring schemes in the questions (e.g. give a project description and ask for a framework score).

Model answers are written as a strong student would write them:
- a short definition first;
- then points, each with a **bold heading** and 1–3 sentences;
- examples where the question asks for application;
- **Marking points** at the end that add up to the marks.

```markdown
**1b.** Differentiate between waterfall and agile in terms of sequencing, handling of change and customer involvement. <span class="marks">(8 marks)</span>

??? success "Model answer"
    | Criterion | Waterfall | Agile |
    |---|---|---|
    | **Sequencing (2)** | … | … |

    **Marking points:** each criterion compared (2 × 3); explanation of "tames the change" (2).
```

**Before you write a scenario question**, see the formatting traps in §9: a bullet list followed by a numbered list merges into one list.

### 5.3 Practice exercises

These are short, varied tasks, each with a reveal answer:
- classify examples;
- fill in a comparison table;
- draw and label a diagram;
- a mini-calculation, such as a framework score;
- explain a term in your own words.

### 5.4 Scenario method (teach it on the exam-technique page)

**I-A-J-A:**
1. **Identify** the concept being tested.
2. **Apply** it to the scenario's facts, quoting them.
3. **Justify** with the courseware's evidence or case.
4. **Act:** make a recommendation, and say why it beats the alternatives.

### 5.5 Crash course page (the cheatsheet)

Write it last. Put it on one long page. The essentials are always visible, and each explanation sits in a collapsed `??? note` or `??? example` box underneath. Sections:

1. **The course in 4–6 big ideas:** the threads that recur across units, each with where it appears.
2. **Practical frameworks toolkit**, the core of the page. For every framework, model or classification that drives applied questions, give:
    - what it is;
    - its items, with a memory aid;
    - how to apply it to a scenario;
    - a collapsed worked mini-example.
3. **Unit cards:** two lines on each unit, plus 3–5 "don't miss" points. Link to the unit and to its toolkit entries instead of repeating the lists.
4. **Traps:** a numbered list of non-obvious points that are easy to get wrong.
5. **Confusable pairs:** a table with columns "A | B | the one-line difference".
6. **Answer outlines** for the 5–6 recurring question types, each with a model paragraph.
7. **Quick sketches:** steps for drawing each key diagram in 2 minutes, with the full diagram collapsed.
8. **About 30 flashcards** (`??? question "…"`), weighted towards traps and framework items.

Don't copy the count-mismatch table or the list-count table from the exam-technique page; link to them.

---

## 6. Diagrams

- **Redraw every source figure.** Never copy images from the PDF. Keep the source figure number in the caption, e.g. "Figure 3.2: … (redrawn)".
- **Mermaid** works for flows, simple trees, comparisons and timelines. **Custom SVG** is better when layout matters: frameworks, scales, nested circles, side-by-side comparisons.
- SVGs go in `docs/assets/diagrams/uN-<name>.svg`. Use a light palette and `font-family="Inter, Arial, sans-serif"`. `extra.css` places them on a fixed white card, so they read the same in dark mode.
- Embed a diagram with a caption:
    ```markdown
    ![Alt text describing the diagram](assets/diagrams/u3-score-bands.svg){ .diagram }

    <p class="caption">Table 3.1 as a scale. The marker at 46 is calculated on this site.</p>
    ```
- When a diagram contains your own interpretation or calculation, **say so in the caption**.
- Check each SVG on its own before embedding it: `magick -background white -density 80 file.svg out.png`, then view the PNG. Look for overlapping labels and text that runs off the edge.

---

## 7. Verification

### 7.1 Every unit

```bash
.venv/bin/mkdocs build --strict              # no warnings
python3 planning/scripts/audit.py            # see below
python3 planning/scripts/build_glossary.py   # after changing any Key terms
```

### 7.2 What the audit checks

| Check | What it means |
|---|---|
| Anchors | Every `page.md#fragment` link points at an id that exists in the built site |
| Sections | Every numbered heading in the unit's source pages appears in a source tag on the page |
| Pages | Every source page in the unit's range is cited by at least one tag |
| Numbers | Every number in the source appears on the page. Leftovers are usually URLs, ISBNs, dates or footers, but **check each one by hand**: this check found a real gap in CSC 584 |
| Collapsibles | The number of `???` in the source equals the number of `<details>` in the built HTML |
| Quizzes | Every quiz has exactly one `data-correct` option |

### 7.3 Visual check

Headless Chromium needs the Bash sandbox disabled; run only this command unsandboxed. An HTTP server started inside the sandbox can't be reached from outside it, so screenshot the built file directly:

```bash
SP=<scratchpad dir>
chromium --headless=new --disable-gpu --no-sandbox --hide-scrollbars --user-data-dir=$SP/chr \
  --window-size=1280,60000 --virtual-time-budget=25000 --screenshot=$SP/page.png \
  "file://$PWD/site/unit-1-<slug>/index.html"
magick $SP/page.png -crop 1280x3000 +repage $SP/part_%02d.png   # then view the parts
```

Find where the content ends with `magick page.png -crop 1280x<h-300>+0+0 -fuzz 1% -trim -format "%@" info:`. Below that point there is only empty window.

---

## 8. Templates

### 8.1 `requirements.txt`

```
mkdocs-material==9.8.0
```

### 8.2 `mkdocs.yml`

```yaml
site_name: <COURSE CODE> — <Course title>
site_url: https://<domain>/<repo>/
site_description: Lecture notes, diagrams, quizzes and exam practice for <COURSE CODE>
docs_dir: docs

theme:
  name: material
  language: en
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      accent: deep orange
      toggle: { icon: material/weather-night, name: Switch to dark mode }
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: deep orange
      toggle: { icon: material/weather-sunny, name: Switch to light mode }
  font: { text: Inter, code: JetBrains Mono }
  icon: { logo: material/school }
  features:
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.footer
    - navigation.indexes
    - toc.follow
    - search.highlight
    - search.suggest
    - content.tabs.link

markdown_extensions:
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - tables
  - toc: { permalink: true, toc_depth: 3 }
  - pymdownx.details
  - pymdownx.mark
  - pymdownx.tabbed: { alternate_style: true }
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format

extra_css: [stylesheets/extra.css, stylesheets/quiz.css]
extra_javascript: [javascripts/quiz.js]

nav:
  - Home: index.md
  - Units:
      - "1. <Unit title>": unit-1-<slug>.md
  - Exam Preparation:
      - "Crash course": exam/crash-course.md
      - "Exam technique": exam/exam-technique.md
      - "Mock exam 1": exam/mock-exam-1.md
      - "Mock exam 2": exam/mock-exam-2.md
  - Glossary: glossary.md
```

### 8.3 `docs/javascripts/quiz.js`

```js
// Interactive MCQs: click an option to mark it, reveal the answer and the explanation.
function initQuizzes() {
  document.querySelectorAll(".quiz:not([data-ready])").forEach((quiz) => {
    quiz.dataset.ready = "true";
    const options = quiz.querySelectorAll(".quiz-options > li");
    const explain = quiz.querySelector(".quiz-explain");
    if (explain) explain.hidden = true;

    const reset = document.createElement("button");
    reset.type = "button";
    reset.className = "quiz-reset";
    reset.textContent = "Try again";
    reset.hidden = true;
    quiz.appendChild(reset);

    options.forEach((option) => {
      option.tabIndex = 0;
      option.setAttribute("role", "button");
      const choose = () => {
        if (quiz.classList.contains("answered")) return;
        quiz.classList.add("answered");
        const correct = option.hasAttribute("data-correct");
        option.classList.add(correct ? "chosen-correct" : "chosen-wrong");
        options.forEach((o) => { if (o.hasAttribute("data-correct")) o.classList.add("is-correct"); });
        if (explain) explain.hidden = false;
        reset.hidden = false;
      };
      option.addEventListener("click", choose);
      option.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); choose(); }
      });
    });

    reset.addEventListener("click", () => {
      quiz.classList.remove("answered");
      options.forEach((o) => o.classList.remove("chosen-correct", "chosen-wrong", "is-correct"));
      if (explain) explain.hidden = true;
      reset.hidden = true;
    });
  });

  // Number the quizzes on the page, wherever they are placed.
  document.querySelectorAll(".quiz-q").forEach((q, i) => { q.dataset.num = String(i + 1); });
}

if (typeof document$ !== "undefined") document$.subscribe(initQuizzes);  // Material instant navigation
else document.addEventListener("DOMContentLoaded", initQuizzes);
```

### 8.4 `docs/stylesheets/quiz.css`

```css
.md-typeset .quiz { border: 1px solid var(--md-default-fg-color--lightest); border-left: 4px solid var(--md-accent-fg-color);
  border-radius: 6px; padding: .8rem 1rem .6rem; margin: 1.2rem 0; background: var(--md-code-bg-color); }
.md-typeset .quiz-q { font-weight: 600; margin: 0 0 .6rem; }
.md-typeset .quiz-q::before { content: "Q" attr(data-num) ". "; color: var(--md-accent-fg-color); }
.md-typeset .quiz-options { list-style: none; margin: 0 0 .6rem; padding: 0; }
.md-typeset .quiz-options > li { margin: .35rem 0; padding: .45rem .75rem; border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 4px; cursor: pointer; transition: background-color .15s, border-color .15s; }
.md-typeset .quiz-options > li:hover, .md-typeset .quiz-options > li:focus-visible { border-color: var(--md-accent-fg-color); outline: none; }
.md-typeset .quiz.answered .quiz-options > li { cursor: default; }
.md-typeset .quiz-options > li.is-correct { border-color: #2e9d58; background: rgba(46,157,88,.14); }
.md-typeset .quiz-options > li.chosen-correct::after { content: "  ✓ Correct"; font-weight: 600; color: #2e9d58; }
.md-typeset .quiz-options > li.chosen-wrong { border-color: #d0453b; background: rgba(208,69,59,.14); }
.md-typeset .quiz-options > li.chosen-wrong::after { content: "  ✗ Not quite"; font-weight: 600; color: #d0453b; }
.md-typeset .quiz-explain { border-top: 1px dashed var(--md-default-fg-color--lighter); padding-top: .5rem; font-size: .95em; }
.md-typeset .quiz-explain > :first-child { margin-top: 0; }
.md-typeset .quiz-reset { margin-top: .4rem; font-size: .75rem; padding: .2rem .6rem; border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 4px; background: transparent; color: var(--md-default-fg-color--light); cursor: pointer; }
.md-typeset .quiz-reset:hover { color: var(--md-accent-fg-color); border-color: var(--md-accent-fg-color); }
```

### 8.5 `docs/stylesheets/extra.css`

```css
/* SVG diagrams are drawn for a light background: give them a fixed white card in both themes. */
.md-typeset img.diagram { display: block; margin: 1rem auto .3rem; max-width: 100%; height: auto; background: #fff;
  border-radius: 8px; padding: .6rem; box-shadow: 0 0 0 1px var(--md-default-fg-color--lightest); }
.md-typeset .caption { text-align: center; font-size: .8rem; color: var(--md-default-fg-color--light); margin-top: .2rem; }
.md-typeset .mermaid { text-align: center; margin: 1rem 0; }
.md-typeset .marks { float: right; font-weight: 600; color: var(--md-default-fg-color--light); font-size: .85em; }
.md-typeset .src { font-size: .7rem; color: var(--md-default-fg-color--light); letter-spacing: .02em; }
.md-typeset .outcomes li { margin-bottom: .2em; }
.md-typeset table:not([class]) { font-size: .78rem; }
.md-typeset blockquote { border-left-color: var(--md-primary-fg-color); }
.exam-header { border: 2px solid var(--md-primary-fg-color); border-radius: 8px; padding: .6rem 1rem; margin: 1rem 0 1.5rem; }
.exam-header p { margin: .3rem 0; }
```

### 8.6 `planning/scripts/build_glossary.py`

```python
"""Regenerate docs/glossary.md from each unit's "## Key terms" definition list.
Run from the project root: python3 planning/scripts/build_glossary.py"""
import pathlib, re

UNITS = [  # (number, file) — keep in step with mkdocs.yml
    (1, "unit-1-<slug>.md"),
]

entries = []
for num, fname in UNITS:
    block = pathlib.Path("docs", fname).read_text().split("## Key terms", 1)[1].split("\n---", 1)[0]
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
```

### 8.7 `planning/scripts/audit.py`

```python
"""Post-build audit. Run from the project root AFTER `.venv/bin/mkdocs build --strict`:
    python3 planning/scripts/audit.py"""
import pathlib, re, subprocess

PDF = "<course>.pdf"
UNITS = [  # (unit number, first PDF page, last PDF page, page file)
    (1, 6, 23, "unit-1-<slug>.md"),
]
DOCS, SITE = pathlib.Path("docs"), pathlib.Path("site")

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
print(f"[anchors] {n} checked, {bad} missing")

for u, a, b, f in UNITS:
    text, page = pdf_text(a, b), (DOCS / f).read_text()
    tags = " ".join(re.findall(r'<span class="src">(.*?)</span>', page))
    # 2. numbers in the source that never appear on the page
    nums = set(re.findall(r"\d[\d,\.]*\d%?|\d%", text))
    flat = page.replace(",", "")
    missing = sorted(x for x in nums if x.replace(",", "").rstrip(".") not in flat)
    # 3. numbered source sections not cited in any source tag
    secs = {s for pair in re.findall(rf"^\s*({u}\.\d+(?:\.\d+)?)\.?\s*$|^\s*({u}\.\d+(?:\.\d+)?)\s", text, re.M) for s in pair if s}
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
```

Expect false positives in the section check when a statistic starts a line in the source (e.g. "1.5 million" in Unit 1). Confirm those by hand.

### 8.8 `.github/workflows/deploy.yml`

```yaml
name: Deploy site to GitHub Pages
on:
  push: { branches: [main] }
  workflow_dispatch:
permissions: { contents: read, pages: write, id-token: write }
concurrency: { group: pages, cancel-in-progress: true }
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict
      - uses: actions/upload-pages-artifact@v3
        with: { path: site }
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: { name: github-pages, url: "${{ steps.deployment.outputs.page_url }}" }
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

**`.gitignore`:**
```
.venv/
site/
__pycache__/
.claude/
*.pdf
pq*.jpg
```

**Hosting notes:**
- On a free GitHub account, Pages needs a **public** repo, so keep the course material out of git.
- After the first push, set **Settings → Pages → Source: GitHub Actions**.
- If the account's `<user>.github.io` repo has a custom domain, a project repo named `<repo>` is served at `https://<domain>/<repo>/`. That needs no CNAME file and no DNS changes. Set `site_url` to match.
- The repo must be empty when created (no README or licence), so the first push doesn't conflict.

### 8.9 `CLAUDE.md` starter

```markdown
# CLAUDE.md — <COURSE CODE> (<title>) study site

Keep this file up to date whenever structure, conventions, status or commands change.

## What this is
MkDocs Material study site built from `<course>.pdf` (<N> pages, <N> units). Follows COURSE_SITE_PLAYBOOK.md.

## Key rules
- Cover everything in the source; restructure freely; tag every section with `<span class="src">§x.y · pp.a–b</span>`.
- Courseware wording for definitions/lists in `>` blockquotes only; extras in "Beyond the notes"; errors in "Courseware note" + planning/ERRATA.md.
- MCQs after each major section (2–3) + mixed review at the end; exam questions per planning/QUESTION_STYLE.md.
- `mkdocs build --strict` and `planning/scripts/audit.py` must be clean.

## Commands
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve | .venv/bin/mkdocs build --strict
python3 planning/scripts/build_glossary.py | python3 planning/scripts/audit.py
pdftotext -f <first> -l <last> "<course>.pdf" -

## Status
- [ ] Planning files  - [ ] Scaffold  - [ ] Unit 1 (reviewed by student)  - [ ] Units 2–N
- [ ] Glossary, exam technique, crash course, mocks  - [ ] Final audit  - [ ] Hosted
```

---

## 9. Lessons learned (don't repeat these)

### Markdown rendering

- **A bullet list followed by a numbered list, with only a blank line between them, merges into one list.** Put a sentence between them, e.g. "Answer the following:". This matters most in scenario questions.
- Inside a list item, a `**Heading:**` line needs a **blank line** before its nested list. Otherwise the list renders before the heading.
- Consecutive `>` lines merge into one paragraph. Separate quoted paragraphs with a bare `>` line.
- Count `???` in the source against `<details` in the HTML to confirm that every collapsible rendered (the audit does this).

### Mermaid

- A `flowchart LR` with a big subgraph renders tiny. Use `direction TB` inside subgraphs, or use a table.
- A `flowchart TB` with one root and 4 or more wordy leaves renders tiny. Use `flowchart LR`.
- A mind map with about 10 branches *and* their leaves is unreadable. Show branch names only, with a table underneath.
- No `( ) [ ]` inside mind-map node text: they change the node shape.

### Content

- Never put your own paraphrase in a blockquote.
- Don't invent facts in comparison tables. Write "Not stated", or label the column as added explanation.
- When you interpret (rank, calculate, infer), **say so** in the caption or text.
- When the source names something without describing it, say so, and explain it in a Beyond box.
- Check learning outcomes vs content vs self-test counts in every unit. Flag mismatches under the outcomes, and collect them in the exam-technique page's mismatch table.
- Cross-unit references must point to the right place. Check each "Unit N says…" claim.
- The final number audit caught a real omission, a summary sentence. Don't dismiss leftovers without looking.

### Tooling

- The Read tool may be blocked on `/tmp/...` text files; use `sed -n` through Bash. Images in the scratchpad can be read.
- Shell for-loops split file names that contain spaces (e.g. the course PDF); use Python `subprocess` with a list of arguments.
- Headless Chromium fails inside the sandbox (`socket() failed: Operation not permitted`). Disable the sandbox for that one command only.

---

## 10. Student preferences (defaults from CSC 584; confirm in Phase 0)

- Full coverage, with clear explanations. No over-summarising.
- Questions should be **a bit challenging**: application, justification, scenarios with numbers or tables.
- MCQs should point out key facts, and the explanations should teach.
- Answers revealed on the same page.
- Local examples are welcome, labelled as examples.
- Extras are fine if clearly labelled and only there to explain the material.
- Keep `CLAUDE.md` and `HANDOVER.md` up to date.
