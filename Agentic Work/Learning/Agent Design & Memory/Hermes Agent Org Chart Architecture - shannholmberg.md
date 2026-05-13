---
title: "Hermes Agent Org Chart Architecture"
url: "https://x.com/shannholmberg/status/2054542245475578147?s=42"
platform: twitter
date_saved: 2026-05-13
source: "Shann³ (@shannholmberg)"
content_type: tweet
topics: [Agent Architecture, Memory Scoping, Orchestration]
tags: [agents, hermes, docker, orchestration, memory, architecture]
status: unread
---

# Hermes Agent Org Chart Architecture

> the org chart for my Hermes Agent company — four layers, all isolated docker containers on one vps

| | |
|---|---|
| **Source** | Shann³ (@shannholmberg) |
| **Saved** | 2026-05-13 |
| **Type** | tweet |
| **Engagement** | 206 likes, 22 retweets |
| **URL** | [Link](https://x.com/shannholmberg/status/2054542245475578147?s=42) |

## Topics

[[Agent Architecture]] | [[Memory Scoping]] | [[Orchestration]]

## Key Points

- **Layer 1: Company Brain** — vision, brand, customers, products; shared context for all layers
- **Layer 2: Orchestrator Hermes Agent** — reads company brain, routes to departments with scoped context
- **Layer 3: Department Brain** — marketing, sales, ops, support; each with own playbook, voice rules, tools
- **Layer 4: Specialized Hermes Agents** — single-task workers with sub-profiles
- Architecture principle: context flows down, work flows up, memory stays scoped to owning layer
- Infrastructure: one VPS hosts entire company; spin up new departments/agents from templates in isolated containers

## Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│           LAYER 1: COMPANY BRAIN                │
│  (vision, brand, customers, products context)   │
└─────────────────────┬───────────────────────────┘
                      │ context ↓
┌─────────────────────┴───────────────────────────┐
│       LAYER 2: ORCHESTRATOR HERMES AGENT        │
│   (reads company brain, routes to departments)  │
└───────┬─────────┬─────────┬─────────┬───────────┘
        │         │         │         │ context ↓
   ┌────┴────┐┌───┴────┐┌───┴────┐┌───┴────┐
   │MARKETING││ SALES  ││  OPS   ││SUPPORT │  LAYER 3
   │ BRAIN   ││ BRAIN  ││ BRAIN  ││ BRAIN  │  DEPT BRAINS
   └────┬────┘└───┬────┘└───┬────┘└───┬────┘
        │         │         │         │ context ↓
   ┌────┴────┐┌───┴────┐┌───┴────┐┌───┴────┐
   │ Agent A ││Agent B ││Agent C ││Agent D │  LAYER 4
   │ Agent A'││Agent B'││Agent C'││Agent D'│  SPECIALISTS
   └─────────┘└────────┘└────────┘└────────┘
        ↑ work   ↑ work   ↑ work   ↑ work
```

## Notes

Interesting parallel to my own harness architecture. Key insight: **memory isolation per layer** prevents cross-contamination. Container-per-agent on single VPS is cost-effective for small-scale deployment.

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
