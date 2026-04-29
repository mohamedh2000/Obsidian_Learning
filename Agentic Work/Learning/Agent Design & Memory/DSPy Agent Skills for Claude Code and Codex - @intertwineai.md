---
title: "Why I Built dspy-agent-skills"
url: "https://x.com/intertwineai/status/2046417913792332224?s=42"
platform: twitter
date_saved: 2026-04-23
source: "Bryan Young (@intertwineai)"
content_type: guide
topics: [DSPy, agents, skills, GEPA, RLM, coding]
tags: [dspy, agents, skills, gepa, rlm, claude-code, codex]
status: unread
---

# Why I Built dspy-agent-skills

> DSPy turns prompts into programs. GEPA optimizes those programs without RL. RLM reasons over inputs bigger than any context window. None of this lands in your coding agent by default, so I packaged it as five skills that do.

| | |
|---|---|
| **Source** | Bryan Young (@intertwineai) |
| **Saved** | 2026-04-23 |
| **Type** | guide |
| **Engagement** | 149 likes |
| **URL** | [Link](https://x.com/intertwineai/status/2046417913792332224?s=42) |

## Topics

[[Agent Design & Memory]] | [[Prompt Engineering]]

## Key Points

- **The Gap**: Spent a week trying to get Claude Code and Codex CLI to write idiomatic DSPy code — agents would silently use deprecated imports or return dicts from metrics that crash `dspy.Evaluate`
- **dspy-agent-skills**: Five Agent Skills that give any compatible coding agent working knowledge of idiomatic DSPy
- **DSPy** (Stanford NLP, Oct 2023): Stop writing prompts by hand, start writing programs that compile down to prompts — declare input/output contract as typed Signature, compose Modules, let optimizer tune prompt strings and few-shot examples
- **GEPA** (ICLR 2026 Oral): Let LM reflect in plain English on why a candidate program failed, then mutate instructions — outperforms GRPO-style RL by 6% avg (up to 20%), uses up to 35x fewer rollouts, beats MIPROv2 by over 10% on benchmarks like AIME-2025
- **Key GEPA requirement**: Metrics must explain WHY something failed — "0.7" tells reflection model nothing; "wrong answer; cited doc ['mars'] but evidence is in ['jupiter']" teaches everything
- GitHub: https://github.com/intertwine/dspy-agent-skills

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
