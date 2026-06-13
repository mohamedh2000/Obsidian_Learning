---
title: "Smooothy - Configurable Smooth Slider API"
url: "https://smooothy.federic.ooo/"
platform: web
date_saved: 2026-06-12
source: "Federico (federic.ooo)"
content_type: tool
topics: [UI & Design Engineering, Animation & Motion]
tags: [slider, carousel, smooth-scroll, animation, javascript, framework-agnostic, lenis, css, frontend]
status: unread
---

> Smooothy is a "bring your own whatever" slider API — a highly configurable, extensible JavaScript library for creating smooth carousels that works with any framework or platform.

| | |
|---|---|
| **Source** | Federico (federic.ooo) |
| **Saved** | 2026-06-12 |
| **Type** | tool |
| **URL** | [Link](https://smooothy.federic.ooo/) |

## Topics

[[UI & Design Engineering]] | [[Animation & Motion]]

## Key Points

- **Framework-Agnostic Design**: Works with vanilla JS, React, Vue, Webflow — no lock-in to any particular framework or build system
- **CSS-Based Styling**: Uses CSS for styling with infinite looping and snap options, keeping configuration declarative
- **Configurable Physics**: Drag speed, lerp/damp speeds, and conditional activation are all customizable parameters
- **Real-Time Parameter Reading**: Exposes speed, progress, and parallax values for building complex scroll-linked effects
- **Extensible API**: Designed for custom behavior — not just a drop-in component but a foundation for building custom slider implementations

### Technical Architecture
```
Smooothy API Stack:
┌─────────────────────────────┐
│   Custom Extensions         │  ← your own behavior
├─────────────────────────────┤
│   Physics Config            │  ← lerp, damp, drag speed
├─────────────────────────────┤
│   Snap & Loop Options       │  ← CSS-driven
├─────────────────────────────┤
│   Core Smooth Engine        │  ← real-time values
└─────────────────────────────┘
```

### Why This Matters
Most slider libraries are opinionated black boxes — you get their preset behavior or nothing. Smooothy inverts this by exposing primitives (speed, progress, parallax) and letting you compose the behavior you need. Similar philosophy to [[Lenis]] for scrolling, but applied to carousels and sliders.

## Notes

(Personal annotations)

---

*Filed in: [[Tools & Products MOC]] | [[Saved Links MOC]]*
