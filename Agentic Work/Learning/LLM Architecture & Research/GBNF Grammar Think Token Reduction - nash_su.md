---
title: "GBNF Grammar for 22x Think Token Reduction"
url: "https://x.com/nash_su/status/2048964204603080771?s=42"
platform: twitter
date_saved: 2026-04-29
source: "nash_su - e/acc (@nash_su)"
content_type: tweet
topics: [llm-optimization, structured-output, reasoning]
tags: [qwen, gbnf, grammar, thinking, optimization]
status: unread
---

> 22x fewer think tokens with no accuracy loss using GBNF Grammar to force structured thinking in Qwen3.5/3.6 models.

| Metric | Count |
|--------|-------|
| Likes | 300 |
| Retweets | 27 |

**Topics:** [[LLM Research]], [[Developer Tools]]

## The Grammar

```
root  ::= think code
think ::= "<think>\n" "GOAL: " line "APPROACH: " line "EDGE: " line "</think>\n\n"
line  ::= [^\n]+ "\n"
code  ::= [\x09\x0A\x0D\x20-\x7E]+
```

## Key Points

- **The Problem**: Qwen3.5/3.6 thinking mode over-thinks, wasting tokens and causing slow responses
- **The Solution**: GBNF Grammar forces structured thinking with three slots: GOAL (what to do), APPROACH (how), EDGE (what pitfalls)
- **Why It Works**: The framework mirrors proven software engineering and math problem-solving patterns: understand → plan → anticipate failures
- **Benchmarks**: HumanEval+: 22x fewer think tokens, no accuracy loss; LiveCodeBench: +14% pass@1, ~5x fewer total tokens

## Connections

- Part of [[LLM Research]] optimization techniques
- Relates to structured prompting and constrained decoding

*Filed in: [[Saved Links MOC]]*
