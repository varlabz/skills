---
name: convert-to-markdown
description: "Read/fetch URL or a file. Supports wide range of formats. Use when the user needs to extract text content from documents."
compatibility: Requires uv (uvx).
metadata:
  tools: "uv (uvx)"
  formats: "PDF, DOCX, PPTX, XLSX, XLS, images, audio, EPUB, CSV, JSON, XML, ZIP, MHTML, YouTube, HTML"
---

# Convert Files and URLs to Markdown

All scripts use [`uvx`](https://docs.astral.sh/uv/) to run dependencies on the fly — no permanent installation needed.

---

## YouTube Transcript

Extract captions/subtitles from YouTube videos.

```bash
./scripts/youtube-transcript <youtube_video_id_or_url>
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
./scripts/youtube-transcript https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Transcript with metadata
./scripts/youtube-transcript --info https://www.youtube.com/watch?v=dQw4w9WgXcQ

# German subtitles
./scripts/youtube-transcript --lang de dQw4w9WgXcQ

# Raw VTT output
./scripts/youtube-transcript --raw dQw4w9WgXcQ
```

---

## MHTML to Markdown

Convert an MHTML file (local path) or a remote URL serving MHTML content into Markdown.

```bash
./scripts/mhtml-to-md <path_or_url>
```

### Examples

```bash
# Local MHTML file
./scripts/mhtml-to-md ./page.mhtml

# Remote MHTML URL
./scripts/mhtml-to-md https://example.com/page.mhtml
```

---

## Web to Markdown

Convert any web page URL into Markdown.

```bash
./scripts/web-to-md <url>
```

**Options:**

| Flag | Description |
|------|-------------|
| `-s`, `--server <url>` | Crawl4AI server URL (default: `http://localhost:11235`, or `$CRAWL4AI_URL`) |
| `-o`, `--output <file>` | Write markdown to a file instead of stdout |

### Examples

```bash
# Print markdown to stdout
./scripts/web-to-md https://example.com

# Save to a file
./scripts/web-to-md https://example.com -o example.md

# Use a custom server
./scripts/web-to-md https://python.org -s http://crawl4ai.lan:11235
```

---

## General File Conversion (via `uvx markitdown`)

Convert any supported file to Markdown using [MarkItDown](https://github.com/microsoft/markitdown). The `markitdown` CLI is available directly via `uvx` — no scripts needed.

```bash
uvx markitdown <path>
```

**Supported formats:**

| Format | File extensions | Notes |
|--------|----------------|-------|
| PDF | `.pdf` | Extracts text, headings, tables |
| Word | `.docx` | Full document structure |
| PowerPoint | `.pptx` | Slides, text, tables, notes |
| Excel | `.xlsx`, `.xls` | Sheets as tables |
| Images | `.jpg`, `.png`, `.gif`, `.webp`, `.bmp`, `.tiff` | EXIF metadata + OCR text |
| Audio | `.mp3`, `.wav`, `.m4a`, `.flac` | EXIF metadata + speech transcription |
| EPUB | `.epub` | eBook content |
| CSV | `.csv` | Table-formatted data |
| JSON | `.json` | Structured content |
| XML | `.xml` | Structured content |
| ZIP | `.zip` | Iterates over and converts contents |
| HTML | `.html`, `.htm` | Web page source |
| Text | `.txt`, `.md`, `.log` | Plain text passthrough |

**Options:**

| Flag | Description |
|------|-------------|
| `-o`, `--output <file>` | Write markdown to a file instead of stdout |

### Examples

```bash
# Convert a PDF
uvx markitdown report.pdf

# Convert a PowerPoint presentation and save to file
uvx markitdown slides.pptx -o slides.md

# Convert an Excel spreadsheet
uvx markitdown data.xlsx

# Convert an image (extracts EXIF metadata and OCR text)
uvx markitdown photo.jpg

# Convert an EPUB ebook
uvx markitdown book.epub

# Convert a CSV file
uvx markitdown data.csv

# Convert a ZIP archive (recursively converts contents)
uvx markitdown archive.zip
```

---

## Tips & Edge Cases

| Scenario | Recommendation |
|----------|---------------|
| **Scanned PDFs** (images-only) | Built-in extraction may yield no text. Try OCR via the image path instead, or use a cloud service. |
| **Password-protected files** | Remove password protection before converting — MarkItDown does not support decryption. |
| **Very large ZIP archives** | MarkItDown iterates all entries. For large archives, consider extracting specific files first. |
| **Audio transcription quality** | Depends on the audio clarity and the underlying speech-to-text engine. Clear speech with minimal background noise works best. |
| **Excel with many sheets** | All sheets are included as separate tables in the output. |
| **YouTube age-restricted videos** | yt-dlp may fail with age-restricted content. No workaround is provided. |
| **Crawl4AI not running** | `web-to-md` will fail with a connection error. Start the server first or use `uvx markitdown` on a saved `.html` file instead. |
