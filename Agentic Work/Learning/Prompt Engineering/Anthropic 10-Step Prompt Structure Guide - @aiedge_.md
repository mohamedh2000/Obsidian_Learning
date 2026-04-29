---
title: "Anthropic 10-Step Prompt Structure Guide"
url: "https://x.com/aiedge_/status/2016553316851896790?s=42"
platform: twitter
date_saved: 2026-01-28
source: "AI Edge (@aiedge_)"
content_type: tweet
topics: [Prompting, Claude, Best Practices]
tags: [anthropic, prompt-engineering, claude, opus, sonnet, haiku, deep-thinking, xml-tags, official-guide]
status: unread
---

> Anthropic recently released a masterclass on prompt engineering. This internal framework is built to deliver top-tier AI responses, and if you use Claude regularly, you need to add this to your prompting toolkit.

| Metric | Count |
|--------|-------|
| Likes | 857 |
| Retweets | 88 |

**Topics:** [[Prompt Engineering]], [[Claude]], [[Best Practices]]

## Key Points
- **Model Selection First**: Choose between Opus 4.5 (complex reasoning), Sonnet 4.5 (balanced everyday), or Haiku 4.5 (fast/cheap high-volume) based on task complexity — model choice affects optimal prompting strategy
- **10-Step Structure**: Task Context → Tone Context → Background Data → Detailed Rules → Examples → Conversation History → Immediate Task → Deep Thinking → (two more steps truncated in thread)
- **Task vs. Immediate Task Distinction**: Task Context sets the role and broad goal; Immediate Task Description is the specific action item for this turn — separating these prevents scope confusion
- **Deep Thinking Trigger**: Inserting phrases like "Think Deeply" activates Claude's extended reasoning mode — increases accuracy on complex problems at cost of latency
- **XML Tags for Structure**: Use `<example>`, `<HISTORY>`, and similar tags to inject structured context — models parse these as semantic boundaries, not just text

### The 10-Step Framework

1. **Task Context** — Role + high-level goal
2. **Tone Context** — Communication style (professional, casual, etc.)
3. **Background Data** — PDFs, files, context profiles
4. **Detailed Task Description & Rules** — Constraints and guidelines
5. **Examples** — Use `<example>` tags for desired output patterns
6. **Conversation History** — Reference with `<HISTORY>` or "Call back on previous conversations..."
7. **Immediate Task Description** — The specific action verb for this turn
8. **Deep Thinking** — Trigger extended reasoning with "Think Deeply"
9. **[Step 9 truncated in thread]**
10. **[Step 10 truncated in thread]**

### Model Cheat Sheet
| Model | Best For | Speed | Cost |
|-------|----------|-------|------|
| Opus 4.5 | Complex reasoning, deep analysis, coding | Slowest | Highest |
| Sonnet 4.5 | Everyday tasks, balanced | Medium | Medium |
| Haiku 4.5 | High-volume, straightforward | Fastest | Lowest |

*Filed in: [[Twitter Posts MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
