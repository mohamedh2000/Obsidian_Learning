---
title: "Verbalized Sampling: Recover LLM Creativity Lost to Alignment"
url: "https://x.com/dailydoseofds_/status/2074425700988465438?s=42"
platform: twitter
date_saved: 2026-07-08
source: "Daily Dose of Data Science (@dailydoseofds_)"
content_type: tweet
topics: [prompt-engineering, verbalized-sampling, rlhf, mode-collapse]
tags: [twitter, dailydoseofds_, prompting, rlhf, diversity, stanford]
status: unread
---

# Verbalized Sampling: Recover LLM Creativity Lost to Alignment

> A ~20-word, training-free prompt tweak — ask for a *distribution* of responses with probabilities — boosts LLM creativity 1.6–2.1x by undoing the mode collapse that RLHF introduces.

| | |
|---|---|
| **Source** | Daily Dose of Data Science (@dailydoseofds_) |
| **Saved** | 2026-07-08 |
| **Type** | Tweet |
| **Engagement** | 121 likes, 13 retweets |
| **URL** | [Link](https://x.com/dailydoseofds_/status/2074425700988465438?s=42) |

## Topics

[[Prompt Engineering]] | [[RLHF & RL Training]]

## Key Points

- Post-training alignment (RLHF) makes LLMs helpful/safe but causes **mode collapse** — a drop in output diversity toward predictable, stereotypical responses.
- Root cause is **typicality bias** in human preference data: annotators favor familiar, easy-to-read, predictable answers, so the reward model sharpens the distribution toward already-likely responses.
- The pre-trained "rich distribution" personality still exists inside the model; alignment just suppresses it.
- **Verbalized Sampling (VS):** instead of "Tell me a joke," prompt "Generate 5 responses with their corresponding probabilities. Tell me a joke." Asking for a *distribution* (not an instance) forces the model to tap its broader pre-trained knowledge.
- Results: 1.6–2.1x more diverse than direct prompting while maintaining/improving quality; +25.7% human-rated diversity; restores 66.8% of lost creativity; beats a fine-tuned model with no retraining.
- Variants VS-CoT and VS-Multi push diversity further.

## Notes

Paper: https://arxiv.org/abs/2510.01171 — Stanford. Training-free, so it's a pure prompt-engineering lever; cross-filed conceptually under RLHF because it directly counteracts an alignment side effect.

(Personal annotations)

---

*Filed in: [[Learning MOC]] | [[Twitter Posts MOC]] | [[Saved Links MOC]]*
