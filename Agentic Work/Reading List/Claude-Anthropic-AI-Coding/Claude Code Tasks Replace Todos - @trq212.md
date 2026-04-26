---
title: "Claude Code Tasks Replace Todos - Thariq Announcement"
url: "https://x.com/trq212/status/2014480496013803643?s=42"
platform: twitter
date_saved: 2026-01-23
source: "Thariq (@trq212)"
content_type: announcement
topics: [Claude Code, AI Agents, Developer Tools]
tags: [claude-code, tasks, todos, multi-session, subagents, anthropic, agent-coordination, file-system]
status: unread
---

> We're turning Todos into Tasks in Claude Code. Tasks are a new primitive that help Claude Code track and complete more complicated projects and collaborate on them across multiple sessions or subagents.

| Metric | Count |
|--------|-------|
| Likes | 5900 |
| Retweets | 754 |

**Topics:** [[Claude Code & Anthropic]], [[AI Agents]], [[Developer Tools]]

## Key Points
- **Evolution rationale**: Opus 4.5 can run autonomously longer and track state better — TodoWrite became unnecessary for small tasks, but complex projects need more
- **Key upgrade**: Tasks support dependencies, blockers, and cross-session coordination — stored in file system (`~/.claude/tasks`) not just context
- **Multi-agent sync**: When one session updates a Task, changes broadcast to all sessions working on the same Task List
- **Inspired by community**: Took inspiration from projects like Beads by Steve Yegge

### How to Use Tasks
Set a shared Task List across sessions via environment variable:
```bash
CLAUDE_CODE_TASK_LIST_ID=groceries claude
```

Works with:
- `claude -p` (prompt mode)
- Agent SDK

### Architecture Change
```
BEFORE (Todos)                    AFTER (Tasks)
─────────────────                 ─────────────────
Context-only storage              File system storage
Single session                    Multi-session broadcast
Flat list                         Dependencies + blockers
Model tracks state                System tracks state
```

### Why This Matters
Tasks are infrastructure for long-running agent projects. Instead of Claude "remembering" what to do, the task state persists across context windows, sessions, and even different Claude instances. This enables true project collaboration between human and multiple agent sessions.

*Filed in: [[Saved Links MOC]]*
