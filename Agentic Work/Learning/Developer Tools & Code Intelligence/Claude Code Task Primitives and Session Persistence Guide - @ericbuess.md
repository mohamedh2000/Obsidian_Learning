---
title: "Claude Code Task Primitives and Session Persistence Guide"
url: "https://x.com/ericbuess/status/2014754767088599513?s=42"
platform: twitter
date_saved: 2026-01-23
source: "Eric Buess (@ericbuess)"
content_type: tweet
topics: [Claude Code, Developer Tools]
tags: [claude-code, task-primitives, session-management, task-list, hooks, persistence, dev-tools]
status: unread
---

> Comprehensive guide to Claude Code's new task primitives (v2.1.17+): how to trigger TaskCreate, persistence behavior across /clear, and using CLAUDE_CODE_TASK_LIST_ID for cross-session sharing.

| Metric | Count |
|--------|-------|
| Likes | 187 |
| Retweets | 14 |

**Topics:** [[Claude Code & Anthropic]], [[Developer Tools]]

## Key Points
- Task system activates when given 3+ items, complex multi-step work, or explicit "track as tasks" requests
- Tasks persist to filesystem but do NOT auto-resume after `/clear` — requires explicit "check tasks" prompt or a hook injection
- `CLAUDE_CODE_TASK_LIST_ID` environment variable enables sharing the same task list across multiple Claude instances
- The system provides durable storage, not autopilot — each session needs prompting or hooks to resume

### Triggering the Task System
Nudge phrases: "create a task list for this", "track these as tasks", "use the task system". After clearing, say "check tasks" or "what's pending?" to reload.

### Making It Seamless
For true automatic continuation, set up a session-start hook that injects "Check TaskList and resume pending work". Alternatively, start each session with "check tasks".

### Discovering New Features
Eric recommends installing [claude-code-docs](https://github.com/ericbuess/claude-code-docs) for a `/docs` command. Pattern: `/docs tell me about [feature]. how does it work? how can i call and use it? use subagents to debate top unexpected and useful things i can do with it`

*Filed in: [[Saved Links MOC]]*
