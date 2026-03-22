---
title: "Cloudflare Tunnel"
url: "https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/"
platform: web
date_saved: 2026-03-13
source: "Cloudflare Docs"
content_type: guide
topics: [cloudflare, networking, secure-access]
tags: [cloudflare, infra, networking]
status: unread
---

# Cloudflare Tunnel

> Cloudflare Tunnel lets private services sit behind Cloudflare without exposing a public IP by having `cloudflared` open outbound-only connections to Cloudflare's edge.

Connects your resources to Cloudflare without a publicly routable IP address through a lightweight daemon called `cloudflared` that establishes outbound-only connections. It supports web servers, SSH, remote desktops, and other protocols while keeping the origin hidden from direct inbound traffic.

## Key Points

- `cloudflared` initiates outbound connections from the origin to Cloudflare, which means most environments can use Tunnel without opening inbound firewall access.
- A single tunnel can have multiple connectors and route traffic to the nearest Cloudflare data center, which improves resilience and avoids direct origin exposure.
- The docs position Tunnel as a practical way to serve private apps through Cloudflare while reducing bypass-attack risk against the underlying origin.

## Why saved
<!-- Fill in when you remember why this caught your eye -->

## Notes
<!-- Fill in after reading -->
