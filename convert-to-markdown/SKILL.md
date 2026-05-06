---
name: convert-to-markdown
description: "Use when converting files or web content to Markdown. Supports extracting YouTube video transcripts (requires URL or video ID) and converting MHTML files/web pages into Markdown for easier reading and processing."
---

# Convert Files and URLs to Markdown

## When to Use
- You need a transcript of a YouTube video
- You need to convert an MHTML file or web page into Markdown for easier reading and processing
- You need to convert a local HTML file into Markdown

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
Converts an MHTML file (local path) or a remote MHTML URL into Markdown using MarkItDown.
```bash
./scripts/mhtml-to-md.py <path_or_url>
```

### HTML to Markdown
Converts a local HTML (or other supported) file into Markdown using MarkItDown directly.
```bash
uvx markitdown <path>
```