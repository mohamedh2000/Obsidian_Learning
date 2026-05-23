---
title: "Anthropic Knowledge Work Plugins"
url: "https://github.com/anthropics/knowledge-work-plugins"
platform: github
date_saved: 2026-05-23
source: "Anthropic (@anthropics)"
content_type: repo
topics: [AI Agents, Claude Code & Anthropic, Developer Tools]
tags: [claude-code, plugins, mcp, knowledge-workers, workflow-automation, anthropic]
status: unread
---

> Open source repository of plugins for knowledge workers to use in Claude Cowork/Code — transforms Claude into a specialist for specific roles, teams, and companies.

| Metric | Count |
|--------|-------|
| Stars | 12.7k |
| Forks | 1.6k |

**Topics:** [[AI Agents]], [[Claude Code & Anthropic]], [[Developer Tools]]

## Key Points
- **11 role-specific plugins**: productivity, sales, customer-support, product-management, marketing, legal, finance, data, enterprise-search, bio-research, cowork-plugin-management
- **File-based configuration**: No code, infrastructure, or build steps — just Markdown and JSON
- **MCP connector integrations**: Slack, Notion, Asana, Linear, Jira, HubSpot, Figma, Snowflake, and 30+ more tools
- **Plugin structure**: `.claude-plugin/plugin.json` manifest, `.mcp.json` for tool connections, `commands/` for slash commands, `skills/` for domain knowledge

### Plugin Structure
```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest
├── .mcp.json                    # Tool connections
├── commands/                    # Slash commands (e.g., /sales:call-prep)
└── skills/                      # Domain knowledge (auto-activated)
```

### Installation
```bash
# Claude Code CLI
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```

*Filed in: [[Saved Links MOC]]*
