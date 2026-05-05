---
title: "Autodata - Agentic Data Scientist for Training Data"
url: "https://x.com/dair_ai/status/2051311905353142328?s=42"
platform: twitter
date_saved: 2026-05-05
source: "DAIR.AI (@dair_ai)"
content_type: tweet
topics: [agent-data-generation, self-instruct, training-data]
tags: [meta-fair, autodata, agentic-loop, self-optimization]
status: unread
---

# Autodata - Agentic Data Scientist for Training Data

> Meta FAIR introduces Autodata, an agentic data scientist that builds high-quality training and evaluation data autonomously through an orchestrator-challenger-judge loop.

| | |
|---|---|
| **Source** | DAIR.AI (@dair_ai) |
| **Saved** | 2026-05-05 |
| **Type** | tweet |
| **Engagement** | 196 likes, 35 retweets |
| **URL** | [Link](https://x.com/dair_ai/status/2051311905353142328?s=42) |

## Topics

[[Agent Design & Memory]] | [[RLHF & RL Training]]

## Key Points

- **Headline Result**: On CS research QA task, Agentic Self-Instruct produces 34-point gap between weak and strong solvers (43.7% vs 77.8%), while standard CoT Self-Instruct produces only 1.9-point gap
- **The Method**: Orchestrator LLM directs challenger agent to generate examples grounded in domain documents; weak and strong solver attempt them; judge scores outputs; orchestrator analyzes failures and prompts regeneration
- **Meta-Optimization**: Outer loop tunes agent instructions based on which harness changes lift validation pass rate — from 12.8% to 42.4% over 126 iterations
- **Scale**: Processed 10,000+ CS papers and produced 2,117 quality-filtered QA pairs
- **Key Insight**: Reframes data generation as an agent loop — more inference compute = harder data = better downstream RL lift

## Notes

Blog: https://facebookresearch.github.io/RAM/blogs/autodata/

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
