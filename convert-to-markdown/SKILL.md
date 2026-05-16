---
name: convert-to-markdown
description: "Convert files and web content to Markdown. Supports YouTube video transcripts (via URL or video ID) and conversion of MHTML files and web pages into Markdown for easier reading and processing."
tags: [youtube, transcript, mhtml, html, markdown, web]
---

# Convert Files and URLs to Markdown

## Prerequisites

These scripts use [`uvx`](https://docs.astral.sh/uv/) to run their dependencies on the fly — no permanent installation needed.

Run any script with `--help` to see its full usage.

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

Convert any web page URL into Markdown using [crawl4ai](https://github.com/unclecode/crawl4ai).

```bash
uvx --from crawl4ai crwl <path_or_url> -o markdown -b "headless=true,user_agent_mode=random"
```

### Example

```bash
uvx --from crawl4ai crwl https://example.com -o markdown -b "headless=true,user_agent_mode=random"
```

## Gotchas

- **YouTube transcripts** fail for age-restricted, private, or deleted videos. The script will report an error and exit.
- **YouTube auto-detected language** may not always match the video's spoken language. Use `--lang <code>` to override when the transcript is in the wrong language.
- **crawl4ai** runs a headless browser, but some heavy JavaScript-rendered SPAs may still produce incomplete output.
- **MHTML conversion** quality depends on how the archive was created. Some MHTML files contain only the main page markup without embedded resources or styling.
```
