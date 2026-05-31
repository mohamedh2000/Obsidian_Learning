---
title: "Midjourney to GPT Image 3D Character Sheet Pipeline"
url: "https://x.com/aimikoda/status/2061042556100608367?s=42"
platform: twitter
date_saved: 2026-05-31
source: "Kōda (@aimikoda)"
content_type: tutorial
topics: [Character Design, AI Image Generation, Prompt Engineering]
tags: [midjourney, gpt-image, character-sheet, 3d-character, prompt-engineering, ai-art, character-design]
status: unread
---

> Kōda shares a two-step workflow: generate a 2D character in Midjourney, then convert to a full 3D character identity board using GPT Image 2.

| Metric | Count |
|--------|-------|
| Likes | 13 |
| Retweets | 0 |

**Topics:** [[Character Design]], [[AI Image Generation]], [[Prompt Engineering]]

## Key Points

- **Step 1**: Midjourney generates the initial character concept (`mage girl --ar 2:3 --profile txgf1m1 --stylize 1000`)
- **Step 2**: GPT Image 2 transforms it into a production-ready 3D character identity board
- Output is designed for downstream AI video/image generation reference

### Pipeline

```
┌───────────────┐     ┌────────────────────┐
│  Midjourney   │────►│   GPT Image 2      │
│ 2D Character  │     │ 3D Identity Board  │
└───────────────┘     └────────────────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Storyboard + Video │
                    │    Generation      │
                    └────────────────────┘
```

### GPT Image 2 Prompt Structure

The prompt creates a 16:9 character identity board with:

1. **Layout Rules**
   - Asymmetrical, elegant, artbook-like layout (NOT standard reference sheets)
   - Large empty space, varied image scale, intentional imbalance
   - No overlapping character images — clear separation and breathing room

2. **Main Composition**
   - One large hero full-body view as visual anchor
   - Supporting studies: neutral pose, back view, profile, seated, leaning, crouching, top-down angle, low-angle, expressive portraits

3. **Identity Lock**
   - Strict consistency: same face, hair, outfit, body proportions, posture language

4. **Artistic Sections**
   - Silhouette study area (2-3 black silhouettes)
   - Expression study area (subtle emotional variations)
   - Detail study area (face, hair, outfit close-ups)

5. **Text Design**
   - Minimal CHARACTER ID block with: Name, Role, Core Mood, Visual Signature

### Design Philosophy

> "The final image should feel like an artistic character identity board designed to help an AI model understand the character's face, silhouette, outfit, posture and emotional range."

This is explicitly production-oriented — the output serves as reference for video generation models like Seedance.

*Filed in: [[Saved Links MOC]]*
