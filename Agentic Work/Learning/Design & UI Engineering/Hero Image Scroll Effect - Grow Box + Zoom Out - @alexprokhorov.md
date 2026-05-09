---
title: "Hero Image Scroll Effect - Grow Box + Zoom Out"
url: "https://x.com/alexprokhorov/status/2052427109407023177?s=42"
platform: twitter
date_saved: 2026-05-08
source: "Alex Prokhorov (@alexprokhorov)"
content_type: tweet
topics: [UI & Design Engineering, Scroll Animations]
tags: [scroll-animation, hero-image, zoom-effect, parallax, ux-pattern, claude-ai, vibe-coding, web-animation]
status: unread
---

> "Most 'hero image expands on scroll' effects do it wrong. The right move: grow the box AND zoom OUT. Same content but more of the scene reveals as it grows."

| Metric | Count |
|--------|-------|
| Likes | 491 |
| Retweets | 17 |

**Topics:** [[UI & Design Engineering]], [[Scroll Animations]]

## Key Points
- Common mistake: Hero images just scale up on scroll (same content, bigger)
- Correct technique: Grow the container AND zoom OUT simultaneously
- Result: Same content initially, but more of the scene reveals as container expands
- Creates a "window opening" effect rather than a simple zoom
- Built with Claude AI ("vibe-coded")

### The Difference Explained

```
WRONG (typical):                     RIGHT (this technique):
┌─────┐                              ┌─────┐
│ IMG │  ──scroll──►  ┌───────┐      │ IMG │  ──scroll──►  ┌───────────┐
│     │               │  IMG  │      │     │               │    IMG    │
└─────┘               │ (same)│      └─────┘               │ (reveals  │
                      └───────┘                            │  more)    │
                                                           └───────────┘
Box grows,            Box grows,
image scales          image zooms OUT
= same view           = expanded scene
```

### Implementation Pattern
1. Container grows on scroll (width/height increase)
2. Image simultaneously zooms out (scale decreases or object-position shifts)
3. Net effect: viewport expands, revealing more content that was cropped initially
4. Requires image to have "bleed" area beyond initial crop

### Design Pattern Context
This is a cinematic technique borrowed from film — the "pull back reveal." It creates a sense of discovery and scale. Unlike simple zoom effects that feel mechanical, this creates emotional impact. High engagement (491 likes) confirms this resonates with designers as an underused technique.

*Filed in: [[Saved Links MOC]]*
