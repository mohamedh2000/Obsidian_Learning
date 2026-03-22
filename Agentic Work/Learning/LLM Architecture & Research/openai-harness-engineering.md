---
title: "Harness Engineering: Leveraging Codex in an Agent-First World"
url: "https://openai.com/index/harness-engineering/"
platform: web
date_saved: 2026-03-13
source: "OpenAI"
content_type: guide
topics: [codex, harness-engineering, agentic-systems]
tags: [openai, codex, engineering]
status: unread
---

# Harness Engineering: Leveraging Codex in an Agent-First World

> OpenAI's harness engineering write-up argues that human leverage now comes less from writing code directly and more from designing the repository, tools, and feedback loops that let agents ship reliably.

OpenAI's methodology for structuring codebases so autonomous AI agents can safely and effectively work on them. The article focuses on the scaffolding layer: repository knowledge, architecture enforcement, observability, and automated review loops that make agent work legible and trustworthy.

## Key Points

- OpenAI describes building and shipping a real product with Codex writing application code, tests, CI, documentation, tooling, and observability artifacts instead of humans writing code directly.
- A central lesson is that repository-local knowledge must be the system of record: short `AGENTS.md` files should point to deeper docs, while architecture and taste invariants are enforced mechanically.
- Agent effectiveness improved as more of the application became legible in-repo and in-tooling, including bootable worktrees, browser automation, logs, metrics, and traces.

## Related
- [[karpathy-autoresearch]]
- [[karpathy-tweet]]
- [[omarsar0-tweet]]
- [[spectral-clustering]]
- [[tree-sitter-ast-parsing]]

## Why saved
<!-- Fill in when you remember why this caught your eye -->

## Notes
<!-- Fill in after reading -->
