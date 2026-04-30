---
title: "Hermes Curator - Automatic Skill Management"
url: "https://x.com/teknium/status/2049717907664581067?s=42"
platform: twitter
date_saved: 2026-04-30
source: "Teknium (@@teknium)"
content_type: tweet
topics: [agent-skills, self-improvement, skill-management]
tags: [hermes, nous-research, agent-memory, skill-pruning]
status: unread
---

# Hermes Curator - Automatic Skill Management

> Hermes Agent now includes a Curator system that automatically consolidates and prunes agent-created skills, keeping the self-improvement loop manageable.

| | |
|---|---|
| **Source** | Teknium (@@teknium) |
| **Saved** | 2026-04-30 |
| **Type** | tweet |
| **Engagement** | 633 likes, 54 retweets |
| **URL** | [Link](https://x.com/teknium/status/2049717907664581067?s=42) |

## Topics

[[Agent Memory]] | [[Skill Systems]] | [[Self-Improving Agents]]

## Key Points

- **Usage Analytics**: Tracks how often each skill is used and when it was last updated/created
- **Automatic Weekly Runs**: Configurable schedule for automatic curation
- **Smart Consolidation**: Converts overly-specific skills into references, templates, or scripts for broader skills
- **Protected Skills**: Skips externally installed skills, built-in skills, and user-pinned skills
- **Manual Control**: Can disable entirely in config.yaml or run manually with `hermes curator run`

## Architecture

```
┌─────────────────────────────────────────────────┐
│               Hermes Curator                    │
├─────────────────────────────────────────────────┤
│  Input: Agent-created/user-written skills       │
│                                                 │
│  ┌─────────────┐     ┌──────────────────┐      │
│  │ Analytics   │ ──► │ Skill Scanner    │      │
│  │ - usage     │     │ - consolidate    │      │
│  │ - recency   │     │ - prune          │      │
│  └─────────────┘     │ - convert to ref │      │
│                      └──────────────────┘      │
│                                                 │
│  Protected: built-in │ external │ pinned       │
└─────────────────────────────────────────────────┘
```

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
