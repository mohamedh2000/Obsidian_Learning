---
title: "Meta-Harness Framework Open Source"
url: "https://x.com/alphasignalai/status/2048371802343149600?s=42"
platform: twitter
date_saved: 2026-04-26
source: "AlphaSignal AI (@alphasignalai)"
content_type: tweet
topics: [AI Agents, Developer Tools]
tags: [meta-harness, stanford, agent-optimization, scaffolding, harness]
status: unread
---

> Stanford just turned the Meta-Harness paper into open source code. A framework that automatically optimizes the scaffolding around a fixed base model.

| Metric | Count |
|--------|-------|
| Likes | 13 |
| Retweets | 1 |

**Topics:** [[AI Agents]], [[Developer Tools]]

## Key Points
- Meta-Harness: auto-optimizes agent scaffolding (memory, retrieval, context)
- Based on Stanford research paper, now open source
- Coding agent acts as the proposer with full filesystem access
- Reads prior attempts, traces, and scores to iterate

### How It Works
1. Proposer agent gets access to ALL prior history files
2. Reads old traces to form hypotheses about failures
3. On Terminal-Bench 2.0: median 82 files read per attempt
4. Unlike reward-only systems, preserves full signal

### Onboarding Flow
1. Point agent at ONBOARDING.md
2. Have a conversation
3. Get domain spec
4. Start iterating

### Key Insight
> "The framework is itself a harness that optimizes harnesses"

Ships with reference experiments including text classification memory search.

*Filed in: [[Saved Links MOC]]*
