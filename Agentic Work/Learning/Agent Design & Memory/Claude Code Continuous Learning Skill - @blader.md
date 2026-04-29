---
title: "Claude Code Continuous Learning Skill - @blader"
url: "https://x.com/blader/status/2012667150440476851?s=42"
platform: twitter
date_saved: 2026-01-18
source: "Siqi Chen (@blader)"
content_type: tool
topics: [Agent Skills, Self-Improvement]
tags: [claude-code, skill-extraction, continuous-learning, ai-agents, meta-learning]
status: unread
---

> Used Claude Code to make a Claude Code skill that learns new Claude Code skills as you use Claude Code — enabling agents to capture discovered knowledge as reusable skills rather than starting fresh each session.

| Metric | Count |
|--------|-------|
| Likes | 2534 |
| Retweets | 175 |

**Topics:** [[Agent Skills]], [[Self-Improvement]]

## Key Points
- **Solves the amnesia problem**: AI coding agents typically start each session with no memory of previous discoveries — Claudeception captures knowledge before it disappears
- **Automatic activation triggers**: Engages when Claude completes debugging with non-obvious solutions, discovers workarounds, resolves errors requiring meaningful problem-solving, or learns project-specific patterns
- **Quality filtering via retrieval-optimized descriptions**: Only extracts knowledge meeting strict criteria — generic descriptions like "helps with database problems" won't match; specific ones like "Fix for PrismaClientKnownRequestError in serverless" will
- **Leverages native skills infrastructure**: Claude Code loads skill descriptions (~100 tokens each) at startup — this skill writes new ones with proper metadata and trigger conditions

### How It Works
Skills are markdown files with YAML frontmatter (name, description, author, version, date) plus sections for: problem description, trigger conditions, solution steps, and verification methods. Users can trigger explicitly via `/claudeception` or request "Save what we just learned as a skill."

**GitHub Repo:** [blader/claude-code-continuous-learning-skill](https://github.com/blader/claude-code-continuous-learning-skill)

*Filed in: [[Saved Links MOC]]*
