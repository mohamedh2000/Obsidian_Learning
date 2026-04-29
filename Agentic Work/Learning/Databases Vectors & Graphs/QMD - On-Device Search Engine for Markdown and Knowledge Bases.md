---
title: "QMD - On-Device Search Engine for Markdown and Knowledge Bases"
url: "https://github.com/tobi/qmd"
platform: github
date_saved: 2026-01-31
source: "Tobi Lütke (@tobi)"
content_type: repo
topics: [Databases, Knowledge Management]
tags: [local-search, markdown, hybrid-search, bm25, vector-search, mcp-server, llm-reranking, sqlite, knowledge-base, obsidian-compatible]
status: unread
---

> On-device search engine for everything you need to remember — indexes markdown notes, meeting transcripts, documentation, and knowledge bases with hybrid BM25 + semantic search and LLM reranking, all offline.

| Metric | Count |
|--------|-------|
| Stars | 23300 |
| Forks | 1500 |

**Topics:** [[Databases Vectors & Graphs]], [[Knowledge Management]]

## Key Points
- Hybrid search combining BM25 full-text search with vector semantic search — best of both keyword and meaning-based retrieval
- LLM-powered query expansion and re-ranking for improved relevance without cloud dependencies
- MCP server integration means AI assistants (Claude, etc.) can search your knowledge base as a tool
- AST-aware code chunking via Tree-sitter — code files are indexed with structural understanding, not just text

### Architecture
- **Storage:** SQLite with FTS5 extension for full-text search
- **Inference:** node-llama-cpp for local GGUF model inference (no API calls)
- **Parsing:** Tree-sitter for language-aware code chunking
- **Runtime:** Node.js/Bun

### Search Modes
- **Keyword:** Traditional BM25 full-text search
- **Semantic:** Vector similarity search
- **Hybrid:** Combined scoring from both methods
- Context tagging for improved relevance

### Why It Matters
Local-first search with no cloud dependency. Your notes, transcripts, and docs stay on-device while getting semantic search capabilities. MCP integration means agents can query your personal knowledge base — powerful for workflows like "find my notes on X" or "what did we discuss about Y in meetings."

*Filed in: [[Saved Links MOC]]*
