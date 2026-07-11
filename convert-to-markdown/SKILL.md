---
name: convert-to-markdown
description: "Convert files and web pages to Markdown. Use this skill whenever the user asks to extract text from PDFs, Word docs (.docx), PowerPoint (.pptx), Excel spreadsheets (.xlsx), images, audio files, EPUB ebooks, CSV/JSON/XML, MHTML archives, YouTube transcripts, or any website URL — even if they don't explicitly say 'markdown' or 'convert'. Also use when the user says 'read this file', 'get the text from', 'extract content from', 'transcribe', or 'grab the transcript' for any of these formats."
compatibility: Requires uvx (uv). Scripts fetch dependencies at runtime.
metadata:
  tools: "uvx"
---

# Convert Files and URLs to Markdown

Run commands via `uvx` — it fetches Python deps on the fly, no permanent install needed. All scripts live in `scripts/`.

## Tool Selection

| Input type | Command | Script location |
|------------|---------|-----------------|
| `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.xls`, `.csv`, `.json`, `.xml`, `.epub`, images (`.jpg`/`.png`/etc.), audio (`.mp3`/`.wav`/etc.), `.html`, `.txt`, `.md` | `uvx markitdown <path>` | built-in CLI |
| YouTube URL or video ID | `./scripts/youtube-transcript <url_or_id>` | `scripts/youtube-transcript` |
| Regular web URL (Crawl4AI server running) | `./scripts/web-to-md <url>` | `scripts/web-to-md` |
| `.mhtml` file or MHTML URL | `./scripts/mhtml-to-md <source>` | `scripts/mhtml-to-md` |

## YouTube Transcript

```bash
./scripts/youtube-transcript <url_or_video_id> [--info] [--lang <code>] [--raw]
```

- `--info`: Include video metadata (title, channel, duration) before transcript.
- `--lang <code>`: Subtitle language (e.g. `en`, `de`). Default: auto-detect source language.
- `--raw`: Output raw VTT instead of cleaned text.

## MHTML to Markdown

```bash
./scripts/mhtml-to-md <path_or_url>
```

Accepts local `.mhtml` files or remote URLs serving MHTML content.

## Web Page to Markdown (via Crawl4AI)

```bash
./scripts/web-to-md <url> [-o output.md] [-s server_url]
```

Requires a [Crawl4AI](https://github.com/unclecode/crawl4ai) server running on `http://localhost:11235` (or set `$CRAWL4AI_URL`). The server fetches the full page HTML; this script converts it to Markdown.

**No Crawl4AI?** Fall back:
```bash
curl -o page.html <url> && uvx markitdown page.html
```

## MarkItDown (General File Conversion)

All other formats use `uvx markitdown`:

```bash
uvx markitdown <path> [-o output.md]
```

Supports: PDF, DOCX, PPTX, XLSX/XLS, images (EXIF + OCR), audio (transcription), EPUB, CSV, JSON, XML, HTML, TXT, ZIP.

## When Things Go Wrong

| Issue | What to do |
|-------|-----------|
| Scanned PDF yields no text | Try `uvx markitdown <path>` treating it as an image — markitdown runs OCR on images |
| Password-protected file | Remove password first; markitdown can't decrypt |
| Large ZIP archive | Extract specific files first, then convert individually |
| YouTube age-restricted video | yt-dlp will fail — no workaround |
| Audio transcription poor quality | Depends on audio clarity; nothing we can do from here |
| Excel has many sheets | All sheets included as separate tables in output |
