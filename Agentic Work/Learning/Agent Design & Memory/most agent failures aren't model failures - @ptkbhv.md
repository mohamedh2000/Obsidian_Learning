---
title: "most agent failures aren't model failures"
url: "https://x.com/ptkbhv/status/2037065141574046050"
platform: twitter
date_saved: 2026-03-26
source: "ptk (@ptkbhv)"
content_type: tweet
topics: [LLMs, AI Agents]
tags: [twitter, ptkbhv]
status: unread
---

# most agent failures aren't model failures

> most agent failures aren't model failures

they're constraint failures. the agent tries to do something the environment doesn't allow, and the model has no idea why it failed.

| | |
|---|---|
| **Source** | ptk (@ptkbhv) |
| **Saved** | 2026-03-26 |
| **Type** | tweet |
| **Engagement** | 98 likes, 15 retweets |
| **URL** | [Link](https://x.com/ptkbhv/status/2037065141574046050) |

## Topics

[[LLMs]] | [[AI Agents]]

## Key Points

- most agent failures aren't model failures
- they're constraint failures.
- the agent tries to do something the environment doesn't allow, and the model has no idea why it failed.
- AutoHarness paper has a number that makes this concrete:

## Tweet

most agent failures aren't model failures

they're constraint failures. the agent tries to do something the environment doesn't allow, and the model has no idea why it failed.

AutoHarness paper has a number that makes this concrete:

in Kaggle GameArena chess, 78% of Gemini-2.5-Flash losses were illegal moves

not bad strategy. not miscalculation. the model just didn't know what it couldn't do.

the usual fix is manual harness engineering. you write a wrapper that validates actions, enforces rules, prevents illegal state transitions. this is the hidden work behind every "we built an agent" announcement.

AutoHarness flips this: the agent synthesizes its own harness through iterative code refinement. run, fail, get environment feedback, patch, repeat. same loop agents already use for coding tasks, applied to their own scaffolding layer.

result: Gemini-2.5-Flash + auto-synthesized harness
- zero illegal moves across 145 TextArena games
- outperforms Gemini-2.5-Pro (a larger model)

smaller model + better harness beats bigger model with no harness

they push it further: generate the entire policy in code. no LLM at decision time. just deterministic logic synthesized once. this beats GPT-5.2-High and Gemini-2.5-Pro on 16 single-player games.

the implication for agent builders: harness quality matters as much as model choice. and you don't have to hand-craft it anymore.

https://arxiv.org/abs/2603.03329

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
