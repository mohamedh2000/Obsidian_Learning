---
title: "Claude Code Ctrl+S Prompt Stash Feature"
url: "https://x.com/adocomplete/status/2014047394585825296?s=42"
platform: twitter
date_saved: 2026-01-21
source: "Ado (@adocomplete)"
content_type: tweet
topics: [Claude Code & Anthropic, Developer Tools]
tags: [claude-code, keyboard-shortcuts, productivity, workflow, prompt-management, terminal]
status: unread
---

> Ctrl+S in Claude Code saves your draft prompt to a stash, letting you send a different prompt first. Your saved draft auto-restores — like git stash, but for prompts.

| Metric | Count |
|--------|-------|
| Likes | 1970 |
| Retweets | 133 |

**Topics:** [[Claude Code & Anthropic]], [[Developer Tools]]

## Key Points
- **Git Stash Mental Model**: The feature mirrors `git stash` behavior — temporarily save work-in-progress, do something else, then restore your WIP automatically
- **Eliminates Copy-Paste Workflow**: Before this, users would copy long prompts to Notes/clipboard before switching context; now Claude Code handles it natively
- **Keyboard-Driven UX**: Ctrl+S is a familiar "save" shortcut, reducing cognitive load for developers already used to that muscle memory
- **Auto-Restore Behavior**: The stashed prompt returns automatically after the interim prompt completes — no manual "pop" command needed

### Workflow Example
```
Workflow WITHOUT stash:
┌──────────────────────────────────┐
│ 1. Writing long prompt...        │
│ 2. Need to ask quick question    │
│ 3. Copy prompt to Notes          │
│ 4. Send quick question           │
│ 5. Paste prompt back             │
│ 6. Continue writing              │
└──────────────────────────────────┘

Workflow WITH Ctrl+S stash:
┌──────────────────────────────────┐
│ 1. Writing long prompt...        │
│ 2. Ctrl+S (stash)                │
│ 3. Send quick question           │
│ 4. Draft auto-restored ✓         │
└──────────────────────────────────┘
```

### Why This Matters
Small UX friction adds up during long coding sessions. This feature acknowledges that Claude Code users often interrupt their prompt-writing to ask clarifying questions or switch context temporarily. Native support means fewer lost prompts and smoother flow states.

*Filed in: [[Saved Links MOC]]*
