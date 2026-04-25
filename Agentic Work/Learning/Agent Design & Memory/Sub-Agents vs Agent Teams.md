---
title: "Sub-Agents vs Agent Teams: The Architecture Decision That Changes Everything"
url: "https://x.com/suryanshti777/status/2047694444787577236?s=42"
platform: twitter
date_saved: 2026-04-24
source: "Suryansh Tiwari (@Suryanshti777)"
content_type: guide
topics: [agent-architecture, multi-agent-systems, orchestration]
tags: [sub-agents, agent-teams, coordination, claude-sdk]
status: unread
---

# Sub-Agents vs Agent Teams

> The real question isn't "should I use multiple agents?" It's "what kind of coordination does this task actually need?"

| | |
|---|---|
| **Source** | Suryansh Tiwari (@Suryanshti777) |
| **Saved** | 2026-04-24 |
| **Type** | Guide |
| **Engagement** | 658 likes, 103 retweets |
| **URL** | [Link](https://x.com/suryanshti777/status/2047694444787577236?s=42) |

## Topics

[[Agent Architecture]] | [[Multi-Agent Systems]] | [[Orchestration Patterns]]

## Key Points

- **Sub-Agents: Parallelism with Isolation**
  - Specialized instance running in isolated context
  - Gets: system prompt, limited tools, isolated context, single scoped task
  - Returns only final output (not reasoning or intermediate steps)
  - Sub-agents are about **compression**, not just speed
  - Strict constraints: cannot talk to each other, cannot spawn agents, everything flows through parent

- **Agent Teams: Coordination Through Communication**
  - Built for collaboration with shared context
  - Components: lead agent (assigns/synthesizes), teammates (execute), shared task layer (tracks progress/dependencies)
  - Real coordination possible—frontend agent can signal backend changes

- **Core Difference**
  - Sub-agents: Isolated, stateless, one-shot, parent-controlled (execution-focused)
  - Agent teams: Collaborative, stateful, ongoing, peer-coordinated (coordination-focused)

## Code Example

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

agents={
    "security-reviewer": AgentDefinition(
        description="Find vulnerabilities and security risks",
        prompt="You are a security expert.",
        tools=["Read", "Grep", "Glob"],
        model="sonnet",
    ),
    "performance-optimizer": AgentDefinition(
        description="Identify performance bottlenecks",
        prompt="You are a performance engineer.",
        tools=["Read", "Grep", "Glob"],
        model="sonnet",
    ),
}
```

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
