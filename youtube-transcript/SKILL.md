---
name: youtube-transcript
description: 'Extract transcripts from YouTube videos. Use for getting video transcripts for analysis, summarization, or content extraction. Supports video ID or URL lookup, configurable language selection, and output formats.'
argument-hint: 'YouTube video ID or URL, optional: --language LANG --info'
allowed-tools: shell
---

# YouTube Transcript Skill

## When to Use
- Retrieve transcripts for YouTube videos (when available)
- Extract text content from videos for analysis or summarization

## Prerequisites

**Python Dependencies**:
- The script uses `uvx` to run with yt-dlp dependency automatically

## Procedure

### Extract Transcript from YouTube Video

Use the script to extract transcript for a specific YouTube video:

```bash
./scripts/extract.py VIDEO_ID_OR_URL [--language LANG] [--info]
```

### Examples

Get transcript for a specific video:
```bash
./scripts/extract.py dQw4w9WgXcQ
```

Get transcript from a YouTube URL:
```bash
./scripts/extract.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Get transcript in Spanish:
```bash
./scripts/extract.py dQw4w9WgXcQ --language es
```

Get video info along with transcript:
```bash
./scripts/extract.py dQw4w9WgXcQ --info
```

Get raw VTT transcript:
```bash
./scripts/extract.py dQw4w9WgXcQ --raw
```

## Output Format

The script outputs cleaned transcript text by default. 
With `--info`, it also outputs video metadata. 
With `--raw`, it outputs the raw VTT transcript.

## Notes

- Transcripts are only available for videos that have captions enabled
- Some videos may not have transcripts available in the requested language
- For best results, provide video ID or full YouTube URL