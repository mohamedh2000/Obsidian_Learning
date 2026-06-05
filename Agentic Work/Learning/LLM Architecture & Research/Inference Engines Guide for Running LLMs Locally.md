---
title: "Inference Engines Guide for Running LLMs Locally"
url: "https://x.com/theahmadosman/status/2062646043687166225?s=10"
platform: twitter
date_saved: 2026-06-05
source: "Ahmad (@theahmadosman)"
content_type: guide
topics: [Inference Engines, Local LLM, LLM Deployment]
tags: [llama-cpp, vllm, sglang, mlx, tensorrt, local-ai, inference]
status: unread
---

# Inference Engines Guide for Running LLMs Locally

> Comprehensive breakdown of inference engines: why they exist, how they work, and how to choose the right one based on hardware, workload, and serving model.

| | |
|---|---|
| **Source** | Ahmad (@theahmadosman) |
| **Saved** | 2026-06-05 |
| **Type** | Guide |
| **Engagement** | 343 likes, 59 retweets |
| **URL** | [Link](https://x.com/theahmadosman/status/2062646043687166225?s=10) |

## Topics

[[LLM Deployment]] | [[Inference Optimization]] | [[Local AI]]

## Key Points

- **Prefill vs Decode**: Different phases with different bottlenecks
- **VRAM vs Bandwidth**: Fit doesn't equal speed
- **KV Cache**: The real memory problem, not model weights
- **Quantization**: Only matters with good kernels
- **Batching vs Scheduling**: Different optimization concerns
- **MoE Routing**: Special challenges for mixture-of-experts
- **Long Context**: Changes the serving problem entirely
- **Multi-GPU**: Interconnect becomes the bottleneck

## Engine Mapping

| Engine | Strength |
|--------|----------|
| **llama.cpp** | Portability king |
| **MLX / MLX-LM** | Apple Silicon weapon |
| **ExLlamaV3** | Multi-GPU consumer CUDA / local MoE |
| **vLLM** | Default open-source production server |
| **SGLang** | Long-context, MoE, routing, ugly workloads |
| **TensorRT-LLM** | Max NVIDIA performance |
| **NVIDIA Dynamo** | Fleet orchestration |

## Selection Process

1. Pick the hardware
2. Pick the workload
3. Pick the serving model
4. Then the engine becomes obvious

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
