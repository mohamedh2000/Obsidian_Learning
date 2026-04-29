---
title: "DAIR.AI Top AI Papers Week April 2026"
url: "https://x.com/dair_ai/status/2045883132419645456?s=42"
platform: twitter
date_saved: 2026-04-23
source: "DAIR.AI (@dair_ai)"
content_type: guide
topics: [AI Research, Agent Design, Autonomous Research]
tags: [dair-ai, papers, automated-research, aiscientist, weak-to-strong]
status: unread
---

> Top AI Papers of the Week (April 13-19) covering Automated Weak-to-Strong Researcher and AiScientist.

| Metric | Count |
|--------|-------|
| Likes | 169 |
| Retweets | 27 |

**Topics:** [[AI Research]], [[Agent Design]], [[Autonomous Research]]

## Paper 1: Automated Weak-to-Strong Researcher (Anthropic)
- Claude runs fully autonomous progress on scalable oversight research
- Team of parallel Automated Alignment Researchers (AARs) built on Claude Opus 4.6
- AARs propose ideas, run experiments, iterate on weak-to-strong supervision
- **Performance Gap Recovered (PGR)**: 0-1 score where 0 = weak teacher, 1 = ground-truth-supervised student
- Human researchers achieved PGR 0.23 after 7 days
- **AARs reached PGR 0.97 in 5 days** with 800 cumulative agent-hours at ~$18K cost
- Forum-based collaboration: each AAR works in isolated sandbox, shares findings to common forum
- **Warning**: Agents sometimes succeeded through reward-hacking behaviors

## Paper 2: AiScientist
- Long-horizon AI research agents as state-management problem
- **Thin control, thick state** principle
- Top-level orchestrator manages stage-level progress
- Specialized agents ground themselves in durable workspace artifacts
- **File-as-Bus coordination**: Routes through durable filesystem artifacts, not in-context message passing
- Analyses, plans, code, logs, evidence live as versioned files in permission-scoped workspace
- Specialists can reconstruct context from scratch without replaying conversations

*Filed in: [[Saved Links MOC]]*
