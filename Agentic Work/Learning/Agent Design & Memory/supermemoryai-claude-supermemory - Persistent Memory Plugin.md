---
title: "supermemoryai/claude-supermemory - Persistent Memory Plugin"
url: "https://github.com/supermemoryai/claude-supermemory"
platform: github
date_saved: 2026-01-29
source: "supermemoryai"
content_type: repo
topics: [Agent Memory, Claude Code]
tags: [supermemory, claude-code, persistent-memory, mcp-plugin, team-memory, auto-capture, session-persistence]
status: unread
---

> Claude Code plugin that integrates with Supermemory to provide persistent memory capabilities — "remember what you worked on - across sessions, across projects"

| Metric | Count |
|--------|-------|
| Stars | N/A |
| Forks | N/A |

**Topics:** [[Agent Memory]], [[Claude Code]]

## Key Points
- **Three core capabilities**: Team Memory (shared project knowledge), Auto Capture (conversations saved on session end), Project Config (per-repo settings)
- **Two primary commands**: `super-search` (query past work), `super-save` (save info for team access)
- **Three-tier configuration**: Environment variables → Global settings → Project-specific config
- **Requires Supermemory Pro**: Not a free tool — needs paid Supermemory account

### Installation
```bash
/plugin marketplace add supermemoryai/claude-supermemory
/plugin install claude-supermemory
```

Set API key:
```bash
export SUPERMEMORY_CC_API_KEY="sm_..."
```

### Configuration Hierarchy
```
Environment variables        ← API key, debug logging
       ↓
~/.supermemory-claude/      ← Global settings (signal extraction, memory limits)
  └── settings.json
       ↓
.claude/.supermemory-claude/ ← Project-specific overrides
  └── config.json
```

### Key Features
1. **Team Memory**: Shared knowledge separate from personal memories — good for team projects
2. **Auto Capture**: Conversations automatically saved when sessions end — no manual action needed
3. **Project Config**: Per-repository settings, API keys, container tags — isolation between projects

### Technology
- JavaScript (87.8%), HTML (12.2%)

*Filed in: [[Saved Links MOC]]*
