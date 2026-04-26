---
title: "Reddit JSON API Trick for LLM Data Extraction"
url: "https://x.com/theahmadosman/status/2017809819147661449?s=42"
platform: twitter
date_saved: 2026-02-01
source: "Ahmad (@theahmadosman)"
content_type: tutorial
topics: [Developer Tools, Data Extraction]
tags: [reddit-api, json-api, llm-data-extraction, web-scraping, data-pipelines, ai-agents, niche-research, automation]
status: unread
---

> "add `/.json` at the end of any Reddit link — get the full thread, all replies to n-th depth, all metadata as JSON — feed to LLMs to extract/analyze"

| Metric | Count |
|--------|-------|
| Likes | 2157 |
| Retweets | 126 |

**Topics:** [[Developer Tools]], [[Data Extraction]]

## Key Points
- **Hidden JSON endpoint**: Append `/.json` to any Reddit URL to get structured data without authentication
- **Full thread depth**: Returns the entire comment tree, not just top-level replies
- **Rich metadata included**: Timestamps, scores, author info, flair, awards — all available programmatically
- **LLM-ready format**: JSON structure is ideal for feeding directly into Claude/GPT for analysis

### How It Works

```
Original URL:
https://reddit.com/r/SaaS/comments/abc123/my_startup_journey

JSON Endpoint:
https://reddit.com/r/SaaS/comments/abc123/my_startup_journey/.json
                                                              ↑
                                                         Add this
```

### Data Structure Returned
```json
[
  {
    "kind": "Listing",
    "data": {
      "children": [
        {
          "kind": "t3",  // Post
          "data": {
            "title": "...",
            "selftext": "...",
            "score": 234,
            "author": "...",
            "created_utc": 1706745600
          }
        }
      ]
    }
  },
  {
    "kind": "Listing",  // Comments
    "data": {
      "children": [
        {
          "kind": "t1",  // Comment
          "data": {
            "body": "...",
            "score": 45,
            "replies": { ... }  // Nested comments
          }
        }
      ]
    }
  }
]
```

### Use Cases for LLM Processing
1. **Market research**: Extract pain points from niche subreddits
2. **Competitor analysis**: Analyze sentiment in product discussion threads
3. **Content ideation**: Find frequently asked questions in your domain
4. **Lead generation**: Identify users expressing buying intent
5. **Sentiment analysis**: Track community reactions to announcements

### Monetization Angles (as Ahmad suggests)
- Build niche research reports from subreddit data
- Create automated competitor monitoring tools
- Offer "community pulse" analytics to brands
- Generate content calendars from trending discussions

### Technical Notes
- **Rate limits apply**: Reddit will throttle aggressive scraping
- **No auth required**: Works without OAuth for public subreddits
- **User-Agent header**: Set a descriptive one to avoid blocks
- **Pagination**: Use `after` parameter for large threads

*Filed in: [[Saved Links MOC]]*
