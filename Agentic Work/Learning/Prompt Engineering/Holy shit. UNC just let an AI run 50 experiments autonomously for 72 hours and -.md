---
title: "Holy shit. UNC just let an AI run 50 experiments autonomously for 72 hours and…"
url: "https://x.com/rryssf_/status/2040378710826860881"
platform: twitter
date_saved: 2026-04-05
source: "Robert Youssef (@rryssf_)"
content_type: tweet
topics: [LLMs, AI Agents, Reinforcement Learning, Prompt Engineering]
tags: [twitter, rryssf_]
status: unread
---

# Holy shit. UNC just let an AI run 50 experiments autonomously for 72 hours and…

> Holy shit. UNC just let an AI run 50 experiments autonomously for 72 hours and it built a memory system that beats every human-designed baseline.

| | |
|---|---|
| **Source** | Robert Youssef (@rryssf_) |
| **Saved** | 2026-04-05 |
| **Type** | tweet |
| **Engagement** | 535 likes, 78 retweets |
| **URL** | [Link](https://x.com/rryssf_/status/2040378710826860881) |

## Topics

[[LLMs]] | [[AI Agents]] | [[Reinforcement Learning]] | [[Prompt Engineering]]

## Key Points

- Holy shit.
- UNC just let an AI run 50 experiments autonomously for 72 hours and it built a memory system that beats every human-designed baseline.
- +411% improvement on long-context benchmarks.
- The biggest gains weren't from tuning parameters they came from fixing bugs and redesigning architecture that humans missed entirely.

## Tweet

Holy shit. UNC just let an AI run 50 experiments autonomously for 72 hours and it built a memory system that beats every human-designed baseline.

+411% improvement on long-context benchmarks. The biggest gains weren't from tuning parameters they came from fixing bugs and redesigning architecture that humans missed entirely.

> The experiment started with a simple text-only memory system scoring F1 = 0.117 on LoCoMo, a benchmark that tests whether AI agents can recall and reason over months of multi-session conversations. UNC gave an autonomous research pipeline called AutoResearchClaw three things: the codebase, two benchmark evaluation harnesses, and API access to LLMs.

> No human touched the inner loop again. The pipeline ran for 72 hours, executed 50 experiments, diagnosed its own failures, rewrote its own architecture, and ended at F1 = 0.598 beating every human-designed memory system ever published on that benchmark. The previous state of the art was 0.432.

> The most important finding is what drove the gains. Traditional AutoML searches hyperparameters: learning rates, batch sizes, temperature values.

> Those contributed almost nothing here. The three categories that actually moved the needle were bug fixes (+175%), architectural redesign (+44%), and prompt engineering (+188% on specific categories). Each of those individually exceeded the cumulative contribution of all hyperparameter tuning combined. This is the finding that should change how the field thinks about automated research: the valuable improvements require code comprehension, failure diagnosis, and cross-component reasoning capabilities that live entirely outside what traditional AutoML can do.

> The single most impactful discovery came in iteration 1. The pipeline found that an API call was missing a response_format parameter. One line of code. Without it, the model produced verbose natural-language answers instead of structured JSON, and the verbosity destroyed F1 precision.

> Fix: +175% improvement in a single step. In iteration 5, the pipeline discovered that all 4,277 stored memory timestamps had been corrupted to the ingestion date rather than the actual conversation date. It autonomously wrote a keyword-matching repair script that corrected 99.98% of them without re-ingesting any data. These are not the kinds of failures a hyperparameter search finds. They require reading code, understanding what it does, and diagnosing why the output is wrong.

The full optimization trajectory across both benchmarks:
→ LoCoMo starting F1: 0.117 naïve baseline, text-only memory
→ Iteration 1: missing response_format parameter found and fixed F1 jumps to 0.322, +175%
→ Iteration 2: pipeline discovers set-union merging of dense and sparse search beats score-based re-ranking F1 to 0.464, +44%
→ Iteration 3: anti-hallucination prompting added F1 to 0.516, +11%
→ Iteration 5: 4,277 corrupted timestamps autonomously repaired F1 to 0.580, +7%
→ Iterations 8 and 9: two failed experiments automatically detected and reverted
→ Final LoCoMo F1: 0.598 +411% from baseline, beats SimpleMem SOTA of 0.432
→ Mem-Gallery starting F1: 0.254
→ Phase 2 breakthrough: pipeline discovers returning full original dialogue text outperforms LLM-generated summaries counterintuitive, since summaries are the standard approach F1 jumps to 0.690, +96% in one phase
→ Phase 3: pipeline finds that prompt constraint positioning before vs. after the question matters more than constraint content one category improves +188% from repositioning alone
→ Phase 5: BM25 tokenization fix stripping punctuation from "sushi." to "sushi" yields +0.018 F1, more than 10 rounds of prompt engineering combined
→ Final Mem-Gallery F1: 0.797 +214% from baseline, beats MuRAG SOTA of 0.697
→ Total wall-clock time: 72 hours equivalent to approximately 4 weeks of human researcher time at 3 experiments per day
→ Throughput with 8 parallel workers: 5.81 queries per second 3.5x faster than the fastest human-designed baseline

> The architecture the pipeline designed is called OMNIMEM and it has three principles that no human researcher had combined before. Selective ingestion: before anything enters memory, lightweight encoders measure novelty and discard redundant content CLIP embeddings detect scene changes across video frames, voice activity detection rejects silence, Jaccard overlap filters near-duplicate text. Only novel information gets stored. Multimodal Atomic Units: every memory regardless of modality gets stored as a compact metadata record with a pointer to raw content in cold storage fast search over small summaries, lazy loading of large assets only when needed. Progressive retrieval: instead of loading all retrieved content at once, the system expands information in three stages gated by a token budget summaries first, then full text for high-confidence matches, then raw images and audio only when necessary.

> The hybrid search discovery is the one that should make every RAG builder pay attention. Standard practice is to combine dense vector search and sparse keyword search by re-ranking their results together using a blended score. The pipeline tested this and found it degrades performance. The reason: score-based re-ranking disrupts the semantic ordering that dense retrieval already established. The fix the pipeline discovered autonomously is set-union merging dense results keep their original ranking, BM25-only results get appended at the end. No re-ranking. No blended scores. Just union. This simple change contributed +44% in a single iteration and was confirmed by ablation: removing BM25 hybrid search costs -14% F1, the second-largest component contribution after pyramid retrieval at -17%.

> The capability threshold is what makes this alarming rather than just impressive. AutoML has existed for decades. It searches hyperparameters efficiently. It finds nothing here because the real gains require understanding why a system is failing reading stack traces, tracing data corruption through a pipeline, recognizing that a missing parameter is causing 9x verbosity, writing a repair script for corrupted timestamps.

These are software engineering tasks that require comprehension, not optimization. The pipeline completed them without human input. The previous state of the art on both benchmarks was built by human researchers over months of manual iteration. The pipeline beat it in 72 hours.

The AI researcher ran the experiment. The AI researcher fixed the bugs. The AI researcher beat the humans.

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
