---
title: "How AI Actually Remembers - KV Cache Guide"
url: "https://x.com/pseudo_sid26/status/2049175615195242821?s=42"
platform: twitter
date_saved: 2026-04-29
source: "Siddharth (@Pseudo_Sid26)"
content_type: tweet
topics: [llm-architecture, memory, kv-cache]
tags: [transformer, attention, memory, kv-cache, streamingllm]
status: unread
---

> Most agent memory bugs aren't retrieval bugs—the memory was wrong before retrieval ever ran. It was wrong at token 4,096, when something important quietly left the cache.

| Metric | Count |
|--------|-------|
| Likes | 121 |

**Topics:** [[LLM Research]], [[AI Agents]]

## Key Points

- **Token-Level Memory**: Every token processed runs through attention, scoring each token in context. Low scorers disappear when memory fills up—no external system, just the model deciding what to pay attention to
- **KV Cache Basics**: Transformers compute Key and Value vectors for every token, cached for efficient generation. Each new token adds a (K,V) pair permanently
- **The Brutal Problem**: Cache grows linearly with context length; at 128k tokens, gigabytes per layer per head. Hardware just runs out of memory
- **StreamingLLM Approach**: Keep first few tokens (attention sinks), keep sliding window of recent tokens, drop everything in between. Fixed budget, simple rule
- **StreamingLLM Limitation**: Recent ≠ important. If task instruction was way up in context and tool call pushed it out of window, model forgets its objective

## Connections

- Related to [[Slate Agent Architecture and Context Management - cedric_chee]] on context as scarce RAM
- Part of [[Agent Architecture]] memory patterns
- See also [[Reverse-Engineered Learning System with Zettelkasten - atenov_d]] on knowledge scarcity management

*Filed in: [[Saved Links MOC]]*
