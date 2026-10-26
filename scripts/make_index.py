"""Build index.md: every wiki note grouped by top folder with a one-line summary. Run from the vault root."""
import re
from pathlib import Path

WIKI = Path("wiki")
ARCHIVE = "99 Archive"
NAV = re.compile(r"^(>\s*)?(←|back to|hub:|hubs:|month:|related:|links:)", re.IGNORECASE)


def clip(s, limit):
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def summary(text, limit=100):
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":  # frontmatter summary: wins, else skip frontmatter
        end = next((i for i, l in enumerate(lines[1:], 1) if l.strip() == "---"), 0)
        for l in lines[1:end]:
            m = re.match(r"summary:\s*(.+)", l)
            if m and m.group(1).strip("'\" "):
                return clip(m.group(1).strip().strip("'\""), limit)
        lines = lines[end + 1:]
    for raw in lines:
        s = raw.strip()
        if not s or s.startswith(("#", "```", "|", "![[", "---")) or NAV.match(s) or re.match(r">\s*\[!", s):
            continue
        s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", s)  # [[a|b]] -> b, [[a]] -> a
        s = re.sub(r"[*`]|^[-*>]\s*|^\*\*Summary\*\*:\s*", "", s).strip()
        s = re.sub(r"^Summary:\s*", "", s)
        if s:
            return clip(s, limit)
    return ""


def build():
    out = ["# Index", "", "Every wiki page with a one-line summary. Rebuild with `python3 scripts/make_index.py`.", ""]
    for top in sorted(p for p in WIKI.iterdir() if p.is_dir()):
        notes = sorted(n for n in top.rglob("*.md") if not n.name.endswith(" — Index.md"))
        out.append(f"## {top.name} ({len(notes)})")
        if top.name == ARCHIVE:
            out += [f"Archived material, not listed. See [[{ARCHIVE} — Index]].", ""]
            continue
        for n in notes:
            line = f"- [[{n.stem}]]"
            s = summary(n.read_text(errors="ignore"))
            out.append(f"{line} — {s}" if s else line)
        out.append("")
    Path("index.md").write_text("\n".join(out))
    return sum(1 for l in out if l.startswith("- [["))


sample = "---\ntype: x\n---\n\n# Title\nBack to [[Home]] · Month: [[2026-10 October]]\n\n**Summary**: A [[Acme Corp|company]] page for **Alex**.\n"
assert summary(sample) == "A company page for Alex.", summary(sample)
assert summary("# Only a heading\n") == ""
assert summary('---\nsummary: "From frontmatter."\n---\n> [!summary] Summary\n> Body.\n') == "From frontmatter."
assert summary("> [!summary] Summary\n> From the callout.\n") == "From the callout."
assert summary("x" * 150).endswith("…") and len(summary("x" * 150)) == 100

if __name__ == "__main__":
    print(f"index.md written: {build()} notes")
