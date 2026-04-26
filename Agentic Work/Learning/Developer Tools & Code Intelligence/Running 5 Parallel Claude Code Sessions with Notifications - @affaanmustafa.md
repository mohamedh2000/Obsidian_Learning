---
title: "Running 5 Parallel Claude Code Sessions with Notifications"
url: "https://x.com/affaanmustafa/status/2014040193557471352?s=42"
platform: twitter
date_saved: 2026-01-22
source: "Affaan Mustafa (@affaanmustafa)"
content_type: tweet
topics: [Claude Code & Anthropic, Developer Tools]
tags: [claude-code, parallel-agents, iterm, terminal, notifications, multi-session, productivity]
status: unread
---

> Affaan describes running 5 Claude Code sessions simultaneously in numbered terminal tabs, using system notifications to know when each agent needs input.

| Metric | Count |
|--------|-------|
| Likes | ~1800 |
| Retweets | N/A |

**Topics:** [[Claude Code & Anthropic]], [[Developer Tools]]

## Key Points
- **5 Parallel Sessions**: Runs 5 Claude Code instances concurrently in separate terminal tabs — multiplies throughput by having agents work on different tasks simultaneously
- **Tab Numbering System**: Tabs numbered 1-5 provide quick visual reference for which agent is which — simple but effective organization pattern
- **System Notifications for Attention**: Uses iTerm 2 system notifications to alert when a Claude session needs human input — avoids constant polling of each tab
- **Documentation Link**: References Claude Code's terminal configuration docs for the notification setup at `code.claude.com/docs/en/terminal-config#iterm-2-system-notifications`

### Parallel Session Architecture
```
Developer Workstation:
┌─────────────────────────────────────────────────┐
│  iTerm 2                                        │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
│  │  1  │ │  2  │ │  3  │ │  4  │ │  5  │       │
│  │     │ │     │ │     │ │     │ │     │       │
│  │Claude│ │Claude│ │Claude│ │Claude│ │Claude│   │
│  │ Code │ │ Code │ │ Code │ │ Code │ │ Code │   │
│  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘   │
│     │        │        │        │        │       │
│     └────────┴────────┴────────┴────────┘       │
│                      │                          │
│                      ▼                          │
│         ┌─────────────────────────┐             │
│         │  macOS Notification    │              │
│         │  "Tab 3 needs input"   │              │
│         └─────────────────────────┘             │
└─────────────────────────────────────────────────┘
```

### Why This Matters
Running multiple Claude Code sessions is the current meta for power users. The notification system solves the key UX problem: you can't watch 5 terminals simultaneously, but you can respond to macOS notifications. This pattern scales better than trying to poll tabs manually.

*Filed in: [[Saved Links MOC]]*
