---
name: searxng-search
description: 'Search the web using a local SearXNG instance. Use for web searches, finding current information, researching topics, or checking news.'
argument-hint: 'Your search query, optional: --engine news --time-range month --max-results 15'
allowed-tools: shell
---

# SearXNG Web Search

Run [scripts/search](scripts/search.py):

```bash
scripts/search.py "your query" [options]
```

**Key options:** `-e` engine (general|news|it|science|images…), `-n` max results (default 10), `-t` time range (day|week|month|year), `-f` format (text|json), `--url` override instance URL.

```bash
scripts/search.py "AI breakthroughs" -e news -t month -f json 
scripts/search.py "Python best practices" -f json -n 15
```
