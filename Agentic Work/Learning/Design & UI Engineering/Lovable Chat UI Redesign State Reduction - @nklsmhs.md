---
title: "Lovable Chat UI Redesign State Reduction"
url: "https://x.com/nklsmhs/status/2016631117248360490?s=42"
platform: twitter
date_saved: 2026-01-29
source: "niklas (@nklsmhs)"
content_type: tweet
topics: [UI & Design Engineering, State Management, Design Systems]
tags: [ui-design, chat-ui, state-management, complexity-reduction, lovable, design-process, ux-engineering]
status: unread
---

> three weeks ago, when i started to redesign @Lovable's chat ui, i tried mapping all possible states. there were 14,400 combinations. today, we shipped our new ui with eight.

| Metric | Count |
|--------|-------|
| Likes | 503 |
| Retweets | 10 |

**Topics:** [[UI & Design Engineering]], [[State Management]], [[Design Systems]]

## Key Points
- **14,400 → 8 States**: Radical state reduction from 14,400 possible combinations to 8 shipped states — demonstrates the power of ruthless simplification in UI design
- **Combinatorial Explosion Problem**: Chat UIs have many variables (loading, error, empty, typing, sent, delivered, read, reactions, threads, etc.) — naive state management explodes exponentially
- **Three-Week Sprint**: Full redesign completed in three weeks — suggests focused scope and decisive design leadership
- **[[Lovable]] Product Context**: Lovable is an AI product builder — their chat UI is likely core to the agent interaction experience, making this simplification business-critical

### Why This Matters
Most chat UI redesigns fail by adding states rather than removing them. This thread demonstrates the inverse approach: start by mapping the full state space, then aggressively collapse dimensions until only essential states remain. The 1,800x reduction (14,400 → 8) is a case study in complexity management.

### Design Principle
The insight is that most state combinations are either:
1. **Unreachable** — can't actually happen given business logic
2. **Visually identical** — user can't distinguish between them
3. **Redundant** — can be merged without information loss

Mapping first, then collapsing, ensures no important states are missed while eliminating noise.

*Filed in: [[Twitter Posts MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
