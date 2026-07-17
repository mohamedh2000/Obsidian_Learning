---
title: "Shepherd: Agent-Native Git by Stanford"
url: "https://x.com/_avichawla/status/2073746091795960237?s=42"
platform: twitter
date_saved: 2026-07-05
source: "Avi Chawla (@_avichawla)"
content_type: tweet
topics: [agent-runtime, checkpointing, agent-harness]
tags: [twitter, _avichawla, shepherd, stanford, kv-cache, agents]
status: unread
---

# Shepherd: Agent-Native Git by Stanford

> Stanford's Shepherd versions a live agent run — process + filesystem together, copy-on-write — so you can fork back to an exact prior step instead of restarting or burning tokens fixing a derailed run.

| | |
|---|---|
| **Source** | Avi Chawla (@_avichawla) |
| **Saved** | 2026-07-05 |
| **Type** | Tweet |
| **Engagement** | 3041 likes, 357 retweets |
| **URL** | [Link](https://x.com/_avichawla/status/2073746091795960237?s=42) |

## Topics

[[Agent Design & Memory]] | [[Agent Harness]]

## Key Points

- A long agent run accumulates live state (edited files, dev server, DB, packages, KV cache) that a flat message log doesn't capture — so you can't cleanly jump back to a good step.
- Git versions files but not the running process or KV cache; checking out step 8 leaves the process in step-10 memory with a cold cache.
- Shepherd records the run as a trace of typed events; each agent–environment interaction is a commit that captures the agent process + filesystem together via copy-on-write.
- Reverting is a single fork call from a prior commit that resumes from the exact state; the CoW fork is ~5x faster than `docker commit` and reuses >95% of the KV cache on replay.
- A meta/supervisor agent can sit on top, watch the trace, and revert a bad step before it commits — implemented as plain Python calling fork/replay/revert.
- Limits: filesystem/sandbox changes undo automatically, but DB writes need a pre-defined undo step, and external side effects (sent email, real charge) can't be reverted — the supervisor must catch them before they fire.
- On CooperBench (two agents on one codebase), adding a live supervisor raised pair-coding pass rate from 28.8% to 54.7%. Still alpha.

## Notes

Repo: https://github.com/shepherd-agents/shepherd
Follow-up thread references Akshay's article on self-repairing harnesses (failing trace → diagnose → verify fix against the exact failing input → lock as a regression test).

(Personal annotations)

---

*Filed in: [[Learning MOC]] | [[Twitter Posts MOC]] | [[Saved Links MOC]]*
