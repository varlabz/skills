---
name: convert-to-markdown
description: "Convert files and web content to Markdown. Supports YouTube video transcripts (via URL or video ID) and conversion of MHTML files and web pages into Markdown for easier reading and processing."
tags: [youtube, transcript, mhtml, html, markdown, web]
---

# Convert Files and URLs to Markdown

## Prerequisites

These scripts use [`uvx`](https://docs.astral.sh/uv/) to run their dependencies on the fly — no permanent installation needed.

## YouTube Transcript

Extract captions/subtitles from YouTube videos.

```bash
./scripts/youtube-transcript.py <youtube_video_id_or_url>
```

**Options:**

| Flag | Description |
|------|-------------|
| `--info` | Include video metadata (title, channel, duration, etc.) before the transcript |
| `--lang <code>` | Language code for subtitles (e.g. `en`, `de`). Defaults to `auto` (detects video's source language) |
| `--raw` | Output the raw VTT text instead of the cleaned/readable transcript |

### Examples

```bash
# Basic transcript (auto-detected language)
./scripts/youtube-transcript.py dQw4w9WgXcQ

# Transcript with metadata
./scripts/youtube-transcript.py --info https://www.youtube.com/watch?v=dQw4w9WgXcQ

# German subtitles
./scripts/youtube-transcript.py --lang de dQw4w9WgXcQ

# Raw VTT output
./scripts/youtube-transcript.py --raw dQw4w9WgXcQ
```

## MHTML to Markdown

Convert an MHTML file (local path) or a remote URL serving MHTML content into Markdown.

```bash
./scripts/mhtml-to-md.py <path_or_url>
```

### Examples

```bash
# Local MHTML file
./scripts/mhtml-to-md.py ./page.mhtml

# Remote MHTML URL
./scripts/mhtml-to-md.py https://example.com/page.mhtml
```

## HTML / Web Page to Markdown

Convert any web page URL into Markdown via a Crawl4AI server.

```bash
./scripts/html-to-md.py <url>
```

**Options:**

| Flag | Description |
|------|-------------|
| `-s`, `--server <url>` | Crawl4AI server URL (default: `http://localhost:11235`, or `$CRAWL4AI_URL`) |
| `-o`, `--output <file>` | Write markdown to a file instead of stdout |

### Examples

```bash
# Print markdown to stdout
./scripts/html-to-md.py https://example.com

# Save to a file
./scripts/html-to-md.py https://example.com -o example.md

# Use a custom server
./scripts/html-to-md.py https://python.org -s http://crawl4ai.lan:11235
```
