---
title: "GitNexus Knowledge Graph for AI Agents"
url: "https://x.com/oliviscusai/status/2032418898516340915?s=42"
platform: twitter
date_saved: 2026-03-13
source: "Oliver Prompts (@oliviscusai)"
content_type: tool
topics: [Code Intelligence, Developer Tools, AI Agents]
tags: [gitnexus, knowledge-graph, mcp, tree-sitter, code-indexing, ai-agents, open-source, graph-rag]
status: unread
---

> GitNexus turns any GitHub repo into an interactive knowledge graph, indexing every dependency, call chain, and execution flow so AI agents never miss code. 100% open source.

| Metric | Count |
|--------|-------|
| Likes | 1901 |
| Retweets | 296 |

**Topics:** [[Code Intelligence]], [[Developer Tools]], [[AI Agents]]

## Key Points
- **Zero-server architecture**: GitNexus runs entirely client-side in the browser or via CLI with `npx gitnexus analyze` — no backend infrastructure required
- **Multi-phase indexing pipeline**: Walks file tree (Structure), extracts symbols via Tree-sitter ASTs (Parsing), resolves imports and calls across files (Resolution), groups symbols into functional communities (Clustering), traces execution flows from entry points (Processes), and builds hybrid search indexes (Search)
- **Deep Claude Code integration**: MCP tools + agent skills + PreToolUse hooks that enrich searches with graph context + PostToolUse hooks that auto-reindex after commits — giving Claude a structural view of your codebase
- **Seven specialized MCP tools**: Hybrid search, symbol context lookups, blast radius analysis, git-diff impact mapping, and coordinated multi-file refactoring exposed to AI agents like Cursor, Claude Code, and Codex
- **Broad language support**: TypeScript, JavaScript, Python, Java, C, C++, C#, Go, Rust, PHP, Swift

### Why This Matters for AI Coding Agents

Traditional AI coding tools operate on flat text slices without understanding dependency relationships or call chains. GitNexus solves this by building a complete knowledge graph of your codebase, so when an agent needs to modify a function, it can see every caller, every downstream dependency, and every execution path that touches that code. The CLI command `npx gitnexus analyze` handles everything: indexing, installing agent skills, registering hooks, and creating AGENTS.md/CLAUDE.md context files.

GitHub: [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)

*Filed in: [[Saved Links MOC]]*
