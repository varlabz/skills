---
name: convert-to-markdown
description: "Use when converting files or web content to Markdown. Supports extracting YouTube video transcripts (requires URL or video ID) and converting MHTML files/web pages into Markdown for easier reading and processing."
---

# Convert URLs into Markdown with tools

## When to Use
- You need a transcript of a YouTube video
- Converting MHTML files or web pages into Markdown format for easier reading and processing.

## Procedure

### YouTube Transcript
To extract YouTube captions, run the [youtube-transcript script](./scripts/youtube-transcript.py):
```bash
./scripts/youtube-transcript.py <youtube_video_id_or_url>
```

### YouTube Transcript with metadata
To extract YouTube captions along with metadata, run the [youtube-transcript script](./scripts/youtube-transcript.py):
```bash
./scripts/youtube-transcript.py --info <youtube_video_id_or_url>
```

### MHTML to Markdown
```bash
./scripts/mhtml-to-html.py <path_or_url> | uvx markitdown
```
