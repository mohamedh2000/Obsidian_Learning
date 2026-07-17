---
title: "RAG as a Standalone Retrieval Service - @_avichawla"
url: "https://x.com/_avichawla/status/2072265080851587239?s=42"
platform: twitter
date_saved: 2026-07-01
source: "Avi Chawla (@_avichawla)"
content_type: tweet
topics: [rag, retrieval, mcp, agents]
tags: [twitter, rag, retrieval, mcp, embeddings]
status: unread
---

# RAG as a Standalone Retrieval Service - @_avichawla

> Google and Anthropic both moved retrieval out of the app and turned it into a standalone service that agents invoke — resolving stale embeddings and coupled infrastructure.

| | |
|---|---|
| **Source** | Avi Chawla (@_avichawla) |
| **Saved** | 2026-07-01 |
| **Type** | tweet |
| **Engagement** | 439 likes, 84 retweets |
| **URL** | [Link](https://x.com/_avichawla/status/2072265080851587239?s=42) |

## Topics

[[LLM Research]] | [[AI Agents]]

## Key Points

- Anthropic's MCP and Google's RAG Engine both expose retrieval as a standalone tool an agent invokes, rather than a pipeline baked into one app.
- Naive in-app RAG fails two ways: stale embeddings (index drifts from source until re-run) and coupled infrastructure (each app duplicates connectors, chunking, embedding).
- Fix: separate ingestion from query and run ingestion as a standing layer with content-hash sync, so only changed data is re-embedded and one API serves both chatbot and agent.
- The agent calls the retrieval layer as a tool in a loop — reason, search, read, refine — instead of retrieving once at the start.
- Remaining issue is the chunk as unit of retrieval (no semantic boundary/version/source); moving to structured blocks that embed a validated Q&A pair cut corpus size 40x and improved vector relevance 2.3x.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
