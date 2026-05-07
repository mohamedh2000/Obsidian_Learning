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
- [[Karpathy's Confusion Protocol in GStack - @garrytan]] — Garry Tan (@garrytan)
- [[Stanford Agentic AI Lecture and Practical Tasks - @deronin_]] — Ronin (@deronin_)
- [[AI Content System Synced With Knowledge Wiki - @shannholmberg]] — Shann³ (@shannholmberg)
- [[Data Driven Agent Design with Evals & Hill Climbing Algorithms]] — Viv (@vtrivedy10)
- [[RLM Task Decomposition for LongCoT]] — Brian Bartoldson (@bartoldson)
- [[Autogenesis Self-Evolving Agent Protocol - @omarsar0]] — elvis (@omarsar0)
- [[Harness Design for Long-Running Apps]] — Bilgin Ibryam (@bibryam)
- [[Compound Engineering Optimization Loops]] — Trevin Chow (@trevin)
- [[Research Papers Every LLM Engineer Must Read]] — Amit Shekhar (@amitiitbhu)
- [[Agent Harness Optimization Guide]] — Alex Ker (@thealexker)
- [[Anthropic Coding Agents 30-Minute Deep Dive]] — Movez (@0xMovez)
- [[EvoForge Self-Evolving Agentic Harness]] — Gauri Gupta (@gauri__gupta)
- [[AutoReason for Ad Creative]] — Shann³ (@shannholmberg)
- [[Zero to ML Framework in 4 Months]] — NVIDIA AI Developer (@nvidiaaidev)
- [[DAIR.AI Top AI Papers Week April 2026]] — DAIR.AI (@dair_ai)
- [[How LangChain Made Their Docs Test Themselves]] — Naomi Pentrel (LangChain)
- [[LeetCUDA - Open Source CUDA System Tutorial]] — Joruno (@wsl8297)
- [[All Agentic Architectures - 17+ State-of-the-Art Patterns]] — FareedKhan-dev
- [[The Ultimate Guide to Claude Opus 4.7]] — Paweł Huryn (@PawelHuryn)
- [[Memory Transfer Learning (MTL) for Coding Agents Explained]] — AVB (@neural_avb)
- [[The Runtime Behind Production Deep Agents]] — Sydney Runkle (@sydneyrunkle)
- [[RLMs Are The New Reasoning Models]] — Raymond Weitekamp (@raw_works)
- [[Why I Built dspy-agent-skills]] — Bryan Young (@intertwineai)
- [[Prompt Auto-Caching Limits Compaction - @rlancemartin]] — Lance Martin (@rlancemartin)
- [[Ten Principles for Production AI Agents - @rohit4verse]] — Rohit (@rohit4verse)
- [[Agents Over Workflows - Erik Schluntz Patterns - @rohit4verse]] — Rohit (@rohit4verse)
- [[11 Essential AI Evals Resources - @pauliusztin_]] — Paul Iusztin (@pauliusztin_)
- [[DSPy Agent Skills Part 2 - @intertwineai]] — Bryan Young (@intertwineai)
- [[30 Minutes with Anthropic Coding Agents Lead - @datachaz]] — Charly Wargnier (@datachaz)
- [[Autoresearch Multi-Agent Dev Automation - @qingq77]] — Geek Lite (@qingq77)
- [[Autoreason for On-Page SEO]] — Shann³ (@shannholmberg)
- [[Karpathy 2-Hour LLM Tutorial]] — Phosphen (@phosphenq)
- [[B-Trees vs LSM Trees]] — ByteByteGo Newsletter
- [[Karpathy ChatGPT Internals Deep Dive]] — divyansh tiwari (@divyansht91162)
- [[Lambda-RLMs Harness Blog Review]] — Haitham Bou Ammar (@hbouammar)
- [[The Definitive Guide to Harness Engineering]] — TRAE (@Trae_ai)
- [[Sub-Agents vs Agent Teams: The Architecture Decision That Changes Everything]] — Suryansh Tiwari (@Suryanshti777)
- [[Production AI Agents in 30 Minutes Anthropic Stack - @codewithimanshu]] — Himanshu Kumar (@codewithimanshu)
- [[Claude Code Orchestration Workflow with Sub-Agents - @kingbootoshi]] — BOOTOSHI 👑 (@kingbootoshi)
- [[Claude Code Setup Plugin - Zero Config Automation]] — divyansh tiwari (@divyansht91162)
- [[Anthropic Applied AI Team - How to Prompt Claude Properly]] — 0xMarioNawfal (@roundtablespace)
- [[Hermes Agent Evolutions - 5 New Plugins]] — GitTrend (@gittrend0x)
- [[The Ultimate Hermes Guide - Multi-Agent Team Architecture]] — Nyk (@nyk_builderz)
- [[Alpha Eval - Agents Making Evals as a Multi-Player Game]] — Viv (@vtrivedy10)
- [[Skill Graph Content Engine - AI Agent for Multi-Platform Content]] — Ronin (@DeRonin_)
- [[Learn Harness Engineering Course - walkinglabs]] — Walking Labs (@walkinglabs)
- [[10 GitHub Repos for AI Engineer Jobs - @heynavtoor]] — Nav Toor (@heynavtoor)
- [[Claude Code Setup Plugin - @nicos_ai]] — Nico (@nicos_ai)
- [[Recursive Language Models MIT Explained - @_avichawla]] — Avi Chawla (@_avichawla)
- [[macOS Native App UI Redesign SSH Support]] — 老鬼 (@laogui)
- [[DeepSeek V4 Coding Agents Launch]] — Together AI (@togethercompute)
- [[RLM GPT-5.2 Performance Boost via Prompting]] — alex zhang (@a1zhang)
- [[Stanford CS336: Language Modeling from Scratch]] — Tech with Mak (@technmak)
- [[Meta-Harness Framework Open Source]] — AlphaSignal AI (@alphasignalai)
- [[Awesome Bitcoin - igorbarinov GitHub]] — Igor Barinov (@igorbarinov)
- [[Planning With Files Manus Pattern - @mysticaltech]] — The Canaanite (@mysticaltech)
- [[snarktank/ralph — Autonomous AI Coding Loop]] — snarktank (github.com)
- [[Ralph Orchestrator Hat-Based Agent Framework]] — mikeyobrien
- [[VibeMux Multi-Agent Terminal Orchestrator]] — UgOrange
- [[Icons Animated Multi-Library Collection]] — LN (@ln_dev7)
- [[Subscription Calendar UI Design]] — Maxim Kuznetsov (@disarto_max)
- [[Liquid Metal WebGL Button Component]] — VengeanceUI
- [[Holy Trinity of Agentic UI Resources]] — Cole (@colderoshay)
- [[Claude Code Continuous Learning Skill - @blader]] — Siqi Chen (@blader)
- [[Design Spells UI Animation Collection - @abmankendrick]] — Abraham John (@abmankendrick)
- [[Design Plugin with 5 Variations and Element Feedback - @0xdesigner]] — 0xDesigner (@0xdesigner)
- [[Morphing Button Interaction - @nitishkmrk]] — Nitish Khagwal (@nitishkmrk)
- [[Shoogle.dev Unified Component Library Search - @melvynxdev]] — Melvyn (@melvynxdev)
- [[Contains Studio 40+ Specialized AI Agents - @oliviscusai]] — Oliver Prompts (@oliviscusai)
- [[Hatch.sh Unified Product Development Desktop App - @serrrfirat]] — Firat Sertgoz (@serrrfirat)
- [[UI Design Resources Collection 60fps Divs Efecto Raydian - @creativestefan]] — Stefan (@creativestefan)
- [[Design Spells - Design Detail Inspiration Resource]] — Beka (@designedbybeka)
- [[CSS Animation Playground - @vojnvk]] — voj (@vojnvk)
- [[Sneak Peek Product Teaser - @bekacru]] — Beka (@bekacru)
- [[Database Research UI Concept - @insank18]] — Insan (@insank18)
- [[Clean UI Showcase - @ahtasham_design]] — Ahtasham (@ahtasham_design)
- [[3D Product Card Design - @Kanishk3D]] — Best Designs On ✧ (@bestdesignsonx)
- [[Oblivion UI Concept - @intrfacer]] — Ayda Oz (@aydaoz)
- [[Cleo Dev - AI-First Web Development Tool]] — Houssein Djirdeh (@hdjirdeh)
- [[Landing Page Showcase App Prompt for V Computer]] — Vibecoding Explained (@learn2vibe)
- [[Team Section Design - @itspeterdesign]] — Peter Design (@itspeterdesign)
- [[Remotion Code-Free Video Creation - @jnybgr]] — Jonny Burger (@jnybgr)
- [[Bento Grid Animations - @marcelkargul]] — Marcel (@marcelkargul)
- [[AI Employee Folder Structure - @ganimcorey]] — Corey Ganim (@ganimcorey)
- [[Motion Layout Prop for Multi-Step Buttons - @mannupaaji]] — Manu Arora (@mannupaaji)
- [[Framer Animation Showcase - @ensaktas]] — Enes Aktas (@ensaktas)
- [[Anime.js Layout API Documentation - @juliangarnier]] — Julian Garnier (@juliangarnier)
- [[GLM-4-Flash on M4 Pro Mac Minis with Exolabs - @alexocheema]] — Alex Cheema (@alexocheema)
- [[Landing Page Micro-Interactions in Days - @jameslaurents]] — James Laurent (@jameslaurents)
- [[Last ASCII Dither Tool You Will Ever Use]] — Alim (@almmaasoglu)
- [[Nucleo Icons Light Active State Design]] — Nucleo Icons (@nucleoicons)
- [[People Yearn for ASCII and Dither]] — Alim (@almmaasoglu)
- [[Selia Open-Source React UI Library V1]] — Nauval (@mhdnauvalazhar)
- [[Claude Code Guide Auto-Updated Every 2 Days]] — Cranot/claude-code-guide on GitHub
- [[Google Stitch MCP Server for Design-to-Code]] — Wes Roth (@wesroth)
- [[Don't Sleep on Expo Skills]] — Beto (@betomoedano)
- [[Google Stitch Documentation]] — David East (@_davideast)
- [[Go-To Sites for Design Inspiration]] — UI/UX Savior (@uisavior)
- [[Locomotive Scroll 5 Now Built on Lenis]] — Locomotive® (@locomotivemtl)
- [[Claude Code Ctrl+S Prompt Stash Feature]] — Ado (@adocomplete)
- [[Pencil Infinite Design Canvas for Claude Code]] — Tom Krcha (@tomkrcha)
- [[Pencil Design Tool]] — Pencil
- [[Agentation Visual Feedback Tool for Agents]] — Benji Taylor (@benjitaylor)
- [[Building Agentation with Agentation]] — Benji Taylor (@benjitaylor)
- [[AI Startup Card Animation in Pure Figma]] — Basit A. Khan (@basit_designs)
- [[Running 5 Parallel Claude Code Sessions with Notifications]] — Affaan Mustafa (@affaanmustafa)
- [[Sim Studio AI Agent Orchestration Platform]] — Oliver Prompts (@oliviscusai)
- [[Flowy Interactive Diagram Tool for Claude Code]] — CJ Hess (@seejayhess)
- [[Top 5 AI Design Tools for Designers]] — Craftwork (@craftworkdesign)
- [[Agentation Open Source Agent Interface Library]] — Benji Taylor (@benjitaylor)
- [[Skills.sh - Agent Skills Directory]] — Skills.sh
- [[Vercel React Best Practices Skill - 12 New Rules]] — Shu (@shuding)
- [[Animated UI Design Showcase]] — Marcel (@marcelkargul)
- [[Personal RAG Over All Your Data]] — 0xSero (@0xsero)
- [[AI-Friendly UI Kits for Vibe Coding]] — Craftwork (@craftworkdesign)
- [[Claude Code System Prompts Accessible via CC Mirror Fork]] — Numman Ali (@nummanali)
- [[Persona Skills for Multi-Stakeholder Feature Evaluation]] — Giuseppe `N3mes1s` (@n3mes1s)
- [[Claude Code Task Primitives and Session Persistence Guide]] — Eric Buess (@ericbuess)
- [[Aceternity UI Component Library - 200+ Animated React Components]] — Aceternity
- [[Marketing Skills for AI Coding Agents - coreyhaines31]] — Corey Haines (@coreyhaines31)
- [[VibeShip AI Coding Security and Memory Toolkit]] — VibeShip
- [[Kernel.sh Browser Pools for Pre-Configured Browser Automation]] — Kernel.sh
- [[Turn Claude Code Into Claude Teacher with FOR[name].md]] — Zara Zhang (@zarazhangrui)
- [[Claude Code Hidden Swarms Feature - Delegation Mode with Parallel Specialists]] — Mike Kelly (@nicerinperson)
- [[Claude Fresh Eyes Code Review Prompt]] — Jeffrey Emanuel (@doodlestein)
- [[Async Hooks Enable Parallel Agent Processes]] — Daniel San (@dani_avila7)
- [[Single Prompt Design Generation]] — Alfi | Design for Startups (@alfifromtoasty)
- [[Marketing Skills for AI Agents]] — Corey Haines
- [[last30days-skill Multi-Platform Research Agent]] — mvanhorn
- [[Autonomous Revenue Growth with Agent SDK and MCPs]] — Sam Hogan 🇺🇸 (@samhogan)
- [[Animated Landing Page Design Showcase]] — Asaad Mahmood - The Small Square (@asaadmahmood5)
- [[Single Animation Elevates Landing Page - @marcelkargul]] — Marcel (@marcelkargul)
- [[Landing Page Design Joy - @galshirart]] — Gal Shir (@galshirart)
- [[Anime.js v4.3 Auto Layout Feature - @juliangarnier]] — Julian Garnier (@juliangarnier)
- [[Micro-interactions on Onboarding Design - @andreamontini]] — Andrea Montini (@andreamontini)
- [[Dark vs Light Mode Comparison - @karaan_dev]] — Karan (@karaan_dev)
- [[Design to Dev in One Week - @dawoodui]] — Dawood (@dawoodui)
- [[Clear Design Removes Explanation Need - @pankajstwt]] — Pankaj (@pankajstwt)
- [[Karpathy Guidelines for Coding Agents - @jiayuan_jy]] — Jiayuan (JY) Zhang (@jiayuan_jy)
- [[Justin Farrugia Maybe Finance Portfolio Work - @justinmfarrugia]] — Justin Farrugia (@justinmfarrugia)
- [[Aceternity Tooltip Card Component - Mouse-Tracking Hover Card]] — Aceternity
- [[Claude Code Custom Keybindings - @bcherny]] — Boris Cherny (@bcherny)
- [[Kimi K2.5 on Ollama Cloud - @ollama]] — ollama (@ollama)
- [[Firecrawl CLI for Agentic Web Access - @firecrawl]] — Firecrawl (@firecrawl)
- [[Remotion Skills Integration Update - @remotion]] — Remotion (@remotion)
- [[Recursive Deep Research Prompt Template - @zxytim]] — Xinyu Zhou (@zxytim)
- [[Design Engineers Are Hot Right Now - @kvncnls]] — Kevin ⨀ (@kvncnls)
- [[Bloom iOS-Style Pull-Down Menu Component - @joshpuckett]] — joshpuckett (@joshpuckett)
- [[Task List Animation Flow - @tanjim38]] — Tanjim | SaaS Product Designer (@tanjim38)
- [[Input Fields That React to Intent - @bossadizenith]] — zenith (@bossadizenith)
- [[antfu/skills - Anthony Fu Agent Skills Collection]] — Anthony Fu (antfu)
- [[detail.design - Thoughtful Design Details Collection - @adhamdannaway]] — Adham Dannaway (@adhamdannaway)
- [[SEO Audit Agent Skill - coreyhaines31]] — coreyhaines31/marketingskills
- [[Interruptible Animation Pattern - detail.design]] — Rene Wang (@renedotwang)
- [[Animated Action Button Pattern - detail.design]] — Rene Wang (@renedotwang)
- [[Morphing Button to Input Pattern - detail.design]] — Rene Wang (@renedotwang) via Nitish Kumar (@nitishkmrk)
- [[Share Modal UI Design]] — Maxim Kuznetsov (@disarto_max)
- [[Beautiful Mermaid Diagram Renderer]] — Balint Orosz (@balintorosz)
- [[Three-Layer Memory System for Clawdbot]] — pixel (@spacepixel)
- [[Anthropic 10-Step Prompt Structure Guide]] — AI Edge (@aiedge_)
- [[React2AWS Infrastructure as React Components]] — kanav (@kanavtwt)
- [[Lovable Chat UI Redesign State Reduction]] — niklas (@nklsmhs)
- [[Remotion Agent Skills HeyGen Integration]] — Remotion (@remotion)
- [[Beautiful Mermaid Agent Skill for SVG-PNG Export]] — Eleanor Berger (@intellectronica)
- [[Login Screen Design for AI Data Tool]] — Andrea Montini (@andreamontini)
- [[Prompt Clarity Article by kloss_xyz]] — am.will (@llmjunky)
- [[FloatPrompt Continuous Compounding Context]] — MDS (@mds)
- [[Claude Code Transcript Context Extraction]] — Zac (@perceptualpeak)
- [[zarazhangrui/frontend-slides - Animation-Rich HTML Presentations Skill]] — zarazhangrui
- [[Supermemory Plugin for Claude Code]] — Dhravya Shah (@dhravyashah)
- [[supermemoryai/claude-supermemory - Persistent Memory Plugin]] — supermemoryai
- [[Your Claude Code is Now Stateful]] — Dhravya Shah (@dhravyashah)
- [[How to Build an Agent That Never Forgets]] — Rohit (@rohit4verse)
- [[Building AI Project Manager with Claude Code]] — Nityesh (@nityeshaga)
- [[Claude Code Playground Plugin for Interactive HTML Playgrounds]] — Thariq (@trq212)
- [[shadcn-builder - No-Code Form Builder for shadcn/ui]] — iduspara
- [[HTML Slides with Interactive Navigation Dots]] — Zara Zhang (@zarazhangrui)
- [[Firecrawl CLI Skill for AI Agent Web Context]] — Sumanth (@sumanth_077)
- [[Kimi 2.5 iOS 26 Glass Effect One-Shot]] — Legendary (@legendaryy)
- [[AGENTS.md Self-Updating Trick]] — Pooya Parsa (@_pi0_)
- [[QMD - On-Device Search Engine for Markdown and Knowledge Bases]] — Tobi Lütke (@tobi)
- [[Claude Code --from-pr Flag for Session Resume]] — Lydia Hallie (@lydiahallie)
- [[Pencil and Paper Design Game Changer]] — Kevin ⨀ (@kvncnls)
- [[AI Agent Three Year Memory System]] — Cathryn (@cathrynlavery)
- [[Reddit JSON API Trick for LLM Data Extraction]] — Ahmad (@theahmadosman)
- [[Mission Control Multi-Agent System Guide]] — Bhanu Teja P (@pbteja1998)
- [[Bun Settings Fix for prefersReducedMotion]] — Daniel San (@dani_avila7)
- [[Tool UI React Framework for Conversation-Native UIs]] — Tw93 (@hitw93)
- [[Claude.md Routing Table Best Practice]] — Alex Hillman (@alexhillman)
- [[Frosted Glass Done Right: iOS vs One UI]] — UI/UX Savior (@uisavior)
- [[Variant UI Import Site Feature for Design Direction]] — Ty Hughey (@tycreated)
- [[Claude Code Orchestration Workflow Tutorial]] — cogsec (@affaanmustafa)
- [[Maestro Automated UI Testing for Twitch]] — Maestro (@maestro__dev)
- [[User Interface Wiki - Growing Collection of UI Patterns and Best Practices]] — Adham Dannaway (@adhamdannaway)
- [[Making Complexity Feel Simple - Motion Design Philosophy]] — litch (@litch_motion)
- [[GSAP WebGL Interactive Web Experience Tutorial on Codrops]] — chakib (@highpfloat)
- [[Why AI/SaaS/Crypto Brands Use Motion Design - You Can't Film a Dashboard]] — Filippo Carnevale (@filippo_mp4)
- [[Ruthless App Requirements Interrogator - Zero Assumptions Prompt]] — klöss (@kloss_xyz)
- [[Kimi K2 Outperforms Gemini 2.5 Flash for Non-Code Applications]] — Theo - t3.gg (@theo)
- [[Agent SEO/AEO Optimization - Making Your Site Agent-Readable]] — Michael (@michael_chomsky)
- [[Improved Agent Experience with llms.txt and Content Negotiation]] — Peri Langlois (@mintlify)
- [[Claude Code Session Sharing Now Available]] — Lydia Hallie (@lydiahallie)
- [[Claude VS Code Extension Browser Connection]] — Thariq (@trq212)
- [[llms.txt for AI-Friendly Sites]] — ty (@tjcages)
- [[AI Product Strategist Prompt Template]] — kloss (@kloss_xyz)
- [[Claude Code /insights Command for Workflow Analysis]] — Thariq (@trq212)
- [[SuperDesign Skill AI Designer for Codebase]] — Shawn Yang (@sanyuan0704)
- [[Claude Code Agent Teams Documentation]] — Anthropic Claude Code Docs
- [[Sandboxes and Snapshots Future Dev Platform]] — can (@can)
- [[Nested CLAUDE.md Context Architecture]] — Raul Junco (@rauljuncov)
- [[Mobile Vibe Coding Setup with tmux and Tailscale - @chongdashu]] — Chong-U (@chongdashu)
- [[Claude Hooks with Game Sound Alerts - @delba_oliveira]] — Delba (@delba_oliveira)
- [[Solo Desktop App Launch - @elithrar]] — Matt Silverlock (@elithrar)
- [[Chief CLI Task Runner for Claude Code - @mathiashansen]] — Mathias Hansen (@mathiashansen)
- [[Agent Role Cards for Scoped Responsibilities - @voxyz_ai]] — Vox (@voxyz_ai)
- [[tmux Mouse Scrolling Fix for Claude Code - @chongdashu]] — Chong-U (@chongdashu)
- [[Destructive Command Guard for AI Agents - @bobjordanjr]] — Bob Jordan (@bobjordanjr)
- [[Handover Command for Session Continuity - @zarazhangrui]] — Zara Zhang (@zarazhangrui)
- [[Recursive Language Models Next Big Thing - @deryatr_]] — Derya Unutmaz, MD (@deryatr_)
- [[jgraph-drawio-mcp - Draw.io MCP Server for AI Diagram Generation]] — jgraph
- [[WebMCP Chrome 146 Early Preview]] — Maximiliano Firtman (@firt)
- [[Claude Code Elegant Redesign Prompt]] — denizen (@dennizor)
- [[Official Excalidraw MCP Launch]] — Excalidraw (@excalidraw)
- [[Claude Code SEO Automation Playbook]] — Cody Schneider (@codyschneiderxx)
- [[Agent-Browser Vercel Sandbox Skill - @ctatedev]] — Chris Tate (@ctatedev)
- [[Portless v0.6 Custom TLDs and Name Flags - @ctatedev]] — Chris Tate (@ctatedev)
- [[OpenRAG - Local RAG Platform]] — @githubprojects
- [[A2UI - Design-to-Code Automation]] — @githubprojects (Google Research)
- [[Vercel Conversation Minimap UI - @raunofreiberg]] — rauno (@raunofreiberg)
- [[JSON-Render with Vercel AI SDK - @ctatedev]] — Chris Tate (@ctatedev)
- [[Agent-Browser DevTools Inspect Command - @ctatedev]] — Chris Tate (@ctatedev)
- [[GitNexus Knowledge Graph for AI Agents]] — Oliver Prompts (@oliviscusai)
- [[OpenViking Context Database for AI Agents]] — Simplifying AI (@simplifyinai)
- [[Pi Agent Review - Minimal Reliable Coding Harness]] — Stefan Streichsbier (@s_streichsbier)
- [[RLM Pi Harness Architecture - Python REPL with Late Interaction Retrieval]] — Isaac Flath (@isaac_flath)
- [[Pi Coding Agent - Minimal Terminal Harness]] — Pi
- [[DAIR.AI Top Papers April 2025 - DeepSeek V4 and Autogenesis]] — DAIR.AI (@dair_ai)
- [[teknium Tweet]] — teknium (@teknium)
- [[hermes-labyrinth - Agent Observability Plugin]] — stainlu
- [[evo v0.3 - Autoresearch Agent Plugin with RLMs]] — Alok Bishoyi (@alokbishoyi97)
- [[AI Engineer GitHub Repos Guide - 10 Essential Repositories]] — そう｜Claude Codeで始めるAI自動化 (@so_ainsight)
- [[LangChain April 2026 Newsletter]] — LangChain Team (@langaboratory)
- [[Hermes Labyrinth - Agent Observability]] — 0xMarioNawfal (@roundtablespace)
- [[Hermes Agent Backup and Transfer]] — Teknium (@teknium)
- [[GPU MODE Kernel Competition Princeton COS 484]] — GPU MODE (@gpu_mode)
- [[Hermes Agent TouchDesigner Creative Coding]] — Nous Research (@nousresearch)
- [[GEPA - Genetic-Pareto Prompt Optimizer]] — Quarq (@quarqlabs)
- [[GEPA Research GitHub Repository]] — Cyrus (@cyrusnewday)
- [[Mismanaged Geniuses Hypothesis and GEPA Loops]] — spacy (@dosco)
- [[Hermes Agent - 15 Features You've Never Touched]] — Sharbel (@sharbel)
- [[The Harness Is the Backend]] — Mike Piccolo (@mfpiccolo)
- [[OpenAI Practical Agent Building Guide]] — Cameron R. Wolfe, Ph.D. (@cwolferesearch)
- [[Symphony Agent Supervision Limit]] — Alex Kotliarskyi (@alex_frantic)
- [[How AI Actually Remembers - KV Cache Guide]] — Siddharth (@Pseudo_Sid26)
- [[GBNF Grammar for 22x Think Token Reduction]] — nash_su - e/acc (@nash_su)
- [[Symphony Launch Announcement]] — Sherwin Wu (@sherwinwu)
- [[Hermes Creative Suite TouchDesigner Integration]] — Wes Roth (@wesroth)
- [[Compound Engineering v3.3.0 - Intent Verification]] — Trevin Chow (@trevin)
- [[Teknium - Hermes Dashboard Plugins Tutorial]] — Teknium 🪽 (@teknium)
- [[AVB - RLM Applications and Practical Insights]] — AVB (@neural_avb)
- [[Agent Skills Force Good Documentation - @vtrivedy10]] — Viv (@vtrivedy10)
- [[RLM Scaffolding Beats Frontier Models on LongCoT]] — Quarq (@quarqlabs)
- [[AgentOS Now Supports Claude Code, LangGraph, and DSPy]] — Ashpreet Bedi (@ashpreetbedi)
- [[Own Your Agent Harness - Intelligence Stack Control]] — Viv (@vtrivedy10)
- [[HALO - Hierarchical Agent Loop Optimizer]] — Sam Hogan 🇺🇸 (@samhogan)
- [[RLM Meets Autoresearch for Harness Optimization]] — AVB (@neural_avb)
- [[Kimi 2.6 + Opus 4.7 + GPT-5.5 Multi-Model Routing]] — Defileo🔮 (@defileo)
- [[RLM Applied to Video Domain Paper]] — AVB (@neural_avb)
- [[Hermes Curator - Automatic Skill Management]] — Teknium (@@teknium)
- [[MIT AI Textbooks as Claude Project Context]] — Dami-Defi (@@DamiDefi)
- [[DSPy vs Agent Frameworks - RLMs]] — spacy (@dosco)
- [[Continual Training and Targeted Forgetting]] — Viv (@vtrivedy10)
- [[Multi-Tenancy for AI Agents - LangSmith]] — Sydney Runkle (@sydneyrunkle)
- [[Reducing Entropy in Agentic Systems - @xdotli]] — Xiangyi Li (@xdotli)
- [[AX Agent RLM with GEPA Built-In - @dosco]] — spacy (@dosco)
- [[Hermes Architecture Diagram Skill - @mr_r0b0t]] — mr-r0b0t (@mr_r0b0t)
- [[Hermes Kanban Board for Agent Tasks - @realsigridjin]] — Sigrid Jin (@realsigridjin)
- [[Auto-Prompting Loop as LLM Scaling Vector - @dosco]] — spacy (@dosco)
- [[2000 DESIGN.md Files for Agent UI Training - @bbssppllvv]] — Mike Bespalov (@bbssppllvv)
- [[DSPy as Competitive Advantage - @dosco]] — spacy (@dosco)
- [[Anime.js Text Animations - @roundtablespace]] — 0xMarioNawfal (@roundtablespace)
- [[GPT-5.5 Codex Full Application Builder - @intheworldofai]] — WorldofAI (@intheworldofai)
- [[CDP Browser Tracing with Browserbase - @ayi_ainotes]] — AYi (@ayi_ainotes)
- [[Agent Curator Four Loops]] — witcheer ☯︎ (@witcheer)
- [[Hermes Agent Goal Loop with Supervisor Model]] — Teknium 🪽 (@teknium)
- [[evoiz/Agentic-Design-Patterns - Complete AI agent design patterns curriculum]] — Antonio Gulli (@evoiz)
- [[Middleware Customization for Agent Harnesses - @sydneyrunkle]] — Sydney Runkle (@sydneyrunkle)
- [[create_agent - Deep Agents Harness Primitive]] — Viv (@vtrivedy10)
- [[Compound Engineering 3.4.0 - Strategy and Product Pulse]] — Trevin Chow (@trevin)
- [[Deep Agents + Browserbase - Web Browsing Agents]] — Harrison Chase (@hwchase17)
- [[A Primer to Understanding Layouts in NVIDIA CuTe]] — Jino Rohit (@jino_rohit)
- [[The Harness is a Context Manager on Behalf of the Model - @vtrivedy10]] — Viv (@vtrivedy10)
- [[OpenAI Symphony 5x Coding Agent Outcome Setup - @jasonzhou1993]] — Jason Zhou (@jasonzhou1993)
- [[Productive Local AI Environment Setup - @0xsero]] — 0xSero (@0xsero)
- [[Build and Sell AI Automations Full Course - @eng_khairallah1]] — Khairallah AL-Awady (@eng_khairallah1)
- [[Hermes Agent Ecosystem Top 10 Repos - @so_ainsight]] — そう｜Claude Codeで始めるAI自動化 (@so_ainsight)
- [[claude-obsidian - AI-Powered Knowledge Engine]] — Maliha Tasnim (@this_is_tasnim)
- [[Image Generation Prompt for AI Agency Website]] — Leon Lin (@lexnlin)
- [[Image First Code Second Workflow]] — Leon Lin (@lexnlin)
- [[ASCII Magic Explorations]] — Kailash (@kail_designs)
- [[Shadcn UI Kit Animated Illustrations]] — Shadcn UI Kit
- [[Animated Shadcn Components Collection - @tobybelhome]] — Toby (@tobybelhome)
- [[Lumis Premium Modal Design - @tanjim38]] — Tanjim | AI Product Designer (@tanjim38)
- [[Grainient Premium Gradients and Backgrounds]] — Grainient
- [[Hiunicorn Studio Lighter Theme - @basit_designs]] — Basit A. Khan (@basit_designs)
- [[Hands-On Modern RL Tutorial]] — Xiuyu Li (@sheriyuo)
- [[Expandable Menu Interaction with Claude]] — Kailash (@kail_designs)
- [[Claude Design Masterclass for Beginners]] — Corey Ganim (@coreyganim)
- [[getdesign.md - Design System Collection]] — getdesign.md
- [[Petdex - CLI Pixel Pets for Codex]] — 币世王 | 🦅🐬TermMax (@0xkingskuan)
- [[Pixel Art AI Agents VS Code Extension]] — Simplifying AI (@simplifyinai)
- [[Imagegen Frontend Web Skill Update - @lexnlin]] — Leon Lin (@lexnlin)
- [[Hermes Agent Kanban Multi-Agent - @nousresearch]] — Nous Research (@nousresearch)
- [[AI Agent Orchestrator Comparison - @dhruvtwt_]] — Dhruv (@dhruvtwt_)
- [[Flightcn Airport Visualization Extension - @ridemountainpig]] — Yen Cheng Lin ✨ (@ridemountainpig)
- [[Codex Plugin CC Adversarial Review - @nicos_ai]] — Nico (@nicos_ai)
- [[Fleet Agents Multi-Model Support at Scale - @LangChain]] — LangChain (@langchain)
- [[Open Model Mission for Agent Builders - @vtrivedy10]] — Viv (@vtrivedy10)
- [[Tuning Deep Agents for Different Models - @vtrivedy10]] — Viv (@vtrivedy10)
- [[Image-to-Code Feedback Request - @lexnlin]] — Leon Lin (@lexnlin)
- [[Local LLM Web Stack Setup - @theahmadosman]] — Ahmad (@theahmadosman)
- [[Local AI Maxxing with Hermes Agent - @witcheer]] — witcheer (@witcheer)
- [[RLM-FORGE Hermes Hackathon Submission - @jqonly]] — JQ Lee (@jqonly)
- [[Rising Agent Costs and Small Models]] — Viv (@vtrivedy10)
- [[Tanjim Dashboard Design Inspiration]] — 老鬼 (@laogui)
- [[anvie/evonic — Distributed Agent Platform with Safety Layer]] — anvie (github.com)
- [[GPT Image Brand Identity System Prompt]] — ABDULLAH (@itxabdullaa)
- [[langchain-ai/deepagents — Agent Harness with Planning and Filesystem]] — langchain-ai (github.com)
- [[Hermes Agent Multi-Profile Gateway Tip]] — Ivan Fioravanti (@ivanfioravanti)
- [[Japanese Editorial Science Poster Prompt]] — sankalp (@dejavucoder)
- [[LangChain AI - The Agent Engineering Platform]] — LangChain (@langchain-ai)
- [[JSON Visual DNA Prompt Engineering]] — Vigo Zhao (@vigocreativeai)
- [[15 Hidden Hermes Agent Features]] — shmidt (@shmidtqq)
- [[Pixel Manipulation Visual Experiments]] — Sha (@its_sslvr)
- [[Simple UI, Powerful Motion]] — ALX 🇺🇸 (@alxui_ux)
- [[Scanning WebGL Background in Unicorn Studio]] — mitkow1 (@mariuszmitkow)
- [[Local GPU AI Research Setup in 3 Months]] — Michel Laclé (@micheltamanda)
- [[Best Landing Page of the Month]] — 𝙉𝙤𝙖𝙧𝙩𝙚.𝙗𝙩𝙘 | 𝘿𝙞𝙜𝙞𝙩𝙖𝙡 𝘽𝙪𝙞𝙡𝙙𝙚r (@gnf_noarte)
- [[The Anatomy of an Agent Harness]] — Vivek Trivedy (LangChain)
- [[Autodata - Agentic Data Scientist for Training Data]] — DAIR.AI (@dair_ai)
- [[LangSmith Platform - Agent Observability and Deployment]] — LangChain
- [[Model Spec Midtraining MSM - @anthropicai]] — Anthropic (@anthropicai)
- [[Hermes Agent HyperFrames Video Skill]] — Nous Research (@nousresearch)
- [[Hermes HyperFrames Skill Installation]] — Nous Research (@nousresearch)
- [[GPT-2 Image Gen Layout Control Discussion]] — AmirMušić (@amirmushich)
- [[ChatGPT Streetwear Poster Prompt Design]] — 波妞PONYO (@ponyodong)
- [[AI Image Gen Design Trends 2026 Research]] — Alex Zhang (@jojogh_007)
- [[GPT Image Gen Prompts & Pipeline Article]] — AmirMušić (@amirmushich)
- [[Micrographics Design App - Produx Lab]] — Alex Socoloff (@socoloffalex)
- [[50 Major Design Styles Reference Guide]] — Slideland｜スライドランド (@slideland229)
- [[Hermes Agent Plugins Documentation - Pluggable Interfaces]] — Nous Research
- [[Footer Design Showcase]] — Swarnima (@swarnima_otw)
- [[Midjourney V8.1 SREF Codes Gallery - TischEins]] — Tischeins (@tisch_eins)
- [[How to Become an AI Engineer in 2026 - Builder's Roadmap]] — Avid (@Av1dlive)
- [[ChatGPT Brand Identity System Workflow]] — Dheepan Ratnam (@dheepanratnam)
- [[Hermes Agent Cronjobs for Gateway Automation]] — Teknium 🪽 (@teknium)
- [[BYO Sandbox with Deep Agents]] — LangChain (@langchain)
