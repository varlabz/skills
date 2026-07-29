---
name: openserp-search
description: 'Search the web using a local OpenSERP instance. Use for web searches, finding current information, researching topics, checking news, looking up documentation, or finding recent events. Supports engines: google, bing, duckduckgo, yandex, baidu, ecosia.'
argument-hint: 'search query'
allowed-tools: shell
---

# OpenSERP Web Search

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

### Default search (Google, Bing, DuckDuckGo)
```bash
./scripts/search "Python asyncio best practices"
```

### Custom engine list
```bash
./scripts/search "AI announcements" --engines bing,yandex
```

### Regional search with result limit
```bash
./scripts/search "Docker multi-stage build" --engines google,bing --limit 15 --region us
```

### Multi-engine mega search with mode
```bash
./scripts/search "golang" --engines google,bing,yandex --mode balanced --limit 20
```

### Filter by domain
```bash
./scripts/search "python" --engines google --site python.org --limit 5
```

### Filter by file type
```bash
./scripts/search "machine learning" --file pdf --limit 10
```

### Extract page content from top result
```bash
./scripts/search "python tutorial" --engines google --limit 1 --extract 1
```

## Options

| Flag | Short | Default | Description |
|------|-------|---------|-------------|
| `--engines` | `-E` | `google,bing,duckduckgo` | Comma-separated engines: `google`, `bing`, `duckduckgo`, `yandex`, `baidu`, `ecosia` |
| `--mode` | — | `balanced` | Mega mode: `balanced`, `any`, `fast` |
| `--limit` | `-l` | `10` | Maximum results to return |
| `--format` | `-f` | `json` | Output format: `json` or `text` |
| `--server` | `-s` | — | OpenSERP instance URL (overrides `OPENSERP_URL` env) |
| `--region` | `-r` | — | Region code (e.g. `us`, `uk`, `de`, `cn`) |
| `--lang` | `-n` | — | Language code (e.g. `EN`, `DE`, `RU`, `ES`, `fr-FR`) |
| `--date` | — | — | Date range in `YYYYMMDD..YYYYMMDD` format |
| `--site` | — | — | Restrict to a specific domain (e.g. `github.com`) |
| `--file` | — | — | File extension filter (e.g. `pdf`, `doc`) |
| `--start` | — | — | Pagination offset (e.g. `0`, `10`, `20`) |
| `--extract` | — | — | Fetch page content for top N results (1-5) |
| `--extract-mode` | — | — | Extraction strategy: `auto`, `fast`, `rendered` |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENSERP_URL` | Default OpenSERP instance URL (default: `http://localhost:7007`) |
