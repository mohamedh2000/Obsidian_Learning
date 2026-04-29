---
title: "Alpha Eval - Agents Making Evals as a Multi-Player Game"
url: "https://x.com/vtrivedy10/status/2048152011783155858?s=42"
platform: twitter
date_saved: 2026-04-26
source: "Viv (@vtrivedy10)"
content_type: tweet
topics: [self-improving-agents, evals, curriculum-learning, RL]
tags: [agents, evals, self-improvement, reinforcement-learning, data-generation]
status: unread
---

# Alpha Eval - Agents Making Evals as a Multi-Player Game

> The holy grail of intelligence is recursive self-improvement where agents can take any task and improve themselves on that task without human intervention.

| | |
|---|---|
| **Source** | Viv (@vtrivedy10) |
| **Saved** | 2026-04-26 |
| **Type** | tweet |
| **Engagement** | 49 likes, 6 retweets |
| **URL** | [Link](https://x.com/vtrivedy10/status/2048152011783155858?s=42) |

## Topics

[[Agent Design & Memory]] | [[RLHF & RL Training]]

## Key Points

- **Self-Improvement Goal**: Recursive self-improvement where agents improve themselves on tasks without human intervention. Key questions: what does this system look like? How to encode "good" for a task? Do we need curriculum learning?

- **Evals as Training Data**: Evals are training data for the agent world. Every failed eval updates the agent definition - analogous to RL/SFT training where data encodes changes to a system.

- **Curriculum Learning**: Progressive batches of tasks designed to train abilities that unlock future abilities. E.g., to do long horizon coding, agent needs to be a great planner. Tasks get harder over time.

- **Production Traces**: Using real-world trace data as a prior for data generation. Captures real scenarios and actions, grounds eval generation in concrete signal.

- **Agent-Driven Eval Generation**: Agents should make evals for other agents to hill-climb on. Inspired by DeepMind's AlphaGo/Zero - treating self-improvement as a game.

- **Challenges**: Eval collapse, hard for agents to capture good signal autonomously. Research groups exploring data generation for self-improvement.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
