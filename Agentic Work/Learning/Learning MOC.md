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
- [[Harness Memory and Context Must-Read - @morganlinton]] — Morgan (@morganlinton)
- [[Hermes Multi-Agent Profiles Tutorial - @teknium]] — Teknium (@teknium)
- [[Meta-Harness Code Release - @yoonholeee]] — Yoonho Lee (@yoonholeee)
- [[Claude Code Session Management and 1M Context - @trq212]] — Thariq (@trq212)
- [[From SIMT to Systolic GPU and TPU Architecture - @MainzOnX]] — Adam Mainz (@MainzOnX)
- [[Claude Code Ultrareview Command and Auto Mode - @claudeai]] — Claude (@claudeai)
- [[Opus 4.7 Xhigh Mode for Agentic Coders - @Vtrivedy10]] — Viv (@vtrivedy10)
- [[Domain-Specific Models and Harnesses Win - @Vtrivedy10]] — Viv (@vtrivedy10)
- [[LLM-as-a-Verifier With Logprob Confidence - @webbigdata]] — webbigdata (@webbigdata)
- [[Prompt Caching in LLMs Clearly Explained - @_avichawla]] — Avi Chawla (@_avichawla)
- [[Single-Agent AI Coding Ceiling and Multi-Agent Workflows - @MilksandMatcha]] — Sarah Chieng (@MilksandMatcha)
- [[From Weights to Context to Harness Engineering - @akshay_pachaar]] — Akshay (@akshay_pachaar)
- [[Context Engineering Checklist for AI Coding - @kmeanskaran]] — Karan (@kmeanskaran)
- [[Memory Is Markdown and the Harness Should Stay Thin - @av1dlive]] — Avid (@av1dlive)
- [[AI Memory Tools Split Into Backends vs Context Substrates - @witcheer]] — witcheer (@witcheer)
- [[Two-Phase Long-Horizon Agent Workflow]] — Han Xiao (@hxiao)
- [[Context Engineering for AI - @witcheer]] — witcheer (@witcheer)
- [[Implemented Google's TurboQuant paper on Gemma 3 4B with a custom Triton kernel…]] — DEJAN (@dejanseo)
- [[Upgrading your RAM is now unnecessary.]] — ComfyUI (@ComfyUI)
- [[so i completed reading the yolov1 paper]] — ShaRPeyE (@sharpeye_wnl)
- [[the bitter lesson is coming for search]] — Jeff Huber (@jeffreyhuber)
- [[Thank god for Droid's shield system. This is the 3rd time today that it decided…]] — 0xSero (@0xSero)
- [[给大家写个小学水平也能理解TurboQuant的解读]] — karminski-牙医 (@karminski3)
- [[yo whoever is training the coding models RL can you please DEDUCT POINTS…]] — BOOTOSHI 👑 (@KingBootoshi)
- [[most agent failures aren't model failures]] — ptk (@ptkbhv)
- [[Unbelievable.]] — ᴅᴀɴɪᴇʟ ᴍɪᴇssʟᴇʀ 🛡️ (@DanielMiessler)
- [[Yohei 的 ai memory 综述非常棒]] — Wey Gu 古思为 (@wey_gu)
- [[The entire Qwen stack is now fine-tunable on your Mac! 🍏]] — Abdur Rahim (@_ARahim_)
- [[more evals != better agents]] — Viv (@Vtrivedy10)
- [[Fine-Tuning is officially a waste of money.. 💀]] — Simplifying AI (@simplifyinAI)
- [[we spend a lot of time intentionally designing/selecting evals that map to…]] — Viv (@Vtrivedy10)
- [[I've been studying this paradigm for the past few weeks guys and I get this…]] — Yacine Mahdid (@yacinelearning)
- [[The Agent Evaluation Readiness Checklist]] — LangChain (@LangChain)
- [[@VictorMoreira16 actually walks through his screen recording in this one lol]] — Viv (@Vtrivedy10)
- [[Harness engineering is as important as model capability scaling.]] — Dan McAteer (@daniel_mac8)
- [[See how @Kensho built a multi-agent data retrieval system on LangGraph to give…]] — LangChain (@LangChain)
- [[Environments in LangSmith Prompt Hub]] — LangChain (@LangChain)
- [[Karpathy 这个autoresearch开源项目，]] — 木子不写代码 (@ai_muzi)
- [[Day 82/365 of GPU Programming]] — levi (@levidiamode)
- [[Yo check out this new paper on retrieval methods.]] — AVB (@neural_avb)
- [[@neural_avb Wrote a paper on those different retrieval methods, issues with…]] — Elias Lumer (@EliasLumer)
- [[pi is so fucking cool]] — umang (@umgbhalla)
- [[Introducing the agent-browser dashboard]] — Chris Tate (@ctatedev)
- [[For everyone with 16 or less GB ram that want to run a coding model locally.]] — 0xSero (@0xSero)
- [[Google TurboQuant Running Locally in Atomic Chat]] — Chubby♨️ (@kimmonismus)
- [[TDD for Documentation Skills]] — 极客杰尼 (@seekjourney)
- [[Karpathy AutoResearch For Marketing Copy]] — Shann³ (@shannholmberg)
- [[Best Local Models By Hardware Tier]] — 0xSero (@0xSero)
- [[Migrated From OpenClaw To Hermes]] — Nyk 🌱 (@nyk_builderz)
- [[Research Papers For AI Engineer Interviews]] — Vivo (@vivoplt)
- [[Johnson-Lindenstrauss Lemma Explained]] — Paata Ivanisvili (@PI010101)
- [[LangGraph Real-Time Knowledge Graph Corrections]] — LangChain OSS (@LangChain_OSS)
- [[Agentic Context Engineering ACE Paper]] — Priyanka Vergadia (@pvergadia)
- [[HyperAgents Self-Improvement Generalizes]] — Igor Kudryk (@fancylancer3991)
- [[TurboQuant Paper Issues Flagged]] — Jianyang Gao (@gaoj0017)
- [[What Every Developer Should Know About GPU Computing]] — Vivek Galatage (@vivekgalatage)
- [[AI Engineering Build-Your-Own Curriculum]] — Piyush (@piyush784066)
- [[A-Evolve GitHub Link]] — Henry Lu (@HenryL_AI)
- [[A-Evolve PyTorch Moment For Self-Evolving AI]] — Henry Lu (@HenryL_AI)
- [[MemCollab Cross-Agent Memory Sleeper Pick]] — Bnaf.OG | 🟧 (@bnafOg)
- [[Finally The Web Has Become Interesting Again]] — Nucleus☕️ (@EsotericCofe)
- [[Pure TypeScript Text Measurement Algorithm]] — Cheng Lou (@_chenglou)
- [[LangGraph Agentic Company Researcher]] — LangChain OSS (@LangChain_OSS)
- [[Hermes Agent Plus Qwen 3.5 27B Local Stack]] — Harveen Singh Chadha (@HarveenChadha)
- [[Smol Training Playbook Recommended Read]] — 0xSero (@0xSero)
- [[New Text Measurement Algorithm Reaction]] — Viv (@Vtrivedy10)
- [[MSA Memory Sparse Attention vs Titans MIRAS]] — 艾略特 (@elliotchen100)
- [[KVCache Quantization Is A No-No]] — Ahmad (@TheAhmadOsman)
- [[Pi Autoresearch Studio Granular Experiment Selection]] — Jordan Hochenbaum (@Jnatanh)
- [[Pretext Turns Static Pages Into Tactile Canvas]] — Vadim (@ukint_vs)
- [[Pretext Resume Builder One Page Realtime]] — Vlad (@VladArtym)
- [[Harness Design Overcomes Lazy Confused Agents]] — Viv (@Vtrivedy10)
- [[Start Async RL With Prime-RL Clean Codebase]] — lux (@novasarc01)
- [[AI Runs the Harness Tsinghua Shenzhen Paper]] — Ronak Malde (@rronak_)
- [[Christian Replies to Novasarc With RL Link]] — Christian (@creet_z)
- [[Novasarc Followup Async RL Link]] — lux (@novasarc01)
- [[Deep Agent To Production Memory Guardrails Durability]] — Sydney Runkle (@sydneyrunkle)
- [[How Memory Works In HyperAgents]] — mem0 (@mem0ai)
- [[Five Most Important Ideas In AI April 2026]] — Daniel Miessler (@DanielMiessler)
- [[RL Behind Cursor Composer 2 Explained]] — AVB (@neural_avb)
- [[MiroShark Knowledge Graph Agent Memory]] — Aaron Mars (@aaronjmars)
- [[Jensen Pushing Open Models And Harness Toolkits]] — Viv (@Vtrivedy10)
- [[Meta-Harness Autonomously Optimizes LLM Harnesses]] — Yoonho Lee (@yoonholeee)
- [[Reading List To Actually Understand Graphs Networks]] — Ahmad (@TheAhmadOsman)
- [[Combine Reading List With NotebookLM Pro Tip]] — Ahmad (@TheAhmadOsman)
- [[Eval Article Traction Open Models Push]] — Viv (@Vtrivedy10)
- [[Cursor Kimi Wrapper Takes Look Dumb]] — AVB (@neural_avb)
- [[Natural-Language Agent Harnesses Paper Explained]] — alphaXiv (@askalphaxiv)
- [[Baseten Training An Autoresearch Substrate]] — Vim (@vim_dzl)
- [[Train Skills From Agent Execution History]] — Muratcan Koylan (@koylanai)
- [[Meta-Harness Automates Harness Engineering]] — Lior Alexander (@LiorOnAI)
- [[Dont Sleep On Transformers.js Browser Models]] — AVB (@neural_avb)
- [[Trust Claude Using Karpathys LLM Council Method]] — Ole Lehmann (@itsolelehmann)
- [[Qwen 3.5 27B Opus Distilled Agentic Model]] — hesam (@Hesamation)
- [[EvoSkill proposer and skill builder iterative loop - @oleg_golev]] — Oleg Golev (@oleg_golev)
- [[The agent improvement loop starts with a trace - @LangChain]] — LangChain (@LangChain)
- [[Best open source repos Paperclip Mirofish Hermes Openclaw - @0xsachi]] — Miss Sentient (@0xsachi)
- [[Six patterns across 30+ LLM eval benchmarks - @cwolferesearch]] — Cameron R. Wolfe (@cwolferesearch)
- [[Neural KV cache compaction STILL 8x compression - @oneill_c]] — Charlie O'Neill (@oneill_c)
- [[Skill chaining and skills should be actions - @realmcore_]] — akira (@realmcore_)
- [[Qwen3.6-Plus matches Opus 4.5 on agent benchmarks - @TheAhmadOsman]] — Ahmad (@TheAhmadOsman)
- [[Optimize agents with LangSmith - @hwchase17]] — Harrison Chase (@hwchase17)
- [[Agents automation teammate vibe coding one month - @Barret_China]] — Barret (@Barret_China)
- [[Meta-harness loops reward hacking on evals - @Vtrivedy10]] — Viv (@Vtrivedy10)
- [[Reasoning distillation high to low budgets - @Vtrivedy10]] — Viv (@Vtrivedy10)
- [[100K rows instruction data 10 tasks 100 papers - @neural_avb]] — AVB (@neural_avb)
- [[Harness Engineering in AI article - @amitiitbhu]] — Amit Shekhar (@amitiitbhu)
- [[Always-on agents that monitor detect and deploy fixes - @Vtrivedy10]] — Viv (@Vtrivedy10)
- [[LLM Knowledge Bases]] — Andrej Karpathy (@karpathy)
- [[karpathy is showing one of the simplest AI architectures that...]] — JUMPERZ (@jumperz)
- [[harness eng day 5: toolsets]] — Sydney Runkle (@sydneyrunkle)
- [[Recommended resources to learn Mechanistic Interpretability...]] — AVB (@neural_avb)
- [[Qwen3]] — stevibe (@stevibe)
- [[meta harness is a great paper from @yoonholeee that came out earlier...]] — Harrison Chase (@hwchase17)
- [[man andrej karpathy really is the fucking goat]] — Ejaaz (@cryptopunk7213)
- [[learning at the context layer is basically memory]] — Harrison Chase (@hwchase17)
- [[Releasing auto-harness: an open source library for our self improving...]] — Gauri Gupta (@gauri__gupta)
- [[Day 91/365 of GPU Programming]] — levi (@levidiamode)
- [[🚀 Just open-sourced 'Harness Engineering' Book — a deep-dive into...]] — AlexZ 🦀 (@blackanger)
- [[NVIDIA drops 4]] — Mitko Vasilev (@iotcoi)
- [[AAAAAND here we go]] — AVB (@neural_avb)
- [[Qwen 3]] — Poe Zhao (@poezhao0605)
- [[cool harness hook that wraps every bash call and does tons of output filtering…]] — Viv (@Vtrivedy10)
- [[whoa this is actually fucking sick, a self-improving ai you can use yourself…]] — Ejaaz (@cryptopunk7213)
- [[Learn about LLMs like an engineer not like researcher.]] — Karan🧋 (@kmeanskaran)
- [[Holy shit. UNC just let an AI run 50 experiments autonomously for 72 hours and…]] — Robert Youssef (@rryssf_)
- [[🚨 BREAKING: Vector databases for AI memory just got replaced by MP4 files.]] — How To AI (@HowToAI_)
- [[BREAKING:🚨 NVIDIA just quantized Gemma 4 31B on Hugging Face 🔥]] — Eric ⚡️ Building... (@outsource_)
- [[a lot of people switched to gemma 4 26b a4b as their main model, but what is…]] — left curve dev (@leftcurvedev_)
- [[THIS CLI PROXY CUTS YOUR CLAUDE CODE TOKEN USAGE BY 60-90%]] — Om Patel (@om_patel5)
- [[Having Hermes make one for Hermes and then will upload the skill from it's…]] — Teknium (e/λ) (@Teknium)
- [[Hype for autoresearch has died down a bit but I believe it is a new paradigm…]] — 0xSero (@0xSero)
- [[My next video will be positively awesome!]] — AVB (@neural_avb)
- [[The Top AI Papers of the Week (March 30 - April 5)]] — DAIR.AI (@dair_ai)
- [[We're launching CodeDB v0.2.53!]] — Rach (@rachpradhan)
- [[Introducing the Manim skill for Hermes Agent.]] — Nous Research (@NousResearch)
- [[more people should be talking about this https://github.com/NVIDIA-NeMo/DataDesi…]] — Hunter Bown (@goodhunt)
- [[regarding agent memory, I'm realizing:]] — James Long (@jlongster)
- [['LLM Reasoning: Surprising effectiveness of self-tuning without rewards'.]] — Antonio Lupetti (@antoniolupetti)
- [[今天 GitHub 被自我进化记忆性 Agent 屠榜了了 🚀]] — GitTrend (@GitTrend0x)
- [[thread of ui ideas for claude code, codex and cowork type products]] — Chris Barber (@chrisbarber)
- [[YOU GUYS NEED TO PUT YOUR AGENTS ON CUSTOM ESLINT RULES ASAP]] — BOOTOSHI 👑 (@KingBootoshi)
- [[Meta Harnesses is Autoresearch on steroids.]] — Deedy (@deedydas)
- [[Let me make local AI easy for you Give Codex Cli the tweet below and tell it -]] — Ahmad (@TheAhmadOsman)
- [[「 MiroMind, MiroEval 」 面向 Deep Research Agent 的多模态的，反映现实世界查询复杂度的 benchmark。]] — 马东锡 NLP (@dongxi_nlp)
- [[Imo a good manim harness needs several things 1]] — AVB (@neural_avb)
- [[RL boys and girls, get on this PufferLib stuff asap I did not fully understand]] — AVB (@neural_avb)
- [[This is one of the best innovations to object storage]] — AVB (@neural_avb)
- [[The GEA project is open sourced now]] — Xin Eric Wang (@xwang_lk)
- [[Post by @carnot_cyclist]] — Ilija Lichkovski (@carnot_cyclist)
- [[agent-browser + Lightpanda + batch + multi-session is a dangerous combo]] — Chris Tate (@ctatedev)
- [[Pretty cool to see Tobi using Hermes and the Manim skill]] — Nous Research (@NousResearch)
- [[Claude Code isn't magic]] — JetBrains (@jetbrains)
- [[Today’s “self-evolving” agents are still stuck in tightly constrained search]] — Paul Liang (@pliang279)
- [[Can't stop thinking about how Claude Code is in LAST PLACE on TerminalBench for]] — Theo - t3.gg (@theo)
- [[The last thing I would ever do is have my product rely on one companies agent]] — BOOTOSHI 👑 (@KingBootoshi)
- [[but I thought Claude Code and RLMs were the same thing s jokes aside this is]] — alex zhang (@a1zhang)
- [[The harness hill-climbing maps closely to what I've seen in my experimental]] — Daniel Kalski (@dankalski)
- [[dude is on some generational run]] — himanshu (@himanshustwts)
- [[Open everything 🔥 Open Harness, Model Choice, Open Memory (take it wherever you]] — Viv (@Vtrivedy10)
- [[Thank you for helping to make Hermes Agent amazing]] — Nous Research (@NousResearch)
- [[Scaling Coding Agents via Atomic Skills  Most coding agents train]] — DAIR.AI (@dair_ai)
- [[Hermes can now command an army of coding agents]] — Agent Orchestrator (@aoagents)
- [[Another banger paper from Microsoft]] — elvis (@omarsar0)
- [[The crux of the whole blog is - 1]] — Diptanu Choudhury (@diptanu)
- [[Multi-Agent Orchestration with deepagents]] — Viv (@Vtrivedy10)
- [[Meta AI 2026 Research Roundup — HyperAgents, TribeV2, SAM 3.1, Neural Computers]] — AVB (@neural_avb)
- [[Dex — Agent with Full Operational Context and Self-Updating Knowledge Base]] — Kevin Gu (@kevingu)
- [[Deep Agents Deploy — Harness, Sandbox, Memory, MCP, A2A]] — Harrison Chase (@hwchase17)
- [[Local Hermes Agent on Plex with Qwen 3.5 9B]] — Ahmad (@TheAhmadOsman)
- [[RLMs 50-Minute Breakdown with Deno and Pyodide]] — AVB (@neural_avb)
- [[Mismanaged Geniuses Hypothesis]] — alex zhang (@a1zhang)
- [[LFM 350M Edge Model Training Guide]] — AVB (@neural_avb)
- [[Studying Meta Neural Computers with paperbreakdown]] — AVB (@neural_avb)
- [[Everything Is Just MatMul — Cache Locality Before CUDA]] — abheecs (@abheecs)
- [[Remotion — Jupyter Notebook to MP4 Tutorial Renderer]] — AVB (@neural_avb)
- [[GitButler Raises $17M Series A]] — Lao Gui (@laogui)
- [[GRPO on RLM-Qwen3-4B Generalizes to 1M-token 8-needle Tasks]] — Omar Khattab (@lateinteraction)
- [[RLM Video Understanding with Moondream]] — AVB (@neural_avb)
- [[Attention Matching for RLM Sub-agent Context]] — alex zhang (@a1zhang)
- [[Crazy RLM Variant via Attention Matching]] — Omar Khattab (@lateinteraction)
- [[Agent Harnesses and Memory Ownership]] — Harrison Chase (@hwchase17)
- [[predict-rlm — RLM as an Agent Runtime]] — Gabriel Lespérance (@GabLesperance)
- [[alchaincyf/hermes-agent-orange-book — Hermes Agent 橙皮书实战指南]] — alchaincyf (github.com)
- [[deepagents Docs Revamp — Agents, Context Engineering, Infra, Prod]] — Viv (@Vtrivedy10)
- [[Parallel Agents — Worktree + Diff-Gated Workflow]] — Ahmad (@TheAhmadOsman)
- [[DART — Agentic RL Decoupling Reasoning from Tool-Use]] — Xiuyu Li (@sheriyuo)
- [[Gather around Deep Learning bros and sis - this update]] — AVB (@neural_avb)
- [[Nous Research开源了hermes-agent-self-evolution——一个让AI agent自己进化自己prompt的代码库， 背后引擎叫GEPA，ICLR 2026 Oral，比强化学习少用35倍数据，效果还高出20个百分点。 别再手调system prompt了。prompt工程这件事，正在被prompt自己取代。 httpsgithub]] — KK.aWSB (@KKaWSB)
- [[Your Hermes Agent can now delegate to RLMs 🙌 Recreated]] — Steffen Röcker (@sroecker)
- [[The Top AI Papers of the Week (April 6 -]] — DAIR.AI (@dair_ai)
- [[Been thinking about what this paper really means]] — AVB (@neural_avb)
- [[i've been working on llm memory systems for 3 years]] — Chrys Bader (@chrysb)
- [[Skill for Parallel Agentic Workflows is now live Works w]] — Ahmad (@TheAhmadOsman)
- [[We built an algorithm that allows agents to communicate KV]] — himanshu (@himanshustwts)
- [[I just love the language of this study]] — Cobus Greyling (@CobusGreylingZA)
- [[Learn LLM internals step by step - from tokenization to]] — Amit Shekhar (@amitiitbhu)
- [[Harness, Memory, Context Fragments, & the Bitter Lesson this is]] — Viv (@Vtrivedy10)
- [[introducing Autoreason, a reasoning method inspired by @karpathy's AutoResearch which]] — 𒐪 (@SHL0MS)
- [[Studying the new Interleaved Head Attention paper this morning Meta]] — AVB (@neural_avb)
- [[agents out there are struggling with these naive and brittle]] — spacy (@dosco)
- [[Exciting news for @NousResearch Hermes users]] — mr-r0b0t (@mr_r0b0t)
- [[Hermes Agent is a great Creative Director]] — Nous Research (@NousResearch)
- [[Introducing TRACE an end-to-end system for environment-specific agent self-improvement🚀 Outperforms]] — Hangoo Kang (@hangoo_kang)
- [[hmmm this wasn’t my takeaway from reading this, anyone else]] — Viv (@Vtrivedy10)
- [[Hermes Telegram Mini App is now AVAILABLE OPEN SOURCE]] — mr-r0b0t (@mr_r0b0t)
- [[Harness Engineering Derived from what Models can’t do alone It]] — Viv (@Vtrivedy10)
- [[Meanwhile there are people who believe agentic memory has been]] — Raphael De Lio (@RaphaelDeLio)
- [[In this blog, we will learn about Feed-Forward Networks in]] — amitiitbhu (@amitiitbhu)
- [[One of the best written articles on Harness out there]] — The Code Newsletter (@code_newsletter)
- [[99% of our production code is written by AI]] — intuitiveml (@intuitiveml)
- [[LLM-as-a-Verifier Scoring Granularity - @cwolferesearch]] — Cameron R. Wolfe, Ph.D. (@cwolferesearch)
- [[Claude Code Skills Workflow - @polydao]] — Mr. Buzzoni (@polydao)
