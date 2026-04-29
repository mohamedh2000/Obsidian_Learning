---
title: "Agent SEO/AEO Optimization - Making Your Site Agent-Readable"
url: "https://x.com/michael_chomsky/status/2018407463910039845?s=42"
platform: twitter
date_saved: 2026-02-03
source: "Michael (@michael_chomsky)"
content_type: guide
topics: [Agent Design & Memory, SEO]
tags: [agent-seo, aeo, llms-txt, ai-agents, web-optimization, content-delivery, http-headers, text-plain, markdown]
status: unread
---

> So much SEO/AEO alpha in optimizing your project for AI agents. Key wins: respect `Accept: text/plain` and `text/markdown` headers, advertise your llms.txt, keep important context at the top of files (agents truncate), and prioritize agent requests.

| Metric | Count |
|--------|-------|
| Likes | 228 |
| Retweets | 5 |

**Topics:** [[Agent Design & Memory]], [[SEO & Discovery]]

## Key Points
- **Respect Accept headers**: Most AI agents don't render JavaScript — responding to `Accept: text/plain` or `Accept: text/markdown` is the biggest win for agent accessibility
- **Advertise your llms.txt**: Agents won't check for llms.txt unless you tell them it exists (similar to robots.txt discovery problem)
- **Front-load important context**: AI agents tend to truncate long pages — put the most critical information at the top of files
- **Prioritize agent traffic**: When serving content, consider agent requests as a distinct traffic class worth optimizing for

### Technical Implementation
```
# Server-side pseudo-code for agent-aware content delivery
if request.headers['Accept'].includes('text/plain') or
   request.headers['Accept'].includes('text/markdown'):
    return render_as_markdown(content)

# In HTML head or HTTP headers, advertise llms.txt
<link rel="llms" href="/llms.txt">
```

### Why This Matters Now
As AI agents become the primary way users discover and interact with content (via tools like Perplexity, Claude with web access, and autonomous browsing agents), optimizing for agent consumption becomes as important as traditional SEO. Sites that serve clean, structured, JS-free content to agents will rank higher in AI-mediated discovery.

### Coming Soon
Michael mentions building "something absolutely insane for agent SEO" — suggesting tooling or automation for this optimization space is forthcoming.

*Filed in: [[Saved Links MOC]]*
