---
title: "Scaling Managed Agents: Decoupling the brain from the hands"
url: "https://www.anthropic.com/engineering/managed-agents"
platform: web
date_saved: 2026-04-08
source: "anthropic.com"
content_type: article
topics: [AI Agents, Engineering]
tags: [anthropic, engineering, managed-agents]
status: unread
---

# Scaling Managed Agents: Decoupling the brain from the hands

> Anthropic's Managed Agents architecture decouples Claude's reasoning engine from execution environments and session storage, enabling scalable, resilient long-horizon agent work.

| | |
|---|---|
| **Source** | anthropic.com |
| **Saved** | 2026-04-08 |
| **Type** | article |
| **URL** | [Link](https://www.anthropic.com/engineering/managed-agents) |

## Topics

[[AI Agents]] | [[Engineering]]

## Key Points

- Virtualizes agent components (harness, sandbox, session) into independent interfaces that can be updated without affecting others, similar to how operating systems abstract hardware.
- Decouples to improve performance by 60% at p50 and over 90% at p95 for time-to-first-token via stateless harnesses and on-demand container provisioning.
- Enhances security by storing credentials outside sandboxes where Claude-generated code executes, preventing prompt injection from accessing sensitive tokens.

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
