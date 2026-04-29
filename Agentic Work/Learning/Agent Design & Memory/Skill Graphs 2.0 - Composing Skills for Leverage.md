---
title: "Skill Graphs 2.0 - Composing Skills for Leverage"
url: "https://x.com/shivsakhuja/status/2047124337191444844?s=42"
platform: twitter
date_saved: 2026-04-23
source: "Shiv (@shivsakhuja)"
content_type: tweet
topics: [agent-design, skill-composition, orchestration]
tags: [agents, skills, leverage, automation]
status: unread
---

# Skill Graphs 2.0 - Composing Skills for Leverage

> Skills operate at different levels: atoms, molecules, and compounds. Higher level skills provide the agent with more judgement on how to orchestrate, lower level skills provide the model with a very clear workflow to execute.

| | |
|---|---|
| **Source** | Shiv (@shivsakhuja) |
| **Saved** | 2026-04-23 |
| **Type** | tweet |
| **Engagement** | 114 likes |
| **URL** | [Link](https://x.com/shivsakhuja/status/2047124337191444844?s=42) |

## Topics

[[Agent Design & Memory MOC]] | [[Skill Composition]]

## Key Points

- **Skill Graphs concept**: Create a graph of skills by linking dependent skills in markdown files, similar to Obsidian notes. A skill encodes knowledge + process into markdown + optional scripts.

- **The problem**: When skill graphs get big enough, agents may not reliably call skills past a certain depth. Dense dependency chains introduce non-determinism and hand off too much judgement to the agent.

- **Solution - Hierarchical skill levels**:
  - **ATOMS**: Base-level, single-purpose building blocks. Super reliable, almost deterministic. Don't call other skills. (e.g., scrape LinkedIn profiles, verify an email, review a PR)
  - **MOLECULES**: Solve larger problems using 2-10 atomic skills. Have explicit instructions on when/how to call atoms. More agent judgement but still scoped.
  - **COMPOUNDS**: (implied) Higher-level compositions for complex orchestration.

- **Key insight**: Push as much composition into the skill itself, minimize the agent's decision-making at runtime. More explicit = more reliable.

## Notes

This framework aligns well with how Claude Code skills work - atomic skills are tight, deterministic operations while higher-level workflows orchestrate them with explicit instructions. The atoms/molecules/compounds mental model is useful for designing reliable agent systems.

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
