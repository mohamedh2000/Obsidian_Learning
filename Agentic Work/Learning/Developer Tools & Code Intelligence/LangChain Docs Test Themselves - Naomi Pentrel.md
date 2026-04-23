---
title: "How LangChain Made Their Docs Test Themselves"
url: "https://www.langchain.com/blog/our-docs-test-themselves"
platform: web
date_saved: 2026-04-23
source: "Naomi Pentrel (LangChain)"
content_type: guide
topics: [documentation, testing, CI/CD, agents, automation]
tags: [langchain, docs, testing, ci-cd, deep-agents, automation]
status: unread
---

# How LangChain Made Their Docs Test Themselves

> Stale code samples are a universal documentation problem — LangChain automated the migration of inline code samples into testable, CI-ready examples using Deep Agents CLI.

| | |
|---|---|
| **Source** | Naomi Pentrel (LangChain) |
| **Saved** | 2026-04-23 |
| **Type** | guide |
| **Engagement** | N/A |
| **URL** | [Link](https://www.langchain.com/blog/our-docs-test-themselves) |

## Topics

[[Developer Tools & Code Intelligence]] | [[Agent Design & Memory]]

## Key Points

- Code samples in documentation become outdated as APIs change and dependencies evolve, but most teams don't test them
- Manual migration to testable samples requires extracting code into separate files, adding setup/teardown logic, implementing markup tags, and CI/CD integration
- LangChain used Deep Agents CLI with a custom `docs-code-samples` skill to automate the entire workflow
- The skill-based approach contains detailed instructions for directory structure, naming conventions, tag placement, and command execution
- Implementation includes automated testing via GitHub Actions that regularly validates code samples and creates tickets when tests fail

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
