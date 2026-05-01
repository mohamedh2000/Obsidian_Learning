---
title: "Harness Engineering MOC"
type: moc
date_created: 2026-04-17
aliases: ["harness", "harness curriculum", "harness engineering", "agent harness"]
tags: [moc, learning, harness-curriculum]
topics: [harness-engineering, agent-architecture, skills, prompting, context-engineering]
---

# Harness Engineering MOC

> **The harness is the scaffolding around the model — tools, context shape, memory, subagents, permissions, evals, loops.** When people say "Claude Code is better than web chat" or "Cursor feels different," they usually mean the harness, not the weights. This MOC curates everything in the vault for learning harness engineering, skill design, and better prompting — structured as a reading curriculum.
>
> Inline tag: `#harness-curriculum` — click the tag in Obsidian's tag pane to see every note in the vault marked with this curriculum.

**Parent:** [[Learning MOC]] · **Related:** [[Claude Code & Anthropic]] · [[AI Agents]] · [[Agent Architecture]]

---

## How to use this MOC

- **Each track is ordered beginner → advanced.** Read top-to-bottom within a track.
- **Type badges** show what you're clicking into: `[blog]`, `[paper]`, `[repo]`, `[thread]`, `[course]`, `[pdf]`.
- **If you only have an hour:** Track 1 (Foundations) + one item from Track 2 (Anthropic) + one repo from Track 5.
- **If you want to build your own harness:** Tracks 1 → 2 → 5 → 6 → 4. Skip Track 8 until you have intuition.
- **If you want to write better skills:** Tracks 6 → 2 → 5. Then read the actual skill directories inside [[Hermes Agent]] and [[Learn Claude Code]].

---

## Track 1 — Foundations: *what is a harness?*

Build the mental model first. Read these in order.

| Resource | Type | Hook |
|---|---|---|
| [[Harness engineering is as important as model capability scaling. - @daniel_mac8]] | `[thread]` | Dan McAteer's thesis — the single sentence that started the discourse |
| [[The Harness Is The Product Not The Model - @nyk_builderz]] | `[thread]` | Infra beats model choice — why identical models feel different inside different harnesses |
| [[From Weights to Context to Harness Engineering - @akshay_pachaar]] | `[thread]` | Timeline: fine-tuning → context engineering → harness engineering |
| [[Harness Engineering in AI article - @amitiitbhu]] | `[blog]` | Clean overview article — great second read |
| [[One of the best written articles on Harness out there - @code_newsletter]] | `[blog]` | Code Newsletter's canonical long-form piece |
| [[Harness Design Overcomes Lazy Confused Agents - @Vtrivedy10]] | `[thread]` | Concrete framing: harness fixes model laziness |
| [[Harness, Memory, Context Fragments, & the Bitter Lesson this is - @Vtrivedy10]] | `[thread]` | Bitter-lesson framing — why harness work doesn't compete with scale |
| [[The Harness Is Everything Built By Cursor Claude - @rohit4verse]] | `[thread]` | Compares Cursor, Claude Code, Perplexity harnesses side by side |
| [[What is Agentic Engineering]] | `[thread]` | Simon Willison's working definition |

---

## Track 2 — Anthropic canonical

Read Anthropic's own material. These are the highest-signal starting points.

