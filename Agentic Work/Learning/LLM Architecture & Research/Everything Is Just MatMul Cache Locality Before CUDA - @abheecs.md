---
title: "Everything Is Just MatMul — Cache Locality Before CUDA"
url: "https://x.com/abheecs/status/2042514428915257767"
platform: twitter
date_saved: 2026-04-10
source: "abheecs (@abheecs)"
content_type: tweet
topics: [LLM, performance, systems]
tags: [twitter, matmul, cuda, cache, performance]
status: unread
---

# Everything Is Just MatMul — Cache Locality Before CUDA

> abheecs links to an article on matrix multiplication optimization: naive, cache-optimized i-k-j loop ordering, and tiling — arguing that optimizing MatMul is optimizing the core of AI itself.

| | |
|---|---|
| **Source** | abheecs (@abheecs) |
| **Saved** | 2026-04-10 |
| **Type** | tweet |
| **Engagement** | 374 likes, 42 retweets |
| **URL** | [Link](https://x.com/abheecs/status/2042514428915257767) |

## Topics

[[Matrix Multiplication]] | [[Systems Performance]]

## Key Points

- Three approaches: naive → cache-optimized loop order → tiling
- Memory access patterns + CPU cache locality drive perf
- MatMul as the core primitive of modern AI workloads

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
