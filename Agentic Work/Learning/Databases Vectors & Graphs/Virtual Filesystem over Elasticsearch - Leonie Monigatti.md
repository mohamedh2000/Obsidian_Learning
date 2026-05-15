---
title: "Virtual Filesystem over Elasticsearch"
url: "https://leoniemonigatti.com/blog/virtual-filesystem-elasticsearch.html"
platform: web
date_saved: 2026-05-14
source: "Leonie Monigatti (@helloiamleonie)"
content_type: guide
topics: [Agent Design, Elasticsearch, Virtual Filesystem]
tags: [elasticsearch, virtual-filesystem, ai-agents, database, retrieval, grep, bash]
status: unread
---

# Virtual Filesystem over Elasticsearch

> Build a filesystem-shaped interface atop Elasticsearch so AI agents can run `ls`, `cat`, `find`, and `grep` over indexed data—same shell commands, different storage backend.

| | |
|---|---|
| **Author** | Leonie Monigatti |
| **Published** | May 2026 |
| **Type** | guide |
| **URL** | [Link](https://leoniemonigatti.com/blog/virtual-filesystem-elasticsearch.html) |

## Topics

[[AI Agents]] | [[Developer Tools]] | [[Databases Vectors & Graphs]]

## Key Points

- **Two meanings of "virtual filesystem"**: In OSes, it's an abstraction layer for uniform file operations across devices. In AI agents, it's a filesystem-shaped interface over persistent storage like databases.
- **Four-layer architecture**: Agent layer → Shell layer → ElasticsearchFs implementation → Data layer
- **Access control via DLS**: Uses Elasticsearch Document Level Security to enforce fine-grained permissions at query time
- **Navigation ops**: `ls`, `cd`, `find` implemented via in-memory tree structures loaded at session init
- **Search optimization**: Two-stage `grep`—coarse database filtering first, then fine-grained regex matching
- **Companion repo**: [elasticsearch-fs on GitHub](https://github.com/iamleonie/elasticsearch-fs)

### Architecture

```
┌─────────────── AGENT LAYER ───────────────┐
│  AI agent issues bash-like commands       │
└─────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────── SHELL LAYER ───────────────┐
│  just-bash library translates commands    │
└─────────────────────────────────────────────┘
                     │
                     ▼
┌────────── ELASTICSEARCH-FS IMPL ──────────┐
│  Converts fs ops → ES queries             │
│  ls/cd/find: in-memory tree traversal     │
│  cat: direct ES doc lookup                │
│  grep: ES filter + regex refinement       │
└─────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────── DATA LAYER ────────────────┐
│  Elasticsearch cluster with DLS           │
└─────────────────────────────────────────────┘
```

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
