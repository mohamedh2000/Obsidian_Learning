---
title: "Ralph Orchestrator Hat-Based Agent Framework"
url: "https://github.com/mikeyobrien/ralph-orchestrator"
platform: github
date_saved: 2026-01-25
source: "mikeyobrien"
content_type: repo
topics: [Agent Architecture, Agent Orchestration, Developer Tools]
tags: [ai-agents, orchestration, rust, multi-agent, claude-code, codex, telegram, mcp, open-source]
status: unread
---

> A hat-based orchestration framework (2.8k stars) that keeps AI agents in a loop until tasks are completed, implementing the "Ralph Wiggum technique" for autonomous task completion through continuous iteration.

| Metric | Count |
|--------|-------|
| Stars | 2.8k |
| Language | Rust (82.6%) |

**Topics:** [[Agent Architecture]], [[Agent Orchestration]], [[Developer Tools]]

## Key Points
- **Multi-Backend Support**: Works with Claude Code, Kiro, Gemini CLI, Codex, Amp, Copilot CLI, and OpenCode — letting you switch agent backends without changing orchestration logic
- **Hat System Architecture**: Specialized personas (hats) coordinate through events, enabling role-based task delegation within a single orchestration loop
- **Backpressure Gates**: Rejects incomplete work by enforcing tests, lint, and typecheck passes before accepting task completion — prevents agents from declaring "done" prematurely
- **Persistent State**: Memories and task tracking persist across iterations, giving agents continuity between loop cycles for complex multi-step tasks
- **5 Built-in Patterns**: Includes code-assist, debug, research, review, and pdd-to-code-assist workflows out of the box
- **Human-in-the-Loop via Telegram**: Agents can ask questions and receive proactive guidance through Telegram integration, bridging autonomous execution with human oversight
- **MCP Server Mode**: Runs as a Model Context Protocol server for compatible clients, enabling integration into existing MCP-based toolchains

### How It Works
Users plan features via interactive sessions, then the system runs autonomous implementation loops. The orchestrator iterates until the agent outputs `LOOP_COMPLETE` or hits configured iteration limits. The hat system allows different personas to handle different aspects of the task (e.g., a "reviewer hat" vs a "coder hat").

### Tech Stack
- **Rust** (82.6%) — Core orchestration engine
- **TypeScript** (13.7%) — Web dashboard and tooling
- **Python** (2.1%) — Auxiliary scripts
- Requires Node.js 18+ and Cargo

*Filed in: [[GitHub Repos MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
