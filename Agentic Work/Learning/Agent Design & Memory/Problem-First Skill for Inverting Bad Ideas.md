---
title: "Problem-First Skill for Inverting Bad Ideas"
url: "https://x.com/nurijanian/status/2063186118409929161"
platform: twitter
date_saved: 2026-06-06
source: "George from prodmgmt.world (@nurijanian)"
content_type: guide
topics: [product management, agent skills, problem discovery]
tags: [PM, skills, claude, discovery, roadmap]
status: unread
---

# Problem-First Skill for Inverting Bad Ideas

> "Treat every solution someone hands you as a compressed, imprecise confession of a problem the team senses but hasn't articulated, then decompress it back into the problem underneath."

| | |
|---|---|
| **Source** | George from prodmgmt.world (@nurijanian) |
| **Saved** | 2026-06-06 |
| **Type** | guide |
| **Engagement** | 375 likes |
| **URL** | [Link](https://x.com/nurijanian/status/2063186118409929161) |

## Topics

[[Agent Design & Memory MOC]] | [[Prompt Engineering MOC]]

## Key Points

- `/problem-first` is a skill (likely for Claude Code) that inverts solution-first thinking
- When teams hand you prebaked solutions, decompress them back to the underlying problem
- Avoids the political trap of "halt and research" by using the proposed solution as research starting point
- The skill runs in one AI call and returns 8 sections:
  - Solution-jumping diagnosis
  - Underlying problem identification
  - Assumption challenges with risk-if-wrong and validation tests

## Example Walkthrough

Team says: "we need to build a new notification system"

Skill decompresses to:
- **Signal detected**: users miss things, support tickets about lost context
- **Underlying problem**: users can't see when state changes, eroding trust
- **Assumption challenges**:
  1. Users want more notifications → Risk: add noise, adoption drops → Validate: pull engagement data
  2. Delivery mechanism is broken → Risk: rebuild plumbing, problem stays → Validate: read last 50 support tickets

## Notes

This is a practical PM skill that could be adapted as a Claude Code slash command for product discovery.

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
