---
title: "Hermes Agent Plugins - Extensible Plugin System"
url: "https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins"
platform: web
date_saved: 2026-06-03
source: "Nous Research (hermes-agent.nousresearch.com)"
content_type: guide
topics: [agent-plugins, extensibility, tool-registration]
tags: [hermes, nous-research, plugins, agent-architecture]
status: unread
---

# Hermes Agent Plugins - Extensible Plugin System

> Hermes' plugin system allows adding custom tools, hooks, and integrations without modifying core code — drop-in extensibility for personal, team, or project-specific solutions.

| | |
|---|---|
| **Source** | Nous Research (hermes-agent.nousresearch.com) |
| **Saved** | 2026-06-03 |
| **Type** | guide |
| **URL** | [Link](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins) |

## Topics

[[Agent Design]] | [[Tool Systems]] | [[Plugin Architecture]]

## Key Points

- **Plugin Structure**: Simple directory with `plugin.yaml` manifest, `__init__.py` registration, `schemas.py` definitions, `tools.py` implementations — dropped into `~/.hermes/plugins/`
- **Four Plugin Types**: General plugins (tools, hooks, commands), Memory providers (single-select), Context engines (single-select), Model providers (multiple load, one active)
- **Capabilities**: Register LLM-invokable tools, hook into lifecycle events, add slash commands/CLI subcommands, inject messages, bundle skills and data files
- **Discovery Sources**: Bundled plugins, user directory (`~/.hermes/plugins/`), project-local (`.hermes/plugins/`), pip packages
- **Security Model**: Third-party plugins disabled by default — discovered but not loaded until explicitly enabled via `plugins.enabled` config
- **Management CLI**: `hermes plugins install/enable/disable/list`

## Notes

(Personal annotations)

---

*Filed in: [[Agent Design MOC]] | [[Saved Links MOC]]*
