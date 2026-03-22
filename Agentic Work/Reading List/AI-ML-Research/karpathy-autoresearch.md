---
title: "AutoResearch - Autonomous Single-GPU LLM Training Research"
url: "https://github.com/karpathy/autoresearch"
platform: github
date_saved: 2026-03-13
source: "GitHub (karpathy)"
content_type: repo
topics: [autoresearch, neural-network-training, ai-agents]
tags: [github, ai, research]
status: unread
---

# AutoResearch - Autonomous Single-GPU LLM Training Research

> Karpathy's `autoresearch` repo turns a small nanochat training setup into an overnight experiment loop where an agent edits `train.py`, runs five-minute trials, and keeps only changes that improve validation loss.

GitHub repo for running autonomous overnight LLM training experiments on a simplified single-GPU nanochat setup, where the agent edits `train.py` and humans steer the research org through `program.md`.

## Key Points

- The repo is intentionally small: `prepare.py` handles data prep and utilities, `train.py` is the file the agent mutates, and `program.md` defines the human-authored research instructions.
- Every training run is constrained to a fixed five-minute budget and evaluated with `val_bpb`, which makes agent-generated experiments directly comparable.
- The setup is designed for one NVIDIA GPU and aims to maximize unattended overnight iteration instead of building a full distributed research stack.

## Related
- [[arxiv-2603-05344]]
- [[karpathy-tweet]]
- [[omarsar0-tweet]]
- [[spectral-clustering]]
- [[tree-sitter-ast-parsing]]

## Why saved
<!-- Fill in when you remember why this caught your eye -->

## Notes
<!-- Fill in after reading -->
