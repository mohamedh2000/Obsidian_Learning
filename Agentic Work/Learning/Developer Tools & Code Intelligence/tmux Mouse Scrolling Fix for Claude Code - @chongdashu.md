---
title: "tmux Mouse Scrolling Fix for Claude Code - @chongdashu"
url: "https://x.com/chongdashu/status/2020792219070763151?s=42"
platform: twitter
date_saved: 2026-02-10
source: "Chong-U (@chongdashu)"
content_type: tip
topics: [Developer Tools, CLI & Terminal]
tags: [tmux, scrolling, mouse-support, claude-code, codex, terminal-config, bug-fix]
status: unread
---

> For those complaining that tmux has a scrolling bug — add `set -g mouse on` to ~/.tmux.conf and restart.

| Metric | Count |
|--------|-------|
| Likes | 123 |
| Retweets | 8 |

**Topics:** [[Developer Tools]], [[CLI & Terminal]]

## Key Points
- tmux's default configuration disables mouse support, causing scroll-wheel behavior to feel broken
- Adding `set -g mouse on` to `~/.tmux.conf` enables mouse scrolling through session history
- This fix is essential for Claude Code/Codex sessions where output can span thousands of lines
- After editing the config, either restart tmux or run `tmux source-file ~/.tmux.conf` to apply

### The Fix
```bash
# 1. Open or create tmux config
nano ~/.tmux.conf

# 2. Add this line
set -g mouse on

# 3. Save and restart tmux (or source the config)
tmux source-file ~/.tmux.conf
```

### Why This Matters
When running Claude Code in tmux for remote/persistent sessions, the inability to scroll back through output is a major UX friction. This one-liner fix restores expected scrolling behavior.

*Filed in: [[Saved Links MOC]]*
