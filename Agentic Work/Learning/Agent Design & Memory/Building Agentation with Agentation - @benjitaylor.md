---
title: "Building Agentation with Agentation"
url: "https://x.com/benjitaylor/status/2014206779169906812?s=42"
platform: twitter
date_saved: 2026-01-22
source: "Benji Taylor (@benjitaylor)"
content_type: tweet
topics: [Agent Tools, Meta-Development]
tags: [agentation, dogfooding, benji-taylor, blog-post, self-hosted-tools]
status: unread
---

> Benji Taylor shares a blog post about using Agentation to build Agentation itself — dogfooding the visual feedback tool during its own development.

| Metric | Count |
|--------|-------|
| Likes | 448 |
| Retweets | 20 |

**Topics:** [[Agent Tools]], [[Meta-Development]]

## Key Points
- **Recursive Dogfooding**: The tool was used to build itself — agents received structured feedback from Agentation while implementing Agentation features
- **Blog Documentation**: Full writeup at benji.org/agentation provides deeper technical context than Twitter allows
- **Companion to Launch Tweet**: This follow-up tweet links to the technical blog post after the initial product launch
- **Real-World Validation**: Using the tool in production during development surfaces edge cases that toy examples miss

### Connection to Main Launch
This tweet is a companion to [[Agentation Visual Feedback Tool for Agents - @benjitaylor|the main Agentation launch tweet]]. The blog post likely covers:
- Technical architecture decisions
- Challenges encountered during development
- Examples of how agents interpreted the structured feedback

### Meta-Development Pattern
```
Traditional Development:
  Developer → Code → Test → Debug

Agentation Development:
  Developer → Agent → Agentation → Code
       ↑_____________________________|
       (Agentation used to build Agentation)
```

*Filed in: [[Saved Links MOC]]*
