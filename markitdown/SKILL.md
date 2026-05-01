---
name: markitdown
description: Convert various files (PDF, PowerPoint, Word, Excel, Images, Audio, HTML, CSV, JSON, XML, ZIP, EPubs, etc.) into clean Markdown using Microsoft's MarkItDown tool. Perfect for quick extraction and format preservation.
compatibility: Requires uv
allowed-tools: shell
---

# Convert various files into Markdown with MarkItDown

Use this skill to convert various document formats into clean Markdown. This is powered by Microsoft's `markitdown` tool, which is designed to preserve important document structure and content like headings, lists, tables, and links for LLMs.

## Capabilities
MarkItDown supports the conversion from a wide variety of formats:
- **Documents**: PDF, Word (DOCX/DOC), PowerPoint (PPTX/PPT), EPubs
- **Data/Spreadsheets**: Excel (XLSX/XLS), CSV, JSON, XML
- **Media**: Images (EXIF metadata and OCR), Audio (EXIF metadata and speech transcription), YouTube video URLs
- **Web**: HTML and remote URLs
- **Archives**: ZIP files (iterates over contents)

## Usage Guide

### Conversion Process
1. **Identify Target**: Locate the file or URL to be converted.
2. **Execute Conversion**: Run the following command in the terminal:
   ```bash
   uvx markitdown <input_path_or_url>
   ```
3. **Verify Output**: Ensure the Markdown output captures the essential structure and content of the source.
4. **Output Output File**: Append `> output.md` or `-o output.md` to save directly to a file (`uvx markitdown docs.pdf -o markdown.md`).

### Example Prompts
- **For PDF Conversion**: "Convert the file at `./docs/report.pdf` to markdown using `uvx markitdown`."
- **For Excel Spreadsheets**: "Turn this spreadsheet into a markdown table: `uvx markitdown ./data/budget.xlsx`"
- **For Remote Web Content**: "Give me a markdown version of the content at `uvx markitdown https://example.com/article`"
- **For Archived Content**: "Convert all the files inside the archive to markdown: `uvx markitdown ./archive/data.zip`"
- **For Media Content**: "Extract the text from this image: `uvx markitdown ./images/receipt.jpg`"
- **For Video Content**: "Get the transcript and metadata from this video: `uvx markitdown <youtube_url>`"

