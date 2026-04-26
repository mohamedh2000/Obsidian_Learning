---
title: "Claude Fresh Eyes Code Review Prompt"
url: "https://x.com/doodlestein/status/2015275392098017303?s=42"
platform: twitter
date_saved: 2026-01-25
source: "Jeffrey Emanuel (@doodlestein)"
content_type: tweet
topics: [Prompt Engineering, Claude Code]
tags: [prompt-engineering, claude-code, code-review, debugging, ai-workflow, best-practices]
status: unread
---

> Jeffrey Emanuel shares a prompt pattern for getting Claude to reliably self-review its own code — repeating a "fresh eyes" review prompt 3-5 times after each code generation.

| Metric | Count |
|--------|-------|
| Likes | 390 |
| Retweets | 9 |

**Topics:** [[Prompt Engineering]], [[Claude Code & Anthropic]]

## Key Points

- The technique involves repeating a specific review prompt 3-5 times after Claude writes code, forcing multiple passes over the same output
- The prompt asks Claude to read code "with fresh eyes" looking for "obvious bugs, errors, problems, issues, confusion"
- Emanuel claims to use this pattern "hundreds of times a day," indicating it's battle-tested in production workflows
- The mechanism works by resetting Claude's attention to the code rather than its prior reasoning, catching errors that slip through on first pass

### The Prompt Pattern

The exact prompt structure: "Great, now I want you to carefully read over all of the new code you just wrote and other existing code you just modified with 'fresh eyes' looking super carefully for any obvious bugs, errors, problems, issues, confusion, etc. Carefully fix anything you uncover."

### Why It Works

LLMs can develop "tunnel vision" where they over-commit to their initial approach. The "fresh eyes" framing explicitly breaks this pattern by asking the model to approach the code as if seeing it for the first time. Multiple repetitions compound the effect.

*Filed in: [[Saved Links MOC]]*
