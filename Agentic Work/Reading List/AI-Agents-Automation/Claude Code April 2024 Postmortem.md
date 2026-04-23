---
title: "Claude Code April 2024 Postmortem"
url: "https://www.anthropic.com/engineering/april-23-postmortem"
platform: web
date_saved: 2026-04-23
source: "Anthropic Engineering"
content_type: guide
topics: [claude-code, anthropic, post-mortem]
tags: [ai-tools, debugging, transparency, engineering]
status: unread
---

# Claude Code April 2024 Postmortem

> Anthropic identified and resolved three separate bugs that degraded Claude Code performance between March and April 2024, each affecting different user segments on different schedules.

| | |
|---|---|
| **Source** | Anthropic Engineering |
| **Saved** | 2026-04-23 |
| **Type** | guide |
| **Engagement** | - |
| **URL** | [Link](https://www.anthropic.com/engineering/april-23-postmortem) |

## Topics

[[AI-Agents-Automation MOC]] | [[Developer Tools]]

## Key Points

- **Reasoning Effort Change (March 4 - April 7)**: Default reasoning switched from "high" to "medium" to reduce latency; reverted after user reports of decreased intelligence
- **Caching Bug (March 26 - April 10)**: Prompt caching optimization had bug that continuously dropped thinking history every turn, making Claude forgetful and repetitive
- **Verbosity Prompt (April 16 - April 20)**: System prompt instruction to reduce output caused unexpected 3% performance loss; immediately reverted
- **Detection Challenges**: Each bug affected different user segments on different schedules, making aggregate effect appear like broad degradation
- **Preventive Measures**: Stricter controls including broader per-model evaluations, improved Code Review tooling, and gradual rollout procedures

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
