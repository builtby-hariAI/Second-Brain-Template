# FAQ and Troubleshooting

Back to the [README](../README.md) · See also: [Getting Started](GETTING-STARTED.md)

---

## Questions

**What is a "second brain"?**
A place outside your head where everything you know, did and decided is written down and linked, so you can find it later. This one adds an AI that does the filing and answers questions from it.

**Do I need to know how to code?**
No. You'll paste a few commands while setting up, and after that you talk to Claude in plain English. The Python scripts run themselves when Claude needs them.

**Is it free?**
Obsidian, Python, GitHub and this template are free. Claude Code needs a paid Claude plan or API credits ([pricing](https://claude.com/pricing)). Without Claude, the vault still works as a normal, well-organised Obsidian vault.

**Can I use a different AI (ChatGPT, Codex, Gemini, Cursor)?**
Mostly yes. The rules live in `CLAUDE.md`, which is plain text. Most AI coding tools read a similar file (often `AGENTS.md`). Copy `CLAUDE.md` to `AGENTS.md` and point your tool at the vault. The workflows were written and tested with Claude Code.

**Where does my data go?**
Your notes are files on your computer. When you ask Claude something, the parts it reads are sent to Anthropic to get an answer, the same as any Claude chat. Nothing is published unless you push it to a **public** repo, so keep yours **private**.

**Phone?**
Obsidian has free iOS and Android apps. To see the same vault on your phone, keep the folder in iCloud Drive (iPhone), use [Obsidian Sync](https://obsidian.md/sync), or another sync app. Claude Code itself runs on your computer.

**What's the difference between `raw/` and `wiki/`?**
`raw/` holds the originals (PDFs, exports) and is never changed, so you can always check a note against its source. `wiki/` holds the notes Claude writes about them.

**What's the "LLM-wiki pattern"?**
A way of using an AI as the librarian of a personal wiki: it ingests sources into linked pages, keeps an index, and answers questions from the pages instead of from memory. This template is a ready-made version of that idea.

**How do I move my existing Obsidian vault into this?**
Copy `CLAUDE.md`, `scripts/` and `.obsidian/snippets/` into your vault, then ask Claude: *"Read CLAUDE.md and reorganise this vault to match it. Show me the plan first."*

**Do I have to use the numbered folders?**
No. Rename them or add your own, then update the table in `CLAUDE.md`, `BLURBS` in `scripts/make_folder_indexes.py`, and `ZONES` in `scripts/make_canvases.py`. (There's a prompt for this in [PROMPTS.md](PROMPTS.md).)

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `command not found: claude` | Close and reopen the terminal. If it still fails, re-run the installer from the [quickstart](https://code.claude.com/docs/en/quickstart) |
| `command not found: python3` | Install [Python](https://www.python.org/downloads/). On Windows try `python` instead of `python3`, and tick **Add Python to PATH** during install |
| `can't open file 'scripts/make_index.py'` | You're in the wrong folder. `cd` into your vault first (the folder that has `CLAUDE.md` in it) |
| The colours / glow don't show | **Settings > Appearance > CSS snippets**, switch on `brain-colors` and `brain-glow`. Click the refresh icon if they aren't listed |
| The Dashboard shows "Bases" errors | Update Obsidian. Bases (`.base` files) need Obsidian 1.9 or newer |
| Diagrams show as code | Mermaid renders in **Reading view** (`Cmd/Ctrl + E` to switch). On GitHub they render automatically |
| Brain Map shows red "missing" cards | A note named in `ZONES` in `scripts/make_canvases.py` doesn't exist. Fix the name and re-run the script |
| Links are purple / "not created yet" | The linked note doesn't exist. Ask Claude to run the LINT workflow; it fixes broken links |
| My export is huge and Claude stops halfway | Ask for a plan first, then "work in batches of 50" (see [PROMPTS.md](PROMPTS.md)) |
| The export email never arrived | Check spam. Some services (LinkedIn "the works", Apple, Spotify extended history) can take days |
| I accidentally made my repo public | GitHub repo > **Settings > General > Danger Zone > Change visibility > Private**. If anything sensitive was pushed, assume it was seen and change any passwords or account numbers it contained |
