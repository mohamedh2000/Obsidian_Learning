#!/usr/bin/env python3
"""
Obsidian Inbox Sorter
=====================
Scans the Inbox/ folder for notes, auto-categorizes them by URL,
adds frontmatter + tags, links to related notes, and moves them
to the appropriate topic folder.

Usage:
  python3 sort-inbox.py          # Process all inbox notes
  python3 sort-inbox.py --dry    # Preview without making changes

Drop a link into Inbox/ as a note (even just a URL as the filename or body)
and this script handles the rest.
"""

import os, re, sys
from datetime import datetime
from collections import defaultdict

VAULT = os.path.expanduser(
    "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Agentic Work"
)
INBOX = os.path.join(VAULT, "Inbox")
READING_LIST = os.path.join(VAULT, "Reading List")
DRY_RUN = "--dry" in sys.argv

# ── Topic inference rules ────────────────────────────────────────
# Each rule: (url_patterns, folder_name, tag)
TOPIC_RULES = [
    # Claude / Anthropic / AI Coding
    (["anthropic.com", "claude", "cursor.com", "code.claude", "claude-code",
      "codex", "copilot"], "Claude-Anthropic-AI-Coding", "claude-ai-coding"),

    # AI/ML Research
    (["arxiv.org", "huggingface", "openai.com/research", "openai.com/index",
      "transformer-circuits", "deepmind", "karpathy", "embedding",
      "spectral", "tree-sitter"], "AI-ML-Research", "ai-ml"),

    # AI Agents
    (["agent", "autogen", "crewai", "langchain", "langgraph",
      "phidata", "pua", "agency"], "AI-Agents-Automation", "ai-agents"),

    # Design / UI
    (["figma.com", "dribbble", "design", "shadcn", "tailwind",
      "framer", "ui", "ux", "css"], "Design-UI", "design"),

    # Infrastructure
    (["cloudflare", "vercel.com/docs", "aws.", "docker",
      "kubernetes", "terraform", "deploy"], "Infrastructure", "infra"),

    # Databases
    (["database", "postgres", "prisma", "vector", "graph-db",
      "neptune", "pinecone", "weaviate", "qdrant", "supabase"], "Databases-Vectors-Graphs", "databases"),

    # Dev Tools / Open Source
    (["github.com", "gitlab.com", "npmjs.com", "dev.to",
      "opensource", "cli", "terminal", "wezterm", "yazi"], "Dev-Tools-Open-Source", "dev-tools"),

    # Business / Marketing / Product
    (["marketing", "sales", "growth", "product", "startup",
      "saas", "revenue", "founder", "business"], "Business-Marketing-Product", "business"),
]


def infer_topic(url, body=""):
    """Infer topic folder and tag from URL and note body."""
    text = (url + " " + body).lower()
    for patterns, folder, tag in TOPIC_RULES:
        for p in patterns:
            if p in text:
                return folder, tag
    return "Misc", "misc"


def get_type(url):
    if "x.com/" in url or "twitter.com/" in url:
        return "tweet"
    if "github.com/" in url:
        return "github"
    if "youtu.be/" in url or "youtube.com/" in url:
        return "video"
    if "arxiv.org/" in url:
        return "research"
    if "figma.com/" in url:
        return "design"
    return "article"


def get_title(url):
    clean = re.sub(r"\?.*$", "", url).rstrip("/")
    m = re.match(r"https?://x\.com/(\w+)/status/", clean)
    if m:
        return f"@{m.group(1)} Tweet"
    m = re.match(r"https?://github\.com/([\w.-]+)/([\w.-]+)", clean)
    if m:
        return f"{m.group(1)}/{m.group(2)}"
    m = re.match(r"https?://youtu\.be/", clean)
    if m:
        return "YouTube Video"
    m = re.match(r"https?://(?:www\.)?([\w.-]+)", clean)
    if m:
        return m.group(1)
    return "Link"


