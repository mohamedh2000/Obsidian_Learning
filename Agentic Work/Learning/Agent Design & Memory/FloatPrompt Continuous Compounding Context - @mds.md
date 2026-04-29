---
title: "FloatPrompt Continuous Compounding Context"
url: "https://x.com/mds/status/2016914747493343446?s=42"
platform: twitter
date_saved: 2026-01-29
source: "MDS (@mds)"
content_type: tweet
topics: [Agent Memory, Context Engineering]
tags: [floatprompt, context-compounding, sqlite, agent-memory, claude-code, cursor, codex, session-persistence, database-first]
status: unread
---

> CONTINUOUS COMPOUNDING CONTEXT — all of my sessions start exactly where i left off, whether conversational, strategic, or code heavy

| Metric | Count |
|--------|-------|
| Likes | 220 |
| Retweets | 12 |

**Topics:** [[Agent Memory]], [[Context Engineering]]

## Key Points
- **Database-first architecture**: `float.db` is the local SQLite brain — all context is queryable, not just stored as flat files
- **Passive context > on-demand retrieval**: Context that's always loaded beats context that must be retrieved — reduces decision points
- **Session continuity across tools**: Works with Claude Code, Cursor, and Codex simultaneously via `.claude/`, `.cursor/`, `.codex/` sync
- **"Buoy" table for cross-session signals**: Important info logged in a buoy table, auto-generated to `buoy.md` — "it floats, get it"
- **"Prefer retrieval-led reasoning over pre-training-led reasoning"**: Explicit philosophy shift from model knowledge to context-provided knowledge

### FloatPrompt Architecture
```
.float/                    ← All floatprompt files
├── float.db               ← SQLite brain (source of truth)
├── agents.md              ← Auto-generated agent map, always loaded
├── buoy.md                ← Latest buoy entry (auto-generated)
└── [session files]        ← Skills, commands, transcripts
```

### Key Commands
- `/float start` — Reads git commits and related context files
- `/float-log` — Commits changes, reviews relationships, enriches float.db with transcript + decisions + "the why", then makes second commit

### Next Steps (Per MDS)
- Get agents to do this automatically during autonomous runs
- Log micro-session info between larger sessions
- Setup with @openclaw for personal mdsOS

*Filed in: [[Saved Links MOC]]*
