---
title: "Agent Harness Optimization Guide"
url: "https://x.com/thealexker/status/2045203785304232162?s=42"
platform: twitter
date_saved: 2026-04-18
source: "Alex Ker (@thealexker)"
content_type: guide
topics: [agent harnesses, LLM agents, prompt engineering]
tags: [harness, agents, claude, config, subagents, RPI-framework]
status: unread
---

# Agent Harness Optimization Guide

> Harnesses are everything. If the model is the source of intelligence, then the harness is what makes that intelligence useful.

| | |
|---|---|
| **Source** | Alex Ker (@thealexker) |
| **Saved** | 2026-04-18 |
| **Type** | guide |
| **Engagement** | 620 likes, 80 retweets |
| **URL** | [Link](https://x.com/thealexker/status/2045203785304232162?s=42) |

## Topics

[[Agent Design]] | [[Prompt Engineering]] | [[LLM Configuration]]

## Key Points

- **Harness = scaffolding** that manages context in stateless LLMs via sessions and compressions, and handles tool calls, I/O processing, and guardrails
- **Keep .md files lean and human-written**: LLM-generated system prompts degrade performance while costing ~20% more in inference (ETH research)
- **Instruction budget**: Frontier LLMs can only follow a few hundred instructions before entering the "dumb zone" — too many instructions encourage hallucination
- **Progressive Disclosure**: Only pull context when needed; give .md files descriptive names so agents know what exists
- **R.P.I. Framework**: Structure prompts so models approach problems like staff engineers
- **Subagents**: Use them to keep main context window clean

## Notes

Relevant harnesses mentioned: Roo Code, DeepAgent CLI, HumanLayer

Quote from Kyle (HumanLayer): Frontier thinking LLMs can only follow a few hundred instructions before missing relevant ones amongst the bloat.

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