def get_filename(url):
    clean = re.sub(r"\?.*$", "", url).rstrip("/")
    m = re.match(r"https?://x\.com/(\w+)/status/(\d+)", clean)
    if m:
        return f"{m.group(1)}-{m.group(2)[-6:]}"
    m = re.match(r"https?://github\.com/([\w.-]+)/([\w.-]+)", clean)
    if m:
        return f"gh-{m.group(1)}-{m.group(2)}"
    m = re.match(r"https?://youtu\.be/([\w-]+)", clean)
    if m:
        return f"yt-{m.group(1)}"
    m = re.match(r"https?://(?:www\.)?([\w.-]+)(?:/(.+))?", clean)
    if m:
        domain = m.group(1).replace(".", "-")
        path = m.group(2)
        if path:
            path = re.sub(r"[^\w-]", "-", path)[:30].rstrip("-")
            return f"{domain}-{path}"
        return domain
    return "link"


def find_related(tag, dest_folder):
    """Find existing notes in the destination folder for linking."""
    related = []
    folder_path = os.path.join(READING_LIST, dest_folder)
    if not os.path.exists(folder_path):
        return related
    for f in os.listdir(folder_path):
        if f.endswith(".md"):
            related.append(f[:-3])  # stem
    return related[:5]


def extract_url(filepath):
    """Extract a URL from a note file — from frontmatter, body, or filename."""
    with open(filepath, "r") as f:
        content = f.read()

    # Check frontmatter url: field
    m = re.search(r"^url:\s*(.+)$", content, re.MULTILINE)
    if m:
        return m.group(1).strip(), content

    # Check body for URLs
    m = re.search(r"(https?://\S+)", content)
    if m:
        return m.group(1).strip(), content

    # Check filename
    name = os.path.basename(filepath)
    m = re.search(r"(https?://\S+)", name)
    if m:
        return m.group(1).strip(), content

    return None, content


def process_inbox():
    if not os.path.exists(INBOX):
        print(f"No inbox folder at {INBOX}")
        return

    files = [f for f in os.listdir(INBOX) if f.endswith(".md") and f != "HOW TO USE INBOX.md"]
    if not files:
        print("Inbox is empty — nothing to process.")
        return

    print(f"Found {len(files)} notes in Inbox\n")

    for fname in sorted(files):
        filepath = os.path.join(INBOX, fname)
        url, original_content = extract_url(filepath)

        if not url:
            print(f"  SKIP  {fname} — no URL found")
            continue

        # Clean tracking params
        clean_url = re.sub(r"\?s=\d+$", "", url)

        # Infer everything
        link_type = get_type(clean_url)
        title = get_title(clean_url)
        dest_folder, tag = infer_topic(clean_url, original_content)
        filename = get_filename(clean_url)
        today = datetime.now().strftime("%Y-%m-%d")
        related = find_related(tag, dest_folder)

        # Build note content
        related_section = ""
        if related:
            related_section = "\n## Related\n"
            for r in related[:5]:
                related_section += f"- [[{r}]]\n"

        content = f"""---
url: {clean_url}
type: {link_type}
status: unread
topic: {dest_folder}
tags: [{tag}]
added: {today}
---

# {title}
{related_section}
## Why saved
<!-- Fill in when you remember why this caught your eye -->

## Notes
<!-- Fill in after reading -->
"""

        # Destination
        dest_dir = os.path.join(READING_LIST, dest_folder)
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, f"{filename}.md")

        # Handle duplicates
        counter = 2
        base = dest_path
        while os.path.exists(dest_path):
            dest_path = base.replace(".md", f"-{counter}.md")
            counter += 1

        rel_dest = os.path.relpath(dest_path, VAULT)

        if DRY_RUN:
            print(f"  WOULD MOVE  {fname}")
            print(f"    → {rel_dest}  [#{tag}]")
        else:
            with open(dest_path, "w") as f:
                f.write(content)
            os.remove(filepath)
            print(f"  SORTED  {fname}")
            print(f"    → {rel_dest}  [#{tag}]")

    print("\nDone!")


if __name__ == "__main__":
    process_inbox()
