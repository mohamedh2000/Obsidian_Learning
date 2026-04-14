---
title: "Learning MOC"
type: moc
date_created: 2026-03-17
tags: [moc, learning]
---

# Learning MOC

Educational resources, tutorials, research papers, and reference materials for self-study. Each section below is a **folder you can browse directly** — open any subfolder to pick and read.

**Parent:** [[Saved Links MOC]]

---

## `RLHF & RL Training/` (10 resources)

Policy gradients, reward modeling, PPO, GRPO, and LLM training methodologies.

| Resource                                                           | What You'll Learn                                                            |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| [[RLHF Book - Policy Gradients]]                                   | PPO, GRPO, REINFORCE, advantage estimation — the textbook chapter `#new`     |
| [[RL for LLMs - aweers]]                                           | Critic-free RL, loss aggregation biases                                      |
| [[RL Methods for Reasoning LLMs - @a_weers]]                       | 10 recent RL methods compared                                                |
| [[NVIDIA Unsloth RL Environments Guide - @akshay_pachaar]]         | Hands-on RL environment construction                                         |
| [[RL Environments Course with NVIDIA - @UnslothAI]]                | GRPO methodology, RLVR techniques                                            |
| [[Scaling RL Environments for Agents - @guohao_li]]                | Multi-agent RL environment scaling                                           |
| [[Reinforcement Learning with NVIDIA - Unsloth AI]]                | Why RL > SFT, GRPO best practices                                            |
| [[Autoresearch Tuning Nanochat Results - @karpathy]]               | Autonomous LLM training, 630 lines, single-GPU                               |
| [[Scott Jeen on RL for Superforecasting - @enjeeneer]]             | RL-trained superforecasting thread linking to recent Mantic results `#new`   |
| [[Training LLMs to Predict World Events (Guest Post with Mantic)]] | RL fine-tuning for judgmental forecasting on ~10,000 binary questions `#new` |

---


| [[OPD + RL on Real Agentic Tasks - @rronak_]] | Pointer to a paper combining OPD and reinforcement learning on real agentic tasks without relying on verifiable... `#new` |
| [[Unsloth Built Its Own Triton Backprop Kernels - @_avichawla]] | High-level explainer on Unsloth replacing default autograd with custom Triton backprop kernels for training... `#new` |
## `Prompt Engineering/` (6 resources)

How to write effective prompts, structure instructions, and optimize LLM outputs.

| Resource | What You'll Learn |
|----------|-------------------|
| [[Anthropic Prompt Eng Interactive Tutorial]] | 9-chapter interactive course, beginner→advanced (33.5K stars) `#new` |
| [[Claude Prompt Engineering Overview]] | Anthropic's official guide, best practices, prompt chaining `#new` |
| [[OpenAI Prompt Engineering Guide]] | Identity→Instructions→Examples→Context structure `#new` |
| [[claude-skills-guide]] | Official Anthropic PDF on building Claude Code skills |
| [[Skeleton of Thought Beats CoT - @ihtesham2005]] | Parallel decoding, 2.39x speedup vs CoT |
| [[ai-prompt-masterclass]] | Curated AI prompts for designers/professionals |

---

## `LLM Architecture & Research/` (23 resources)

How LLMs work internally — architecture, reasoning, interpretability, hardware.

