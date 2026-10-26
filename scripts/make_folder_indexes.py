"""Write wiki/<folder>/<folder> — Index.md for each top-level wiki folder. Run from the vault root."""
from pathlib import Path

WIKI = Path("wiki")
BLURBS = {
    "00 Inbox": "Unsorted captures and plans waiting to be filed. Empty it regularly: every note here should move to a numbered folder or the archive.",
    "01 Timeline": "Your life in time order. Life Timeline gives one line per event with a link to the real note; year and month notes give the per-period view.",
    "02 Me": "Who you are: profile, people, career, skills and education.",
    "03 Knowledge": "Evergreen knowledge you have learned or researched, grouped into hubs.",
    "04 Projects": "One note or folder per project. Code projects keep notes here and source code in raw/04 Projects/Code/.",
    "05 Journals & Trackers": "Logs, trackers, lists and journals. Time-bound records, not evergreen knowledge.",
    "06 Library": "Material you consume or keep for reference: books, courses, links and note templates.",
    "07 Chats": "Summaries of AI chat sessions, filed by topic. Good query answers get filed here too.",
    "99 Archive": "Retired or superseded material, kept for history. Don't edit it; restore a note by moving it back out.",
    "entities": "One page per person, organization or project. Each page summarises the thing and links its source notes.",
    "concepts": "One page per idea or strategy. Each page summarises the concept and links its source notes.",
}


def write_index(top):
    lines = [f"# {top.name}", "", BLURBS.get(top.name, ""), ""]
    subs = sorted(p for p in top.iterdir() if p.is_dir() and not p.name.startswith(".") and any(p.rglob("*.md")))
    if subs:
        lines += ["## Subfolders"] + [f"- {s.name}/ ({sum(1 for _ in s.rglob('*.md'))} notes)" for s in subs] + [""]
    notes = sorted(n for n in top.glob("*.md") if not n.name.endswith(" — Index.md"))
    if notes:
        lines += ["## Notes"] + [f"- [[{n.stem}]]" for n in notes] + [""]
    (top / f"{top.name} — Index.md").write_text("\n".join(lines))


if __name__ == "__main__":
    tops = sorted(p for p in WIKI.iterdir() if p.is_dir())
    missing = [t.name for t in tops if t.name not in BLURBS]
    for t in tops:
        write_index(t)
    print(f"folder indexes written for {len(tops)} folders; no blurb for: {missing or 'none'}")
