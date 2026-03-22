---
title: "Flash-MoE"
url: "https://github.com/danveloper/flash-moe"
platform: github
date_saved: 2026-03-20
source: "GitHub (danveloper)"
content_type: repo
topics: [mixture-of-experts, inference, metal]
tags: [github, llm-research, learning]
status: unread
---

# Flash-MoE

> Pure C and Metal inference engine that streams a 397B-parameter MoE from SSD and runs it on a 48GB MacBook Pro at roughly 4.4 tokens per second. 255 stars.

| | |
|---|---|
| **Source** | GitHub (danveloper) |
| **Saved** | 2026-03-20 |
| **Type** | GitHub repo |
| **Stars** | 255 |
| **URL** | [Link](https://github.com/danveloper/flash-moe) |

## Topics

[[LLM Research]] | [[Developer Tools]]

## Key Points

- Streams Qwen3.5-397B-A17B expert weights from SSD instead of loading the full model into RAM.
- Uses hand-tuned Metal kernels plus an FMA-optimized dequant path to keep 4-bit inference viable on Apple Silicon.
- Documents the engineering tradeoffs behind the pipeline, including why the OS page cache beat custom expert caches.

## Notes

(Personal annotations)

---

*Filed in: [[GitHub Repos MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
