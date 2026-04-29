---
title: "snarktank/ralph — Autonomous AI Coding Loop"
url: "https://github.com/snarktank/ralph"
platform: github
date_saved: 2026-01-13
source: "snarktank (github.com)"
content_type: repo
topics: [Agent Design, Autonomous Coding]
tags: [github, ralph, autonomous-agents, ai-coding, prd-execution, amp, claude-code, iteration-loop]
status: unread
---

# snarktank/ralph — Autonomous AI Coding Loop

> An autonomous AI agent loop that executes AI coding tools repeatedly until all product requirements are fulfilled. Each iteration is a fresh instance with clean context. Memory persists via git history, progress.txt, and prd.json.

| | |
|---|---|
| **Source** | snarktank (github.com) |
| **Saved** | 2026-01-13 |
| **Type** | repo |
| **Language** | TypeScript (62.9%), Shell (17.6%), CSS (14.6%) |
| **URL** | [Link](https://github.com/snarktank/ralph) |

## Topics

[[Agent Design]] | [[Autonomous Coding]]

## Key Points

- **Autonomous iteration loop** — spawns fresh AI coding instances to implement user stories sequentially until PRD complete
- **Fresh context per iteration** — each cycle starts with clean context, avoiding context pollution
- **Memory via filesystem:** git commits, progress.txt, and prd.json persist learnings across iterations
- **Supports multiple AI tools:** Amp and Claude Code
- **Quality checks built-in:** runs typecheck and tests after each implementation attempt
- **Automatic archiving:** previous runs archived for reference

### Architecture

```
┌─────────────────────────────────────────────────────┐
│                     RALPH LOOP                       │
├─────────────────────────────────────────────────────┤
│  1. Pick highest-priority incomplete story           │
│  2. Spawn fresh AI coding instance                   │
│  3. Implement story                                  │
│  4. Run quality checks (typecheck, tests)            │
│  5. If pass → commit + update progress               │
│     If fail → log learnings + retry                  │
│  6. Repeat until all stories complete                │
└─────────────────────────────────────────────────────┘
```

### Why Fresh Context Matters

Traditional agent loops accumulate context across iterations, leading to:
- Token exhaustion
- Hallucinated references to old state
- Slow responses as context grows

Ralph's "fresh instance" model mirrors how human developers work — start each task with a clean slate, reference artifacts on disk.

## Notes

(Personal annotations)

---

*Filed in: [[GitHub Repos MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
