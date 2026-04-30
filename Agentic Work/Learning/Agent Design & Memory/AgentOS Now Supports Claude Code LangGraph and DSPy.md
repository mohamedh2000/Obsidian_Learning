---
title: "AgentOS Now Supports Claude Code, LangGraph, and DSPy"
url: "https://x.com/ashpreetbedi/status/2049511642946249143?s=42"
platform: twitter
date_saved: 2026-04-29
source: "Ashpreet Bedi (@ashpreetbedi)"
content_type: tweet
topics: [agent-frameworks, orchestration, harnesses]
tags: [agentos, agno, claude-code, langgraph, dspy, agent-sdk]
status: unread
---

# AgentOS Now Supports Claude Code, LangGraph, and DSPy

> AgentOS can now serve Claude Code agents and Agno agents in the same deployment, sharing one db, one API, one UI — with multi-user auth, JWT-backed RBAC, streaming, and horizontal scaling.

| | |
|---|---|
| **Source** | Ashpreet Bedi (@ashpreetbedi) |
| **Saved** | 2026-04-29 |
| **Type** | Announcement |
| **Engagement** | 91 likes |
| **URL** | [Link](https://x.com/ashpreetbedi/status/2049511642946249143?s=42) |

## Topics

[[Agent Frameworks]] | [[Agent Orchestration]] | [[Claude Code]]

## Key Points

- **AgentOS alpha release** adds support for Claude Code (via Claude Agent SDK), LangGraph, and DSPy
- **Unified deployment**: Run multiple agent types (Claude Code, Agno, etc.) in one AgentOS sharing db/API/UI
- **Enterprise features**: Multi-user auth, JWT-backed RBAC, streaming, background tasks, scheduling, observability
- **SDK vs Harness distinction**:
  - **SDK** (like Agno): Primitives for building agentic software, you control the loop
  - **Harness** (like Claude Code): Opinionated execution environment with pre-built tools and architecture
- **Rule of thumb**: Customize architecture → use SDK; Task fits harness → use harness and benefit from their engineering

## Code Example

```python
from agno.agent import Agent
from agno.agents.claude import ClaudeAgent
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS
from agno.tools.workspace import Workspace

claude_agent = ClaudeAgent(
    name="Claude Code Agent",
    model="claude-sonnet-4-6",
    allowed_tools=["Read", "Edit", "Bash"],
    permission_mode="acceptEdits",
    max_turns=10,
)

agno_agent = Agent(
    name="Agno Agent",
    model="openai:gpt-5.4",
    tools=[Workspace(root=".", allowed=["read", "list", "search"])],
)

agent_os = AgentOS(
    agents=[agno_agent, claude_agent],
    db=SqliteDb(db_file="tmp/agentos.db"),
)
```

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
