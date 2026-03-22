---
tags:
  - moc
  - agents
  - architecture
type: moc
---

# Agent Architecture

Patterns and approaches for building multi-agent systems — coordination, context management, reliability, and self-improvement.

## Notes

- [[Slate Agent Architecture and Context Management - cedric_chee]] — Context-as-RAM, thread/episode design, agent OS
- [[Slate CLI Review - RLM Coding Agent - nummanali]] — Practical DX with multi-agent visibility
- [[Autoresearcher on Agent Swarms - jumperz]] — Observer agents for self-optimization, separate from coordinator
- [[Cognee Self-Healing AI Skills - iruletheworldmo]] — Skills that detect and fix their own failures at runtime

## Key Themes

- **Systems > Models**: The bottleneck is increasingly systems design, not model capability (Cedric)
- **Observability**: You need to see what agents are doing (Numman, Jumperz)
- **Self-healing**: Agents that notice and fix their own failures (Cognee, Jumperz's autoresearcher)
- **Separation of concerns**: Observer agents separate from coordinators (Jumperz)

## Related

- [[Autoresearch]] — Automated experimentation within agent systems
- [[Self-Optimizing Systems]] — The broader pattern
- [[Slate]] — A specific implementation of these ideas
