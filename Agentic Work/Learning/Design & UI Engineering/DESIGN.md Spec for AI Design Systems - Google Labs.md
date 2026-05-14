---
title: "DESIGN.md Spec for AI Design Systems"
url: "https://github.com/google-labs-code/design.md"
platform: github
date_saved: 2026-05-14
source: "Google Labs (@google-labs-code)"
content_type: repo
topics: [UI & Design Engineering, Developer Tools]
tags: [design-systems, ai-agents, design-tokens, tailwind, typescript]
status: unread
---

# DESIGN.md Spec for AI Design Systems

> A format specification for describing visual identity to coding agents — merges machine-readable design tokens (YAML) with human-readable design rationale (Markdown).

| | |
|---|---|
| **Source** | Google Labs (@google-labs-code) |
| **Saved** | 2026-05-14 |
| **Type** | repo |
| **Stars** | 13.7k |
| **URL** | [Link](https://github.com/google-labs-code/design.md) |

## Topics

[[UI & Design Engineering]] | [[Developer Tools]]

## Key Points

- **Core innovation**: Dual-layer format — YAML front matter for machine-readable tokens + Markdown prose for design rationale
- **Purpose**: Give AI agents both exact values AND contextual understanding of *why* those values exist
- **Features**:
  - Linting & validation — catches broken token refs and WCAG contrast violations
  - Diff comparison — detects token-level changes between design versions
  - Format export — converts to Tailwind, W3C DTCG, and other standards
  - Programmatic API — TypeScript library for integration
- **Token types**: Colors (hex), dimensions (px/em/rem), typography objects, token references, component definitions
- **Status**: Alpha, actively developed
- **Package**: `@google/design.md` on npm

## Notes

Could integrate this with Claude Code harness for consistent UI generation. Check if compatible with existing Tailwind config.

---

*Filed in: [[GitHub Repos MOC]] | [[Saved Links MOC]] | [[Tools & Products MOC]]*
