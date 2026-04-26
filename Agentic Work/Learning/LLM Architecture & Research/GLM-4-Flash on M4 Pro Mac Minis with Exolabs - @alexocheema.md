---
title: "GLM-4-Flash on M4 Pro Mac Minis with Exolabs - @alexocheema"
url: "https://x.com/alexocheema/status/2013694573910937980?s=42"
platform: twitter
date_saved: 2026-01-20
source: "Alex Cheema (@alexocheema)"
content_type: tweet
topics: [Local Inference, Distributed Computing]
tags: [exolabs, glm-4, mac-mini, m4-pro, tensor-parallelism, mlx, rdma, thunderbolt, local-llm, distributed-inference]
status: unread
---

> Running GLM-4.7-Flash on 4 x M4 Pro Mac Minis using @exolabs. Uses tensor parallelism with RDMA over Thunderbolt & MLX backend. Runs at 100 tok/sec. We're working on optimizing this at @exolabs. Aiming to hit ~200 tok/sec on this setup soon.

| Metric | Count |
|--------|-------|
| Likes | 583 |
| Retweets | 65 |

**Topics:** [[Local Inference]], [[Distributed Computing]]

## Key Points
- **100 tok/sec on 4x M4 Pro Mac Minis**: Consumer-grade distributed inference achieving respectable throughput on GLM-4-Flash
- **Tensor parallelism via RDMA over Thunderbolt**: Low-latency inter-node communication using Thunderbolt's RDMA capability for model sharding
- **MLX backend**: Apple's [[MLX]] framework handles the actual matrix operations, optimized for Apple Silicon
- **2x speedup target**: Exolabs aiming for 200 tok/sec on same hardware — suggests significant optimization headroom remains

### Technical Architecture
```
[Mac Mini 1] ──Thunderbolt/RDMA──┐
[Mac Mini 2] ──Thunderbolt/RDMA──┼── Tensor Parallel Inference
[Mac Mini 3] ──Thunderbolt/RDMA──┤   (GLM-4-Flash sharded across GPUs)
[Mac Mini 4] ──Thunderbolt/RDMA──┘
                    │
                    ▼
              MLX Backend
              100 tok/sec (→ 200 tok/sec target)
```

### Why This Matters
[[Exolabs]] demonstrates that consumer Apple hardware can run large models at production-relevant speeds when properly distributed. This approach is more accessible than NVIDIA cluster setups while staying within the Mac ecosystem.

*Filed in: [[Saved Links MOC]]*
