# Second Brain: Vault Schema

This is a personal second brain kept as an Obsidian vault. It follows the LLM-wiki pattern: sources go in `raw/` and never change, Claude writes and maintains `wiki/`, and this file holds the rules. Replace the standing facts at the bottom with your own.

## Layout
```
CLAUDE.md     this file (the schema)
index.md      catalog of every wiki page with a one-line summary. READ FIRST.
log.md        append-only history of ingest / query / lint / restructure
raw/          immutable sources (PDF, docx, images, csv, code). Same sub-paths as wiki/. raw/private/ is git-ignored.
docs/         setup guide, where to get exports, prompts, FAQ (for humans)
wiki/         every markdown note, maintained by Claude
scripts/      make_index.py, make_folder_indexes.py, make_canvases.py
graphify-out/ searchable knowledge graph of the vault (rebuilt, not edited)
.obsidian/    Obsidian settings
```

| wiki/ folder | What goes there |
|---|---|
| `00 Inbox` | Unsorted captures and plans waiting to be filed |
| `01 Timeline` | Life Timeline, year notes, month notes |
| `02 Me` | Profile, people (`People/`), career, skills, education |
| `03 Knowledge` | Evergreen knowledge, grouped into hubs |
| `04 Projects` | One note or folder per project |
| `05 Journals & Trackers` | Logs, trackers, lists, journals |
| `06 Library` | Books, courses, links, note templates |
| `07 Chats` | Summaries of AI chats, filed by topic subfolder |
| `99 Archive` | Retired or superseded material. Read-only unless restoring. |
| `entities/` | One page per person, organization or project |
| `concepts/` | One page per idea or strategy |

`raw/` is read-only. Never edit, rename or delete a file there. Embed it from wiki notes with `![[file.pdf]]`.

## Naming rules
- Every note name is unique across the vault, because Obsidian links by name. Check before creating: `find wiki -iname "<name>.md"`.
- Dates use `YYYY-MM-DD`. Month notes use `YYYY-MM Month`.
- Entity pages are named after the thing itself (`Acme Corp`). Concept pages are named after the idea (`Compound Interest`).
- Renaming a note means rewriting every `[[Old Name]]` link in the same change.

## Frontmatter
Use the fields existing notes already use, and leave out the ones that don't apply:
```yaml
---
type: project | person | concept | entity | finance | library | hub
date: 2026-10           # or created: / updated: YYYY-MM-DD
summary: One line that index.md will show.
tags: [finance, example]
sources:
  - raw/path/to/source.pdf
---
```
After the frontmatter: an H1, a nav line (`Back to [[Hub]] · Month: [[YYYY-MM Month]]`), then a short **Summary**.

## Workflows

### INGEST (new source)
1. Put the source in `raw/<matching folder>/`, with its original name kept.
2. Write a summary note in the matching `wiki/` folder that links the source and has frontmatter `sources:`.
3. Update every affected entity and concept page (a single source often touches 5-15 pages). Create a missing page only after the name check.
4. Rebuild the catalog: `python3 scripts/make_index.py`, then `python3 scripts/make_folder_indexes.py`.
5. Append to `log.md`.

**Big exports** (ChatGPT, LinkedIn, Takeout, Spotify, see `docs/EXPORTS.md`): look at the export's structure first and show the owner a plan (which notes, roughly how many, what gets skipped) before writing anything. Then work in batches. File only what is worth keeping: chats that taught something or recorded a decision, not every message. Exports in `raw/private/` and `.zip` files are git-ignored on purpose; never move them out to get them committed.

### BRAIN QUESTIONS
`wiki/Brain Questions.md` holds questions for the owner, answered after `A::`. When the owner says "I answered" or runs `/answered`, follow `.claude/commands/answered.md`. When an ingest leaves a gap you can't fill from sources, add a question there instead of guessing.

### QUERY (answering a question)
1. Read `index.md` first.
2. Run `graphify query "<question>"` from the vault root.
3. Read the cited notes and answer with `[[note]]` citations. Mark anything missing as UNKNOWN.
4. If the answer is worth keeping, file it as a note in `wiki/07 Chats/<topic>/` and log it.

### LINT (health check)
Check for contradictions between notes, stale claims, orphan notes, duplicate names, missing entity or concept pages for things mentioned in 3 or more notes, and broken `[[links]]` or `![[embeds]]`. Fix what is safe, list the rest, and log the result.

## log.md format
```
## [YYYY-MM-DD] ingest|query|lint|restructure | Title
- one to three bullets: what changed, which notes
```

## Standing facts (replace with yours)
- **Private data stays private.** Contact details, resumes, account numbers and health data never leave the vault. Don't paste them into web tools or artifacts.
- **Label evidence.** Anything with numbers says whether it is a claim, a backtest, simulated, paper or live.
- **Say UNKNOWN instead of guessing** when two sources disagree.

## Search map
`graphify-out/` is the knowledge graph (graph.json, GRAPH_REPORT.md). Refresh it after big changes with `/graphify --update`.
