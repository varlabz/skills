---
name: llm-wiki
description: "Search, retrieve, and read wiki pages. Provides commands for searching, retrieving articles, building context, reading pages, and managing wiki health."
argument-hint: "<query> with optional <wiki-id> (if multiple vaults configured)"
allowed-tools: shell
---

# LLM Wiki Skill

## When NOT to Use
- Wiki administration (ingesting, linting, reindexing) if you are not explicitly asked to perform those tasks
- Real-time web searches — use a web search skill instead
- Simple factual questions the agent already knows

The `./scripts/wiki` script resolves vault aliases from `.llm-wiki` (shell variables, isolated in subshell).

Usage: `./scripts/wiki [--id <wiki-id>] <command> [args...]`

## Procedure

### search
Search for pages matching a query without generating an answer.

```bash
./scripts/wiki [--id <wiki-id>] search "<query>" [--limit N]
```

**Arguments:**
- `query` — One or more search terms (positional)

**Options:**
- `--limit N` — Limit the number of results

### search-following
Search and return the matched page plus N subsequent pages/excerpt for broader context.

```bash
./scripts/wiki [--id <wiki-id>] search-following "<query>" [--pages N] [--context-chars N] [--max-chars N] [--limit N]
```

**Arguments:**
- `query` — One or more search terms (positional)

**Options:**
- `--pages N` / `--following-pages N` — Number of following pages to include
- `--context-chars N` — Character limit for context
- `--max-chars N` — Maximum total characters in output 

### retrieve
Prompt → search → retrieve top-k wiki articles. Returns a summary table of matched articles.

```bash
./scripts/wiki [--id <wiki-id>] retrieve "<query>" [--top-k N] [--max-chars-per-article N] [--max-total-chars N] [--show]
```

**Arguments:**
- `query` — One or more search terms (positional)

**Options:**
- `--top-k N` — Number of top articles to retrieve
- `--max-chars-per-article N` — Maximum characters per article 
- `--max-total-chars N` — Maximum total characters across all articles 
- `--show` — Print the LLM-ready context text instead of the summary table

### context
Build a compact LLM-ready context pack from search results.

```bash
./scripts/wiki [--id <wiki-id>] context "<query>" [--max-chars N] [--limit N]
```

**Arguments:**
- `query` — One or more search terms (positional)

**Options:**
- `--max-chars N` — Maximum characters in output 
- `--limit N` — Limit the number of results

### read
Read the full content of a specific wiki page by title.

```bash
./scripts/wiki [--id <wiki-id>] read "Page Title"
```

**Arguments:**
- `title` — One or more page titles (positional)

### why
Explain how a query was normalised and what suggestions were made during search.

```bash
./scripts/wiki [--id <wiki-id>] why "<query>" [--limit N]
```

**Arguments:**
- `query` — One or more search terms (positional)

**Options:**
- `--limit N` — Limit the number of results

### pages
List all pages in the wiki.

```bash
./scripts/wiki [--id <wiki-id>] pages
```

### stats
Show wiki vault health and statistics.

```bash
./scripts/wiki [--id <wiki-id>] stats
```

### lint
Run lint checks for broken links, orphan pages, and very short pages.

```bash
./scripts/wiki [--id <wiki-id>] lint
```

### repair
Plan or apply safe wiki lint repairs. By default runs in dry-run mode.

```bash
./scripts/wiki [--id <wiki-id>] repair [--apply] [--create-missing] [--no-fix-broken] [--no-link-orphans] [--no-expand-short] [--index-page TITLE]
```

**Options:**
- `--apply` — Apply proposed safe repairs (default is dry-run)
- `--create-missing` — Create stub pages for unresolved missing link targets
- `--no-fix-broken` — Do not rewrite broken links to resolved canonical pages
- `--no-link-orphans` — Do not link orphan pages from the index
- `--no-expand-short` — Do not add retrieval scaffolds to very short pages
- `--index-page TITLE` — Page used to link orphan pages

### reindex
Rebuild the SQLite search index from Markdown files.

```bash
./scripts/wiki [--id <wiki-id>] reindex
```
