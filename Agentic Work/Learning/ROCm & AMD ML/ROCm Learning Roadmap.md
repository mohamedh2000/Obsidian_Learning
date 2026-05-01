---
title: "ROCm Learning Roadmap"
type: roadmap
date_created: 2026-04-17
topics: [rocm, amd-gpu, ml-training, fine-tuning, transformers, pytorch]
tags: [roadmap, learning, ml-ml, training, hardware]
status: in-progress
hardware: "AMD Radeon AI PRO R9700 (Navi 48, gfx1201, 32 GB VRAM)"
os: "Ubuntu 26.04 (Resolute Raccoon, dev branch)"
---

# ROCm Learning Roadmap

> 4–5 month ramp from **no ML** to **fine-tuning a 7B+ open model on an AMD Radeon AI PRO R9700**, with upstream community contribution as a byproduct.

**Parent:** [[Learning MOC]]
**Related topics:** [[Fine-tuning & Training]] | [[LLM Research]]

---

## Context

This box was bought specifically to learn low-level ML training and ROCm on AMD, and to find a niche in the AMD ML community by running into real bugs and fixing/forking as needed.

**Current state (2026-04-17):**
- GPU: **AMD Radeon AI PRO R9700** — Navi 48, RDNA 4, `gfx1201`, 32 GB VRAM. Brand-new silicon; still thin support surface across libraries. Excellent leverage for community contribution.
- OS: **Ubuntu 26.04 "Resolute Raccoon" (dev branch, non-LTS)**, kernel 7.0.0. AMD's official ROCm apt repos target LTS — this is an install-time complication.
- Memory / disk / cores: 29 GiB RAM, 1.7 TB free, 12 cores.
- Python 3.14.4, `uv`, Docker installed. No ROCm yet. Clean slate.

**Choices that shaped this roadmap:**
- **Starting point:** strong coding, weak Python, no ML → needs a compact Python/ML on-ramp before heavy GPU work.
- **Goal:** research-direction — train and fine-tune open models on AMD. Community contribution is a byproduct of hitting real bugs along the way.
- **Install path:** containers-first (official `rocm/pytorch` images) → keeps the host clean, sidesteps the 26.04 packaging issue, industry-standard workflow.

**End-state in ~4–5 months:**
1. Real mental model of how GPUs train transformers.
2. Fine-tuned a ≥7B open model on the R9700.
3. A handful of legitimate upstream issues/PRs against ROCm or PyTorch/HF ecosystem.
4. Public notes repo worth something to the community.

---

## Guiding principles

1. **Containers for everything.** Never install ROCm libs bare-metal on 26.04 until much later. One host-side piece (the kernel driver); everything else lives in a container.
2. **Write as you go.** Keep a `notes/` repo (public GitHub) from day one: install logs, commands that worked, commands that didn't, version matrices.
3. **Every error is a candidate ticket.** Before you "just Google it", spend 10 min reproducing it minimally. If you can repro on `rocm/pytorch:latest` with a 15-line script, that's a bug report.
4. **Measure everything.** `rocm-smi`, `rocprof`, PyTorch profiler. You can't contribute to performance discussions without numbers.
5. **Default to reading real code.** PyTorch, HuggingFace Transformers, TRL, vLLM sources are how you actually understand the stack. Clone repos locally; grep aggressively.

---

## Phase 0 — Bring ROCm up, prove the GPU works (2–4 evenings)

**Goal:** "I can run a PyTorch tensor op on my R9700 from inside a container."

**Steps:**
1. Confirm GPU groups: add user to `video` and `render` groups. Log out / back in.
2. Install the **AMDGPU kernel driver only** (`amdgpu-dkms`) on the host. This is the one host-side piece. Everything else (ROCm userspace, HIP runtime, PyTorch) stays in the container. On 26.04 this may need the 24.04 repo — document exactly what you did.
3. Pull `rocm/pytorch:latest` (or the specific tagged ROCm 7.x + PyTorch image AMD publishes).
4. Run container with `--device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 16G`.
5. Inside: `rocm-smi` should list the R9700. `python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"` should return `True` and the device name (note: PyTorch ROCm still uses the `cuda` namespace — correct, not a typo).
6. Run a toy matmul on `cuda:0` and print `.device`.

