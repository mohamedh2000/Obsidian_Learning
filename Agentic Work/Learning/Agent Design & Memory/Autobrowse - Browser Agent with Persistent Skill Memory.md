---
title: "Autobrowse - Browser Agent with Persistent Skill Memory"
url: "https://x.com/deronin_/status/2052697237856088114?s=42"
platform: twitter
date_saved: 2025-05-08
source: "Ronin (@deronin_)"
content_type: tweet
topics: [Browser Agents, Agent Memory, Web Scraping]
tags: [autobrowse, browserbase, agent-memory, web-scraping, open-source, skills]
status: unread
---

# Autobrowse - Browser Agent with Persistent Skill Memory

> Open-source browser agent that learns websites once, saves learnings as SKILL.md files, then runs 10x cheaper forever

| | |
|---|---|
| **Source** | Ronin (@deronin_) |
| **Saved** | 2025-05-08 |
| **Type** | tweet |
| **Engagement** | 607 likes, 27 retweets |
| **URL** | [Link](https://x.com/deronin_/status/2052697237856088114?s=42) |

## Topics

[[Browser Agents]] | [[Agent Memory]] | [[Web Scraping]]

## Key Points

- **Core insight**: Every browser agent before this had AMNESIA — figured out the site, then forgot when session closed
- **Solution**: Agent writes learnings to markdown file (SKILL.md) that next agent reads BEFORE starting
- **Learning loop**: 3-5 iterations → converges on working path → saves as skill file
- **Karpathy connection**: Same auto-research idea but applied to the open web, with CROSS-SESSION persistence

## Cost Savings

| Task | Without Skill | With Skill |
|------|--------------|------------|
| Craigslist scrape | $0.22 / 71s | $0.12 / 27s |
| Form-fill (run 1) | $1.40 | — |
| Form-fill (run 4) | — | $0.24 |
| 10 website scrape | $1.02 | $0.12 |

## Killer Feature

> Pointed at federal grants portal → found undocumented JSON endpoint humans missed for years → 28-page scrape collapsed into one fetch

"An agent tried something a person never would and found something a person would never see"

## How It Works

```
1. Give agent a real task on a real site
2. Agent tries, fails, learns, tries again
3. 3-5 rounds → converges on working path
4. Writes path as SKILL.md
5. Next agent loads skill → skips discovery phase
```

## Use Cases Solved

- Writing scrapers for new sites (half a day per site → minutes)
- Chasing selectors when sites redesign
- Finding hidden APIs in network traffic
- Explaining HOW the agent does the job (audit trail)

## Notes

100% open-source from Browserbase. The markdown file IS the memory — elegant simplicity.

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
