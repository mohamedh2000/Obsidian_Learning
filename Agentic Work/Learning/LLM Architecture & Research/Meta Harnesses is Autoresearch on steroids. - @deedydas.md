---
title: "Meta Harnesses is Autoresearch on steroids."
url: "https://x.com/deedydas/status/2041189706910875869"
platform: twitter
date_saved: 2026-04-06
source: "Deedy (@deedydas)"
content_type: tweet
topics: [LLMs, AI Agents, Prompt Engineering]
tags: [twitter, deedydas]
status: unread
---

# Meta Harnesses is Autoresearch on steroids.

> Meta Harnesses is Autoresearch on steroids. Something I've been exploring recently is to get long running agents to hill climb on a verifiable task to continuously improve without my intervention.

| | |
|---|---|
| **Source** | Deedy (@deedydas) |
| **Saved** | 2026-04-06 |
| **Type** | tweet |
| **Engagement** | 1247 likes, 145 retweets |
| **URL** | [Link](https://x.com/deedydas/status/2041189706910875869) |

## Topics

[[LLMs]] | [[AI Agents]] | [[Prompt Engineering]]

## Key Points

- Meta Harnesses is Autoresearch on steroids.
- Something I've been exploring recently is to get long running agents to hill climb on a verifiable task to continuously improve without my intervention.
- Karpathy's Autoresearch did this pretty well on specific tasks, but this weekend I tried Meta Harnesses which moves one level of abstraction up.
- What does Meta Harness do?

## Tweet

Meta Harnesses is Autoresearch on steroids.

Something I've been exploring recently is to get long running agents to hill climb on a verifiable task to continuously improve without my intervention. Karpathy's Autoresearch did this pretty well on specific tasks, but this weekend I tried Meta Harnesses which moves one level of abstraction up.

What does Meta Harness do?
Autoresearch can be used in harness like Claude Code / Codex to generate experiments to try, evaluate results, and continue looping. Meta Harness generates a harness itself that optimizes on a task or a set of task. Here, we define a harness as "a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic". The idea is that LLMs are very powerful today, but to harness [pun intended] their power, you need to give it the right prompts and context. Meta Harnesses automates coming up with the right prompts and the right way to retrieve context to solve a problem.

Where did this idea come from?
This is from a paper from Stanford and the author of DSPy written last week. The paper shows fantastic performance on 3 tasks: text classification, math reasoning (IMO level problems) and coding (Terminal Bench 2.0), far outperforming traditional harnesses. The discovered harnesses are interesting: math for example, splits up the logic into different categories (Combinatorics, Geometry, Number Theory, Algebra) and prompts and looks at the context differently. The coding harness, amongst other things, pre-processes the tools available in the environment to save exploratory turns.

When should you use and not use it?
Meta Harnesses seem pretty useful for tackling a specific but wide set of problems where the result is verifiable. In contrast, when I tried it on a specific task like Chess, it arbitrarily divides the problem into separate tasks - opening, mid game, end game, and creates different approaches for each. This "works" but isn't really clean because we believe there should be one approach that does all three. It does far better on things like examinations (JEE, Gaokao) where it splits problems into categories and tackles each category with different strategies.

This paper covers a pretty light version of what a harness means. In the future, we can split up tasks into harnesses that have access to specific kinds of data, specific toolchains and various models to get even better results.

Overall, pretty cool applied AI approach to hillclimb a verifiable task in a specific domain with variety within the problem space.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
