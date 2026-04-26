---
title: "Claude Hooks with Game Sound Alerts - @delba_oliveira"
url: "https://x.com/delba_oliveira/status/2020515010985005255?s=42"
platform: twitter
date_saved: 2026-02-09
source: "Delba (@delba_oliveira)"
content_type: tip
topics: [Claude Code & Anthropic, Developer Experience]
tags: [claude-code, hooks, notifications, audio-alerts, productivity, starcraft, warcraft, mario, developer-experience]
status: unread
---

> 10x productivity tip: use Claude hooks with sounds so Claude alerts you when it finishes a task or needs permission. Add your favourite childhood game sounds like Starcraft, Warcraft, or Mario.

| Metric | Count |
|--------|-------|
| Likes | 5,711 |
| Retweets | 419 |

**Topics:** [[Claude Code & Anthropic]], [[Developer Experience]]

## Key Points
- Claude Code's hooks system can trigger shell commands on events like task completion or permission requests
- Playing audio alerts via hooks solves the "staring at terminal waiting" problem — work on other things and get notified
- Using nostalgic game sounds (Starcraft "job done", Mario coin, Warcraft "work complete") adds delight and makes alerts distinctive
- High engagement (5.7K likes) reflects strong demand for async-friendly agent workflows

### Implementation Pattern
```bash
# Example hook in settings.json or CLAUDE.md
"hooks": {
  "onTaskComplete": "afplay ~/sounds/starcraft-job-done.mp3",
  "onPermissionRequired": "afplay ~/sounds/mario-coin.mp3"
}
```

### Why It Matters
AI coding agents are fundamentally async — they work while you don't watch. Audio notifications bridge the gap between "fire and forget" and "babysitting the terminal," enabling true parallel work.

*Filed in: [[Saved Links MOC]]*
