---
title: "Kernel.sh Browser Pools for Pre-Configured Browser Automation"
url: "https://www.kernel.sh/docs/browsers/pools"
platform: web
date_saved: 2026-01-24
source: "Kernel.sh"
content_type: guide
topics: [Browser Automation, Developer Tools]
tags: [kernel-sh, browser-pools, browser-automation, stealth-browsers, web-scraping, playwright-alternative]
status: unread
---

> Browser pools pre-configure a fixed set of browsers that aren't charged until acquired — enables instant-availability browser automation with custom extensions, proxies, and profiles.

**Topics:** [[Developer Tools]], [[Browser Automation]]

## Key Points
- Pools maintain a fixed number of pre-warmed browsers ready for immediate use without startup latency
- Browsers are borrowed/returned, not auto-replenished — you manage the pool lifecycle
- Each pool can be configured with custom extensions, proxies, viewport settings, stealth mode, and timeout rules
- SDK available for TypeScript/JavaScript and Python

### Pool Lifecycle: Declare → Acquire → Release
1. **Declaration:** Create pool with size and config (stealth mode, viewport, timeouts)
2. **Acquisition:** Borrow a browser when needed; request waits if none available
3. **Release:** Return browser to pool for reuse or destruction

### Pool Management Operations
- Update pool configuration
- Flush idle instances
- Retrieve status metrics
- List all pools
- Delete pools

### Why It Matters
Pre-warmed browser pools eliminate cold-start latency that kills scraping and automation performance. Pay-per-acquisition model means you only pay when browsers are actually used, not while they sit idle.

*Filed in: [[Saved Links MOC]]*
