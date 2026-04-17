---
title: "LLM-as-a-Verifier Scoring Granularity - @cwolferesearch"
url: "https://x.com/cwolferesearch/status/2044555271792406577?s=42"
platform: twitter
date_saved: 2026-04-17
source: "Cameron R. Wolfe, Ph.D. (@cwolferesearch)"
content_type: guide
topics: [llm-reasoning, evaluation, verification]
tags: [llm-as-judge, verifiers, logprobs, scoring, best-practices, rlhf]
status: unread
---

# LLM-as-a-Verifier Scoring Granularity - @cwolferesearch

> Increasing scoring granularity makes the verifier more effective - LLMs now handle fine-grained scores (1-100) better than before, potentially obsoleting the old best practice of using coarse scales (binary, 1-5 Likert).

| | |
|---|---|
| **Source** | Cameron R. Wolfe, Ph.D. (@cwolferesearch) |
| **Type** | guide |
| **Engagement** | 852 likes, 84 retweets |
| **URL** | [Link](https://x.com/cwolferesearch/status/2044555271792406577?s=42) |

## Topics

[[LLM Evaluation]] | [[Verification]] | [[RLHF]]

## Key Points

- Old best practice: lower scoring granularity (binary, ternary, 1-5 Likert) worked better than granular scores (1-100)
- New finding: frontier LLMs now handle fine-grained scoring, making old advice potentially obsolete
- Logprob-based scoring setup: compute logprob of each score token, take weighted average
- Reward formula: `Reward = (1 / CK) * ∑ score_logprob * score_value` across C criteria, K verifications, G granularity levels
- Consistent gains from: increasing scoring granularity G, repeated verifications K, more evaluation criteria C
- Round-robin tournament used for pairwise verification to select best trajectory among N candidates

## Notes

Important shift in LLM-as-a-Judge best practices. The logprob-based weighted averaging approach is key to unlocking higher granularity benefits.

---

*Filed in: [[Learning MOC]] | [[Saved Links MOC]]*
