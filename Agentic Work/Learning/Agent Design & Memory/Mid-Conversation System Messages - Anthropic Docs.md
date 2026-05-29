---
title: "Mid-Conversation System Messages - Anthropic Docs"
url: "https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages"
platform: web
date_saved: 2026-05-29
source: "Anthropic (platform.claude.com)"
content_type: guide
topics: [claude-api, prompt-caching, system-messages]
tags: [anthropic, claude-code, api-patterns, caching]
status: unread
---

# Mid-Conversation System Messages - Anthropic Docs

> Add or update system instructions partway through a conversation without invalidating the cached prefix — enables mid-session policy changes, per-turn context, and mode switches while preserving cache hits.

| | |
|---|---|
| **Source** | Anthropic (platform.claude.com) |
| **Saved** | 2026-05-29 |
| **Type** | guide |
| **Engagement** | Official documentation |
| **URL** | [Link](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) |

## Topics

[[Claude Code & Anthropic]] | [[API Patterns]]

## Key Points

- System instructions in the top-level `system` field invalidate the cache when edited; mid-conversation system messages let you append instructions after the cached prefix
- Use `{"role": "system"}` in the `messages` array to add instruction with system-level priority without a cache miss
- Use cases: mid-session policy changes, per-turn authoritative context, tool results that reshape behavior, mode switches granting standing permissions
- A mid-conversation system message must immediately follow a `user` message (or assistant ending in server tool use)
- Available on Claude API and Claude Platform on AWS; Opus 4 only; no beta header required
- Later system messages take precedence over earlier ones; mid-conversation messages override the top-level `system` field for turns that follow

## Notes

(Personal annotations)

---

*Filed in: [[Learning MOC]] | [[Saved Links MOC]]*
