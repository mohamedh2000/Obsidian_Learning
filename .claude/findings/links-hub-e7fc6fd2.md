---
topic: links-hub
session: e7fc6fd2
date: 2026-05-28
status: shipped
---

# Links Hub — by-platform / by-topic browser for the iMessage-synced vault

## Problem

User has ~2,110 link notes synced from iMessage into this Obsidian vault.
Wanted a single "pretty central place" that updates continuously, lets them
browse with progressive disclosure: outer platform (Twitter, Instagram,
GitHub…) → inner topic → individual notes.

## Key data discoveries (do not re-investigate)

1. **Vault is already fully tagged.** The iMessage sync writes rich
   frontmatter to every note. No backfill needed.
   - 2049 / 2110 notes have `url:`
   - 2048 / 2110 have `platform:` (one of: twitter, web, instagram, github,
     tiktok, youtube, local, arxiv, spotify, reddit)
   - 2048 / 2110 have `date_saved:`, `content_type:`, `topics:`, `tags:`,
     `status:`, `source:`
   - The 62 untagged notes are MOCs, Topic hubs, Templates, daily notes —
     filter them out via `note.url != null`
2. **`topics:` is noisy.** 1,605 distinct topic values with mixed casing
   ('AI Agents' 214 + 'ai-agents' 148 = same concept). Solution: case-
   insensitive grouping via `re.sub(r"[^a-z0-9]+", "-", t.lower())`, display
   the most-common spelling.
3. **Bases doesn't do nested groupBy.** Verified at obsidian.md/help/bases/
   syntax — exactly ONE `groupBy` per view. For nested progressive disclosure
   use Obsidian native callouts (snapshot) or Dataview (live).
4. **Folder ≠ topic.** Folder structure (17 dirs) is much coarser than
   `topics:` field. Use `topics:` array, not parent folder.

## Decision: single Bases file, 8 views

Final state after user feedback ("this is just ugly and bulky"):

- **Links Hub.base** — ONE file, 8 views: Grid (cards), By Platform,
  By Genre, By Topic, By Date, This Month, Unread, Compact list.
  User clicks tab at top to switch axis. Native sortable columns
  within each view. Lives at vault root.
- **Snapshot.md and live.md DELETED.** Static markdown was the wrong
  tool for 2K notes — pre-computed every combination = bulky no matter
  the bucketing. Progressive disclosure with 324 items in one section
  ("AI Agents · 324") was unbrowseable.

## Why Bases (not Dataview/static)

- Dataview NOT installed in this vault; Bases IS (core plugin, enabled).
- Bases 1.9+ supports: table, cards, list view types; per-view groupBy
  on any property; per-view filters; sortable columns; multiple views
  in one file.
- Embed syntax `![[file.base#ViewName]]` works for inline in markdown
  (not used here — opening the .base directly is cleaner).
- Limitation: only ONE groupBy per view. Solution: 8 views, each grouped
  on a different axis. User picks the lens via the tab bar.

## Files (zero existing notes touched)

```
/home/momo/obsidian_learning/
└── Links Hub.base                          (2.6 KB, 8 views)
    ├── Grid          (type=cards, sort date_saved DESC)
    ├── By Platform   (groupBy platform)
    ├── By Genre      (groupBy content_type)
    ├── By Topic      (groupBy topics)
    ├── By Date       (flat, sort DESC)
    ├── This Month    (filter date_saved >= today-30d, group platform)
    ├── Unread        (filter status=unread, group platform)
    └── Compact       (type=list)
```

## Regeneration

None needed. Bases is live — edits to any note's frontmatter reshuffle
the views automatically.

## Lessons / future-self notes

- **PRE-FLIGHT FAIL on turn 1.** I inferred schema from a 6-note sample and
  proposed a 2,000-file backfill. Dry-run caught it — but a single
  `grep -c "^platform:" -r vault` at the start would have saved a full
  AskUserQuestion cycle. Always grep the schema field directly across the
  full corpus before designing migrations.
- **PUSH-BACK WORKED.** Twice the user said "this isn't useable" after I
  delivered what they selected. The right move was: restate, propose
  different shapes, not double down on the failing approach.
- **Static markdown is wrong above ~500 notes.** Even with nested callouts
  and progressive disclosure, pre-computing every combination produces a
  file that's "ugly and bulky" — and once you expand a big topic (324
  notes) you're stuck scrolling a flat list with no further drilldown.
  Always reach for a database UI (Bases, Dataview) for 1K+ notes, not
  static MD.
- **Bases v1.9 grammar pitfalls:** only `groupBy` (singular), no nested.
  Per-view `filters: { and: [...] }`. View types: `table`, `cards`, `list`,
  `map`. Multiple views in one .base file is the canonical way to give
  multiple lenses.
- **Solve "I want N grouping axes" with N views in one Bases file**, not
  one super-view trying to do everything.

## Status

Current: shipped. User needs to open the hubs in Obsidian and visually
confirm rendering.
Next: (optional) wire generate-links-snapshot.py to a git pre-commit hook so
the snapshot stays fresh after each iMessage sync.
Blocked: nothing.
