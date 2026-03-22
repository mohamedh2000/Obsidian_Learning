---
title: "Cloudflare Browser Rendering Limits"
url: "https://developers.cloudflare.com/browser-rendering/limits/"
platform: web
date_saved: 2026-03-11
source: "Cloudflare Docs"
content_type: guide
topics: [cloudflare, browser-automation, limits]
tags: [cloudflare, infra, browser-automation]
status: unread
---

# Cloudflare Browser Rendering Limits

> Cloudflare Browser Rendering limits depend heavily on your Workers plan, with tight free-tier caps and a 60-second inactivity timeout that can be extended with `keep_alive`.

Documentation page covering plan-specific quotas, concurrency ceilings, rate limits, crawl caps, and timeout behavior for Cloudflare's Browser Rendering product.

## Key Points

- Workers Free is tightly capped at 10 browser minutes per day, 3 concurrent browsers, 3 new browser instances per minute, and 6 REST API requests per minute.
- Workers Paid raises the ceiling to 30 concurrent browsers, 30 new instances per minute, and 600 REST API requests per minute, while removing the browser-hours cap.
- Sessions time out after 60 seconds of inactivity by default, `keep_alive` can extend inactivity windows up to 10 minutes, and failing to call `browser.close()` is a common cause of excess usage and `429` rate limits.
