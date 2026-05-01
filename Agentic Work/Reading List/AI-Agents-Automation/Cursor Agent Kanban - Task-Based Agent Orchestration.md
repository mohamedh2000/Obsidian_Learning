---
title: "Cursor Agent Kanban - Task-Based Agent Orchestration"
url: "https://x.com/ayi_ainotes/status/2049731613328548187?s=42"
platform: twitter
date_saved: 2025-04-30
source: "阿绎 AYi (@ayi_ainotes)"
content_type: tweet
topics: [AI Agents, Developer Tools, Cursor, Task Orchestration]
tags: [cursor, agent-kanban, task-management, ai-coding]
status: unread
---

# Cursor Agent Kanban - Task-Based Agent Orchestration

> Cursor's Agent Kanban shifts the paradigm: instead of prompting AI to write code, you throw tasks into a backlog and agents claim, execute, and update status autonomously.

| | |
|---|---|
| **Source** | 阿绎 AYi (@ayi_ainotes) |
| **Saved** | 2025-04-30 |
| **Type** | tweet |
| **Engagement** | 67 likes, 8 retweets |
| **URL** | [Link](https://x.com/ayi_ainotes/status/2049731613328548187?s=42) |

## Topics

[[AI Agents]] | [[Developer Tools]] | [[Cursor]]

## Key Points

- Cursor's Agent Kanban is a cookbook/reference implementation where each card represents a running Agent with states: Completed, Failed, Running, Pending
- Real-time status updates with artifact and PR links, failure reasons visible at a glance
- Shifts the relationship with code: from writing code → prompting AI → throwing tasks for agents to claim and execute
- Backlog becomes the programming language; you sit behind the kanban watching progress
- Production caveats remain: 60-min runtime limits, rate limits, failure rates - "原型迭代快，生产还是得靠人扛" (prototypes iterate fast, production still needs humans)
- Core insight: mechanical, repetitive, clearly-describable work shouldn't be done manually

## Original Text

我最近在想一件事，

为什么 Cursor 要做 Agent Kanban？

表面上是个看板——像 Linear，或者像 Trello，
但每张卡片对应的不是任务，
更像一个正在运行的 Agent。

Completed、Failed、Running、Pending，状态实时更新，
还能直接看 artifact、PR 链接，失败原因一目了然。

你不需要去聊天框里一遍遍 @它 ，
只需要把任务扔进去。

更有意思的是，
这个东西叫 cookbook 示例，
官方说这是个参考实现，
你拿去自己造。

Cursor 也没说这是个完整的产品，
他们说的是你照着这个思路自己搭。

我觉得这是个很重要的信号。

讲真我想了一下才反应过来，这件事真正改变的是啥。

首先肯定不是速度，也不是界面，
真正改变的是你和代码之间的关系。

比如说以前是你写代码 ，
后来是你 prompt AI 写代码，

现在是你扔任务，
Agent 去认领、执行、更新状态，
你坐在看板后面看进度，
然后backlog 变成了编程语言。

当然，也有没说清楚的部分，
比如demo 里就有 FAILED 和 EXPIRED 的卡片，
看到社区有人说，没有人在做 review 层，Agent 标 Completed 不代表它做对了之类的，
但其实60 分钟运行上限、rate limit、失败率，这些都还在。

所以原型迭代快，生产还是得靠人扛才行
但我一直觉得，工具的边界在哪里其实也没那么重要，
真正重要的是你在用它之前，有没有想清楚，那些机械的、重复的、可以被描述清楚的活儿，为什么还要自己做？

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
