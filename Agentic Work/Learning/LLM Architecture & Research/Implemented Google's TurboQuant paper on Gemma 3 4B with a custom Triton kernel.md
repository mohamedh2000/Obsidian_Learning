---
title: "Implemented Google's TurboQuant paper on Gemma 3 4B with a custom Triton kernel…"
url: "https://x.com/dejanseo/status/2036697911262908912"
platform: twitter
date_saved: 2026-03-26
source: "DEJAN (@dejanseo)"
content_type: tweet
topics: [Prompt Engineering]
tags: [twitter, dejanseo]
status: unread
---

# Implemented Google's TurboQuant paper on Gemma 3 4B with a custom Triton kernel…

> Implemented Google's TurboQuant paper on Gemma 3 4B with a custom Triton kernel for fused quantized attention. It's real.

| | |
|---|---|
| **Source** | DEJAN (@dejanseo) |
| **Saved** | 2026-03-26 |
| **Type** | tweet |
| **Engagement** | 1052 likes, 82 retweets |
| **URL** | [Link](https://x.com/dejanseo/status/2036697911262908912) |

## Topics

[[Prompt Engineering]]

## Key Points

- Implemented Google's TurboQuant paper on Gemma 3 4B with a custom Triton kernel for fused quantized attention.
- It's real.
- Results on RTX 4090:
- 2-bit FUSED: character-for-character identical to fp16 baseline.

## Tweet

Implemented Google's TurboQuant paper on Gemma 3 4B with a custom Triton kernel for fused quantized attention. 

It's real.

Results on RTX 4090:

2-bit FUSED: character-for-character identical to fp16 baseline. On every prompt. At 16x theoretical compression.

The Triton kernel reads uint8 key indices directly — never materializes fp16 keys. Pre-rotate query once (R is orthogonal so ⟨q, Rᵀ·centroids[idx]⟩ = ⟨R·q, centroids[idx]⟩), then per-position work is just a table lookup + dot.

Speed (avg tok/s across 3 prompts):
→ fp16 baseline: 17.7
→ 4-bit fused: 16.5 (-7%)
→ 2-bit fused: 17.7 (0% — matches baseline)

VRAM (KV cache delta):
→ fp16: 26 MB
→ 4-bit fused: 4 MB
→ 2-bit fused: 7 MB

The paper's theoretical guarantees hold up completely in practice. Zero accuracy loss, zero speed loss, fraction of the memory.

Paper: http://arxiv.org/abs/2504.19874

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
