---
title: "Liquid Metal WebGL Button Component"
url: "https://www.vengenceui.com/docs/liquid-metal"
platform: web
date_saved: 2026-01-29
source: "VengeanceUI"
content_type: tutorial
topics: [UI & Design Engineering, WebGL, Component Libraries]
tags: [react, webgl, shaders, button, tailwind, nextjs, design-system, animation, chrome-effect]
status: unread
---

> A mesmerizing liquid chrome border effect button using WebGL shaders — premium component from VengeanceUI that creates flowing, metallic reflections through animated distortion patterns.

| | |
|---|---|
| **Source** | VengeanceUI Docs |
| **Type** | Component Library |
| **Framework** | React / Next.js |

**Topics:** [[UI & Design Engineering]], [[WebGL]], [[Component Libraries]]

## Key Points
- **WebGL Shader Technology**: Uses GPU-accelerated shaders to render the liquid chrome effect — not CSS animations, meaning smooth performance even on complex distortion patterns
- **Layered Architecture**: The component layers a WebGL-powered liquid metal shader as a border behind a standard button element — the shader runs independently of the button's content
- **Customizable Parameters**: Exposes configurable props for colors, animation speed, distortion intensity, and scale — tune the chrome effect to match your design system
- **Multiple Size Variants**: Ships with small, medium, and large presets, plus icon support for left-side decorations

### Technical Implementation
```
Button Layer Stack:
┌─────────────────────────────┐
│     Button Content          │  ← Standard React children
├─────────────────────────────┤
│   WebGL Shader Border       │  ← @paper-design/shaders-react
│   (liquid metal effect)     │
└─────────────────────────────┘
```

The shader creates flowing, chrome-like reflections through animated distortion patterns, generating a dynamic visual effect that responds to time but not user input.

### Tech Stack
- **Framework**: React with Next.js support
- **Styling**: Tailwind CSS
- **Shader Library**: @paper-design/shaders-react
- **Utilities**: clsx + tailwind-merge for className management

### Installation
```bash
# Via shadcn CLI
npx shadcn@latest add liquid-metal

# Or manual: install deps + copy component source
npm install @paper-design/shaders-react clsx tailwind-merge
```

### Why This Matters
WebGL buttons are rare in production — most teams avoid the complexity. VengeanceUI packaging this as a drop-in component lowers the barrier for adding GPU-accelerated effects to React apps. Good reference for learning how shader-based UI components are structured.

*Filed in: [[Design Systems MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
