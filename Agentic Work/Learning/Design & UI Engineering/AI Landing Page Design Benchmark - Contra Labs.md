---
title: "Sol Has Taste, Fable Takes Direction — AI Landing Page Benchmark"
url: "https://contralabs.com/research/landing-page-h2h-jul26"
platform: web
date_saved: 2026-07-17
source: "Contra Labs (Creative Arena)"
content_type: guide
topics: [Design Evaluation, AI Web Design, LLM Benchmarks]
tags: [design-eval, benchmark, llm-comparison, landing-pages, contra-labs, elo]
status: unread
---

# Sol Has Taste, Fable Takes Direction — AI Landing Page Benchmark

> Contra Labs put GPT 5.6 Sol, Claude Fable 5, Grok 4.5, and Muse Spark 1.1 against the same ten landing-page briefs, judged blind by 9 working designers. There is no single winner — the brief's specificity decides which model wins.

**Topics:** [[Design Evaluation]], [[AI Web Design]], [[LLM Benchmarks]]

| | |
|---|---|
| **Source** | Contra Labs (Creative Arena) |
| **Saved** | 2026-07-17 |
| **Type** | Research benchmark |
| **Method** | Blind pairwise preference + client-readiness vote; Bradley-Terry Elo anchored at 1500 |
| **Sample** | 10 briefs · 540 pairwise matchups · 360 written assessments · 9 working designers |
| **URL** | [Link](https://contralabs.com/research/landing-page-h2h-jul26) |

## Key Points

- **The spec decides the winner.** Overall, Sol won 63.3% of matchups — but split by brief type the ranking inverts. On loose briefs Sol scored 1703 Elo; on structured briefs it dropped to 1455, *last* in the field, behind Fable at 1569.
- **Sol owns loose briefs.** It took first on all four loose briefs (Bramble 93%, Groundwork 81%, Rue Mistral 78%, Tidewater 78%) and beat each rival ~81–83%. 61% of its loose pages were client-ready vs 31% for the rest of the field combined.
- **A spec more than doubles what Fable can ship.** Given a specification, Fable's client-ready rate jumped 31% → 72%; on structured briefs it beat Sol 64%, Grok 61%, Muse Spark 64%. Its Switchboard page was the only one of forty that all nine designers would present to a client.
- **Sol is spec-invariant, Fable is spec-dependent.** Sol holds 61% client-ready on *both* brief types — it wins loose briefs because the field gets worse, not because Sol gets better. Fable plays safe on a mood ("boring") and excels on a spec.
- **All four write better than they design.** Copywriting was the most-praised dimension across every model; visual execution was the most-criticized. Grok is "competent and forgettable"; Muse Spark follows the plan but "cannot compose the page."
- **Each model fails its own way.** Sol over-scales (96px hero headline vs Fable's 56px) and fills unspecified gaps with its own opinion; Fable lacks nerve without direction; shared AI tells — em dashes, letter-spaced all-caps eyebrows, placeholder imagery.

## The Takeaway

There is no best model — only how much you've already decided. As raw capability converges, what separates good from bad output keeps moving away from the model and toward the brief. A spec with a hole in it is a spec the model will finish for you, and you won't learn which way it went until a designer tells you. Briefing well now means knowing *which* model you're talking to.

## Methodology & Limitations

- 9 working UI/UX designers from Contra's network; 10 invented (un-trainable) client briefs across 5 dimensions of explicit direction (type, spacing/grid, layout, palette, references/constraints).
- One page per model per brief — the ceiling on every claim; individual cells carry ~30-point CIs, treated as evidence about the aggregate, not a ranking.
- Sol's loose-brief edge is firm (all 9 raters agree, sign test p = 0.004); Fable's structured advantage is larger but noisier (7/9 raters, p = 0.18, lost one of four structured briefs).

## Notes

(Personal annotations — follow-up to Contra Labs' [[Design Crit AI Design Judgment Dataset - @contralabs_ai|Design Crit]] dataset; earlier round pitted Fable against Opus 4.8.)

---

*Filed in: [[Saved Links MOC]]*
