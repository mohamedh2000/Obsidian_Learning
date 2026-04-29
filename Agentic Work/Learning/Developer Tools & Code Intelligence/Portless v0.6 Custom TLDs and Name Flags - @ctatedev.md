---
title: "Portless v0.6 Custom TLDs and Name Flags - @ctatedev"
url: "https://x.com/ctatedev/status/2031508669725036833?s=42"
platform: twitter
date_saved: 2026-03-09
source: "Chris Tate (@ctatedev)"
content_type: tweet
topics: [Developer Tools, Local Development]
tags: [twitter, portless, local-development, networking, tld, cli-tools]
status: unread
---

# Portless v0.6 Custom TLDs and Name Flags - @ctatedev

> Portless v0.6 release with custom TLDs (.test, .internal), `portless get` command, and --name flag for explicit service naming.

| Metric | Count |
|--------|-------|
| Likes | 369 |
| Retweets | 17 |

**Topics:** [[Developer Tools]], [[Local Development]]

## Key Points

- **Custom TLDs** — Use `.test`, `.internal`, or any TLD instead of `.localhost` — useful for matching production domain structures or avoiding browser localhost special handling
- **`portless get` command** — Print the URL for any registered service by name — enables scripting and integration with other tools that need to discover service endpoints
- **`--name` flag** — Override the auto-inferred service name while preserving git worktree prefixes — solves the problem of multiple similar services needing distinct identifiers
- The release framing as "one helluva update" suggests these were highly requested features from the community

### Why This Matters

Local development networking is deceptively complex: port conflicts, service discovery, SSL for localhost, and consistent naming across team members. Portless abstracts this into a simple CLI while remaining composable with worktree-based development workflows (common in monorepos and multi-branch parallel work).

*Filed in: [[Saved Links MOC]]*