**Verification:** both `rocm-smi` and `torch.cuda.is_available()` return successfully inside the container. Save the exact `docker run` command to `notes/run-rocm.sh`.

**Community hook:** Document any friction on 26.04 in `notes/rocm-on-ubuntu-26.04.md`. First public write-up.

---

## Phase 1 — Python on-ramp for someone who already codes (5–10 days)

**Goal:** idiomatic Python/NumPy without friction.

Skip beginner syntax tutorials. Focus on what's different:

- **Python-specific idioms:** list/dict/generator comprehensions, `itertools`, `dataclasses`, context managers, `*args/**kwargs`, type hints (`typing`, `TypedDict`, `Protocol`), packages, `with`, decorators.
- **Environment management:** `uv` is already installed — learn `uv venv`, `uv pip`, `uv run`, `pyproject.toml`. This replaces pip+venv+pyenv. Don't touch conda.
- **NumPy:** arrays vs lists, dtypes, broadcasting rules, axis semantics, `einsum`, `np.newaxis`, vectorization vs loops (10–100× differences).
- **Jupyter:** `uv run jupyter lab`, or VS Code notebook support.

**Exercises (~5, pure NumPy, no sklearn):**
1. Linear regression (closed form, then gradient descent).
2. k-means.
3. k-NN.
4. Naive Bayes on a tiny text dataset.
5. A 2-layer MLP with manual backprop on MNIST-ish data.

**Verification:** write a 50–100 line NumPy script without reaching for docs every 5 minutes. The MLP trains to ≥95% on a small MNIST-like set.

**Resource:** skim *Python for Data Analysis* (Wes McKinney) chapters 2–4 — reference, not cover-to-cover.

---

## Phase 2 — ML from scratch (3–4 weeks) — the Karpathy track

The canonical zero-to-hero path. Not filler; it's how you build real intuition for everything that comes after.

Work through Andrej Karpathy's **Neural Networks: Zero to Hero** (YouTube + `karpathy/nn-zero-to-hero`, free):

1. **micrograd** — from-scratch autograd engine in ~100 lines. You implement backprop yourself. The single most important week of the whole plan.
2. **makemore** (4 videos) — character-level LM, bigram → MLP → RNN → small transformer. By the end you've coded every layer of a transformer from primitives.
3. **nanoGPT** — train a tiny GPT (≤20M params) on the R9700 end-to-end. First real ROCm training run. Watch `rocm-smi` in another terminal while it runs.
4. **GPT tokenizer** video — understand BPE before touching HuggingFace.

As you work: clone `karpathy/nanoGPT`, `karpathy/makemore`. Train nanoGPT on TinyShakespeare on the GPU. Then a slightly bigger dataset (TinyStories, OpenWebText subset).

**Verification:**
- Trained a transformer from scratch on the R9700.
- Can draw the forward and backward pass of a single attention head on paper without looking it up.
- `notes/first-training-run.md` with nanoGPT loss curves, tokens/sec, peak VRAM, and any ROCm weirdness.

**First real community output:** a blog post or GitHub README: *"Training nanoGPT on an AMD Radeon AI PRO R9700"* — numbers, install steps, gotchas. The first time "gfx1201" shows up in a public training log is valuable.

---

## Phase 3 — Real PyTorch, real profiling (2–3 weeks)

**Goal:** comfort with the full PyTorch stack and with measuring what the GPU is actually doing.

