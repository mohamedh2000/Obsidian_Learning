---
author: "Rijndael (@rot13maxi)"
date: 2026-03-14
source: https://x.com/rot13maxi/status/2032794746918252677
tags:
  - tla-plus
  - formal-verification
  - model-checking
  - state-machines
type: tweet
---

# TLA+ State Machines and Model Checking

TLA+ functions as a state machine where "variables" and "actions that update those variables" form the basis. A key feature allows nondeterministic next states — the next action could be any of several things. The TLA model checker explores valid states by branching at each nondeterministic choice point and verifies invariants and temporal constraints.

State spaces can easily become too large for the model checker to walk through exhaustively. Three solutions: avoid creating oversized state spaces, employ sampling instead of exhaustive checking, or utilize SAT solvers for large state spaces.

## Connections

- Formal verification parallels the [[Autoresearch]] approach — both exhaustively explore state/experiment spaces
- SAT solver scaling relates to the systems bottleneck discussed in [[Slate Agent Architecture and Context Management - cedric_chee]]
- The [[Reinforcement Learning with NVIDIA - Unsloth AI]] note covers another approach to exploring large search spaces via RL

---
[Original Tweet](https://x.com/rot13maxi/status/2032794746918252677)
