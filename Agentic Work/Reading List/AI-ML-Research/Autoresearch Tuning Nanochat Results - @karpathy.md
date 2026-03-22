---
title: "Autoresearch Tuning Nanochat Results - @karpathy"
url: "https://x.com/karpathy/status/2031135152349524125"
platform: twitter
date_saved: 2026-03-13
source: "Andrej Karpathy (@karpathy)"
content_type: showcase
topics: [autoresearch, neural-network-training, agent-swarms, nanochat]
tags: [twitter, ai, deep-learning]
status: unread
---

# Autoresearch Tuning Nanochat Results - @karpathy

> Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12 model. It found ~20 changes that improved the validation loss.

| | |
|---|---|
| **Source** | Andrej Karpathy (@karpathy) |
| **Saved** | 2026-03-13 |
| **Type** | showcase |
| **Engagement** | 19,215 likes, 2,110 retweets |
| **URL** | [Link](https://x.com/karpathy/status/2031135152349524125) |

## Topics

[[LLM Research]] | [[Fine-tuning & Training]]

## Key Points

- Autoresearch agent autonomously found ~20 improvements to nanochat validation loss over 2 days, all additive and transferable to larger models
- GPT-2 training time dropped from 2.02h to 1.80h (~11% improvement) by stacking agent-discovered changes
- Agent found real oversights: missing QKnorm scaler, missing Value Embedding regularization, conservative banded attention, misconfigured AdamW betas
- Vision: all LLM frontier labs will run agent swarms to collaboratively tune training at scale -- "the final boss battle"

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*