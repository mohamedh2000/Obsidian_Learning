---
title: "VibeMux Multi-Agent Terminal Orchestrator"
url: "https://github.com/UgOrange/vibemux"
platform: github
date_saved: 2026-01-27
source: "UgOrange"
content_type: repo
topics: [Developer Tools, Agent Orchestration, Terminal Tools]
tags: [ai-agents, terminal, tui, go, claude-code, codex, multiplexer, multi-agent, open-source]
status: unread
---

> A TUI-based AI Agent Orchestration Terminal (50 stars) for managing multiple Claude Code and Codex instances simultaneously — like lazydocker but for AI coding agents.

| Metric | Count |
|--------|-------|
| Stars | 50 |
| Language | Go (100%) |

**Topics:** [[Developer Tools]], [[Agent Orchestration]], [[Terminal Tools]]

## Key Points
- **Multi-Pane Layout**: Supports up to 9 concurrent agent sessions in a 3×3 grid — watch multiple Claude Code or Codex instances work in parallel across different projects
- **Profile Management**: Stores per-project configurations, letting you quickly switch between different setups (different CLAUDE.md files, different prompts, different agent backends)
- **Multi-Driver Support**: Works with `claude`, `codex`, or `ccr` commands — backend-agnostic orchestration for whichever AI coding agent you prefer
- **PTY Integration**: Full terminal emulation with ANSI support means agents see a real terminal, not a stripped-down subprocess — critical for tools that expect interactive TTYs
- **Non-Intrusive Architecture**: Uses environment variable injection rather than patching agents, so it works with vanilla installations of Claude Code/Codex
- **Smart Notifications**: Desktop alerts and optional webhooks notify you when agents need attention or complete tasks — work on other things while agents run

### Architecture
```
~/.config/vibemux/
├── projects.json    # Project definitions
├── profiles.json    # Per-project configs
└── settings.json    # Global settings
```

Toggle between **Control Mode** (navigate panes) and **Terminal Mode** (type into agent) via F12. Grid layouts are configurable: 2×2, 2×3, or 3×3.

### Tech Stack
- **Bubble Tea** — Elm-architecture TUI framework
- **Lip Gloss** — Declarative UI styling
- **Bubbles** — TUI component library
- **creack/pty** — Terminal emulation wrapper
- **Go 1.25+**

### Installation
```bash
# Quick install
curl -sSL https://raw.githubusercontent.com/UgOrange/vibemux/main/install.sh | bash

# Or via Go
go install github.com/UgOrange/vibemux@latest
```

*Filed in: [[GitHub Repos MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
