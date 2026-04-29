---
title: "Cloudflare Caching VPS Unlimited Bandwidth - @thethiny"
url: "https://x.com/thethiny/status/2020969392172052835?s=42"
platform: twitter
date_saved: 2026-02-10
source: "thethiny (@thethiny)"
content_type: tweet
topics: [Infrastructure, Developer Tools]
tags: [twitter, cloudflare, vps, caching, cost-optimization, cdn]
status: unread
---

# Cloudflare Caching VPS Unlimited Bandwidth - @thethiny

> thethiny outlines a practical architecture: cache all pages on Cloudflare, host backend on a $50 VPS with unlimited bandwidth — impossible for this to net $50K/month in bills.

| | |
|---|---|
| **Source** | thethiny (@thethiny) |
| **Saved** | 2026-02-10 |
| **Type** | tweet |
| **Engagement** | 55 likes, 1 retweet |
| **URL** | [Link](https://x.com/thethiny/status/2020969392172052835?s=42) |

## Topics

[[Infrastructure]] | [[Developer Tools]]

## Key Points

- The tweet responds to @rtwlz in the Vercel pricing thread with a concrete alternative architecture
- Strategy: cache all static pages on Cloudflare (free CDN) and host backend services on a VPS with unlimited bandwidth
- Claims $50/month VPS with unlimited bandwidth can handle the load that generated a $50K Vercel bill
- Points out that reloading "the same pages over and over" should never cost that much — implies poor caching strategy

### The Architecture

```
[User] → [Cloudflare CDN (free tier)] → cache hit? → serve cached
                                      ↓ cache miss
                              [VPS $50/mo unlimited BW]
```

Cloudflare absorbs the traffic spikes; the VPS only handles cache misses and dynamic requests. This inversion of the cost model makes viral traffic manageable.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