- **PyTorch core:** `nn.Module`, `autograd`, `Optimizer`, `DataLoader`, `Dataset`, `torch.save`/`torch.load`, mixed-precision (`torch.amp`), `torch.compile` (ROCm support is live but uneven on gfx1201 — contribution territory).
- **Numerics on your GPU:** benchmark `fp32` vs `fp16` vs `bf16` matmuls on the R9700. `bf16` is the right default for training on RDNA 4.
- **Profiling:**
    - `rocm-smi` in a loop — basic utilization and temp.
    - `torch.profiler` — layer-level timing, memory.
    - `rocprofv2` / `rocprofv3` — kernel-level, flame graphs.
- **Memory:** understand what's using VRAM (weights, activations, gradients, optimizer state). Do the math for a 7B model in bf16 with Adam.

**Exercises:**
- Take nanoGPT from Phase 2 and profile it. Find the slowest kernel. Find where memory peaks. Write it up.
- Intentionally OOM the GPU, then fix it with gradient checkpointing.
- Compare `torch.compile()` on vs off — note any compile errors (likely file-worthy).

**Verification:** can read a `torch.profiler` trace and point at the slowest op. Knows (within 10%) how much VRAM a given model+batch will use before running it.

---

## Phase 4 — Fine-tune a real open model on the R9700 (4–6 weeks)

**The milestone that justifies the box.** 32 GB VRAM is the sweet spot for this.

- **Stack:** HuggingFace `transformers`, `datasets`, `accelerate`, `peft` (LoRA/QLoRA), `trl` (SFT/DPO). All run on ROCm via the PyTorch image. `bitsandbytes` has an AMD fork — test it, file issues against it.
- **Model targets (in order):**
    1. GPT-2 (small) — sanity check the pipeline.
    2. **Llama-3.2-3B** or **Qwen2.5-3B** — full fine-tune in bf16.
    3. **Llama-3.1-8B** or **Qwen2.5-7B** — LoRA SFT in bf16. Fits comfortably in 32 GB.
    4. **Llama-3.1-13B** or similar — QLoRA (4-bit). Genuinely useful territory.
- **Datasets:** start small and clean (Dolly, OpenAssistant subset, Alpaca, or a domain set you care about). Learn tokenization, chat-template formatting, train/val split.
- **Training recipe:** SFT with TRL. Learn `SFTTrainer`, `DataCollatorForLanguageModeling`, gradient accumulation, LR schedules, LoRA rank/alpha tuning.
- **Evaluation:** run `lm-evaluation-harness` on the fine-tune. Compare to base. Note how that harness behaves on ROCm — exceptions are ticket-worthy.
- **Save + share:** push the adapter to HuggingFace Hub. Now anyone can use it.

**Community output in this phase:**
- A reproducible fine-tuning notebook for the R9700 / gfx1201, pinned to exact image and library versions.
- One or more real issues/PRs against: ROCm itself, PyTorch ROCm backend, `bitsandbytes` AMD fork, `xformers`, `flash-attention` ROCm fork, `trl`, `transformers`, or `accelerate`.

**Verification:** a fine-tuned model on HF Hub trained 100% on the R9700, with a README documenting data, hyperparameters, hardware, training time, cost (electricity + time), and at least one gfx1201-specific gotcha.

---

## Phase 5 — Deeper systems + ongoing contribution (ongoing, months)

By now you're a legitimate AMD-ML-on-RDNA 4 practitioner. Where to go deep:

- **Attention kernels:** Flash Attention has a ROCm port (`ROCm/flash-attention`). Read the Triton kernels. Benchmark against PyTorch SDPA fallback on gfx1201. Kernel authorship is the highest-leverage community contribution.
- **Triton on ROCm:** AMD is investing heavily here. Write a fused kernel (e.g., layernorm + residual). Compare performance to PyTorch.
- **Quantization:** AWQ, GPTQ, bitsandbytes 4-bit — varying AMD support. Map what works on gfx1201 and what doesn't. The mapping itself is publishable.
- **Serving:** `vLLM` has a ROCm branch (`ROCm/vllm` or upstream `--device=rocm`). Serve the fine-tune. Benchmark throughput vs `transformers` vanilla.
- **Multi-model / distributed:** only one GPU, but learn `FSDP` / `DeepSpeed ZeRO` on a single device — still matters, and is how you'd scale if you ever rent 8×MI300X. DeepSpeed's AMD support is good; FSDP works on ROCm but edges are rough.
- **Read PyTorch source:** specifically the HIP backend in `aten/src/ATen/native/hip/` and the ROCm-specific code paths. How you make the jump from "user" to "contributor".

