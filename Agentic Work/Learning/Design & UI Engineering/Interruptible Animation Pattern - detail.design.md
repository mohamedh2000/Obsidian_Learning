---
title: "Interruptible Animation Pattern - detail.design"
url: "https://detail.design/detail/interruptible-animation"
platform: web
date_saved: 2026-01-29
source: "Rene Wang (@renedotwang)"
content_type: guide
topics: [UI Animation, Micro-Interactions]
tags: [animation, interruptible, motion-design, perceived-performance, user-control, detail-design, ux-pattern]
status: unread
---

> The ability to immediately trigger close events without waiting for an animation to complete makes interfaces feel durable, snappy, and well considered.

**Topics:** [[UI Animation]], [[Micro-Interactions]]

## Key Points
- **Core principle**: Animations should be interruptible—never force users to wait for motion to finish before accepting their next input
- **Perceived quality signals**: "Durable, snappy, and well considered"—three adjectives that define premium interface feel
- **User intent > animation completion**: Respecting user intent (e.g., wanting to dismiss) takes priority over finishing decorative motion
- **Anti-pattern**: Interfaces that queue inputs or ignore them during animations feel sluggish and unresponsive

### Implementation Implications
- Use animation libraries that support interruption (Framer Motion, GSAP, anime.js) rather than CSS transitions that can't be canceled mid-flight
- Design state machines where close/dismiss events short-circuit any in-progress animation
- Consider `will-change` and GPU compositing for smooth mid-animation cancellation
- Test by rapidly opening/closing modals, tooltips, drawers—if there's lag, the pattern is broken

### Why This Matters
Interruptible animations are one of the clearest signals of craft in interface design. They're invisible when done right (users don't notice them) but immediately frustrating when done wrong. This pattern applies to modals, tooltips, dropdowns, drawers, toasts, and any animated UI that can be dismissed.

*Filed in: [[Saved Links MOC]]*
