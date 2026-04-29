---
title: "Mission Control Multi-Agent System Guide"
url: "https://x.com/pbteja1998/status/2017662163540971756?s=42"
platform: twitter
date_saved: 2026-02-01
source: "Bhanu Teja P (@pbteja1998)"
content_type: guide
topics: [Agent Design & Memory, Multi-Agent Systems]
tags: [multi-agent, claude-code, openclaw, ai-orchestration, persistent-agents, telegram-integration, agent-swarm, clawdbot]
status: unread
---

> "The Complete Guide to Building Mission Control: How We Built an AI Agent Squad — 10 AI agents working together like a real team."

| Metric | Count |
|--------|-------|
| Likes | 8500 |
| Retweets | 1100 |

**Topics:** [[Agent Design & Memory]], [[Multi-Agent Systems]]

## Key Points
- **10 concurrent AI agents** operating as a coordinated team with shared context and distinct specializations
- **Built on Clawdbot/OpenClaw**: Open-source agent framework that runs as a persistent daemon with tool access (file system, shell, web, APIs)
- **Persistent sessions with continuity**: Unlike chat-based AI, these agents remember context across restarts and conversations
- **Telegram integration**: Agents connect to messaging channels for human-in-the-loop interaction

### The Problem Solved
Traditional AI assistants suffer from:
- **No continuity**: Every conversation starts fresh
- **Lost context**: Research from yesterday is gone
- **Single-threaded**: One assistant, one task at a time
- **No coordination**: Can't delegate or collaborate

### Mission Control Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      GATEWAY (Core Process)                 │
│  └── Runs 24/7 as daemon                                    │
│  └── Manages all active sessions                            │
│  └── Handles cron jobs (scheduled tasks)                    │
│  └── Routes messages between channels and sessions          │
│  └── Provides WebSocket API for control                     │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
    ┌───────────┐      ┌───────────┐      ┌───────────┐
    │ Session 1 │      │ Session 2 │      │ Session N │
    │  (Jarvis) │      │  (Friday) │      │   (...)   │
    │           │      │           │      │           │
    │ • Unique  │      │ • Own     │      │ • Own     │
    │   context │      │   persona │      │   tools   │
    │ • Own     │      │ • Own     │      │ • Own     │
    │   history │      │   channel │      │   tasks   │
    └───────────┘      └───────────┘      └───────────┘
```

### Key Concepts

**Gateway**: Core daemon process that:
- Starts with `clawdbot gateway start`
- Manages all session lifecycles
- Routes messages to correct agents
- Handles scheduled automation

**Sessions**: Persistent conversation contexts
- Each session has a unique key
- Survives restarts
- Can have different AI providers/models
- Connects to specific channels (Telegram, Discord, etc.)

### Why "Multiple Clawdbots"?
The insight: If one Clawdbot instance = one AI assistant (Jarvis), then N instances = N specialized agents that can:
- Work in parallel on different tasks
- Share a workspace directory
- Hand off tasks to each other
- Maintain separate conversation histories

### Technical Implementation
```bash
# Start the gateway
clawdbot gateway start

# Configuration defines:
# - AI provider and model
# - Connected channels
# - Tool access permissions
# - System prompts
# - Workspace paths
```

### Use Case: SiteGPT Customer Support
Author runs @SiteGPT (AI chatbot for support). Mission Control allows:
- **Research Agent**: Gathers context on customer issues
- **Response Agent**: Drafts support replies
- **Escalation Agent**: Routes complex issues to humans
- **Analytics Agent**: Tracks patterns across tickets

### People/Tools Mentioned
- [[Bhanu Teja P]] (@pbteja1998) — SiteGPT founder, Mission Control creator
- [[OpenClaw]] (formerly Clawdbot) — open-source agent framework
- [[Claude]] — AI model backend (Anthropic)

*Filed in: [[Saved Links MOC]]*
