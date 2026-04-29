---
title: "Bun Settings Fix for prefersReducedMotion"
url: "https://x.com/dani_avila7/status/2018096128474915110?s=42"
platform: twitter
date_saved: 2026-04-02
source: "Daniel San (@dani_avila7)"
content_type: tweet
topics: [Bun, Developer Tools]
tags: [bun, developer-tools, settings-json, accessibility, terminal, motion-preferences, config-fix]
status: unread
---

> Quick fix for Bun motion issues: add "prefersReducedMotion": true to settings.json and everything works fine.

| Metric | Count |
|--------|-------|
| Likes | 116 |
| Retweets | 3 |

**Topics:** [[Bun]], [[Developer Tools]]

## Key Points
- The `prefersReducedMotion` setting in `settings.json` resolves animation-related issues in Bun's terminal output
- This is a configuration-level fix rather than a code change, making it non-invasive and easy to apply
- The setting aligns Bun with accessibility preferences for reduced motion, which also fixes rendering glitches
- Credit given to @jarredsumner (Bun's creator) for the solution, suggesting this is an officially endorsed workaround

### Context
Bun's terminal animations can sometimes cause rendering issues depending on terminal emulator capabilities. The `prefersReducedMotion` flag disables these animations, which both improves accessibility and sidesteps compatibility problems with certain terminal environments.

*Filed in: [[Saved Links MOC]]*
