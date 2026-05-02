---
name: markitdown
description: Convert files and URLs (PDF, Word, Excel, PowerPoint, Images, Audio, HTML, CSV, JSON, XML, ZIP, EPubs, YouTube) into Markdown using Microsoft's MarkItDown tool.
compatibility: Requires uv
allowed-tools: shell
---

# Convert files and URLs into Markdown with MarkItDown

## Supported formats
- **Documents**: PDF, Word (DOCX/DOC), PowerPoint (PPTX/PPT), EPubs
- **Data**: Excel (XLSX/XLS), CSV, JSON, XML
- **Media**: Images (EXIF + OCR), Audio (EXIF + transcription), YouTube URLs
- **Web**: HTML, remote URLs
- **Archives**: ZIP (iterates contents)

## Usage

```bash
uvx markitdown <path_or_url>             # print to stdout
uvx markitdown <path_or_url> -o out.md  # save to file
```

