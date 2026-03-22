---
title: "On the Biology of a Large Language Model"
url: "https://transformer-circuits.pub/2025/attribution-graphs/biology.html"
platform: web
date_saved: 2026-03-13
source: "Transformer Circuits"
content_type: guide
topics: [mechanistic-interpretability, attribution-graphs, llm-research]
tags: [research, ai, interpretability]
status: unread
---

# On the Biology of a Large Language Model

> Anthropic's attribution-graph work traces how Claude 3.5 Haiku routes information through internal features, showing multi-step reasoning and reusable abstract circuits rather than simple next-token heuristics.

Investigates Claude 3.5 Haiku's internal mechanisms using circuit tracing. Attribution graphs map how the model transforms inputs into outputs, with features as nodes and causal interactions as edges.

## Key Points

- The article shows concrete circuit-level examples, including reasoning chains like Dallas to Texas to Austin and early selection of rhyming targets before a poem is completed.
- Attribution graphs are presented as a way to inspect intermediate computation instead of only correlating inputs and outputs.
- The main takeaway is that useful model behavior appears to arise from structured, reusable internal computations that can be traced across tasks and languages.

## Related
- [[karpathy-autoresearch]]
- [[karpathy-tweet]]
- [[omarsar0-tweet]]
- [[spectral-clustering]]
- [[tree-sitter-ast-parsing]]

## Why saved
<!-- Fill in when you remember why this caught your eye -->

## Notes
<!-- Fill in after reading -->
