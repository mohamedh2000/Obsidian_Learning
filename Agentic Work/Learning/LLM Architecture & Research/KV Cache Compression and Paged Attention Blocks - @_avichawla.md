---
title: "KV Cache Compression and Paged Attention Blocks - @_avichawla"
url: "https://x.com/_avichawla/status/2070828078247604480?s=42"
platform: twitter
date_saved: 2026-06-27
source: "Avi Chawla (@_avichawla)"
content_type: guide
topics: [LLM Inference, KV Cache]
tags: [twitter, kv-cache, vllm, paged-attention, flashattention, inference, triattention]
status: unread
---

# KV Cache Compression and Paged Attention Blocks - @_avichawla

> Avi Chawla explained why evicting most KV cache tokens may not reduce GPU memory when production servers allocate cache in fixed paged-attention blocks.

| | |
|---|---|
| **Source** | Avi Chawla (@_avichawla) |
| **Saved** | 2026-06-27 |
| **Type** | guide |
| **Engagement** | 1295 likes, 179 retweets |
| **URL** | [Link](https://x.com/_avichawla/status/2070828078247604480?s=42) |

## Topics

[[LLM Inference]] | [[KV Cache]]

## Key Points

- Token-level KV eviction can leave nearly every physical block partially occupied, so the allocator frees little or no GPU memory.
- Production fast attention kernels often do not retain the attention scores that many eviction methods need.
- NVIDIA TriAttention is cited as addressing both scoring and compaction by using pre-RoPE key/query geometry and periodic cache compaction.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
