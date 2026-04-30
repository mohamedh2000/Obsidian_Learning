---
title: "RLM Scaffolding Beats Frontier Models on LongCoT"
url: "https://x.com/quarqlabs/status/2049392959616143809?s=42"
platform: twitter
date_saved: 2026-04-29
source: "Quarq (@quarqlabs)"
content_type: tweet
topics: [agent-scaffolding, reasoning, benchmarks]
tags: [rlm, dspy, longcot, reasoning, agents]
status: unread
---

# RLM Scaffolding Beats Frontier Models on LongCoT

> A 9B parameter model (Qwen3.5-9B) with dspy.RLM scaffolding achieved 15.69% on LongCoT-Full vs GPT-5.2's 9.83% — proving scaffolding can unlock latent model capabilities.

| | |
|---|---|
| **Source** | Quarq (@quarqlabs) |
| **Saved** | 2026-04-29 |
| **Type** | Thread |
| **Engagement** | 77 likes, 10 retweets |
| **URL** | [Link](https://x.com/quarqlabs/status/2049392959616143809?s=42) |

## Topics

[[Agent Scaffolding]] | [[LLM Reasoning]] | [[DSPy]]

## Key Points

- **LongCoT benchmark** measures sustained reasoning over long horizons (tens to hundreds of thousands of tokens) across math, chemistry, CS, chess, and logic
- **dspy.RLM on Claude Sonnet 4.5**: jumped from ~13% to 45.4% overall; categories like Dungeon, Packaging, Hanoi, Sudoku went from near-zero to perfect scores
- **Refined prompting setup**: pushed LongCoT-mini from 38.7% to 65.6% — nearly 2x improvement just from better scaffold design
- **Qwen3.5-9B + dspy.RLM**: beat GPT-5.2 by meaningful margin on LongCoT-Full (15.69% vs 9.83%)
- **LongMemEval**: dspy.RLM variants consistently hit 87–89.8% accuracy at ~$0.035 per query
- **The Mismanaged Geniuses Hypothesis** (@a1zhang): models already have raw capability; bottleneck is task management, not intelligence
- **RLM mechanism**: recursive execution environment with shared REPL state, typed I/O via DSPy signatures, structured delegation

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
