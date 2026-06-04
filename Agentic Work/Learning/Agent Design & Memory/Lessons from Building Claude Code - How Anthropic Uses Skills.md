---
title: "Lessons from Building Claude Code - How Anthropic Uses Skills"
url: "https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills"
platform: web
date_saved: 2026-06-04
source: "Thariq Shihipar (Anthropic)"
content_type: guide
topics: [agent-design, skills, claude-code, orchestration]
tags: [anthropic, claude-code, skills-framework, agent-patterns, best-practices]
status: unread
---

# Lessons from Building Claude Code - How Anthropic Uses Skills

> Practical insights from Anthropic on building and scaling hundreds of skills for Claude Code, including a framework for categorizing skills, best practices, and measurement approaches.

| | |
|---|---|
| **Source** | Thariq Shihipar (Anthropic) |
| **Saved** | 2026-06-04 |
| **Type** | guide |
| **Published** | June 3, 2026 |
| **URL** | [Link](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) |

## Topics

[[Agent Design & Memory]] | [[Claude-Anthropic-AI-Coding]]

## Key Points

- **Skills are folders, not just markdown** — They can include scripts, assets, and data that agents discover and use, with configuration options and dynamic hooks
- **Nine skill categories**: library references, verification, data fetching, automation, scaffolding, code quality, CI/CD, runbooks, infrastructure
- **Avoid stating the obvious** — Skills should emphasize information that pushes Claude out of its normal way of thinking
- **Gotchas sections matter most** — The highest-value skill content captures common failure points Claude encounters
- **Progressive disclosure strategy** — Organize skills using folder structure and cross-references so Claude accesses detailed information contextually
- **Let Claude adapt** — Provide necessary information while avoiding overly specific instructions that limit flexibility
- **Memory and state tracking** — Skills can store data in logs or JSON files to help Claude remember previous executions
- **Marketplace governance** — Successful skills emerge organically; users sandbox new skills before moving to official marketplaces

## Notes

(Personal annotations)

---

*Filed in: [[Learning MOC]] | [[Saved Links MOC]]*
