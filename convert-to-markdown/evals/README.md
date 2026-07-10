# convert-to-markdown — Eval Data

Reusable evaluation test cases for the convert-to-markdown skill.

## Structure

```
evals/
├── README.md              ← this file
├── eval-metadata.json     ← grading rubric, weights, config
└── cases/                 ← 18 individual test case JSON files
    ├── index.json         ← master index with all categories
    ├── pdf-conversion.json
    ├── youtube-transcript.json
    ├── ...
```

## Categories (18 total)

| Category | Cases |
|----------|-------|
| Core formats | PDF, DOCX, PPTX, XLSX, EPUB |
| Web & media | YouTube, web pages, MHTML |
| Structured data | CSV, JSON, XML |
| Media processing | Images (OCR), audio transcription |
| Archive & special | ZIP, HTML |
| Edge cases | Scanned PDFs, missing deps, unsupported formats, batch conversion |

## Grading Rubric

Each case scored out of 12 points:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Tool Selection | 3 | Correct tool/script for file type |
| Command Syntax | 2 | Proper flags/options used |
| Error Handling | 3 | Graceful failures with helpful messages |
| Output Quality | 2 | Reasonable markdown produced |
| Edge Case Awareness | 2 | Acknowledges limitations, suggests alternatives |

## Usage

To reuse in a future eval run:
1. Copy `evals/cases/` into a skill-creator iteration's cases directory
2. Reference `eval-metadata.json` for grading weights and config
3. Run via `/sc` or manually invoke prompts against the skill
