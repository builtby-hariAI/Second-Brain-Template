"""Build the Brain Map canvas: a hub in the middle, one group per wiki folder around it. Run from the vault root.

Edit ZONES to point at your own notes. A missing note shows up as a red "missing" card so you notice it.
"""
import json
from itertools import count
from pathlib import Path

NOTES = {p.stem: p for p in Path("wiki").rglob("*.md")}
BLUE = {"cyan": "#00e5ff", "sky": "#4cc9f0", "ice": "#7fdfff", "mid": "#5b9cf5", "deep": "#3a7bd5", "red": "#1e4690"}
ids = count(1)
nodes, edges = [], []


def add(kind, x, y, w, h, color=None, **extra):
    node = {"id": f"n{next(ids)}", "type": kind, "x": x, "y": y, "width": w, "height": h, **extra}
    if color:
        node["color"] = BLUE[color]
    nodes.append(node)
    return node["id"]


def note_card(name, x, y, color):
    p = NOTES.get(name)
    if p is None:
        return add("text", x, y, 460, 80, "red", text=f"missing: {name}")
    return add("file", x, y, 460, 220, color, file=str(p))


ZONES = [  # (label, color, notes) placed clockwise around the hub
    ("02 Me", "sky", ["Alex Rivera - Profile", "Jordan Lee"]),
    ("04 Projects", "deep", ["Sample Project"]),
    ("03 Knowledge", "mid", ["Finance Hub"]),
    ("Concepts", "ice", ["Compound Interest"]),
    ("Entities", "mid", ["Acme Corp"]),
    ("05 Journals & Trackers", "ice", ["Workout Log"]),
    ("01 Timeline", "cyan", ["Life Timeline", "2026-10 October"]),
    ("07 Chats", "sky", ["Sample Chat Summary"]),
]
SPOTS = [(-1300, -1150), (-200, -1150), (900, -1150), (900, 250), (900, 1650), (-200, 1650), (-1300, 1650), (-1300, 250)]

hub = add("text", -260, -120, 520, 240, "cyan",
          text="# Second Brain\nraw/ sources -> wiki/ notes -> index, log, map\n\n[[Home]] / [[Diagrams]] / [[index]]")
for (label, color, notes), (gx, gy) in zip(ZONES, SPOTS):
    add("group", gx, gy, 1060, 330 + 240 * ((len(notes) + 1) // 2), color, label=label)
    first = None
    for i, n in enumerate(notes):
        nid = note_card(n, gx + 40 + (i % 2) * 500, gy + 60 + (i // 2) * 260, color)
        first = first or nid
    top = gy > 0
    edges.append({"id": f"e{next(ids)}", "fromNode": hub if top else first, "fromSide": "top" if top else "bottom",
                  "toNode": first if top else hub, "toSide": "bottom" if top else "top", "color": BLUE[color]})

Path("wiki/Brain Map.canvas").write_text(json.dumps({"nodes": nodes, "edges": edges}, indent="\t", ensure_ascii=False))
missing = [n["text"] for n in nodes if n["type"] == "text" and n["text"].startswith("missing")]
print(f"Brain Map.canvas: {len(nodes)} nodes, {len(edges)} edges, missing={missing or 'none'}")
