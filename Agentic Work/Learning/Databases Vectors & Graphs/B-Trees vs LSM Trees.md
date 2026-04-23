---
title: "B-Trees vs LSM Trees"
url: "https://blog.bytebytego.com/p/b-trees-vs-lsm-trees-comparison-and?launch_post_unlock_offer=true&utm_medium=email&triedRedirect=true"
platform: web
date_saved: 2026-04-23
source: "ByteByteGo Newsletter"
content_type: guide
topics: [databases, data-structures, indexing]
tags: [b-tree, lsm-tree, system-design]
status: unread
---

# B-Trees vs LSM Trees

> Neither approach is better — B-Trees and LSM Trees represent opposing strategies for handling disk I/O constraints, trading off read vs write performance.

| | |
|---|---|
| **Source** | ByteByteGo Newsletter |
| **Saved** | 2026-04-23 |
| **Type** | guide |
| **Engagement** | - |
| **URL** | [Link](https://blog.bytebytego.com/p/b-trees-vs-lsm-trees-comparison-and) |

## Topics

[[Databases Vectors & Graphs MOC]] | [[System Design]]

## Key Points

- **Core Design Philosophy**: B-Trees prioritize fast reads by maintaining sorted data on disk; LSM Trees optimize writes by buffering in memory before bulk flushing
- **Write Performance**: LSM Trees make writes cheaper through batching; B-Trees incur costs on every write due to sorted structure maintenance
- **Read Performance**: B-Trees deliver faster reads thanks to sorted organization; LSM Trees require searching across multiple memory and disk layers
- **The Fundamental Trade-off**: One of the most useful mental models in system design — no universal winner, depends on workload
- **Use Cases**: B-Trees for read-heavy (OLTP), LSM Trees for write-heavy (logging, time-series)

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
