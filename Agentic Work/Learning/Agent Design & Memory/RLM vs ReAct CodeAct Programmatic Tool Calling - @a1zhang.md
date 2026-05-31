---
title: "RLM vs ReAct CodeAct Programmatic Tool Calling"
url: "https://x.com/a1zhang/status/2060933445191168030?s=42"
platform: twitter
date_saved: 2026-05-31
source: "alex zhang (@a1zhang)"
content_type: tweet
topics: [rlm, agent-design, tool-calling, harness-architecture]
tags: [rlm, react, codeact, tool-calling, agent-harness, model-harness-codesign]
status: unread
---

# RLM vs ReAct CodeAct Programmatic Tool Calling

> Analysis of the differences between RLM-style programmatic tool calling and traditional ReAct JSON tool calls.

| | |
|---|---|
| **Source** | alex zhang (@a1zhang) |
| **Saved** | 2026-05-31 |
| **Type** | tweet |
| **Engagement** | 55 likes, 6 retweets |
| **URL** | [Link](https://x.com/a1zhang/status/2060933445191168030?s=42) |

## Topics

[[AI Agents]] | [[LLM Research]]

## Key Points

- RLM changes what LLMs should condition on and output vs traditional approaches
- **Model-harness codesign** is extremely important for modern AI products
- ReAct vs CodeAct debate: JSON tool calls vs functions in code
- CodeAct lost to ReAct in 2024-2026, affecting harness infrastructure built since
- RLMs push for "Programmatic Tool Calling" (PTC) style
- Emphasis on: **context as an object** + **sub-calls as a function**

## Historical Context

- RLM-style patterns existed pre-October 2025 but were poor design decisions for production
- Community acceptance of standards (like ReAct) has ripple effects on future models and infra
- Similar to MITO vs TITO debate - simple ideas with long-term infrastructure implications

## Why This Matters

- RLMs currently show "sparks of potential" on frontier models for long-context tasks
- Significant work needed:
  - **Infra side**: guardrails, sandboxing, training
  - **Model training side**: models that are good at this style of thinking
- Formalizing ideas is important to justify pushing in this direction

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
