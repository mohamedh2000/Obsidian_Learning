---
title: "GEPA - Evolutionary Parameter Optimization Framework"
url: "https://github.com/gepa-ai/gepa"
platform: github
date_saved: 2026-06-09
source: "gepa-ai (@gepa-ai)"
content_type: repo
topics: [AI Agents, LLM Research, Developer Tools]
tags: [optimization, prompts, evolutionary-search, dspy, reflection, open-source]
status: unread
---

# GEPA - Evolutionary Parameter Optimization Framework

> LLM-based reflection and evolutionary search for optimizing any textual parameter — prompts, code, agent architectures, configs — with 90x cost reduction vs Claude Opus.

| | |
|---|---|
| **Source** | gepa-ai (@gepa-ai) |
| **Saved** | 2026-06-09 |
| **Type** | repo |
| **Engagement** | — |
| **URL** | [Link](https://github.com/gepa-ai/gepa) |

## Topics

[[AI Agents]] | [[LLM Research]] | [[Developer Tools]]

## Key Points

- **Reflection-based mutation**: LLMs diagnose execution failures and generate informed improvements
- **Pareto-efficient selection**: Maintains diverse candidates excelling on different task subsets
- **Minimal evaluations**: 100-500 evals vs 5,000-25,000+ for RL approaches
- **Universal applicability**: Works with as few as 3 examples, API-only models
- **Built-in adapters**: DSPy, RAG systems, LangChain, specialized tasks
- **Interpretable**: Human-readable optimization traces

## Results

| Metric | Value |
|--------|-------|
| Cost reduction | 90x vs Claude Opus 4.1 |
| Speed | 35x faster than RL |
| ARC-AGI accuracy | 32% → 89% |

## Quote

> "Both DSPy and especially GEPA are severely under hyped" — Tobi Lutke, Shopify CEO

## Tech Stack

- **Language**: Python
- **Dependencies**: LLM APIs (OpenAI, Anthropic, Google), DSPy
- **Integrations**: MLflow, Comet ML, Google ADK, Pydantic AI

## Research

- arXiv:2507.19457
- Authors from Berkeley, Stanford

## Notes

Connects directly to DSPy ecosystem. This is the optimization layer that tunes prompts/signatures automatically. Potential integration with agent harness work.

---

*Filed in: [[GitHub Repos MOC]] | [[Saved Links MOC]]*
