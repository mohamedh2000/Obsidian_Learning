---
title: "Design Plugin with 5 Variations and Element Feedback - @0xdesigner"
url: "https://x.com/0xdesigner/status/2012985885680132423?s=42"
platform: twitter
date_saved: 2026-01-18
source: "0xDesigner (@0xdesigner)"
content_type: tool
topics: [Design Tools, AI Agents]
tags: [claude-code, design-plugin, ui-variations, iterative-design, ai-design, figma-style-feedback]
status: unread
---

> Great idea by @benjitaylor. I just added this into the design-plugin. Claude will ask you what you want to design/refine and generate 5 variations. Then you can leave comments directly on the elements for claude.

| Metric | Count |
|--------|-------|
| Likes | 395 |
| Retweets | 22 |

**Topics:** [[Design Tools]], [[AI Agents]]

## Key Points
- **5 distinct variations per request**: Claude generates multiple design approaches for comparison rather than a single option
- **Figma-style element feedback**: Click any element to annotate specific design aspects with precision — Claude understands feedback at the element level
- **Design system inference**: Automatically detects colors, typography, and spacing from existing Tailwind configs or component libraries
- **Real code output**: Produces functional React/Next.js components in your actual framework, not static mockups

### How It Works
1. Invoke `/design-and-refine:start` in Claude Code
2. Plugin interviews designer about goals and constraints
3. Generates 5 distinct approaches displayed at `/__design_lab` route
4. User provides element-level feedback
5. Claude synthesizes refined versions through iterative loops
6. Clean handoff with `DESIGN_PLAN.md` documenting implementation

**Supports:** Next.js, Vite, Remix, Astro, Create React App

**GitHub Repo:** [0xdesign/design-plugin](https://github.com/0xdesign/design-plugin)

*Filed in: [[Saved Links MOC]]*
