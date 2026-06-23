---
title: "Give Your Agents an Interpreter"
url: "https://www.langchain.com/blog/give-your-agents-an-interpreter"
platform: web
date_saved: 2026-06-23
source: "LangChain Accounts (@langchain)"
content_type: guide
topics: [Agent Design, LangChain, Tool Use]
tags: [langchain, deep-agents, interpreters, tool-use, sandboxes]
status: unread
---

# Give Your Agents an Interpreter

> Deep Agents now supports interpreters: embedded runtimes where agents can write code to coordinate tools, maintain working state, and control what enters model context.

| | |
|---|---|
| **Source** | LangChain Accounts (@langchain) |
| **Saved** | 2026-06-23 |
| **Type** | guide |
| **Engagement** | — |
| **URL** | [Link](https://www.langchain.com/blog/give-your-agents-an-interpreter) |

## Topics

[[Agent Design]] | [[LangChain]] | [[Tool Use]]

## Key Points

- Interpreters sit between serial tool calls and full sandboxes, giving agents code-level composition over scoped capabilities.
- Interpreter state acts as a third context surface: message history is for current reasoning, files are for durable artifacts, and interpreter memory holds live working values.
- Programmatic tool calling can be exposed as middleware through an allowlisted `tools` namespace inside the interpreter.
- LangChain reports early tests where this approach used up to 35% fewer tokens on some tasks.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
