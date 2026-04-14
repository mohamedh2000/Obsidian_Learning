---
title: "Auto-Inference Optimiser for LLM Inference - @manthanguptaa"
url: "https://x.com/manthanguptaa/status/2036785420349174073?s=42"
platform: twitter
date_saved: 2026-03-25
source: "Manthan Gupta (@manthanguptaa)"
content_type: tweet
topics: [llm-inference, autoresearch, mlx]
tags: [twitter, llm, inference, developer-tools]
status: unread
---

# Auto-Inference Optimiser for LLM Inference - @manthanguptaa

> Manthan Gupta applies Karpathy's autoresearch idea to MLX inference, using an AI coding agent to search for speed improvements inside a tightly bounded benchmark harness.

| | |
|---|---|
| **Source** | Manthan Gupta (@manthanguptaa) |
| **Saved** | 2026-03-25 |
| **Type** | tweet |
| **Engagement** | 308 likes, 25 retweets |
| **URL** | [Link](https://x.com/manthanguptaa/status/2036785420349174073?s=42) |

## Topics

[[LLM Research]] | [[Developer Tools]]

## Key Points

- The repo design is intentionally constrained: `prepare.py` locks the evaluation harness and quality gates, while `inference.py` is the only file the agent is allowed to mutate.
- The workflow is a practical example of hill-climbing on real hardware, with the agent keeping or reverting changes based on measured throughput and quality outcomes.
- The post is useful as a pattern for trustworthy agent-driven optimization because it emphasizes fixed evals, narrow search surfaces, and automated rollback.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
