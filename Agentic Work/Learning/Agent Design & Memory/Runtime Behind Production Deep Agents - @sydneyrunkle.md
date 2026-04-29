---
title: "The Runtime Behind Production Deep Agents"
url: "https://x.com/sydneyrunkle/status/2046277232537256002?s=42"
platform: twitter
date_saved: 2026-04-23
source: "Sydney Runkle (@sydneyrunkle)"
content_type: guide
topics: [agent, runtime, production, durable-execution, LangSmith]
tags: [agents, production, runtime, durable-execution, langsmith, deep-agents]
status: unread
---

# The Runtime Behind Production Deep Agents

> To build a good agent, you need a good harness. To deploy that agent, you need a good runtime — durable execution, memory, multi-tenancy, observability.

| | |
|---|---|
| **Source** | Sydney Runkle (@sydneyrunkle) |
| **Saved** | 2026-04-23 |
| **Type** | guide |
| **Engagement** | 441 likes |
| **URL** | [Link](https://x.com/sydneyrunkle/status/2046277232537256002?s=42) |

## Topics

[[Agent Design & Memory]] | [[Developer Tools & Code Intelligence]]

## Key Points

- **Harness vs Runtime**: Harness = prompts, tools, skills around the model; Runtime = durable execution, memory, multi-tenancy, observability underneath
- **Durable Execution**: Agent loops can span minutes/hours — crashes shouldn't erase prior work
- Long runs need to survive infrastructure failures — resumption from last completed step with all prior state intact
- Agents need to truly stop and wait (e.g., for human approval) — free resources, release workers, pick up later exactly where left off
- Managed task queue with automatic checkpointing — runs can be retried, replayed, or resumed from exact point of interruption
- Each super-step writes a checkpoint to persistence layer (PostgreSQL by default), keyed by thread_id as persistent cursor
- When worker crashes, run's lease is released and another worker picks up from latest checkpoint

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
