---
title: "Data Driven Agent Design with Evals & Hill Climbing Algorithms"
url: "https://x.com/vtrivedy10/status/2045230994656305485?s=42"
platform: twitter
date_saved: 2026-04-17
source: "Viv (@vtrivedy10)"
content_type: tweet
topics: [agent-design, evals, self-improvement]
tags: [agents, evals, hill-climbing, data-driven, harness]
status: unread
---

# Data Driven Agent Design with Evals & Hill Climbing Algorithms

> Evals are training data for agents - every eval encodes behavior we want to see in our agent, just as every training data point in standard ML produces a gradient to shift model weights.

| | |
|---|---|
| **Source** | Viv (@vtrivedy10) |
| **Saved** | 2026-04-17 |
| **Type** | tweet |
| **Engagement** | 55 likes, 5 retweets |
| **URL** | [Link](https://x.com/vtrivedy10/status/2045230994656305485?s=42) |

## Topics

[[Agent Design]] | [[Evals]] | [[Self-Improving Agents]]

## Key Points

- Agent fitting formula: `agent = fit(model, harness, evals)` - analogous to sklearn's fit function
- Evals are like specs but better because they're verifiable and measurable - you can directly see which pass/fail
- Every eval "votes" for how to alter the harness to make it pass
- Verifiable signals include: rubrics for dense feedback, programmatic verification, LLM-as-judge for subjective behavior
- Evals are model and harness dependent - requires "spring cleaning" and updates over time
- Future of specialized agents depends on encoding specialization as something measurable

## Full Thread

Data Driven Agent Design with Evals & Hill Climbing Algorithms

this is a mental model dump i've been thinking through + iterating on as we're building self-improvement infra around agents:
- mining Trace Data to find errors and tweak the agent harness
- building + maintaining evals
- using evals to guide the agent update/generation process

What are the inputs for fitting an agent:
the main idea is what does a sklearn fit(model, data) function look like for agents

agent = fit (model, harness, evals)

Data Driven Agent Design:
Evals are training data for agents - every eval encodes behavior we want to see in our agent, just as every training data point in standard ML produces a gradient to shift model weights

Every eval we fit our agent towards votes for how to alter the harness to make that eval pass

"Can I start from an empty harness. Fit to evals, and produce a great agent? Should that be how we do things + inject some more human priors"

Verifiable Signals:
Evals are akin to specs but better because they're verifiable and measurable

We can use rubrics that give a dense feedback signal for work, programmatic verification, and LLM as a judge to evaluate subjective behavior

You can directly measure which evals pass and which don't at a glance. This is very useful, you can't as easily do the same attribution via a simple markdown spec

Iterating on Evals over Time:
Evals are model and harness dependent. "Spring Cleaning" and updating of Evals is important as you no longer need them

Agent design is focused on vibes today, but could benefit by being open to more data driven design. Just as frontier labs spend millions on data quality, teams can invest time into fantastic eval curation and design.

The future of specialized agents will depend on encoding that specialization is something measurable. Data matters, and good evals are a data signal to build a good agent.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
