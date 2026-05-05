---
title: "Tuning Deep Agents for Different Models - @vtrivedy10"
url: "https://x.com/vtrivedy10/status/2049535740233523600?s=42"
platform: twitter
date_saved: 2026-05-05
source: "Viv (@vtrivedy10)"
content_type: tweet
topics: [agent-design, harness-engineering, prompt-engineering]
tags: [twitter, agent-design, deepagents, harness-profiles]
status: unread
---

# Tuning Deep Agents for Different Models - @vtrivedy10

> Deep Agents adding model-specific profiles to adjust prompts, tools, and middleware — leads to 10-20 point jump on tau2-bench.

| | |
|---|---|
| **Source** | Viv (@vtrivedy10) |
| **Saved** | 2026-05-05 |
| **Type** | tweet |
| **Engagement** | 221 likes |
| **URL** | [Link](https://x.com/vtrivedy10/status/2049535740233523600?s=42) |

## Topics

[[AI Agents]] | [[Harness Engineering]]

## Key Points

- Deep Agents was previously designed generically to work across model families
- Now adding harness profiles to control prompts, tools, and middleware per-model
- Prompting guides differ per model — OpenAI Codex vs Anthropic Claude have different conventions
- Same model in different harness yields different performance (Terminal-Bench 2.0 shows this)
- For Codex: apply_patch tool, shell_command aliasing, specific prompting around tool calling
- For Opus: different prompt-level changes per migration guide
- A single harness can't be optimal for every model

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
