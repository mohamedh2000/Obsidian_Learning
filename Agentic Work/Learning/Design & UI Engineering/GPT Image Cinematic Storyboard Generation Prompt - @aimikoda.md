---
title: "GPT Image Cinematic Storyboard Generation Prompt"
url: "https://x.com/aimikoda/status/2061042840889639278?s=42"
platform: twitter
date_saved: 2026-05-31
source: "Kōda (@aimikoda)"
content_type: tutorial
topics: [Storyboarding, AI Image Generation, Prompt Engineering]
tags: [gpt-image, storyboard, cinematic, prompt-engineering, animation, visual-storytelling]
status: unread
---

> Kōda shares a comprehensive GPT Image 2 prompt for generating cinematic storyboards from a character sheet reference — complete with director strip, style keyframes, and 8-panel sequence.

| Metric | Count |
|--------|-------|
| Likes | 5 |
| Retweets | 0 |

**Topics:** [[Storyboarding]], [[AI Image Generation]], [[Prompt Engineering]]

## Key Points

- Uses character sheet as reference input
- Generates a 4x2 grid (8 panels) storyboard with production metadata
- Includes director strip with beat line, camera path, action path, rhythm track, escalation map, state track, and style track

### Storyboard Pipeline

```
┌────────────────┐     ┌─────────────────┐     ┌───────────────┐
│ Character Sheet│────►│ GPT Image 2     │────►│ Storyboard    │
│   Reference    │     │ Storyboard Gen  │     │   Output      │
└────────────────┘     └─────────────────┘     └───────┬───────┘
                                                       │
                                                       ▼
                                               ┌───────────────┐
                                               │ Seedance 2.0  │
                                               │ Video Output  │
                                               └───────────────┘
```

### Prompt Architecture

The prompt is structured into distinct sections:

1. **PROJECT CARD**: Title lockup, meta line, priority line, micro brief
2. **CONTINUITY HEADER**: Sequence ID, style packet (visual direction), reference priority
3. **SCENE PACKET**: Premise, summary, location, character roles, start/end state, action chain, prop/effect state, must-read theme
4. **STYLE KEYFRAMES**: Small swatches showing final video rendering intent
5. **STYLE LOCKS**: Visual constraints (anime-fantasy, 35mm film feel, emerald light, ruby flame)
6. **SHEET POLISH**: Layout rules for the storyboard sheet itself
7. **DRAWING ENERGY**: Pose and rhythm guidance
8. **PANEL RULES**: Monochrome sketch style, no color inside panels
9. **DIRECTOR STRIP**: 7-track animatic metadata board
10. **SEQUENCE**: 8 individual panel specifications

### Example Panel Spec (Panel 07 - Ruby Flame Impact)

```
Shot intent: Deliver the spectacular magical payoff.
Camera: Low-angle wide 24mm with strong parallax, wand foreground, monster midground.
Action: Ruby flame blast erupts from wand, engulfs monster in one decisive strike.
Continuity: Ruby holds ground screen-left; flame travels left-to-right; monster hit screen-right.
Strip cell: [P07 impact] / [low parallax] / [flame strikes] / [final hit] / [peak] / [monster hit] / [red fire]
```

### Design Philosophy

The prompt explicitly differentiates between:
- **Standard reference sheet** (rejected): grid-based, blueprint-style, catalog layout
- **Cinematic identity board** (desired): asymmetrical, elegant, artbook-like, animation studio character study

Panel rules enforce monochrome low-detail sketches with no color, labels, or overlays inside the artwork — keeping the focus on composition and action flow.

*Filed in: [[Saved Links MOC]]*
