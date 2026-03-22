---
title: "State of RL for Reasoning LLMs"
url: "https://aweers.de/blog/2026/rl-for-llms/"
platform: web
date_saved: 2026-03-16
source: "A. Weers"
content_type: research
topics: [llm-research, fine-tuning-training]
tags: [ai, reinforcement-learning, llm, research]
status: unread
---

# State of RL for Reasoning LLMs

> A comprehensive technical overview of reinforcement learning methods for LLMs, tracing developments from PPO through recent innovations like CISPO and MaxRL.

| | |
|---|---|
| **Source** | A. Weers |
| **Saved** | 2026-03-16 |
| **Type** | research |
| **URL** | [Link](https://aweers.de/blog/2026/rl-for-llms/) |

## Topics

[[LLM Research]] | [[Fine-tuning & Training]]

## Key Points

- Critic-free approaches dominate: methods since PPO have eliminated learned value functions in favor of simpler baselines (group means, leave-one-out), reducing memory costs by ~50% while maintaining or improving performance
- Loss aggregation matters significantly: sequence-level reward averaging combined with sample normalization introduces subtle biases; token-level or prompt-level aggregation provides cleaner learning signals
- Trust regions need rethinking: PPO's symmetric clipping works surprisingly well, but recent methods challenge this with asymmetric bounds (DAPO), weight-clipping (CISPO), or divergence-based masking (DPPO)
- Standard deviation normalization is problematic: dividing advantages by group standard deviation over-weights nearly-solved problems; removing this component improves asymptotic performance
- Unresolved challenges remain: credit assignment at token-level, sample efficiency, hard problem handling, and empirical reliability across different model families

## Notes

(Personal annotations)

---

*Filed in: [[Blog Posts]] | [[Saved Links MOC]]*