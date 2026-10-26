# Prompts to Copy

Paste these into Claude Code (started inside your vault folder). Swap the parts in `<angle brackets>`. You don't need exact wording; plain English works. These just save you thinking time.

Back to the [README](../README.md) · Previous: [Where to get your data](EXPORTS.md) · Next: [FAQ](FAQ.md)

---

## First day

**Get oriented**
```
Read CLAUDE.md and index.md, then explain in three sentences how this vault works.
```

**Swap out the sample person**
```
Replace the Alex Rivera sample content with a blank profile for me. My name is <name>. Keep the folder structure, Home, Diagrams, Brain Questions, the Note Template and the folder index notes. Delete the other sample notes, fix broken links, update ZONES in scripts/make_canvases.py, then rebuild the index, folder indexes and canvas.
```

**Let it interview you**
```
Interview me to build my profile. Ask 5 questions at a time about my background, work, goals, people and interests. After each batch, update my profile and the right notes, then ask the next 5. Stop when I say stop.
```

## Ingesting things

**One file**
```
Ingest raw/<folder>/<file> following CLAUDE.md.
```

**A big export (always plan first)**
```
raw/<folder>/<export-folder>/ is my <ChatGPT / LinkedIn / Spotify / ...> export. Look at its structure and tell me your plan: which notes you'll create or update, roughly how many, and what you'll skip. Don't write anything yet.
```
Then, once the plan looks right:
```
Go ahead with that plan. Work in batches, rebuild the index at the end, and log it.
```

**AI chat history**
```
Ingest my ChatGPT export in raw/07 Chats/<folder>/. File only chats that taught me something or recorded a decision; skip quick one-off questions. One summary note per chat in wiki/07 Chats/<topic>/, linked to the month it happened and to any people, projects or concepts it touches.
```

**LinkedIn**
```
Ingest my LinkedIn export in raw/02 Me/Career/<folder>/. Build my career timeline (jobs, schools, dates) into my profile and the Life Timeline. Create entity pages for employers and schools. Don't create pages for every connection; just list how many I have.
```

**Spotify**
```
Ingest my Spotify extended streaming history in raw/05 Journals & Trackers/<folder>/. Make one listening-history note: top artists and songs per year, total hours per year, and any big shifts in taste. Link each year to the timeline.
```

**Old notes imported with the Obsidian Importer**
```
Everything in wiki/00 Inbox/ came from my old notes app. Sort each note into the right numbered folder, give it frontmatter and a one-line summary per CLAUDE.md, merge duplicates, and list anything you're unsure about instead of guessing.
```

**A web page**
```
Read <URL> and save the useful parts as a note in wiki/06 Library/, with a link back to the page and the date.
```

**A photo or screenshot**
```
Read the image raw/<folder>/<image>. Pull out the text and the important facts and file them in the right note.
```

## Asking questions

**Normal question**
```
<Your question>? Answer from my notes with [[links]], and say UNKNOWN for anything you can't find.
```

**Timeline question**
```
What was I doing in <year>? Build a short month-by-month summary from my notes.
```

**Keep a good answer**
```
That answer is worth keeping. File it as a note in wiki/07 Chats/<topic>/ and log it.
```

## Keeping it healthy

**Weekly tidy-up (lint)**
```
Run the LINT workflow from CLAUDE.md. Fix what is safe, list the rest, and log it.
```

**Empty the inbox**
```
File everything in wiki/00 Inbox/ into the right folders, then rebuild the indexes.
```

**Rebuild all the generated files**
```
Run make_index.py, make_folder_indexes.py and make_canvases.py and tell me if anything is missing.
```

**Back up**
```
Commit my changes with a short plain message and push them.
```

## Making it yours

**Add a folder**
```
Add a new wiki folder "<name>" for <what goes there>. Update the folder table in CLAUDE.md, the BLURBS in scripts/make_folder_indexes.py, and ZONES in scripts/make_canvases.py, then rebuild.
```

**Add a standing rule**
```
Add a standing fact to CLAUDE.md: <rule>. For example: "My dog is named Max; never confuse him with my coworker Max."
```

**Make a tracker**
```
Make a tracker note in wiki/05 Journals & Trackers/ for <habit, workouts, job applications...> with a dated table, and link it from Home.
```
