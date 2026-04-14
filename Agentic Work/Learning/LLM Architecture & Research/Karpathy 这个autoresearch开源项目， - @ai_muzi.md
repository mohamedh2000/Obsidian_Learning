---
title: "Karpathy 这个autoresearch开源项目，"
url: "https://x.com/ai_muzi/status/2037490168412750233"
platform: twitter
date_saved: 2026-03-27
source: "木子不写代码 (@ai_muzi)"
content_type: tweet
topics: [AI Agents, Prompt Engineering]
tags: [twitter, ai_muzi]
status: unread
---

# Karpathy 这个autoresearch开源项目，

> Karpathy 这个autoresearch开源项目，

让我有些恍惚。

做过将近 4 年数据科学家/时间序列预测，

当时很多 Data Scientist 和 ML Researcher 工作正在被替代，

而且是被同行发明的工具替代。

过去数据科学家的工作，本质上就是这一套循环：
了解业务，
选模型建模，
实验超参数，模型深度，优化器选择，
训练循环细节，
跑训练，
看指标，
调整以上的策略，
然后继续下一轮

而 autoresearch，

它给了一个小但真实

| | |
|---|---|
| **Source** | 木子不写代码 (@ai_muzi) |
| **Saved** | 2026-03-27 |
| **Type** | tweet |
| **Engagement** | 237 likes, 44 retweets |
| **URL** | [Link](https://x.com/ai_muzi/status/2037490168412750233) |

## Topics

[[AI Agents]] | [[Prompt Engineering]]

## Key Points

- Karpathy 这个autoresearch开源项目，
- 让我有些恍惚。
- 做过将近 4 年数据科学家/时间序列预测，
- 当时很多 Data Scientist 和 ML Researcher 工作正在被替代，

## Tweet

Karpathy 这个autoresearch开源项目，

让我有些恍惚。

做过将近 4 年数据科学家/时间序列预测，

当时很多 Data Scientist 和 ML Researcher 工作正在被替代，

而且是被同行发明的工具替代。

过去数据科学家的工作，本质上就是这一套循环：
了解业务，
选模型建模，
实验超参数，模型深度，优化器选择，
训练循环细节，
跑训练，
看指标，
调整以上的策略，
然后继续下一轮

而 autoresearch，

它给了一个小但真实的 语言模型 训练环境，

让它在固定的 5 分钟预算里反复做实验，

而且它改的不只是 learning rate 或 batch size

它可以直接改训练代码本身，
包括模型深度，
优化器选择，
attention pattern，
训练循环细节，
甚至模型结构的一部分

然后系统自己跑实验，
自己看结果，
有效就保留，
无效就回滚，
再继续往前推进

最重复，最耗时间，最像实验流水线的那一层，

都被自动化了。

而且这件事对今天做 agent 的我们也很有启发，

完全可以把同样的方法用到 agent 系统本身

比如让 agent 自己去搜索和迭代：
prompt，
tool 组合，
memory 规则，
routing 方式，
任务拆分，
handoff 结构，
评估方法

跑一轮，
看结果，
保留更好的版本，
继续迭代

同一个循环，

只是优化对象从 model training，变成了 agent system design

Repo：
https://github.com/karpathy/autoresearch

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
