---
title: "Claude Code in Large Codebases - Best Practices"
url: "https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start"
platform: web
date_saved: 2026-05-18
source: "Anthropic Applied AI Team"
content_type: guide
topics: [claude-code, agent-harness, enterprise-ai, codebase-navigation]
tags: [anthropic, claude-code, best-practices, enterprise, harness]
status: unread
---

# Claude Code in Large Codebases - Best Practices

> Agentic search over local files beats RAG for codebases—Claude Code follows references like an engineer rather than relying on stale embeddings.

| | |
|---|---|
| **Source** | Anthropic Applied AI Team |
| **Saved** | 2026-05-18 |
| **Type** | guide |
| **Published** | May 14, 2026 |
| **URL** | [Link](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) |

## Topics

[[Claude Code & Anthropic]] | [[AI Agents]] | [[Agent Harness Design]]

## Key Points

- **Agentic search > RAG**: Claude Code traverses files locally and follows references like an engineer, avoiding stale indices that plague RAG systems.
- **The Harness Framework**: Five extension points—CLAUDE.md files, hooks, skills, plugins, MCP servers, LSP integrations, and subagents.
- **Configuration patterns**: Keep CLAUDE.md lean and layered; initialize in subdirectories; scope test/lint commands per directory; use `.claudeignore` for generated files.
- **Organizational success**: Requires dedicated infrastructure investment before broad rollout with clear ownership (infrastructure team or designated DRI).

## The Harness Extension Points

1. **CLAUDE.md files** — context loaded per session
2. **Hooks** — automation at key moments
3. **Skills** — specialized expertise on-demand
4. **Plugins** — distributable, packaged configurations
5. **MCP servers** — connections to internal tools
6. **LSP integrations** — symbol-level code intelligence
7. **Subagents** — isolated instances for specific tasks

## Notes

(Personal annotations)

---

*Filed in: [[Agent Design & Memory MOC]] | [[Saved Links MOC]]*
