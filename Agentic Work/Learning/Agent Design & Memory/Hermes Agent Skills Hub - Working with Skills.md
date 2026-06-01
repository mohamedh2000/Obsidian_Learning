---
title: "Hermes Agent Skills Hub - Working with Skills"
url: "https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#the-skills-hub"
platform: web
date_saved: 2026-06-01
source: "Nous Research"
content_type: guide
topics: [agent design, skills, hermes agent]
tags: [hermes-agent, skills, progressive-disclosure, nous-research]
status: unread
---

# Hermes Agent Skills Hub - Working with Skills

> Official guide to the Hermes Agent Skills Hub — how to browse, install, and create skills that extend agent capabilities.

| | |
|---|---|
| **Source** | Nous Research |
| **Saved** | 2026-06-01 |
| **Type** | Guide/Documentation |
| **Engagement** | — |
| **URL** | [Link](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#the-skills-hub) |

## Topics

[[Agent Design]] | [[Hermes Agent]] | [[Skills]]

## Key Points

- **Skills Hub** offers official optional skills (heavier or niche) not active by default — browse via `/skills browse` and `/skills search`
- **Progressive disclosure pattern**: `skills_list()` (~3k tokens) loads at session start; `skill_view(name)` fetches full content on demand — zero tokens until used
- **Skills vs Memory**: Skills = procedural knowledge (how-to), Memory = factual knowledge (preferences, facts)
- **Installation**: `hermes skills install official/research/arxiv` or from URL with `--name`
- **Usage**: Invoke via `/<skill-name>` slash command (e.g., `/ascii-art Make a banner`) or natural conversation
- **Custom skills**: Create `~/.hermes/skills/category/skill-name/SKILL.md` with YAML frontmatter (name, description, version) plus sections: When to Use, Procedure, Pitfalls, Verification

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
