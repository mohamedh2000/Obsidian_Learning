---
title: "Compound Engineering v3.3.0 - Intent Verification"
url: "https://x.com/trevin/status/2049199159073550790?s=42"
platform: twitter
date_saved: 2026-04-29
source: "Trevin Chow (@trevin)"
content_type: tweet
topics: [ai-agents, developer-tools, agent-ux]
tags: [compound-engineering, agent-ux, intent-verification, scope-drift]
status: unread
---

> Show me what you think I asked for, before you spend 10 minutes on it. The cost of catching scope drift drops from "rerun the whole skill" to "edit a bullet."

| Metric | Count |
|--------|-------|
| Likes | 62 |

**Topics:** [[AI Agents]], [[Developer Tools]]

## Key Points

- **The Problem**: Agent skills could spend 5+ minutes producing polished plans built on wrong assumptions—painful to fix once baked into a dozen places
- **Solution**: /ce-brainstorm and /ce-plan now pause and play back what they heard before doing real work
- **Three-Part Playback**: Stated (what you literally said), Inferred (what agent assumes you also want), Out-of-scope (what it's deliberately leaving alone)
- **Ideate Improvements**: /ce-ideate now asks scoping questions upfront, tags ideas with grounding (direct evidence, external prior art, or reasoned argument)
- **Reduced Ceremony**: /ce-doc-review and /ce-code-review now auto-fix more issues instead of deferring everything to human review

## Design Philosophy

> "You're absolutely right" → "We can supervise about 3–5 agents" The goal: make the agent cheaper to correct and faster to trust.

## Connections

- Related to [[OpenAI Practical Agent Building Guide - cwolferesearch]] on instruction quality
- Part of [[Agent Architecture]] UX patterns
- See also human-agent collaboration patterns

*Filed in: [[Saved Links MOC]]*