**Sustained output cadence:**
- Every 1–2 weeks: a notes-repo commit or short blog post.
- Every month: aim for 1 meaningful upstream issue or PR.
- Every 2–3 months: a deeper write-up (benchmark post, "state of ROCm for fine-tuning", a reproducible training recipe).

---

## Ongoing habits (from day 1)

- Keep `notes/` public on GitHub. Commit early and often. Messy is fine.
- On any error: produce a **minimal repro** before asking about it. Most errors in this ecosystem are worth a bug report if they survive minimization.
- Follow the AMD ROCm GitHub orgs, `pytorch/pytorch` issues tagged `module: rocm`, and a handful of people doing this work publicly. Reply to issues you can reproduce — low-effort community currency.
- Pin every environment. A reproducible `Dockerfile` + `uv.lock` / `requirements.txt` per experiment.

---

## Resources

**Essential:**
- Karpathy "Neural Networks: Zero to Hero" — YouTube + `karpathy/nn-zero-to-hero`. **Core of Phase 2.**
- PyTorch ROCm install docs — `pytorch.org/get-started/locally/` (select ROCm).
- AMD ROCm docs — `rocm.docs.amd.com`.
- HuggingFace "NLP Course" and "Transformers Docs" for Phase 4.

**Reference:**
- *Deep Learning* (Goodfellow/Bengio/Courville) — pick chapters as needed.
- *The Annotated Transformer* (Harvard) — read alongside Karpathy's attention lectures.
- Umar Jamil's YouTube (transformer/LLM implementations from scratch).

**Ecosystem:**
- `ROCm/pytorch`, `ROCm/flash-attention`, `ROCm/vllm` — the AMD forks you'll live in.
- `pytorch/pytorch` issues filtered `module: rocm`.
- AMD Infinity Hub, `rocm/pytorch` Docker Hub.

**Related notes in this vault:**
- [[AI Engineer Roadmap Free Resources - @heynavtoor]] — a broader 6-month AI engineer path, complements this AMD-specific track.
- [[How to Become AI Engineer in 6 Months - @deronin_]] — parallel roadmap perspective.
- [[What Every Developer Should Know About GPU Computing]] — GPU fundamentals primer.
- [[From SIMT to Systolic GPU and TPU Architecture - @MainzOnX]] — hardware context.
- [[Day 82/365 of GPU Programming]] and [[Day 91/365 of GPU Programming]] — example community learn-in-public rhythm.

---

## Progress log

Keep a running log here as phases complete. Each entry: date, phase, what shipped, what broke, what's public.

| Date | Phase | Shipped | Blocked | Public artifact |
|------|-------|---------|---------|-----------------|
| _pending_ | 0 | _Docker + amdgpu-dkms + rocm/pytorch image_ | | |

---

## Verification plan

By end of ~4–5 months, should be able to demonstrate all five:

1. `docker run ... rocm/pytorch` → PyTorch sees the R9700; can demo in under a minute.
2. A local clone of nanoGPT trained on the R9700, with notes on tokens/sec and VRAM usage.
3. A HuggingFace Hub repo with a LoRA adapter fine-tuned on the R9700, plus a README that reproduces the training.
4. A public `notes/` repo with install guides, gotchas, and benchmarks.
5. At least one merged or seriously-engaged-with upstream issue/PR against ROCm or a PyTorch-ecosystem project, cited with the hardware.

If all 5 are true: goal achieved.
