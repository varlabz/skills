---
name: searxng-search
description: 'Search the web using a local SearXNG instance. Use for web searches, finding current information, researching topics, checking news, looking up documentation, or finding recent events. Supports categories: general, news, images, videos, it, science, social media.'
argument-hint: '<query> [--engine news|it|science|images|videos] [--time-range day|week|month|year] [--max-results 15]'
allowed-tools: shell
---

# SearXNG Web Search

## When to Use
- You need up-to-date information not in your training data
- Researching a topic, technology, library, or recent event
- Searching for news articles or current affairs
- Finding documentation, tutorials, or code examples
- Looking up anything that benefits from a live web search

## Procedure

Run the [search script](./scripts/search.py) with your query:

```bash
./scripts/search.py "<query>"
```

### General web search
```bash
./scripts/search.py "Python asyncio best practices"
```

### News search with time filter
```bash
./scripts/search.py "AI announcements" --engine news --time-range week
```

### Technical / IT search
```bash
./scripts/search.py "Docker multi-stage build" --engine it --max-results 15
```

### Science or academic topics
```bash
./scripts/search.py "transformer architecture attention mechanism" --engine science
```

## Options

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--engine` | `-e` | `general` | Category: `general`, `news`, `images`, `videos`, `it`, `science`, `files`, `social media`, `music`, `map` |
| `--max-results` | `-n` | `10` | Number of results to return |
| `--time-range` | `-t` | — | Filter by `day`, `week`, `month`, or `year` |
| `--language` | `-l` | `en-US` | Language code (e.g. `zh-CN`, `fr-FR`) |
| `--format` | `-f` | `json` | Output format: `json` or `text` |
| `--url` | — | `$SEARXNG_URL` | Override the SearXNG instance URL |

## Configuration

Set `SEARXNG_URL` to point at your instance (defaults to `http://localhost:8080`):
```bash
export SEARXNG_URL="http://localhost:8080"
```
