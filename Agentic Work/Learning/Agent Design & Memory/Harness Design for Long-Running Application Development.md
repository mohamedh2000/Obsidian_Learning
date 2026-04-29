---
title: "Harness Design for Long-Running Application Development"
url: "https://www.anthropic.com/engineering/harness-design-long-running-apps"
platform: web
date_saved: 2026-03-25
source: "Prithvi Rajasekaran (Anthropic)"
content_type: guide
topics: [agent-harnesses, multi-agent-evaluation, context-resets]
tags: [web, anthropic, ai-agents, learning, harness-curriculum]
status: unread
---

# Harness Design for Long-Running Application Development

> Anthropic's March 24, 2026 engineering post explains how better harness design pushed Claude further on long-running app builds by combining context resets with generator-evaluator style agent structures.

| | |
|---|---|
| **Source** | Prithvi Rajasekaran (Anthropic) |
| **Saved** | 2026-03-25 |
| **Type** | guide |
| **Engagement** | not published, not published |
| **URL** | [Link](https://www.anthropic.com/engineering/harness-design-long-running-apps) |

## Topics

[[AI Agents]] | [[Claude Code & Anthropic]]

## Key Points

- The article connects two threads of work: improving frontend-design quality and improving fully autonomous long-running application development.
- It argues that context resets plus structured handoff artifacts work better than simple compaction for long tasks because they avoid context anxiety and coherence loss.
- Anthropic describes a planner-generator-evaluator style setup where evaluation criteria and independent critique are part of the harness rather than left to a single agent.

## Notes

(Personal annotations)

---

*Filed in: [[Learning MOC]] | [[Saved Links MOC]]*
