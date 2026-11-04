# PLAN — CSC 583 study site

## Goal
A MkDocs Material study site covering **all** of `CSC 583 Note3_052848.pdf` (82 pages, Computer and Information Security, University of Ibadan), following COURSE_SITE_PLAYBOOK.md, plus exam preparation.

## Intake answers (Phase 0, 2026-11-04)
1. **Source:** only the courseware PDF. No past papers available.
2. **Exam format (student's description):** written exam, about **5 questions**, possibly a **compulsory Question 1**, answer **3 or 4** in total. Questions test knowledge of the concepts *exactly as taught*, plus some scenario-based application questions. Duration/marks not known: assume **2 hours, ~20 marks per question, parts a/b/c(/d)**.
3. **Difficulty:** "a bit challenging" (scenarios, application, justification) **but also full recall coverage**. In the student's words: *"I should know every possible recall question that can come out since I trust in my ability to apply them to actual scenarios."* → recall coverage is the top priority; scenarios are second.
4. **Local context:** not specified; Nigerian examples are fine (UI student), always in Example / Beyond boxes.
5. **Hosting:** GitHub Pages. Set up the workflow and `git init`, but **the student creates the repo and pushes**. PDF is git-ignored. `site_url` is a placeholder until the repo name is known.
6. **Changes from the playbook:**
    - **No Unit 1 review pause.** Each unit is written by its own subagent; context is passed forward through `HANDOVER.md`.
    - **Recall drill** added to every unit (see STRUCTURE.md): a complete bank of short recall questions, one per definition / list / comparison / named item in the source, with collapsed answers.

## Source structure decisions
- No printed page numbers: all page references are **PDF page indices**.
- The courseware has **no Chapter 5** and **two Chapter 8s**. The site numbers units 1–12 sequentially; source tags keep the courseware's section numbers (§6.4.1 etc.). Mapping: see CLAUDE.md.
- The courseware has **no learning outcomes and no self-test questions** (except the Unit 10 case study questions). Units replace "Learning outcomes" with "What you should be able to do" (written by us, labelled as such) and include "Self-test" only where the source has questions.
- [x] Final phase: upgrade page-level cross-unit links to anchors (Unit 3 and others); glossary duplicates across units are accepted (each links to its unit).
