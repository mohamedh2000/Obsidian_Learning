# Reading Dashboard

## Summary by Topic
```dataview
TABLE length(rows) AS "Count"
FROM "Agentic Work/Reading List" OR "Agentic Work/Learning"
WHERE status
GROUP BY topic AS "Topic"
SORT length(rows) DESC
```

## Recently Added
```dataview
TABLE
  date_saved AS "Date",
  type AS "Type",
  topic AS "Topic"
FROM "Agentic Work/Reading List" OR "Agentic Work/Learning"
WHERE status = "unread"
SORT date_saved DESC
LIMIT 25
```

## Timeline (all notes by date)
```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  date_saved AS "Date",
  type AS "Type",
  topic AS "Topic"
FROM "Agentic Work/Reading List" OR "Agentic Work/Learning"
SORT date_saved DESC
```

## Quick Capture Inbox
```dataview
TABLE
  url AS "URL",
  type AS "Type",
  date_saved AS "Added"
FROM "Agentic Work/Inbox"
WHERE status = "unread"
SORT date_saved DESC
```

## Unread by Topic
```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  type AS "Type",
  date_saved AS "Added"
FROM "Agentic Work/Reading List" OR "Agentic Work/Learning"
WHERE status = "unread"
GROUP BY topic
SORT topic ASC
```

## All Unread
```dataview
TABLE
  url AS "URL",
  type AS "Type",
  topic AS "Topic"
FROM "Agentic Work/Reading List" OR "Agentic Work/Learning" OR "Agentic Work/Inbox"
WHERE status = "unread"
SORT date_saved DESC
```

## Currently Reading
```dataview
TABLE
  url AS "URL",
  type AS "Type",
  topic AS "Topic"
FROM "Agentic Work/Reading List" OR "Agentic Work/Learning" OR "Agentic Work/Inbox"
WHERE status = "reading"
SORT file.mtime DESC
```

## Completed
```dataview
TABLE
  url AS "URL",
  type AS "Type",
  topic AS "Topic"
FROM "Agentic Work/Reading List" OR "Agentic Work/Learning" OR "Agentic Work/Inbox"
WHERE status = "done"
SORT file.mtime DESC
```

---

### How to use
1. **Quick capture**: Dump links into `Inbox/` — sort them later
2. Open any note and change `status: unread` → `status: reading` when you start
3. Change to `status: done` when finished
4. Fill in the **Why saved** and **Notes** sections as you go
5. This dashboard auto-updates via Dataview queries

### Topic folders
| Folder | Focus |
|--------|-------|
| AI-Agents-Automation | AI coding agents, vibe coding, automation tools |
| AI-ML-Research | ML research papers, models, training, embeddings |
| Business-Marketing-Product | Startups, SaaS, marketing, product strategy |
| Claude-Anthropic-AI-Coding | Claude Code, Anthropic tools, skills, MCP |
| Databases-Vectors-Graphs | Databases, vector stores, graph databases |
| Design-UI | UI/UX design, Figma, CSS, component libraries |
| Dev-Tools-Open-Source | Developer tools, open source projects, frameworks |
| Finance-Markets | Stocks, crypto, trading, market analysis |
| Infrastructure | Cloud, DevOps, deployment, CI/CD |
| Misc | Everything else |
