---
name: searxng-search
description: 'Search the web using a local SearXNG instance via search.py script. Use for web searches, finding information, researching topics, checking current events, or gathering data from the internet. Supports configurable server URL (default: http://localhost:8080), time range filtering, category filtering, language selection, safe search, and text/JSON output formats.'
argument-hint: 'Your search query, optional: --engine news --time-range month --max-results 15 --url http://searxng.local:8080'
allowed-tools: shell
---

# SearXNG Web Search

## When to Use
- Search the web for current information
- Research topics or find resources
- Check recent news or events
- Gather data from multiple sources
- Find documentation or tutorials online

## Prerequisites

Ensure a SearXNG instance is running and accessible. The default URL is `http://localhost:8080`, but this can be configured via `--url` argument or `SEARXNG_URL` environment variable.

## Procedure

### Run the Search Script

Use the bundled [search script](./scripts/search.py) to perform web searches:

```bash
./scripts/search.py --query "your search query" [options]
```

### Available Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--query` | `-q` | Search query (required) | — |
| `--engine` | `-e` | Category: general, images, videos, news, map, music, it, science, files, social media | general |
| `--max-results` | `-n` | Maximum results to return | 10 |
| `--language` | `-l` | Language code (e.g. en-US, zh-CN) | en-US |
| `--safesearch` | `-s` | Safe search: 0=off, 1=moderate, 2=strict | 0 |
| `--time-range` | `-t` | Filter by time: day, week, month, year | none |
| `--format` | `-f` | Output format: text, json | text |
| `--url` | — | SearXNG instance URL (overrides SEARXNG_URL env) | http://localhost:8080 |

### Example Usage

**Simple search:**
```bash
./scripts/search.py --query "latest JavaScript features 2026"
```

**Recent news:**
```bash
./scripts/search.py --query "AI breakthroughs" --engine news --time-range month
```

**Technical research:**
```bash
./scripts/search.py --query "React performance optimization" --engine it --max-results 15
```

**JSON output for parsing:**
```bash
./scripts/search.py --query "Python best practices" --format json
```

**Custom server (searxng.local):**
```bash
./scripts/search.py --query "search terms" --url http://searxng.local:8080
```

**With language and safe search:**
```bash
./scripts/search.py --query "recherche Python" --language fr-FR --safesearch 1
```

## Tips

- Be specific with search queries for better results
- Use `--time-range` when you need recent information
- Use `--format json` when you need structured data for further processing
- Set `SEARXNG_URL` environment variable to avoid repeating `--url`
- If localhost:8080 is unavailable, ask the user to verify their SearXNG instance

## Troubleshooting

- **Connection refused**: Verify SearXNG is running at the configured URL
- **No results**: Try broadening the query or removing filters
- **Slow responses**: Reduce `--max-results` or use specific categories
