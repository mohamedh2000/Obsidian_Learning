---
title: "Codex Skills Auto-Discovery Prompt"
url: "https://x.com/reach_vb/status/2058538305872949490?s=42"
platform: twitter
date_saved: 2026-05-24
source: "Vaibhav (VB) Srivastav (@reach_vb)"
content_type: guide
topics: [ai-agents, automation, skills, codex]
tags: [codex, skills, automation, prompt, self-improving-systems]
status: unread
---

# Codex Skills Auto-Discovery Prompt

> Prompt to ask Codex to analyze your work patterns and automatically identify repeated workflows worth packaging into skills, subagents, or automations

| | |
|---|---|
| **Source** | Vaibhav (VB) Srivastav (@reach_vb) |
| **Saved** | 2026-05-24 |
| **Type** | guide |
| **Engagement** | 2410 likes, 184 retweets |
| **URL** | [Link](https://x.com/reach_vb/status/2058538305872949490?s=42) |

## Topics

[[AI Agents]] | [[Self-Optimizing Systems]] | [[Autoresearch]]

## Key Points

- Analyzes last 30 days of work to identify patterns
- Uses sessions, Memories, Chronicle, and existing skills as evidence sources
- Categorizes recommendations: Skill, Custom subagent, Automation, or Skip
- Produces compact shortlist before creating only high-confidence items
- Avoids speculative, overlapping, or overly broad assets

## The Prompt

```
Look back over my recent work from the last 30 days, or all available history if shorter, and identify repeated manual workflows worth packaging.

Use available evidence in this order:
- Recent Codex sessions and task summaries.
- Codex Memories and rollout summaries to find patterns repeated across sessions.
- Chronicle, if enabled, to spot repeated work outside Codex. Use Chronicle for discovery only; confirm important details in the relevant source system when possible.
- Existing skills, custom agents, and automations, so you reuse or extend what already exists instead of duplicating it.

Look broadly for work that is repeated, time-consuming, error-prone, context-heavy, or benefits from a consistent process. Include workflows across coding, research, writing, planning, communication, operations, analysis, and personal administration.

Only act on a candidate when it:
- occurred at least twice, or is clearly likely to recur and costly to repeat;
- has stable inputs, a repeatable procedure, and a clear output or stopping condition;
- would materially improve speed, quality, consistency, or reliability;
- is not already adequately covered.

Choose the smallest appropriate form:
- Skill: a reusable workflow or playbook.
- Custom subagent: a bounded specialist role or investigation task suitable for delegation.
- Automation: a scheduled or recurring check, report, reminder, or monitor.
- Skip: work that is too one-off, ambiguous, sensitive, or poorly evidenced to package.

First produce a compact shortlist with:
- repeated workflow
- supporting evidence and dates
- frequency/confidence
- recommended form: skill, subagent, automation, extend existing, or skip
- why it is or is not worth creating

Then create only the high-confidence missing items. Keep them narrow, practical, source-aware, and easy to validate. Do not create speculative, overlapping, or overly broad assets.

Finish with:
- what you created or extended
- what you deliberately skipped
- what needs more evidence before packaging
```

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
