---
title: "Seedance 2.0 Storyboard to Video Prompt"
url: "https://x.com/aimikoda/status/2061043111023837249?s=42"
platform: twitter
date_saved: 2026-05-31
source: "Kōda (@aimikoda)"
content_type: tutorial
topics: [AI Video Generation, Prompt Engineering, Animation Pipeline]
tags: [seedance, video-generation, storyboard-to-video, prompt-engineering, ai-animation, character-animation]
status: unread
---

> Kōda completes the pipeline: using both character sheet and storyboard as references to generate the final cinematic video with Seedance 2.0.

| Metric | Count |
|--------|-------|
| Likes | 6 |
| Retweets | 0 |

**Topics:** [[AI Video Generation]], [[Prompt Engineering]], [[Animation Pipeline]]

## Key Points

- Final step in the Midjourney → GPT Image → Seedance pipeline
- Uses BOTH character sheet and storyboard as reference inputs
- Explicit instructions to ignore storyboard layout elements (borders, text, frames)
- Adds a time-slow-motion narrative beat not in the original storyboard

### Complete Pipeline

```
┌───────────────┐     ┌────────────────┐     ┌──────────────┐     ┌──────────────┐
│  Midjourney   │────►│  GPT Image 2   │────►│  GPT Image 2 │────►│ Seedance 2.0 │
│ 2D Character  │     │ Character Sheet│     │  Storyboard  │     │ Final Video  │
└───────────────┘     └────────────────┘     └──────────────┘     └──────────────┘
```

### Seedance Prompt Structure

The prompt provides:

1. **Reference Rules**
   - `@[storyboard ref]` = authoritative shot blueprint (ignore visual layout elements)
   - `@[character ref]` = authoritative Ruby character reference
   - Each storyboard panel = one sequential cinematic beat

2. **Final Style Definition**
   - Premium cinematic anime-fantasy film
   - Stylized cinematic realism
   - Painterly forest depth, emerald woodland atmosphere
   - 35mm film texture, clean cel shading

3. **8-Beat Sequence** (with time-manipulation enhancement)
   1. Ruby walks through quiet forest clearing
   2. Monster bursts from foliage
   3. **Time suddenly slows** — falling leaves and debris hang in air
   4. Ruby plants feet, thrusts spellbook forward
   5. Pages flip rapidly through magical wind (world still slowed)
   6. Pages lock on spell; Ruby raises wand
   7. **Time snaps back** — ruby flame blast engulfs monster
   8. Monster vanishes to ash; Ruby holds stance with lingering particles

### Notable Enhancement

The video prompt adds a **bullet-time / time-dilation effect** (beats 3-6) that wasn't explicitly in the storyboard — demonstrating how the final prompt can layer additional narrative techniques on top of the storyboard structure.

### Full Workflow Summary

| Step | Tool | Output |
|------|------|--------|
| 1 | Midjourney | 2D character concept |
| 2 | GPT Image 2 | 3D character identity board |
| 3 | GPT Image 2 | Cinematic storyboard (8 panels) |
| 4 | Seedance 2.0 | Final 16:9 video |

This represents a complete AI-native animation production pipeline from concept to rendered video.

*Filed in: [[Saved Links MOC]]*
