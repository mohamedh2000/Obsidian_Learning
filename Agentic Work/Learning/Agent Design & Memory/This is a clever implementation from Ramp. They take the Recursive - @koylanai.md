---
title: "This is a clever implementation from Ramp. They take the Recursive - @koylanai"
url: "https://x.com/koylanai/status/2044053004924420450?s=42"
platform: twitter
date_saved: 2026-04-14
source: "Muratcan Koylan (@koylanai)"
content_type: social
topics: [AI Agents, Agent Memory, Prompt Engineering]
tags: [twitter, ai-agents, memory, prompt-engineering, llm-research]
status: unread
---

# This is a clever implementation from Ramp. They take the Recursive - @koylanai

> This is a clever implementation from Ramp. They take the Recursive Language Model setup and make the worker semi-stateful across recursive calls, without replaying the full reasoning trace as text.

| | |
|---|---|
| **Source** | Muratcan Koylan (@koylanai) |
| **Saved** | 2026-04-14 |
| **Type** | social |
| **Engagement** | 161 likes, 10 retweets |
| **URL** | [Link](https://x.com/koylanai/status/2044053004924420450?s=42) |

## Topics

[[AI Agents]] | [[Agent Memory]] | [[Prompt Engineering]]

## Key Points

- This is a clever implementation from Ramp. They take the Recursive Language Model setup and make the worker semi-stateful across recursive calls, without replaying the full reasoning trace as text.
- Instead of summarizing prior reasoning, retrieving chunks with RAG, or passing the full history every time, run the orchestrator’s trajectory through the worker, use the current task prompt to score what matters, keep the useful parts of the worker’s KV cache, and initialize the next call with that compacted latent state.
- - Inter-agent memory should be selective, not exhaustive
- - Canonical facts should be separated from scratch reasoning

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
