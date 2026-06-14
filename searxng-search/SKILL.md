---
name: searxng-search
description: 'Search the web using a local SearXNG instance. Use for web searches, finding current information, researching topics, checking news, looking up documentation, or finding recent events. Supports categories: general, news, images, videos, it, science, social media.'
argument-hint: 'search query'
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

Run the [search script](./scripts/search) with your query:

```bash
./scripts/search "<query>"
```

> **Categories** can be combined with a comma: `--category "general,news"`

### General web search
```bash
./scripts/search "Python asyncio best practices"
```

### News search with time filter
```bash
./scripts/search "AI announcements" --category news --time-range week
```

### Technical / IT search
```bash
./scripts/search "Docker multi-stage build" --category "general,it" --max-results 15
```

### Science or academic topics
```bash
./scripts/search "transformer architecture attention mechanism" --category "science"
```

### Video search
```bash
./scripts/search "transformer architecture attention mechanism" --category "general,videos"
```

## Options

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--category` | `-c` | `general` | Category (comma-separated for multiple): `general`, `news`, `images`, `videos`, `it`, `science`, `files`, `social media`, `music`, `map` |
| `--max-results` | `-m` | `10` | Number of results to return |
| `--time-range` | `-t` | — | Filter by `day`, `week`, `month`, or `year` |
| `--language` | `-l` | `en-US` | Language code (e.g. `zh-CN`, `fr-FR`) |
| `--format` | `-f` | `json` | Output format: `json` or `text` |
| `--server` | `-s` | `http://localhost:8080` | Override the SearXNG instance URL |
| `--safesearch` | `-S` | `0` | Safe search level: `0` (off), `1` (moderate), `2` (strict) |

