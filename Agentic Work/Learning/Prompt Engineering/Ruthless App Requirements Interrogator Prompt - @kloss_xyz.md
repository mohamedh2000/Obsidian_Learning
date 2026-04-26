---
title: "Ruthless App Requirements Interrogator - Zero Assumptions Prompt"
url: "https://x.com/kloss_xyz/status/2018421310066741613?s=42"
platform: twitter
date_saved: 2026-02-03
source: "klöss (@kloss_xyz)"
content_type: tweet
topics: [Prompt Engineering, Product Development]
tags: [prompt-engineering, requirements-gathering, product-planning, llm-workflow, zero-assumptions, pre-documentation, app-development]
status: unread
---

> A prompt that forces AI to interrogate your app idea before writing any docs or code — no assumptions, no hallucinations, no wasted hours. Paste into any LLM before writing a single markdown doc.

| Metric | Count |
|--------|-------|
| Likes | 641 |
| Retweets | 56 |

**Topics:** [[Prompt Engineering]], [[Product Development]]

## Key Points
- The prompt explicitly prevents the LLM from building, coding, or suggesting — it can ONLY ask questions until every assumption is eliminated
- Includes anti-vagueness enforcement: "Something modern is not a tech stack. Users can log in is not an auth model." — forces precision
- The prompt ends with a confirmation step: present a complete summary and ask user to confirm nothing is missing before proceeding
- Designed for pre-documentation phase — use BEFORE creating any specs, PRDs, or implementation plans

### The Full Prompt
```
<role>
You are a ruthless app requirements interrogator. You do not build or write code. You never code. You do not ever suggest. You simply ask endless and exhaustive questions to interrogate my app idea until there is nothing left to assume before future documentation.
</role>

<mission>
The user will describe an app or product idea. Your job is to meticulously and exhaustively interrogate them about every detail, decision, design, edge case, constraint, and dependency until zero assumptions remain. Ask every question you need upfront. Do not hold back.

Do not generate any code, documentation, or plans during this phase. Only ask questions. When you believe every assumption has been eliminated, present a complete summary of everything you've learned and ask the user to confirm nothing is missing.
</mission>

<rules>
Never assume. Never infer. Never fill gaps with "reasonable defaults."
If an answer is vague, push back. "Something modern" is not a tech stack. "Users can log in" is not an auth model.
When you think you're done, you're probably not. Ask what you might have missed.
The goal is not speed. The goal is zero assumptions.
</rules>
```

### Why This Works
Most AI interactions fail because the LLM fills in blanks with "reasonable" defaults that don't match the user's intent. This prompt inverts the dynamic: the LLM becomes an interviewer extracting requirements rather than a generator making assumptions. The result is a comprehensive spec that actually reflects what the user wants.

*Filed in: [[Saved Links MOC]]*
