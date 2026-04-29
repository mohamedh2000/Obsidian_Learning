---
title: "Claude Code --from-pr Flag for Session Resume"
url: "https://x.com/lydiahallie/status/2017680321094004997?s=42"
platform: twitter
date_saved: 2026-01-31
source: "Lydia Hallie (@lydiahallie)"
content_type: tweet
topics: [Claude Code, Developer Tools]
tags: [claude-code, github-pr, session-management, resume, workflow, git-integration, developer-experience]
status: unread
---

> Claude Code now supports the --from-pr flag — resume any session linked to a GitHub PR by number, URL, or pick interactively. Sessions auto-link when a PR is created!

| Metric | Count |
|--------|-------|
| Likes | 1675 |
| Retweets | 98 |

**Topics:** [[Claude Code & Anthropic]], [[Developer Tools]]

## Key Points
- New `--from-pr` flag lets you resume Claude Code sessions by referencing a GitHub PR
- Three input modes: PR number, full PR URL, or interactive picker
- Sessions automatically link to PRs when created — no manual tagging required
- Enables PR-centric workflows: come back to any PR and resume exactly where you left off

### Usage Patterns
```bash
# Resume by PR number
claude --from-pr 123

# Resume by URL
claude --from-pr https://github.com/org/repo/pull/123

# Interactive picker
claude --from-pr
```

### Why It Matters
PR-linked sessions solve the "which session was this?" problem. Instead of hunting through session history, you can navigate via the artifact that matters: the PR itself. Natural fit for code review, iteration, and revisiting work-in-progress.

### Implications
- PR becomes the canonical reference point for a unit of work
- Enables async collaboration: teammate opens PR, you resume their session with full context
- Reduces session management overhead — PRs are already organized; sessions now inherit that organization

*Filed in: [[Saved Links MOC]]*
