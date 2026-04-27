---
title: "DAIR.AI Top Papers April 2025 - DeepSeek V4 and Autogenesis"
url: "https://x.com/dair_ai/status/2048428649288712206?s=42"
platform: twitter
date_saved: 2025-04-27
source: "DAIR.AI (@dair_ai)"
content_type: tweet
topics: [llm-research, deepseek, self-evolving-agents, attention]
tags: [deepseek, v4, autogenesis, papers, llm, architecture]
status: unread
---

# DAIR.AI Top Papers April 2025 - DeepSeek V4 and Autogenesis

> "DeepSeek V4 is the first open model family built from the ground up around million-token contexts as a default rather than a bolt-on feature."

| | |
|---|---|
| **Source** | DAIR.AI (@dair_ai) |
| **Saved** | 2025-04-27 |
| **Type** | tweet |
| **Engagement** | 128 likes |
| **URL** | [Link](https://x.com/dair_ai/status/2048428649288712206?s=42) |

## Topics

[[LLM Architecture]] | [[AI Research Papers]]

## Key Papers

### 1. DeepSeek V4

First open model family with native 1M context length.

**Models:**
- DeepSeek-V4-Pro: 1.6T total / 49B active params
- DeepSeek-V4-Flash: 284B total / 13B active params

**Key Innovations:**

1. **Hybrid Attention (CSA + HCA)**
   - Compressed Sparse Attention (CSA): Compresses KV entries, applies DeepSeek Sparse Attention with sliding-window KV
   - Heavily Compressed Attention (HCA): Aggressive KV compression for extreme-context layers

2. **Training Stability at Trillion Scale**
   - Anticipatory Routing: Decouples backbone and router updates
   - SwiGLU Clamping: Bounds linear and gate components

3. **Domain-Specialist Post-Training**
   - Separate specialist expert per domain
   - SFT → GRPO RL with domain-specific reward models
   - Merge specialists into final model

**Performance:** V4-Pro-Max beats GPT-5.2 and Gemini 3.0-Pro, trails GPT-5.4 and Gemini 3.1-Pro by ~3-6 months.

### 2. Autogenesis

Self-evolving agent protocol for autonomous capability expansion.

**Architecture:**
- Resource Substrate Protocol Layer (RSPL): Standardizes access to prompts, tools, environments, memory
- Self-Evolution Protocol Layer (SEPL): Generate → Reflect → Improve → Evaluate loop

Agents identify capability gaps, generate improvements, validate through testing, integrate back.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
