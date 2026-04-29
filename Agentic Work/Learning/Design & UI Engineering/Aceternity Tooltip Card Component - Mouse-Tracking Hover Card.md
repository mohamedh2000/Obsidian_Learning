---
title: "Aceternity Tooltip Card Component - Mouse-Tracking Hover Card"
url: "https://ui.aceternity.com/components/tooltip-card"
platform: web
date_saved: 2026-01-27
source: "Aceternity"
content_type: guide
topics: [Design Systems, React]
tags: [aceternity, react-component, tooltip, framer-motion, hover-effect, mouse-tracking, tailwind-css, shadcn-compatible]
status: unread
---

> A tooltip card container that dynamically tracks cursor position, displaying contextual information in an animated card when hovering over trigger elements.

**Topics:** [[Design & UI Engineering]], [[React]]

## Key Points
- The tooltip dynamically positions itself relative to cursor movement while maintaining proximity to the trigger element
- Automatic viewport boundary detection prevents overflow on all edges (top, bottom, left, right)
- Uses Framer Motion for spring-based height and opacity transitions during appear/disappear
- Touch support included with 2-second visibility delay after touch — works across desktop and mobile

### Installation
```bash
npx shadcn@latest add @aceternity/tooltip-card
```

### Props
- `content` (required): string or React.ReactNode — the tooltip content
- `children` (required): React.ReactNode — the trigger element
- `containerClassName` (optional): string for additional CSS customization

### Why It Matters
Mouse-tracking tooltips add subtle interactivity that makes UIs feel responsive and tactile. This component packages the math (viewport boundary detection, spring physics, touch handling) into a drop-in solution compatible with shadcn patterns.

*Filed in: [[Saved Links MOC]]*