| Resource | What You'll Learn |
|----------|-------------------|
| [[Anthropic - Tracing Thoughts in Language Models]] | Claude's semantic space, ahead-of-time planning, hallucination circuits |
| [[How LLMs Actually Think - @0xSero]] | LLM reasoning internals, parallel computation |
| [[LLM Architecture Gallery Resource - @rohanpaul_ai]] | Visual reference for LLM architectures |
| [[Claude Opus Explains MLA and DSA - @eliebakouch]] | Multi-head Latent Attention, DeepSeek architecture |
| [[Attention Residuals Visual Summary Kimi - @eliebakouch]] | Attention residual mechanisms (703 likes) `#new` |
| [[Fast K-Means Clustering Embeddings - @neural_avb]] | Millions of embeddings in 5s `#new` |
| [[SKILLRL New Learning Paradigm for Agents - @_avichawla]] | Agents that distill experiences into reusable skills `#new` |
| [[KV Caching in LLMs Clearly Explained - @_avichawla]] | First-token latency and KV-cache decoding speedups `#new` |
| [[How to Become AI Engineer in 6 Months - @deronin_]] | Full AI engineering roadmap (4.5K likes) `#new` |
| [[AI Engineer Roadmap Free Resources - @heynavtoor]] | Python→Math→ML→DL→GenAI→MLOps roadmap `#new` |
| [[GPUs Wrong for AI Inference - @joshkale]] | Alternative AI hardware approaches |
| [[Flash-MoE]] | 397B MoE inference on a MacBook Pro via Metal + SSD streaming `#new` |
| [[Architectural Breakdown of Transformers - @Hesamation]] | Transformer visuals plus a linked BERT build guide `#new` |
| [[Autoresearching Apple's LLM in a Flash for Qwen 397B - @danveloper]] | Claude Code-assisted local 397B inference exploration `#new` |
| [[MiroThinker 1.7 and H1 Top Hugging Face Paper - @miromind_ai]] | Verification-oriented reasoning models and open weights `#new` |
| [[Recursive Language Models Aha Moment - @neural_avb]] | Recursive language model intuition from a from-scratch implementation `#new` |
| [[Recursive Language Models Aha Moment Hits 1.2K Bookmarks - @neural_avb]] | Follow-up signal that the explainer crossed 1.2K bookmarks and is resonating widely `#new` |
| [[Recursive Language Models Mirror Notebook EDA - @neural_avb]] | Notebook-style EDA analogy for recursive language model workflows `#new` |
| [[MSA Memory Sparse Attention Paper - @elliotchen100]] | Sparse long-memory attention with document-aware RoPE, interleaving, and 100M-token claims `#new` |
| [[EverMind Open-Sources MSA 100M-Token Memory - @IndieDevHailey]] | Chinese-language recap of the MSA release, 100M-token memory, document-wise RoPE, and Memory Interleaving `#new` |
| [[openai-harness-engineering]] | Making codebases "agent-ready" |
| [[spectral-clustering]] | Eigenvalue clustering (foundational for code intelligence) |
| [[Why MSA Memory Interleaving Matters - @elliotchen100]] | Follow-up argument that Memory Interleaving is MSA's real breakthrough for multi-hop recall across fragmented long-context memory `#new` |

---


| [[EvoX Evolves the Search Strategy Itself - @shulynnliu]] | Meta-evolution pipeline for optimization systems that lets AI tune the exploration strategy instead of hand-coding... `#new` |
| [[Qwen3.5-397B Running on M3 Max via Claude Code - @danveloper]] | Using Claude Code with Karpathy's autoresearch repo and Apple's LLM in a Flash paper to run a 397B model on local... `#new` |
| [[Very Big Models on Smaller GPUs Soon - @0xSero]] | Short thesis that improved inference techniques are about to make very large models practical on smaller GPUs. `#new` |
| [[LLM in a Flash]] | Apple paper on running models larger than available DRAM by serving weights from flash with windowing and... `#new` |
| [[MSA: Memory Sparse Attention]] | Repository for Memory Sparse Attention, a sparse latent-memory framework targeting 100M-token contexts with Memory... `#new` |
| [[Promising Results Beyond Test-Time Compute - @YouJiacheng]] | Short research reaction noting promising empirical results beyond earlier concurrent work if the new method truly... `#new` |
## `Agent Design & Memory/` (24 resources)

Agent architectures, memory patterns, multi-agent coordination, self-improving systems.

| Resource                                                            | What You'll Learn                                        |
| ------------------------------------------------------------------- | -------------------------------------------------------- |
| [[Seven Agent Memory Architectures - @TheTuringPost]]               | 7 memory patterns: AgeMem, Memex, MemRL, UMA, Pancake    |
| [[Slate Agent Architecture and Context Management - cedric_chee]]   | Context-as-RAM, thread/episode design                    |
| [[Claude Obsidian Memory Stack Compounds - @nyk_builderz]]          | Three-tier agent memory system (1.4K likes) `#new`       |
| [[The Harness Is The Product Not The Model - @nyk_builderz]]        | Infrastructure > model selection `#new`                  |
| [[Context Engineering for AI - @witcheer]]                          | Context config > prompt refinement (305 likes) `#new`    |
| [[The Harness Is Everything Built By Cursor Claude - @rohit4verse]] | Harness analysis: Cursor, Claude Code, Perplexity `#new` |
| [[Lessons Building Claude Code How We Use Skills - @trq212]]        | Skill categories & best practices (2.7K likes) `#new`    |
| [[Agreement Is a Bug - 11 Claude Code Agents Disagree - @nyk_builderz]] | Multi-agent dissent as a decision-quality pattern for Claude Code `#new` |
| [[SKILLRL New Learning Paradigm for Agents - @_avichawla]]          | Agent skill distillation `#new`                          |
| [[Cognee Self-Healing AI Skills - iruletheworldmo]]                 | Self-correcting skills at runtime                        |
| [[Self Improving Skills for Agents - @tricalt]]                     | Self-improving agent patterns (3.4K likes)               |
| [[Autoresearcher on Agent Swarms - jumperz]]                        | Swarm + observer agent patterns                          |
| [[Context Graphs Beyond Chat Memory - @kirkmarple]]                 | Agent memory via context graphs                          |
| [[TLA+ State Machines and Model Checking - rot13maxi]]              | Formal verification, SAT solvers                         |
| [[PUA Plugin Pressures AI Agents - @abxxai]]                        | 5-step AI debugging pressure framework                   |
| [[Free AI Learning System Breakdown - @atenov_d]]                   | NotebookLM + Obsidian + atomic notes                     |
| [[Reverse-Engineered Learning System with Zettelkasten - atenov_d]] | Atomic note methodology                                  |
| [[Deep Agents Open-Source Coding Agent Harness - @hasantoxr]]      | LangChain/LangGraph coding-agent harness with subagents  |
| [[RLMs with GEPA for DSPy Autoresearch - @lateinteraction]]        | DSPy autoresearch idea for ColBERTv3                     |
| [[Graph Based AI Agent Workflow with Fabro - @tom_doerr]]          | Graph-shaped software-factory workflow anchored to Fabro `#new` |
| [[Control Planes Keep Agents Out of Incident Review - @nyk_builderz]] | Policy, approvals, rollback gates, and audit layers for production-ready agents `#new` |
| [[Skills Are Executable Systems - @sitinme]]                       | Claude Code skills as executable systems with scripts, memory, gotchas, and trigger descriptions `#new` |
| [[Agent Architecture]]                                              | Multi-agent system patterns (MOC)                        |
| [[Self-Optimizing Systems]]                                         | Systems that study and improve themselves (MOC)          |

---


| [[What is Agentic Engineering?]] | Simon Willison defines agentic engineering as building software with coding agents that run tools in loops toward... `#new` |
| [[Autoresearch-Inspired Skill Self-Improvement - @Hesamation]] | Skill-testing workflow where Claude Code skills are iteratively improved against an eval suite until performance... `#new` |
| [[AutoResearch, Unsloth Studio, and alphaXiv MCP - @himanshustwts]] | Quick roundup of emerging research automation primitives across experiment loops, training UI, and paper-reading... `#new` |
| [[AI-Researcher Automates the Scientific Lifecycle - @ihtesham2005]] | Highlight of HKU's AI-Researcher system, which takes references and produces full research papers accepted at... `#new` |
| [[Agent Memory: Building Memory-Aware Agents - @AndrewYNg]] | Andrew Ng course announcement focused on building agents that retain useful context across sessions instead of... `#new` |
| [[Open Models, Open Runtime, Open Harness - @hwchase17]] | Agent architecture framing that breaks systems into model, runtime, and harness so teams can build their own stack. `#new` |
| [[SkyPilot Removes the Single-GPU Autoresearch Bottleneck - @skypilot_org]] | SkyPilot gives Karpathy-style autoresearch direct access to a cluster so it can provision its own H100 and H200... `#new` |
## `Developer Tools & Code Intelligence/` (13 resources)

Code analysis, development tools, and coding skill enhancement.

| Resource | What You'll Learn |
|----------|-------------------|
| [[Matt Pocock Skills]] | Claude Code skills: TDD, PRD, architecture `#new` |
| [[Impeccable Style]] | 20+ design commands for AI coding assistants `#new` |
| [[contextplus]] | RAG + AST + spectral clustering for codebase graphs |
| [[GitNexus Code Intelligence Open Source - @sukh_saroy]] | Tree-sitter AST, code graph indexing (4.5K likes) |
| [[Chrome DevTools MCP]] | Agents connecting to active browser sessions |
| [[Extract Code From Open Source - @tekbog]] | Extracting code from OSS instead of blind dependencies |
| [[tree-sitter-ast-parsing]] | Incremental parsing for programming tools |
| [[Codex Playwright Interactive Skill Demo]] | JavaScript REPL for front-end dev |
| [[Open SWE Internal Coding Agents - @langchain]] | Internal coding agent patterns from Stripe/Ramp/Coinbase `#new` |
| [[Using Linters to Direct Agents]] | Lint rules as executable constraints for self-healing coding agents `#new` |
| [[Introducing Agent Readiness]] | Measuring repo readiness across pillars, levels, and remediation `#new` |
| [[Factory AI Agent Readiness Links Roundup - @alvinsng]] | Compact roundup of Factory articles on readiness, missions, and compression `#new` |
| [[303-Page Field Guide on Code Models and Coding Agents - @mdancho84]] | Survey-scale snapshot of code-model and coding-agent research from 50 authors `#new` |

---


| [[Eval Skills for AI Coding Agents]] | Hamel's eval-skills repo packages reusable audits and judge-building skills for AI coding-agent eval pipelines. `#new` |
| [[Library for Inspecting and Debugging Claude Code - @NeelNanda5]] | Recommendation for a tool that reveals exact Claude Code API calls, enabling reproducibility and causal debugging... `#new` |
## `Databases Vectors & Graphs/` (9 resources)

Database concepts, vector search, graph databases, and data architecture.

| Resource | What You'll Learn |
|----------|-------------------|
| [[vector-database-deep-dive]] | Vector DB internals and use cases |
| [[embedding-vector-graph-explainer]] | Embeddings ↔ vector DBs ↔ graph DBs |
| [[graph-database-deep-dive]] | Graph concepts, traversals, use cases |
| [[database-paradigms-and-vectors]] | Different DB paradigms, vector focus |
| [[time-series-database-deep-dive]] | Time-series architecture |
| [[Semantic Search Replacing Grep - @helloiamleonie]] | Semantic search for coding agents |
| [[RAG Query Optimization 4 Techniques - @femke_plantinga]] | Query Decomposition, Routing, Transformation, Agent `#new` |
| [[Production Agentic RAG Course]] | Production-oriented course repo for building agentic retrieval systems `#new` |
| [[Best RAG Engineers Model Information Topology - @ihtesham2005]] | Production RAG depends on modeling information topology, hierarchy, and related context instead of flat chunking. `#new` |

---

## `Design & UI Engineering/` (5 resources)

Animation, typography, UX psychology, and interface patterns.

| Resource | What You'll Learn |
|----------|-------------------|
| [[UserInterface Wiki]] | Animation principles, Laws of UX, web audio `#new` |
| [[desengs.com]] | Design engineering resource hub |
| [[Generative UI for MCP Apps - @ctatedev]] | AI-assembled component catalogs |
| [[rauno-freiberg-tweets]] | Conversation minimap, long message UX (Vercel) |
| [[How to Build Astonishing UI with Codex - @emanueledpt]] | Prompting guide for stronger Codex-generated frontend work `#new` |

---

## `Knowledge Management/` (5 resources)

Organizing, retrieving, and compounding knowledge over time.

| Resource | What You'll Learn |
|----------|-------------------|
| [[Knowledge Management]] | AI-augmented knowledge systems (MOC) |
| [[Obsidian AI Second Brain Setup - @atenov_d]] | AI + Obsidian setup (1.3K likes) |
| [[AI Agent Obsidian Automation Setup - @atenov_d]] | Agent Obsidian automation |
| [[Cortex Hybrid Semantic Graph Engine - @darlingtondev]] | Semantic graph engine |
| [[Automating Research With AI Agents - @dhasandev]] | Research automation workflows |

---


| [[Why File-Based AI Memory Beats Black-Box Vectors - @Atenov_D]] | Readable folder-based memory stack for research agents instead of opaque vector-only memory that is hard to audit... `#new` |
## Stats

- **Total learning resources:** 103
- **Disciplines:** 8
- **New this session:** 37
- **Last updated:** 2026-03-21

## Recent

- [[Karpathy's 10 Actionable Insights for Working with AI Agents - @daniel_mac8]] — Dan McAteer (@daniel_mac8)
- [[MiniMax Skills]] — MiniMax-AI on GitHub
- [[Hermes Agent]] — Nous Research on GitHub
- [[LangChain Docs]] — LangChain Docs
- [[Best Practices for Prompt Engineering with the OpenAI API]] — OpenAI Help Center
- [[Benchmarks Without Tool Use Will Become Obsolete - @a1zhang]] — alex zhang (@a1zhang)
- [[iii Docs]] — iii Docs
- [[HF Papers Benchmarks Before Reimplementation - @mingtakaivo]] — Mingta Kaivo 明塔 开沃 (@mingtakaivo)
- [[RL for LLMs The Reading List]] — Yunze (Lorenzo) Xiao
- [[Qwen3.5-9B Claude Opus Reasoning Distillation Debate - @off_thetarget]] — pepper 花椒 (@off_thetarget)
- [[Hermes Agent Four-Layer Memory System - @shao__meng]] — meng shao (@shao__meng)
- [[Unsloth Democratizes Qwen3.5 RL Training - @neural_avb]] — AVB (@neural_avb)
- [[How to 10x Your Claude Skills - @itsolelehmann]] — Ole Lehmann (@itsolelehmann)
- [[Evals First for Coding Agents - @synopsi]] — Rasty Turek (@synopsi)
- [[Qwen3.5 RL Free Notebook - @UnslothAI]] — Unsloth AI (@UnslothAI)
- [[Three-Layer Agent Harness for Product Design - @PrajwalTomar_]] — Prajwal Tomar (@PrajwalTomar_)
- [[Hyperagents and Metacognitive Self-Modification - @jennyzhangzt]] — Jenny Zhang (@jennyzhangzt)
- [[AutoResearch Memory Eval Framework - @kingbootoshi]] — BOOTOSHI (@kingbootoshi)
- [[Agentic Design Patterns Curriculum - @techxutkarsh]] — Utkarsh Sharma (@techxutkarsh)
- [[Generative TUI Live Terminal Dashboards - @ctatedev]] — Chris Tate (@ctatedev)
- [[Emulate Makes Google Sign-In Testable - @ctatedev]] — Chris Tate (@ctatedev)
- [[MSA Memory Sparse Attention to 100M Tokens - @troyhua]] — Troy Hua (@troyhua)
- [[Learn Claude Code]] — shareAI-lab/learn-claude-code on GitHub
- [[Anatomy of the .claude Folder Guide - @akshay_pachaar]] — Akshay (@akshay_pachaar)
- [[Cloudflare Code Mode Reframes Tool Use as SDKs - @jpschroeder]] — Justin Schroeder (@jpschroeder)
- [[Open-SWE Open Source Coding Agent - @sitinme]] — sitin (@sitinme)
- [[Why AGENTS.md Can Hurt Coding Agents - @shao__meng]] — meng shao (@shao__meng)
- [[Harness Design for Long-Running Application Development]] — Prithvi Rajasekaran (Anthropic)
- [[Structured Test-Time Scaling Analysis Endorsement - @a1zhang]] — alex zhang (@a1zhang)
- [[Structured Test-Time Scaling: From Multi-Agent Systems to General Inference Architectures]] — Xinming Tu
- [[TurboQuant 6x KV Compression 8x Speedup - @googleresearch]] — Google Research (@googleresearch)
- [[TurboQuant: Redefining AI Efficiency with Extreme Compression]] — Google Research
- [[Claude Courses]] — Anthropic
- [[AI That Evolves Its Own Evolution]] — Richard Cornelius Suwandi
- [[Anthropic Multi-Agent Harness Lessons - @wangray]] — Ray Wang (@wangray)
- [[Auto-Research Agent Memory Framework - @kingbootoshi]] — BOOTOSHI (@kingbootoshi)
- [[Perplexity Open-Sources PPLX-Embed - @natjin]] — nat (@natjin)
- [[HyperAgents Recursive Self-Improvement - @daniel_mac8]] — Dan McAteer (@daniel_mac8)
- [[Claude Code Auto Mode Safer Permission Skipping]] — Anthropic Engineering
- [[Auto-Inference Optimiser for LLM Inference - @manthanguptaa]] — Manthan Gupta (@manthanguptaa)
- [[OpenSpace Agent Self-Evolution and Shared Skills - @axiaisacat]] — axiaisacat (@axiaisacat)
- [[The Harness Is Everything Built By Cursor Claude - @rohit4verse]] — Rohit (@rohit4verse)
- [[How To Be A World-Class Agentic Engineer - @systematicls]] — sysls (@systematicls)
