---
title: "Turn Opus 4.8 into Fable 5 with a Skill File"
url: "https://x.com/0x_kaize/status/2073857861931667946?s=42"
platform: twitter
date_saved: 2026-07-06
source: "kaize (@0x_kaize)"
content_type: tweet
topics: [skills, ai-workflow, model-strategy]
tags: [twitter, 0x_kaize, fable, opus, skills, claude]
status: unread
---

# Turn Opus 4.8 into Fable 5 with a Skill File

> Before Fable 5 moves to pay-per-use, have it write a SKILL.md capturing its own reasoning, verification habits, and task decomposition — so your daily Opus/Sonnet model inherits the patterns after the window closes.

| | |
|---|---|
| **Source** | kaize (@0x_kaize) |
| **Saved** | 2026-07-06 |
| **Type** | Tweet |
| **Engagement** | 1341 likes, 135 retweets |
| **URL** | [Link](https://x.com/0x_kaize/status/2073857861931667946?s=42) |

## Topics

[[Agent Design & Memory]] | [[Skills]]

## Key Points

- **The core move:** prompt Fable 5 with "write a SKILL.md for Opus 4.8 capturing how you decompose hard tasks, verify your own work, and decide what to do next." The files it writes outlast your access to the model.
- Give it your *hardest* problems — it's built for work that takes humans days; easy tasks waste the window.
- One big brief (full context, constraints, edge cases in message one) instead of 20 back-and-forth messages — it decomposes the rest.
- Default effort to high; reserve xhigh for genuinely brutal runs (high on Fable often beats xhigh on older models).
- Keep one `.md` memory file that accumulates learnings across sessions.
- Make it verify its own work before reporting — kills the fake "done."
- Delete over-detailed Opus-era prompts — heavy instructions actively hurt Fable 5.

## Notes

Framing is time-boxed to a pricing change ($10/$50 per Mtok, 2x Opus). The transferable idea: distill a stronger model's judgment into reusable skill files before losing cheap access.

(Personal annotations)

---

*Filed in: [[Learning MOC]] | [[Twitter Posts MOC]] | [[Saved Links MOC]]*
