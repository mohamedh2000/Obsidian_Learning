---
title: "Locomotive Scroll 5 Now Built on Lenis"
url: "https://x.com/locomotivemtl/status/2013993927435505915?s=42"
platform: twitter
date_saved: 2026-01-21
source: "Locomotive® (@locomotivemtl)"
content_type: tweet
topics: [UI & Design Engineering, Animation & Motion]
tags: [scroll-library, lenis, parallax, intersection-observer, typescript, animation, smooth-scroll, frontend]
status: unread
---

> Locomotive releases v5 of their scroll library — now built on Lenis for smooth scrolling, plus their own detection and animation layer. 9.4kB total for in-view detection, parallax, and progress tracking.

| Metric | Count |
|--------|-------|
| Likes | 562 |
| Retweets | 47 |

**Topics:** [[UI & Design Engineering]], [[Animation & Motion]]

## Key Points
- **Complete Rewrite on Lenis**: Version 5 is built as a wrapper around [[Lenis]] (smooth scroll library), adding Locomotive's detection and animation capabilities on top — combining two popular scroll libraries into one cohesive package
- **9.4kB Lightweight Bundle**: Full feature set including in-view detection, parallax, progress tracking, and smooth easing in under 10kB — competitive with standalone Intersection Observer utilities
- **Dual Intersection Observers**: Uses two separate observers internally for optimized performance — one for in-view triggers, one for progress calculations
- **TypeScript-First Development**: Full type support out of the box, unlike earlier JavaScript-only versions

### Technical Features
```
Locomotive Scroll 5 Feature Stack:
┌─────────────────────────────┐
│   Parallax Effects          │  ← data-attribute driven
├─────────────────────────────┤
│   Progress Tracking         │  ← CSS vars + JS events
├─────────────────────────────┤
│   In-View Detection         │  ← Intersection Observer
├─────────────────────────────┤
│   Smooth Scrolling (Lenis)  │  ← lerp, duration, easing
└─────────────────────────────┘
```

### Why This Matters
The Locomotive + Lenis combination addresses the fragmentation in scroll libraries — previously you'd pick Lenis for smooth scrolling OR Locomotive for detection/animation. Now they're unified. Smart touch detection auto-disables parallax on mobile, and it works with native scrollbars (no custom scrollbar hacks).

*Filed in: [[Saved Links MOC]]*
