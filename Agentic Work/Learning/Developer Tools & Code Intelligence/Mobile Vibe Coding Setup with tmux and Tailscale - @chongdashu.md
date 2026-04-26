---
title: "Mobile Vibe Coding Setup with tmux and Tailscale - @chongdashu"
url: "https://x.com/chongdashu/status/2020497451409641894?s=42"
platform: twitter
date_saved: 2026-02-09
source: "Chong-U (@chongdashu)"
content_type: tutorial
topics: [Developer Tools, Remote Development]
tags: [tmux, tailscale, termius, mobile-coding, remote-development, claude-code, codex, ios, session-persistence]
status: unread
---

> Mobile vibe coding setup: tmux for persistent sessions, Tailscale for private secure network, Termius for SSH client. iOS and macOS always in sync — pick up where you left off.

| Metric | Count |
|--------|-------|
| Likes | 1,618 |
| Retweets | 67 |

**Topics:** [[Developer Tools]], [[Remote Development]]

## Key Points
- **tmux** provides persistent terminal sessions that survive disconnects — essential for long-running agent tasks
- **Tailscale** creates a private, secure network layer (WireGuard-based VPN) connecting devices without exposing ports
- **Termius** serves as the mobile SSH client (iOS/Android) with a polished UX for on-the-go connections
- The setup enables seamless context-switching between desktop (macOS) and mobile (iOS) — both see the same Claude Code/Codex session state

### Architecture Pattern
```
┌──────────┐     Tailscale VPN     ┌───────────────┐
│   iOS    │ ◄──────────────────► │   macOS Host  │
│ Termius  │                       │  (tmux server)│
└──────────┘                       └───────────────┘
                                          │
                                   Claude Code /
                                   Codex session
```

This pattern addresses the "I had to step away" problem with AI coding agents — the session keeps running on the host, and you can re-attach from any device on your Tailscale network.

*Filed in: [[Saved Links MOC]]*
