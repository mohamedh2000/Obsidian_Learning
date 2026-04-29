---
title: "AI Employee Folder Structure - @ganimcorey"
url: "https://x.com/ganimcorey/status/2013374176690577904?s=42"
platform: twitter
date_saved: 2026-01-20
source: "Corey Ganim (@ganimcorey)"
content_type: tweet
topics: [Agent Architecture, Self-Optimizing Systems]
tags: [ai-agents, agent-memory, agent-config, self-improvement, agent-harness, folder-structure, autonomous-agents]
status: unread
---

> This is the real folder structure of one of my AI employees. Every file has a purpose: Config = what they can access, Workspace = how they think and act, Memory = what they remember, Skills = what they're trained to do. We also set her up with a "self improvement skill" where she logs learnings and errors in order to improve herself over time.

| Metric | Count |
|--------|-------|
| Likes | 742 |
| Retweets | 59 |

**Topics:** [[Agent Architecture]], [[Self-Optimizing Systems]]

## Key Points
- **Four-pillar agent architecture**: Config (permissions/access), Workspace (behavior), Memory (persistence), Skills (capabilities) — clean separation of concerns
- **Self-improvement skill**: Agent logs learnings and errors to a `learnings/` directory, enabling iterative refinement without human intervention
- **"AI employees" mental model**: Framing agents as new hires changes context on setup expectations — more upfront investment for ongoing autonomy
- **24/7 unsupervised operation**: Once properly configured, agents run continuously without requiring constant oversight

### Agent Folder Architecture Pattern
```
agent/
├── config/      # Access control, API keys, permissions
├── workspace/   # Behavior rules, thinking patterns, SOPs
├── memory/      # Persistent context, conversation history
├── skills/      # Callable capabilities, tool definitions
└── learnings/   # Self-logged errors, improvements, insights
```

### Why This Matters
This is a practical implementation of the "harness engineering" pattern — the agent's environment and memory structure determine capabilities more than the model itself. The `learnings/` directory enables compound improvement over time.

*Filed in: [[Saved Links MOC]]*
