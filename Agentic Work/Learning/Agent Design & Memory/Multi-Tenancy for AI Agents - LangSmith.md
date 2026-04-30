---
title: "Multi-Tenancy for AI Agents - LangSmith"
url: "https://x.com/sydneyrunkle/status/2049956826670911809?s=42"
platform: twitter
date_saved: 2025-04-30
source: "Sydney Runkle (@sydneyrunkle)"
content_type: tweet
topics: [Multi-Tenancy, Agent Auth, LangSmith]
tags: [langsmith, multi-tenancy, agent-auth, rbac, oauth]
status: unread
---

# Multi-Tenancy for AI Agents - LangSmith

> Serving multiple users from a single agent deployment introduces three distinct problems. Luckily, LangSmith's agent server has a solution for each!

| | |
|---|---|
| **Source** | Sydney Runkle (@sydneyrunkle) |
| **Saved** | 2025-04-30 |
| **Type** | tweet |
| **Engagement** | 8 likes, 2 retweets |
| **URL** | [Link](https://x.com/sydneyrunkle/status/2049956826670911809?s=42) |

## Topics

[[Agent Design & Memory MOC]] | [[Developer Tools & Code Intelligence MOC]]

## Key Points

- **Data isolation**: `@auth.authenticate` handler tags every resource with ownership on write, filters on read
- **Delegated credentials**: Agent auth handles OAuth flow so agent can act as the user across runs
- **Operator access**: RBAC controls who on your team can deploy, trace, or change auth policies
- Reference: [LangChain Multi-Tenancy Docs](https://docs.langchain.com/oss/python/deepagents/going-to-production#multi-tenancy)

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
