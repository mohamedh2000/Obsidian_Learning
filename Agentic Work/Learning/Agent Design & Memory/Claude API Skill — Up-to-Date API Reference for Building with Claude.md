---
title: "Claude API Skill — Up-to-Date API Reference for Building with Claude"
url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill"
platform: web
date_saved: 2026-06-30
source: "Anthropic (platform.claude.com docs)"
content_type: guide
topics: [agent-skills, claude-api]
tags: [anthropic, claude-api, agent-skills, sdk, managed-agents, progressive-disclosure]
status: unread
---

# Claude API Skill — Up-to-Date API Reference for Building with Claude

> An open-source Agent Skill that equips Claude with current API reference material, SDK docs, and best practices for the Messages API and Claude Managed Agents.

| | |
|---|---|
| **Source** | Anthropic (platform.claude.com docs) |
| **Saved** | 2026-06-30 |
| **Type** | guide |
| **URL** | [Link](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) |

## Topics

[[Agent Skills]] | [[Claude API]]

## Key Points

- **Two surfaces covered:** the Messages API (single requests, streaming, tool use, batch, prompt caching, structured outputs, custom agent loops) and Claude Managed Agents (beta) — Anthropic-hosted stateful agents with persistent configs and per-session sandboxes
- **Eight languages:** Python, TypeScript, C#, Go, Java, PHP, Ruby, and cURL, with tool-runner support in beta for all but cURL
- **Progressive disclosure:** loads only the docs relevant to your language, surface, and task (tool use, streaming, batches) rather than everything at once
- **Bundled with Claude Code** and installable from the open-source Anthropic skills repo (`npx skills add ...` or as a plugin); activates automatically when a project imports an Anthropic SDK or when you ask Claude to build/debug/optimize with the API
- **Model migration built in:** `/claude-api migrate ... to claude-opus-4-8` handles model ID swaps, breaking param changes (removing temperature/top_p/top_k, converting manual thinking to adaptive), beta-header cleanup, effort calibration, prefill→structured-outputs, and refusal-fallback setup, emitting a manual-verification checklist

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
