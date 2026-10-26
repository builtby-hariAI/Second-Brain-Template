---
description: Apply the answers in wiki/Brain Questions.md to the vault, then write the next batch of questions
---
The owner has answered questions in `wiki/Brain Questions.md`. Apply them:

1. Read `wiki/Brain Questions.md` and collect every `A::` line that has an answer.
2. For each answer, update the right notes following CLAUDE.md: the profile, Life Timeline, person, project, entity or concept pages. Create a missing page only after the name check. If an answer changes a standing fact in CLAUDE.md, ask before editing it.
3. Remove the answered questions. Keep unanswered ones.
4. Add up to 10 new questions, aimed at the biggest gaps: lines marked UNKNOWN in notes, people or projects mentioned but thin, and missing years in the Life Timeline. Keep them short and group them under headings.
5. Rebuild the catalog: `python3 scripts/make_index.py`, then `python3 scripts/make_folder_indexes.py`.
6. Append one entry to `log.md` (`## [YYYY-MM-DD] query | Brain Questions answers`).
7. Tell the owner, in a few lines, what changed and how many questions are left.

Only change what the answers say. Never guess; mark anything unclear as UNKNOWN.