| Resource                                                                       | Type          | Hook                                                                                      |
| ------------------------------------------------------------------------------ | ------------- | ----------------------------------------------------------------------------------------- |
| [[Harness Design for Long-Running Application Development]]                    | `[blog]`      | **Start here.** Anthropic engineering post — context resets + planner/generator/evaluator |
| [[Scaling Managed Agents Decoupling the brain from the hands - anthropic.com]] | `[blog]`      | Brain vs. hands — Anthropic's managed-agents framing                                      |
| [[Anthropic Multi-Agent Harness Lessons - @wangray]]                           | `[thread]`    | Lessons from the Anthropic multi-agent research harness                                   |
| [[Claude Prompt Engineering Overview]]                                         | `[guide]`     | Official prompt engineering guide                                                         |
| [[Anthropic Prompt Eng Interactive Tutorial]]                                  | `[course]`    | 9-chapter interactive course (33.5K stars) — do the exercises                             |
| [[claude-skills-guide]]                                                        | `[pdf]`       | Anthropic's official PDF on building Claude Code skills                                   |
| [[Lessons Building Claude Code How We Use Skills - @trq212]]                   | `[thread]`    | Thariq: skill categories, composition, and failure modes                                  |
| [[Claude Code Architecture Harness Deep Dive - @rohit4verse]]                  | `[blog]`      | Architecture walk-through of the Claude Code harness                                      |
| [[The Claude Code Harness - Everything you need to know - @neural_avb]]        | `[blog]`      | AVB's tour of every Claude Code harness feature                                           |
| [[Why Claude Code works better than Claude web chat - @rasbt]]                 | `[blog]`      | Sebastian Raschka: what the harness adds on top of the model                              |
| [[What We Can Learn from Claude Code - @yq_acc]]                               | `[thread]`    | Design patterns extracted from Claude Code internals                                      |
| [[Claude Code Overview - DeepWiki]]                                            | `[reference]` | DeepWiki map of Claude Code modules                                                       |
| [[Anatomy of the .claude Folder Guide - @akshay_pachaar]]                      | `[thread]`    | Field guide to every file in `.claude/`                                                   |
| [[How plan mode in Claude Code works - @DharmiKumbhani]]                       | `[thread]`    | Plan mode internals explained                                                             |
| [[Claude Code Session Management and 1M Context - @trq212]]                    | `[thread]`    | How Claude Code manages the 1M window                                                     |
| [[Claude Code 7-layer memory architecture walkthrough - @elliotchen100]]       | `[thread]`    | Seven memory layers inside Claude Code                                                    |
| [[Claude Code three layer compaction MicroCompact - @himanshustwts]]           | `[thread]`    | Three-layer compaction strategy                                                           |
| [[Claude Code isn't magic - @jetbrains]]                                       | `[blog]`      | JetBrains' demystification — how it actually works                                        |
| [[Favorite Hidden Claude Code Features - @bcherny]]                            | `[thread]`    | Boris Cherny on underused Claude Code features                                            |
| [[Claude Courses]]                                                             | `[course]`    | Anthropic's full course catalog                                                           |

---

## Track 3 — LangChain & Harrison Chase

The other canonical source. LangChain has been publishing more harness-adjacent material than anyone else.

| Resource | Type | Hook |
|---|---|---|
| [[Agent Harnesses and Memory Ownership - @hwchase17]] | `[thread]` | Harrison on who owns memory vs. harness |
| [[Deep Agents Deploy Harness Sandbox Memory MCP - @hwchase17]] | `[thread]` | Harrison's five-pillar model of a deep-agent stack |
| [[Deep Agents Open-Source Coding Agent Harness - @hasantoxr]] | `[repo]` | LangGraph-based coding-agent harness |
| [[Open Models, Open Runtime, Open Harness - @hwchase17]] | `[thread]` | The three-layer decomposition: model / runtime / harness |
| [[Multi-Agent Orchestration with deepagents - @Vtrivedy10]] | `[thread]` | Multi-agent orchestration via deepagents |
| [[Harrison pulls on a bunch of interesting threads at the frontier of - @vtrivedy10]] | `[thread]` | Viv's summary of Harrison's frontier posts |
| [[meta harness is a great paper from @yoonholeee that came out earlier... - @hwchase17]] | `[thread]` | Harrison recommending the Meta-Harness paper |
| [[learning at the context layer is basically memory - @hwchase17]] | `[thread]` | Harrison on context-layer learning vs. weight-layer |
| [[Optimize agents with LangSmith - @hwchase17]] | `[blog]` | LangSmith as the eval/optimization harness |
| [[The agent improvement loop starts with a trace - @LangChain]] | `[thread]` | Trace → diagnose → fix — the improvement loop |
| [[Open SWE Internal Coding Agents - @langchain]] | `[blog]` | Patterns from Stripe/Ramp/Coinbase internal coding agents |
| [[Environments in LangSmith Prompt Hub - @LangChain]] | `[blog]` | LangSmith environments feature |
| [[The Agent Evaluation Readiness Checklist - @LangChain]] | `[blog]` | Are you ready to evaluate your agent? |
| [[LangChain Docs]] | `[reference]` | LangChain documentation root |
| [[LangGraph Agentic Company Researcher - @LangChain_OSS]] | `[repo]` | Reference implementation of an agentic researcher |
| [[deepagents Docs Revamp Context Eng Patterns - @Vtrivedy10]] | `[thread]` | deepagents docs revamp preview |

---

## Track 4 — Papers (academic + open research)

The research frontier. Read the Anthropic/LangChain stuff first so you have context for what the papers are responding to.

| Resource | Type | Hook |
|---|---|---|
| [[AutoHarness Improving LLM Agents by Automatically Synthesizing a Code Harness - arxiv.org]] | `[paper]` | Small LLMs synthesize code harnesses to beat larger models |
| [[Meta-Harness Autonomously Optimizes LLM Harnesses - @yoonholeee]] | `[paper]` | Yoonho Lee's Meta-Harness paper — the harness tunes itself |
| [[Meta-Harness Code Release - @yoonholeee]] | `[repo]` | Code release accompanying the Meta-Harness paper |
| [[Meta-Harness Automates Harness Engineering - @LiorOnAI]] | `[thread]` | Lior's breakdown of Meta-Harness |
| [[Meta-harness loops reward hacking on evals - @Vtrivedy10]] | `[thread]` | Critical take: meta-harness loops can reward-hack their evals |
| [[Meta Harnesses is Autoresearch on steroids. - @deedydas]] | `[thread]` | Deedy's reframing of Meta-Harness |
| [[Natural-Language Agent Harnesses Paper Explained - @askalphaxiv]] | `[paper]` | Natural-language harness specification |
| [[AI Runs the Harness Tsinghua Shenzhen Paper - @rronak_]] | `[paper]` | Tsinghua/Shenzhen paper on AI-run harnesses |
| [[Agentic Context Engineering ACE Paper - @pvergadia]] | `[paper]` | ACE — formalizing context engineering |
| [[OpenDev CLI Agent Design Paper - @omarsar0]] | `[paper]` | CLI-agent design paper (OpenDev) |
| [[Releasing auto-harness an open source library for our self improving... - @gauri__gupta]] | `[repo]` | auto-harness library release |
| [[openai-harness-engineering]] | `[blog]` | Making codebases "agent-ready" — OpenAI perspective |
| [[Stanford MIT Meta-Harness beats Claude Code - @omarsar0]] | `[thread]` | Stanford/MIT meta-harness outperforming Claude Code on a benchmark |
| [[Structured Test-Time Scaling - Multi-Agent Systems to General Inference Architectures]] | `[paper]` | From multi-agent systems to inference architectures |
| [[Three-Layer Agent Harness for Product Design - @PrajwalTomar_]] | `[blog]` | Three-layer harness model for product design |
| [[303-Page Field Guide on Code Models and Coding Agents - @mdancho84]] | `[paper]` | Survey of code-model and coding-agent research (50 authors) |
| [[Six patterns across 30+ LLM eval benchmarks - @cwolferesearch]] | `[paper]` | Cameron Wolfe — eval benchmark patterns |

---

## Track 5 — Open-source harnesses to study

Read the code. This is the fastest way to internalize patterns.

| Resource | Type | Hook |
|---|---|---|
| [[Hermes Agent]] | `[repo]` | Nous Research's agent — built for self-evolution |
| [[NousResearch-hermes-agent-self-evolution - Evolutionary self-improvement for Hermes Agent optimize]] | `[repo]` | Hermes self-evolution engine (GEPA) |
| [[Hermes Agent — An Agent That Grows With You - hermes-agent.nousresearch.com]] | `[blog]` | Nous Research's pitch for Hermes |
| [[Best open source repos Paperclip Mirofish Hermes Openclaw - @0xsachi]] | `[thread]` | Curated list: Paperclip, Mirofish, Hermes, Openclaw |
| [[langchain-ai-deepagents - Agent harness with planning and filesystem]] | `[repo]` | Reference deep-agent harness |
| [[Learn Claude Code]] | `[repo]` | `shareAI-lab/learn-claude-code` — annotated Claude Code |
| [[kevinrgu-autoagent - autonomous harness engineering]] | `[repo]` | AutoAgent — autonomous harness |
| [[jhochenbaum-pi-autoresearch-studio - Autoresearch dashboard and PR workflow]] | `[repo]` | Autoresearch Studio + PR workflow dashboard |
| [[PrimeIntellect-ai-prime-rl - Agentic RL training at scale]] | `[repo]` | Prime-RL — agentic RL at scale |
| [[walkinglabs-awesome-harness-engineering - Awesome harness engineering list]] | `[repo]` | Awesome-list: every harness-engineering resource worth knowing |
| [[🚀 Just open-sourced Harness Engineering Book — a deep-dive into... - @blackanger]] | `[repo]` | Blackanger's open-sourced harness engineering book |
| [[Paperclip CLI for Scientific Literature - gxl.ai]] | `[repo]` | Paperclip harness for science literature |
| [[ComposioHQ-agent-orchestrator - Agentic orchestrator for parallel coding agents — plans]] | `[repo]` | Composio's parallel coding-agent orchestrator |
| [[Open-SWE Open Source Coding Agent - @sitinme]] | `[repo]` | Open-SWE — open-source coding agent |
| [[Cmux Open Source Agent Terminal]] | `[repo]` | Open-source agent terminal |
| [[MiniMax Skills]] | `[repo]` | MiniMax's open-source skill library |

---

## Track 6 — Skills & prompting

How to write skills and prompts that compose into a harness.

| Resource | Type | Hook |
|---|---|---|
| [[claude-skills-guide]] | `[pdf]` | Official Anthropic skill-building guide (repeated from Track 2 — essential) |
| [[Lessons Building Claude Code How We Use Skills - @trq212]] | `[thread]` | Thariq on skill categories and composition |
| [[Claude Code Skills Workflow - @polydao]] | `[thread]` | End-to-end skills workflow |
| [[Skills Are Executable Systems - @sitinme]] | `[thread]` | Skills as executable systems with scripts, memory, triggers |
| [[Anthropic Skill Creator Evaluation Update]] | `[announcement]` | Skill-creator evaluation update |
| [[Skill Creator Test Generation Update]] | `[announcement]` | Auto-test-generation for skills |
| [[Autoresearch-Inspired Skill Self-Improvement - @Hesamation]] | `[thread]` | Skills iterate against an eval suite |
| [[Self Improving Skills for Agents - @tricalt]] | `[thread]` | Self-improving-skills patterns (3.4K likes) |
| [[EvoSkill proposer and skill builder iterative loop - @oleg_golev]] | `[thread]` | Proposer + builder iterative skill loop |
| [[SKILLRL New Learning Paradigm for Agents - @_avichawla]] | `[thread]` | Agents distill experience into reusable skills |
| [[Cognee Self-Healing AI Skills - iruletheworldmo]] | `[thread]` | Self-correcting skills at runtime |
| [[How to 10x Your Claude Skills - @itsolelehmann]] | `[thread]` | Practical 10x tips |
| [[Matt Pocock Skills]] | `[repo]` | Matt Pocock's skill pack — TDD/PRD/architecture |
| [[Impeccable Style]] | `[repo]` | 20+ design commands for AI coding assistants |
| [[Introducing the Manim skill for Hermes Agent. - @NousResearch]] | `[thread]` | Manim skill for Hermes — reference implementation |
| [[Imo a good manim harness needs several things 1 - @neural_avb]] | `[thread]` | AVB on what a manim harness needs |
| [[Skill chaining and skills should be actions - @realmcore_]] | `[thread]` | Skills as chainable actions |
| [[Massive Skill Speedup vs Recommended Setups - @MeganTStevenson]] | `[thread]` | Benchmark: skill packs vs. recommended setups |
| [[ClaudeKit Spec Driven Workflow - @dani_avila7]] | `[thread]` | Spec-driven skill workflow |
| [[Why AGENTS.md Can Hurt Coding Agents - @shao__meng]] | `[thread]` | Counter-take on AGENTS.md files |
| [[Train Skills From Agent Execution History - @koylanai]] | `[thread]` | Bootstrap skills from execution traces |
| [[TDD for Documentation Skills - @seekjourney]] | `[thread]` | TDD applied to documentation skills |
| [[OpenAI Prompt Engineering Guide]] | `[guide]` | Identity → Instructions → Examples → Context |
| [[Best Practices for Prompt Engineering with the OpenAI API]] | `[guide]` | OpenAI's official help-center guide |
| [[Skeleton of Thought Beats CoT - @ihtesham2005]] | `[paper]` | Parallel decoding — 2.39x speedup vs. CoT |
| [[Prompt Caching in LLMs Clearly Explained - @_avichawla]] | `[thread]` | Prompt caching mechanics |
| [[ai-prompt-masterclass]] | `[reference]` | Curated prompt masterclass |

---

## Track 7 — Memory & context engineering (the other half of the harness)

A harness without good memory/context shape is a chat window. These explain the other half.

| Resource | Type | Hook |
|---|---|---|
| [[Harness Memory and Context Must-Read - @morganlinton]] | `[thread]` | "Must-read" summary on harness + memory + context |
| [[Memory Is Markdown and the Harness Should Stay Thin - @av1dlive]] | `[thread]` | Keep memory readable; keep harness thin |
| [[AI Memory Tools Split Into Backends vs Context Substrates - @witcheer]] | `[thread]` | Backends vs. substrates — the key distinction |
| [[Context Engineering for AI - @witcheer]] | `[thread]` | Context config beats prompt refinement |
| [[Context Engineering Checklist for AI Coding - @kmeanskaran]] | `[thread]` | Checklist you can apply today |
| [[Agent Memory Building Memory-Aware Agents - @AndrewYNg]] | `[course]` | Andrew Ng's memory-aware agents course |
| [[Seven Agent Memory Architectures - @TheTuringPost]] | `[thread]` | 7 memory patterns surveyed (AgeMem, Memex, MemRL, UMA, Pancake) |
| [[Hermes Agent Four-Layer Memory System - @shao__meng]] | `[thread]` | Hermes' 4-layer memory design |
| [[Claude Obsidian Memory Stack Compounds - @nyk_builderz]] | `[thread]` | Three-tier memory stack using Claude + Obsidian |
| [[How Memory Works In HyperAgents - @mem0ai]] | `[thread]` | mem0 team on HyperAgent memory |
| [[Deep Agent To Production Memory Guardrails Durability - @sydneyrunkle]] | `[thread]` | Memory guardrails for production deep-agents |
| [[Context Graphs Beyond Chat Memory - @kirkmarple]] | `[thread]` | Context graphs — beyond chat history |
| [[Context Hub Curated API Docs for Agents - @slash1sol]] | `[thread]` | Curated API docs hub for agents |
| [[Why File-Based AI Memory Beats Black-Box Vectors - @Atenov_D]] | `[thread]` | Folder-based memory > opaque vector memory |
| [[Best RAG Engineers Model Information Topology - @ihtesham2005]] | `[thread]` | Production RAG models information topology |

---

## Track 8 — X/Twitter threads (high-signal short reads)

Short-form takes worth a scroll-through. Ordered roughly by signal.

| Resource | Hook |
|---|---|
| [[harness eng day 5 toolsets - @sydneyrunkle]] | Sydney Runkle's harness-eng series day 5 — toolsets |
| [[cool harness hook that wraps every bash call and does tons of output filtering -]] | Concrete: wrap bash calls with output filtering |
| [[here’s a good application of harness permissions - @vtrivedy10]] | Practical use of harness permissions |
| [[Harness Engineering Derived from what Models can’t do alone It - @Vtrivedy10]] | Harness as "what the model can't do alone" |
| [[Domain-Specific Models and Harnesses Win - @Vtrivedy10]] | Case for domain-specific harnesses |
| [[Jensen Pushing Open Models And Harness Toolkits - @Vtrivedy10]] | Jensen on open models + harness toolkits |
| [[Open everything 🔥 Open Harness, Model Choice, Open Memory (take it wherever you - @Vtrivedy10]] | "Open everything" framing |
| [[How To Be A World-Class Agentic Engineer - @systematicls]] | Checklist for being a top-tier agentic engineer |
| [[Karpathy's 10 Actionable Insights for Working with AI Agents - @daniel_mac8]] | 10 actionable insights from Karpathy's recent work |
| [[most agent failures aren't model failures - @ptkbhv]] | Thesis: failures trace to harness, not weights |
| [[Two major shifts will be seen in Agentic AI after Harness and YOU - @kmeanskaran]] | Two shifts coming after harness engineering matures |
| [[Agreement Is a Bug - 11 Claude Code Agents Disagree - @nyk_builderz]] | Multi-agent dissent as a decision pattern |
| [[Single-Agent AI Coding Ceiling and Multi-Agent Workflows - @MilksandMatcha]] | Why single-agent ceilings exist |
| [[Claude Subagents vs Agent Teams - @akshay_pachaar]] | Subagents vs. agent teams — which when |
| [[agents out there are struggling with these naive and brittle - @dosco]] | Brittleness in naive agents |
| [[Control Planes Keep Agents Out of Incident Review - @nyk_builderz]] | Control plane: policy, approvals, audit |
| [[Karpathy's Confusion Protocol in GStack - @garrytan]] | Karpathy's confusion-protocol pattern |
| [[Claude Scientific Method for Debugging - @KingBootoshi]] | Scientific-method debugging pattern |
| [[Claude Workflow Efficiency Audit Prompt]] | Prompt that audits your workflow |

---

## Track 9 — Advanced: meta-harness, self-improving agents

Only after you understand the basics. These assume you know what a harness *is*.

| Resource | Type | Hook |
|---|---|---|
| [[HyperAgents Recursive Self-Improvement - @daniel_mac8]] | `[thread]` | Recursive self-improvement in HyperAgents |
| [[HyperAgents Self-Improvement Generalizes - @fancylancer3991]] | `[thread]` | Evidence the approach generalizes |
| [[Hyperagents and Metacognitive Self-Modification - @jennyzhangzt]] | `[thread]` | Metacognitive self-modification |
| [[AI That Evolves Its Own Evolution]] | `[blog]` | Agents that evolve their evolution process |
| [[A-Evolve PyTorch Moment For Self-Evolving AI - @HenryL_AI]] | `[thread]` | "PyTorch moment" claim for self-evolving AI |
| [[Introducing TRACE an end-to-end system for environment-specific agent self-impro - @hangoo_kang]] | `[paper]` | TRACE — environment-specific self-improvement |
| [[Auto-Research Agent Memory Framework - @kingbootoshi]] | `[thread]` | Memory framework for autoresearch agents |
| [[AutoResearch in Claude Code Magic - @andrewjiang]] | `[thread]` | Autoresearch flow inside Claude Code |
| [[OpenSpace Agent Self-Evolution and Shared Skills - @axiaisacat]] | `[thread]` | Shared-skills self-evolution |
| [[Coding Agent Harness at Scale - @juliandeangeiis]] | `[thread]` | Running coding-agent harnesses at scale |
| [[Always-on agents that monitor detect and deploy fixes - @Vtrivedy10]] | `[thread]` | Always-on monitoring agents |

---

## Bonus — Ecosystem context

Not strictly harness engineering but directly adjacent — helpful for a complete mental model.

- [[LLM Knowledge Bases - @karpathy]] — Karpathy on knowledge bases for LLMs
- [[Agent Architecture]] — multi-agent system patterns (MOC)
- [[Eval Skills for AI Coding Agents]] — Hamel's eval-skills repo
- [[Evals First for Coding Agents - @synopsi]] — why evals come before features
- [[Factory AI Agent Readiness Links Roundup - @alvinsng]] — readiness / missions / compression
- [[Introducing Agent Readiness]] — measuring agent-readiness of a repo
- [[Using Linters to Direct Agents]] — lint rules as executable constraints
- [[Library for Inspecting and Debugging Claude Code - @NeelNanda5]] — inspect Claude Code's API calls
- [[Trust Claude Using Karpathys LLM Council Method - @itsolelehmann]] — LLM Council as a harness pattern

---

## Suggested 2-week reading plan

**Week 1 — intuition**
- Day 1: Track 1 (all 9 items, ~30 min)
- Day 2–3: Track 2 items 1–5 (core Anthropic posts + Prompt Eng Tutorial chapter 1)
- Day 4–5: Track 3 items 1–5 (Harrison's framing)
- Day 6: Track 6 items 1–4 (start building your own skill)
- Day 7: Pick one repo from Track 5, read for an hour

**Week 2 — depth**
- Day 8–9: Tracks 4 items 1–4 (AutoHarness + Meta-Harness papers)
- Day 10: Track 7 items 1–6 (memory & context)
- Day 11: Track 8 (scroll through threads, star favorites)
- Day 12–13: Build a toy harness — one tool, one skill, one eval
- Day 14: Re-read Track 1 and Track 2 item 1 — notice how much more now clicks

---

## Stats

- **Tracks:** 9 + bonus
- **Curated items:** ~130
- **Created:** 2026-04-17
- **Tag:** `#harness-curriculum`
- **Parent:** [[Learning MOC]]

## Maintenance notes

- When a new harness-related note is added to the vault, add it here under the correct track and add a `#harness-curriculum` inline tag to the note itself (optional but recommended).
- If a track grows past ~25 items, split it into sub-tracks (e.g., "Anthropic — blogs" and "Anthropic — talks").
- Dead wikilinks (red in Obsidian) usually mean a filename was renamed — check the Learning MOC or use Obsidian's search for the closest match.
