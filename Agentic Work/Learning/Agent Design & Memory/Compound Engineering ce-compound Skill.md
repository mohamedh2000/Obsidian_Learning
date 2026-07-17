---
title: "Compound Engineering ce-compound Skill"
url: "https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/skills/ce-compound.md"
platform: github
date_saved: 2026-07-13
source: "Every Inc (EveryInc)"
content_type: guide
topics: [agent-skills, knowledge-management, compound-engineering]
tags: [github, claude-code, skills, agent-memory, knowledge-capture]
status: unread
---

# Compound Engineering ce-compound Skill

> Document a recently solved problem so the next encounter takes minutes instead of hours — knowledge compounds.

| | |
|---|---|
| **Source** | Every Inc (EveryInc) |
| **Saved** | 2026-07-13 |
| **Type** | skill doc |
| **Engagement** | N/A |
| **URL** | [Link](https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/skills/ce-compound.md) |

## Topics

[[Claude Code & Anthropic]] | [[AI Agents]]

## Key Points

- `ce-compound` is the **knowledge-capture** skill in the compound-engineering plugin — after solving a non-trivial problem it writes a structured doc to `docs/solutions/` covering symptoms, root cause, what didn't work, the working fix, and prevention.
- It is the **closing loop** of the ideation chain `/ce-ideate → /ce-brainstorm → /ce-plan → /ce-work`; captured docs feed back upstream so future runs of `ce-plan`, `ce-ideate`, `ce-debug`, and `ce-work` consult them as institutional memory.
- Triggers when the user says "that worked", "it's fixed", "problem solved"; output is one doc (bug-track or knowledge-track) plus optional `CONCEPTS.md` vocabulary capture, and can edit `AGENTS.md`/`CLAUDE.md` for discoverability after consent.
- Solves the "solve the same problem twice" failure mode where solutions live in chat threads, Linear comments, or agent transcripts and vanish in a week.

## Notes

(Personal annotations)

---

*Filed in: [[GitHub Repos MOC]] | [[Saved Links MOC]]*
