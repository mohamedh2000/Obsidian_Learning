---
title: "Loop Engineering - Agent Orchestration Paradigm"
url: "https://x.com/addyosmani/status/2064127981161959567?s=42"
platform: twitter
date_saved: 2026-06-09
source: "Addy Osmani (@addyosmani)"
content_type: guide
topics: [AI Agents, Agent Architecture, Claude Code]
tags: [loop-engineering, agent-harness, orchestration, coding-agents, automation]
status: unread
---

# Loop Engineering - Agent Orchestration Paradigm

> "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." — @steipete

| | |
|---|---|
| **Source** | Addy Osmani (@addyosmani) |
| **Saved** | 2026-06-09 |
| **Type** | guide |
| **Engagement** | 4.9K likes |
| **URL** | [Link](https://x.com/addyosmani/status/2064127981161959567?s=42) |

## Topics

[[AI Agents]] | [[Agent Architecture]] | [[Claude Code & Anthropic]]

## Key Points

- **Loop engineering replaces manual prompting**: Design systems that prompt agents rather than typing prompts yourself
- **Five building blocks**: Automations (scheduled discovery/triage), Worktrees (parallel isolation), Skills (project knowledge), Plugins/Connectors (tool integration), Sub-agents (idea + validation separation)
- **Claude Code and Codex both have all five pieces now** — the shape is the same across tools
- **Agent harness engineering** is the cousin pattern: making the environment a single agent runs inside
- **Factory model** builds the software; loop engineering sits one floor above the harness
- **Token cost concerns remain valid** — usage patterns vary wildly based on token budget
- **Quality assurance still matters** — concerns about "slop" are legitimate

## The Five Pieces

1. **Automations** — Schedule-driven discovery and triage
2. **Worktrees** — Parallel agent isolation (no stepping on each other)
3. **Skills** — Codified project knowledge (not guessing)
4. **Plugins/Connectors** — Integration with existing tooling
5. **Sub-agents** — Separation between ideation and validation

## Key Quotes

> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops" — @bcherny, head of Claude Code at Anthropic

> "A year ago if you wanted a loop you wrote a pile of bash and maintained it forever. Now the pieces just ship inside the products."

## Notes

This is a foundational concept for scaling agent work. The shift from "human prompts agent" to "system prompts agent on schedule" is the paradigm change. Relates directly to autoresearch patterns and the harness engineering work in my CLAUDE.md.

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
