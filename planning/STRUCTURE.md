# STRUCTURE — page template and markup conventions

Copied from COURSE_SITE_PLAYBOOK.md §4–§6 and §9, with the **CSC 583 overrides** below. Where they conflict, the overrides win.

## CSC 583 overrides (read first)

1. **Learning outcomes:** the courseware has none. In their place, put `## What you should be able to do`: 4–8 bullet points written by us, introduced by the sentence *"The courseware lists no learning outcomes; these are written for this site."* No blockquote, no source tag needed.
2. **Self-test assessment:** only where the source has questions (Unit 10 case study). Otherwise omit the section.
3. **Recall drill (new, mandatory):** after the Mixed review, add `## Recall drill`. It is a complete bank of short recall questions that could appear as exam part (a)/(b): **one question for every definition, every list (asking for its full count), every comparison, every named algorithm/protocol/type/tool, and every figure** in the unit's pages. Format each as:

    ```markdown
    **R1.** Define *data integrity* and *system integrity*.

    ??? success "Answer"
        **Data integrity:** courseware wording… **System integrity:** …
    ```

    Group them with `### ` sub-headings by section. Answers use the courseware's wording (they may be compact). Aim for completeness, not a fixed number: typically 25–60 per unit, more for long units. If a reader learns every recall-drill answer, they can answer any recall question the examiner could set from the unit.
4. **Sample exam questions:** 3–4 per unit, in the format in QUESTION_STYLE.md: **at least one mostly-recall question** ("Define…, list and explain…, differentiate…") and the rest mixing recall with a scenario part.
5. **Section numbers:** source tags use the **courseware's** section numbers (§6.4.1 in Unit 5, Firewalls). Where the courseware has no numbering (Chapters 1, 2, 8, 8, 9, 11, 12 are partly or wholly unnumbered), use the courseware heading name: `Impact levels · pp.3–4`.
6. **Order of the end matter:** Key terms → Unit summary → Mixed review → Recall drill → Self-test (if any) → Practice exercises → Sample exam questions.

## Conventions set by Unit 1 (reference unit: docs/unit-1-security-concepts.md)

1. **Headings:** H2 = teaching sections in plain sentence case, no numbers (e.g. `## Impact levels of a security breach`), optionally with a colon subtitle. H3 = sub-items when each needs its own quote + explanation (e.g. one `###` per design principle). Recall-drill groups are H3. Don't put "Check your understanding" in a heading.
2. **Source tags for unnumbered sections:** use the courseware's own heading text in its original capitalisation (`Computer Security Terminologies · pp.4–5`, `Fundamental Security Design Principles · p.11`). Untitled opening text = `Chapter N opening · p.x`. Figures: `Fig. 1 · p.3`. Each `###` sub-section gets its own tag with its own page(s).
3. **Courseware quotes:** each definition/term is its own `>` block, bold term name first (`> **Term:** text`). Keep the source's (i)/(ii) inline when inline in the source; when the source sets them on separate lines, put each on its own paragraph separated by a bare `>` line. Courseware bullets "•" are kept as typed characters inside the quote. Typos are quoted as given, with `[sic]` only where it would otherwise confuse, plus a Courseware note.
4. **Section rhythm:** tag → (one bridging sentence) → quote(s) → `!!! note "In plain terms"` and/or a comparison table → `!!! example` (local, Nigerian) → `!!! tip "Exam angle"` → Courseware note / Beyond box if needed → `**Check your understanding**` + 2 MCQs (3 for the largest section). In long principle-style lists, a short bold lead phrase ("**Default deny.**") + 1–3 sentences replaces the "In plain terms" box to avoid admonition overload.
5. **Site-added material in tables/diagrams is labelled**: column header "*(site example)*" / "*(site summary)*", and captions say "colours added by this site" / "drawn for this site".
6. **Counts not stated by the courseware** (e.g. 17 practices) are given with "(the courseware does not number or count them; the count is ours)". Recall questions that ask for a list state the count in brackets: "List the essential security practices. (There are 17.)".
7. **Recall drill:** H3 groups mirror the teaching sections in page order; numbering R1…Rn runs continuously across groups; every multi-part practice/list gets its own question naming the number of parts ("State the four parts of…"); add "Differentiate…" questions for every confusable pair; answers in courseware wording, with key words bolded.
8. **Exam questions:** `**Question N** *(recall-heavy)*` / `*(applied: <topic>)*` label line, then parts `**Na.**` with `<span class="marks">`, each followed by its own `??? success "Model answer"`. Scenario cases are put in a bullet list followed by a lead-in sentence ("For each incident…") before the task, and fictional organisations are labelled fictional where they could be mistaken for real ones. Marking points must add up exactly.
9. **SVG palette** (light card; `font-family="Inter, Arial, sans-serif"`; white background rect): primary/defence teal fill `#e0f2f1` / `#b2dfdb` / `#80cbc4`, stroke `#00796b`, dark text `#004d40`; threat/attack/"added" orange fill `#fbe9e7` / `#ffccbc`, stroke `#d84315`, text `#bf360c`; neutral grey fill `#cfd8dc`, stroke `#455a64` (also arrow colour); highlight amber fill `#fff8e1`, stroke `#f9a825`; dark centre `#37474f` with white text; body text `#263238`. Box labels 15px bold, edge labels 13px. Rounded rects `rx="10"`.
10. **Memory aids** (mnemonics, groupings) go inside `!!! note "In plain terms"` and say they are the site's, not the courseware's.

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

