---
title: "Building AI Project Manager with Claude Code"
url: "https://x.com/nityeshaga/status/2017128005714530780?s=42"
platform: twitter
date_saved: 2026-01-29
source: "Nityesh (@nityeshaga)"
content_type: tweet
topics: [Agent Design, Claude Code]
tags: [claude-code, mcp-server, google-workspace, sub-agents, orchestration, project-management, context-engineering, applied-ai]
status: unread
---

> How We Built an AI Project Manager Using Claude Code — a detailed case study on building "Claudie," an internal PM agent for consulting work, covering MCP server creation, sub-agent orchestration, and the evolution from slash commands to a unified handbook architecture.

| Metric | Count |
|--------|-------|
| Likes | 639 |
| Retweets | 47 |

**Topics:** [[Agent Design & Memory]], [[Claude Code & Anthropic]]

## Key Points
- Built custom Google Workspace MCP server using Claude Code's MCP Builder skill to access Gmail, Calendar, Drive, and Sheets APIs
- Initial slash command approach failed due to context window exhaustion when reading data sources and populating sheets
- Sub-agent orchestration with Tasks feature solved the problem but overwhelmed the orchestrator when 10+ agents returned detailed reports simultaneously
- Key fix: sub-agents write outputs to a shared temp folder instead of returning to orchestrator — downstream agents read reports directly without relay summarization
- Evolved from 11 fragmented skills to a single "handbook" structured in chapters: Foundation, Daily Operations, Client Dashboards, New Clients

### The Architecture Evolution
Three major architectural generations in two weeks:
1. **Slash Commands** — treated as text expanders, failed due to context exhaustion
2. **Orchestrator + Sub-Agents** — context overwhelmed when parallel agents returned reports
3. **Shared Folder + Handbook** — file-based inter-agent communication + unified onboarding doc

### Why 2026 Is the Breakthrough Year
The stack that made this possible:
- **MCP Builder** — build custom MCP servers from any API (released Oct 2025)
- **Opus 4.5** — reasoning and planning capabilities for complex sheet structures (released Nov 2025)
- **Tasks feature** — sub-agent orchestration primitive (released Jan 2026)

### Key Insight: Job Description → Handbook
Framing automation as "hiring a person" guided architecture: write job description first, then create an onboarding handbook. Sub-agents read foundation chapters (context) then task-specific chapters (instructions).

*Filed in: [[Saved Links MOC]]*
