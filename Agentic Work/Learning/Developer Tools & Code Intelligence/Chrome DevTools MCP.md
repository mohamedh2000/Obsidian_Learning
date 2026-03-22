---
title: "Let Your Coding Agent Debug Your Browser Session with Chrome DevTools MCP"
url: "https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session"
platform: web
date_saved: 2026-03-15
source: "Chrome Developer Blog"
content_type: tutorial
topics: [browser-automation, developer-tools]
tags: [chrome, devtools, mcp, debugging, ai-agents]
status: unread
---

# Let Your Coding Agent Debug Your Browser Session with Chrome DevTools MCP

> Chrome DevTools MCP enables coding agents to connect directly to active browser sessions for debugging, eliminating the need for separate sign-ins.

| | |
|---|---|
| **Source** | Chrome Developer Blog |
| **Saved** | 2026-03-15 |
| **Type** | tutorial |
| **URL** | [Link](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session) |

## Topics

[[Browser Automation]] | [[Developer Tools]]

## Key Points

- Agents can reuse existing browsing sessions, which is especially helpful for debugging issues behind authentication walls
- Users can select elements or network requests in DevTools and ask agents to investigate without manual context-switching
- Every remote debugging connection requires explicit user permission via dialog; Chrome displays a control banner during active sessions
- Requires Chrome M144+ with remote debugging enabled at `chrome://inspect/#remote-debugging` and the `--autoConnect` flag configured
- This represents the first step toward exposing more DevTools panel data to coding agents in future updates

## Notes

(Personal annotations)

---

*Filed in: [[Blog Posts]] | [[Saved Links MOC]]*