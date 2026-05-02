---
name: youtube-transcript
description: 'Extract transcripts from YouTube videos. Use for getting video transcripts for analysis, summarization, or content extraction. Supports video ID or URL lookup, configurable language selection, and output formats.'
argument-hint: 'YouTube video ID or URL, optional: --lang LANG --info --raw'
compatibility: Requires uv
allowed-tools: shell
---

# YouTube Transcript Skill

## Usage

```bash
scripts/extract VIDEO_ID_OR_URL [--lang LANG] [--info] [--raw]
```

- `VIDEO_ID_OR_URL`: YouTube video ID or full URL
- `--lang LANG`: language code (e.g. `en`, `es`); defaults to auto-detect
- `--info`: also print video metadata (title, description, etc.)
- `--raw`: output raw VTT instead of cleaned text

## Examples

```bash
scripts/extract dQw4w9WgXcQ
scripts/extract "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --info
scripts/extract dQw4w9WgXcQ --lang es
```

## Notes

- Transcripts are only available for videos with captions enabled
- Falls back to auto-generated captions if manual captions are unavailable