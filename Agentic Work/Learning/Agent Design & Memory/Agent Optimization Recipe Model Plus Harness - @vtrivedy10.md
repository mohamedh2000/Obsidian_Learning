---
title: "Agent Optimization Recipe: Model + Harness"
url: "https://x.com/vtrivedy10/status/2063429138304668093"
platform: twitter
date_saved: 2026-06-07
source: "Viv (@vtrivedy10)"
content_type: tweet
topics: [AI Agents, Fine-tuning & Training]
tags: [agent, harness, sft, rl, training, optimization]
status: unread
---

> Default recipe for optimizing Agent = Model + Harness. Train both: harness engineering with evals, SFT from traces, RL with environments, then light harness tuning.

| Metric | Count |
|--------|-------|
| Likes | 353 |
| Retweets | 38 |

**Topics:** [[AI Agents]], [[Fine-tuning & Training]]

## Key Points

### The 5-Step Agent Optimization Loop

1. **Build v1 agent** - Sensible base harness + task-specific prompting + tools
2. **Harness Engineering** - Iterate using eval tasks that roughly match production
3. **SFT (Supervised Fine-Tuning)** - Train on traces or synthetic data; good for distillation to cheaper models
4. **RL (Reinforcement Learning)** - Create environments and design rewards to push past SFT "copying" behavior
5. **Light harness engineering** - Squeeze remaining juice with slight prompting adjustments

### Key Insights
- Most companies can get acceptable performance with just steps 1-2
- Collect traces, mine patterns, make slight tweaks from there
- RL requires bandwidth and ability to create environments and design rewards
- This loop will be productized as a general-purpose recipe
- We're in the earliest innings of companies getting comfortable with steps 1-2
- Harness engineering will probably be the dominant optimization method
- Expect many companies to onboard through the entire loop in the next year

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
