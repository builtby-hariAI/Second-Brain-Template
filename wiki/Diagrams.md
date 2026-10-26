---
type: dashboard
summary: "Mermaid diagrams: how sources flow into notes, a vault mindmap and a sample life timeline."
tags: [dashboard, diagrams]
---

# Diagrams

Back to [[Home]] · Canvas: [[Brain Map.canvas|Brain Map]]

> [!summary] Summary
> Three diagrams. The first shows how a new source becomes notes and answers, the second maps the vault, the third is a sample timeline. Mermaid renders these natively in Obsidian.

## How this brain works
```mermaid
%%{init: {'theme': 'dark'}}%%
flowchart LR
    S[("New source<br/>PDF, chat, link")]:::src --> R["raw/<br/>untouched sources"]:::raw
    R -->|ingest| W["wiki/<br/>notes Claude maintains"]:::wiki
    W --> E["entities/<br/>people, orgs, projects"]:::wiki
    W --> C["concepts/<br/>ideas, strategies"]:::wiki
    W --> I["index.md<br/>catalog, read first"]:::meta
    W --> L["log.md<br/>every change"]:::meta
    W --> G["graphify map<br/>search + clusters"]:::meta
    Q(["Question"]):::q -->|query| I --> A(["Answer with citations"]):::q
    G --> A
    A -.->|worth keeping| W
    K(["lint, weekly"]):::q -.-> W
    classDef src fill:#1b2a3a,stroke:#00e5ff,color:#e6f7ff
    classDef raw fill:#14283a,stroke:#7fdfff,color:#e6f7ff
    classDef wiki fill:#132338,stroke:#4cc9f0,color:#e6f7ff
    classDef meta fill:#111d33,stroke:#3a7bd5,color:#e6f7ff
    classDef q fill:#0f2236,stroke:#5b9cf5,color:#e6f7ff
```

## The brain at a glance
```mermaid
%%{init: {'theme': 'dark'}}%%
mindmap
  root((Second Brain))
    Me
      Profile
      People
      Career
    Knowledge
      Finance hub
      Research
    Projects
      Sample Project
    Journals and trackers
      Workout log
    Library
      Templates
    Chats
      AI and tech
    Entities and concepts
      Acme Corp
      Compound Interest
```

## Sample life timeline
```mermaid
%%{init: {'theme': 'dark'}}%%
timeline
    title Alex Rivera (fictional)
    2018 : High school graduation
    2022 : Finished a finance degree
    2023 : First analyst job at Acme Corp
    2026 : Started this second brain
```
