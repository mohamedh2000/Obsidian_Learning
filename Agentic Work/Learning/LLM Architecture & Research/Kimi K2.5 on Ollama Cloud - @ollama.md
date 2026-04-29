---
title: "Kimi K2.5 on Ollama Cloud - @ollama"
url: "https://x.com/ollama/status/2016086374005538932?s=42"
platform: twitter
date_saved: 2026-01-27
source: "ollama (@ollama)"
content_type: tweet
topics: [LLM Models, AI Agents]
tags: [twitter, ollama, kimi-k2.5, local-llm, claude-code, codex, open-code, model-hosting]
status: unread
---

> Ollama announces Kimi K2.5 is available on Ollama's cloud, with direct integration to Claude Code, Codex, OpenCode, and other agent tools via `ollama launch`.

| Metric | Count |
|--------|-------|
| Likes | 4,983 |
| Retweets | 374 |

**Topics:** [[LLM Architecture & Research]], [[AI Agents]]

## Key Points
- Kimi K2.5 is now hosted on Ollama's cloud infrastructure, accessible via `ollama run kimi-k2.5:cloud`
- Integrates directly with major coding agents: Claude Code, Codex, OpenCode, Clawdbot, and Droid
- The `ollama launch claude --model kimi-k2.5:cloud` pattern enables swapping underlying models in agent harnesses
- 5K likes signals strong community interest in using alternative models within familiar agent interfaces

### Usage
```bash
# Run Kimi K2.5 directly
ollama run kimi-k2.5:cloud

# Launch Claude Code backed by Kimi K2.5
ollama launch claude --model kimi-k2.5:cloud
```

### Why It Matters
This exemplifies the harness-model separation: the coding agent (Claude Code, Codex) provides the harness, skills, and tools — while the underlying model becomes swappable. This decoupling lets users experiment with different models without losing their workflow.

*Filed in: [[Saved Links MOC]]*
