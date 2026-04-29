---
title: "Agent Role Cards for Scoped Responsibilities - @voxyz_ai"
url: "https://x.com/voxyz_ai/status/2020633743401345158?s=42"
platform: twitter
date_saved: 2026-02-09
source: "Vox (@voxyz_ai)"
content_type: tweet
topics: [Agent Design & Memory, Multi-Agent Systems]
tags: [agent-roles, role-cards, multi-agent, responsibility-scoping, escalation, agent-architecture]
status: unread
---

> "Every agent now has a role card. What they own, what they deliver, what they can't touch, when to escalate. Went from vibes to actual job descriptions."

| Metric | Count |
|--------|-------|
| Likes | 1,655 |
| Retweets | 110 |

**Topics:** [[Agent Design & Memory]], [[Multi-Agent Systems]]

## Key Points
- **Role cards** formalize agent responsibilities — moving from implicit "vibes" to explicit contracts
- Each card defines four boundaries: **ownership** (what the agent is responsible for), **deliverables** (what output it produces), **restrictions** (what it must not touch), and **escalation triggers** (when to hand off)
- This pattern prevents agents from overstepping scope — a common failure mode in multi-agent systems
- High engagement (1.6K likes) suggests the pattern resonates with practitioners building agent swarms

### Role Card Template
```yaml
agent: backend-engineer
owns:
  - API endpoints
  - Database queries
  - Server-side validation
delivers:
  - Working API routes
  - Migration files
  - Integration tests
cannot_touch:
  - Frontend components
  - CI/CD configuration
  - Infrastructure
escalate_when:
  - Requires frontend changes
  - Needs infrastructure provisioning
  - Security-sensitive operations
```

### Why It Matters
In multi-agent systems, ambiguous boundaries cause either duplication (two agents editing the same file) or gaps (no agent handles the task). Role cards make the division of labor explicit and auditable.

*Filed in: [[Saved Links MOC]]*
