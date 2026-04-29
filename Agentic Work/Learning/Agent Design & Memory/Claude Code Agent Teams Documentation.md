---
title: "Claude Code Agent Teams Documentation"
url: "https://code.claude.com/docs/en/agent-teams"
platform: web
date_saved: 2026-02-06
source: "Anthropic Claude Code Docs"
content_type: guide
topics: [AI Agents, Claude Code & Anthropic]
tags: [claude-code, agent-teams, multi-agent, orchestration, parallel-agents, subagents, task-coordination, ai-coding]
status: unread
---

> Agent teams let you coordinate multiple Claude Code instances working together — one session acts as team lead, coordinating work, assigning tasks, and synthesizing results while teammates work independently in their own context windows.

**Topics:** [[AI Agents]], [[Claude Code & Anthropic]]

## Key Points
- Agent teams are EXPERIMENTAL (require `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` to enable)
- Unlike subagents (which report back to caller only), teammates can message EACH OTHER directly via shared mailbox
- Teams consist of: Team Lead, Teammates (separate Claude instances), Shared Task List, and Mailbox
- Best use cases: research/review tasks, new modules/features, debugging with competing hypotheses, cross-layer coordination
- Significantly higher token costs than subagents — each teammate has its own context window
- Two display modes: in-process (cycle with Shift+Down) or split-panes (tmux/iTerm2 required)

### Agent Teams vs Subagents

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARCHITECTURE COMPARISON                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SUBAGENTS:                    AGENT TEAMS:                     │
│  ───────────                   ───────────────                  │
│                                                                  │
│      [Main]                        [Lead]                       │
│       │ │ │                       /  │  \                       │
│       ▼ ▼ ▼                      ▼   ▼   ▼                      │
│      [A][B][C]               [TM1]─[TM2]─[TM3]                  │
│       │ │ │                    │     │     │                    │
│       └─┴─┘                    └─────┴─────┘                    │
│         │                    ┌───────────────┐                  │
│    Report back              │  Shared Tasks  │                  │
│    to main only             │    Mailbox     │                  │
│                             └───────────────┘                   │
│                                                                  │
│  Context:     Own window          Own window                    │
│  Comms:       Results → Main      Teammates ↔ Each other       │
│  Coord:       Main manages        Self-coordination + lead     │
│  Cost:        Lower               Higher (N context windows)   │
│  Best for:    Focused tasks       Collaboration/discussion     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Team Architecture

| Component | Role |
|-----------|------|
| **Team Lead** | Main session that creates team, spawns teammates, coordinates work |
| **Teammates** | Separate Claude Code instances with own context windows |
| **Task List** | Shared work items with states: pending → in progress → completed |
| **Mailbox** | Inter-agent messaging system for direct teammate communication |

### Key Use Cases

1. **Parallel Code Review** — 3 reviewers with distinct lenses (security, performance, test coverage)
2. **Competing Hypotheses** — Multiple investigators trying to disprove each other's theories
3. **Independent Modules** — Each teammate owns a separate piece without file conflicts
4. **Cross-Layer Coordination** — Frontend, backend, tests each owned by different teammate

### Best Practices

- Start with 3-5 teammates for most workflows (5-6 tasks per teammate)
- Give teammates enough context in spawn prompt (they don't inherit lead's conversation)
- Avoid file conflicts — assign different file sets to each teammate
- Size tasks appropriately: not too small (overhead exceeds benefit), not too large (drift risk)
- Pre-approve common operations in permission settings to reduce interruptions

### Hooks for Quality Gates

- `TeammateIdle` — runs when teammate about to go idle (exit code 2 keeps them working)
- `TaskCreated` — runs on task creation (exit code 2 prevents + sends feedback)
- `TaskCompleted` — runs on task completion (exit code 2 prevents completion)

### Limitations

- No session resumption with in-process teammates
- Task status can lag (teammates may not mark tasks complete)
- One team per session, no nested teams
- Lead is fixed for team lifetime
- Split panes require tmux or iTerm2 (not VS Code terminal)

*Filed in: [[Saved Links MOC]]*
