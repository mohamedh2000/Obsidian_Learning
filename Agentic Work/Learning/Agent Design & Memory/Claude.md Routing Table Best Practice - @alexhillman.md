---
title: "Claude.md Routing Table Best Practice"
url: "https://x.com/alexhillman/status/2018038033111736427?s=42"
platform: twitter
date_saved: 2026-04-02
source: "Alex Hillman (@alexhillman)"
content_type: tweet
topics: [Claude Code, Best Practices]
tags: [claude-code, claude-md, includes, routing, context-engineering, session-history, workflow-optimization]
status: unread
---

> Don't put everything in your claude.md—use a routing table of contents near the top that tells the agent when to use specific includes based on task/workflow.

| Metric | Count |
|--------|-------|
| Likes | 59 |
| Retweets | 0 |

**Topics:** [[Claude Code & Anthropic]], [[Agent Design & Memory]]

## Key Points
- Bug-fixing instructions belong in a task-specific include, not the main `claude.md`—unless you're fixing bugs in every single session
- The recommended pattern is a **routing table** near the top of `claude.md` that maps task types to their respective include files
- This keeps the main instructions lightweight while preserving access to specialized knowledge when needed
- **Advanced technique:** Create a command that periodically scans session history and suggests updates/additions/removals from routing rules based on actual usage patterns

### Implementation Pattern
```
# claude.md routing table
- Bug fixes → @include(debugging.md)
- Feature dev → @include(feature-workflow.md)
- Refactoring → @include(refactor-patterns.md)
```

### Why It Matters
Context window is precious. Loading every instruction into every session wastes tokens on irrelevant guidance. The routing pattern ensures agents get task-relevant context without the bloat.

*Filed in: [[Saved Links MOC]]*
