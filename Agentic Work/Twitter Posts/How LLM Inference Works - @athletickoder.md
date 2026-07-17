---
title: "How LLM Inference Works - @athletickoder"
url: "https://x.com/athletickoder/status/2072674178311057783?s=42"
platform: twitter
date_saved: 2026-07-02
source: "anshuman (@athletickoder)"
content_type: tweet
topics: [llm-inference, transformers, serving]
tags: [twitter, llm-inference, kv-cache, batching, vllm]
status: unread
---

# How LLM Inference Works - @athletickoder

> A 1600-word note building LLM inference up from first principles — attention, KV caching, chunked prefill, and continuous batching.

| | |
|---|---|
| **Source** | anshuman (@athletickoder) |
| **Saved** | 2026-07-02 |
| **Type** | tweet |
| **Engagement** | 479 likes, 60 retweets |
| **URL** | [Link](https://x.com/athletickoder/status/2072674178311057783?s=42) |

## Topics

[[LLM Research]] | [[LLM Inference]]

## Key Points

- Attention is the only place tokens interact.
- KV caching is why decoding is cheap once prefill is done.
- Chunked prefill handles prompts too big to fit in memory.
- Naive batching wastes throughput on padding; continuous batching combines ragged batching with dynamic scheduling.
- These techniques quietly power vLLM, SGLang, and every modern serving stack.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
