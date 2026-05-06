#!/usr/bin/env -S uvx --with markitdown python 
"""Convert MHTML (file or URL) to Markdown using MarkItDown."""

import argparse
import io
import sys
import urllib.request
from email import message_from_bytes
from markitdown import MarkItDown

def extract_html(mhtml_content: bytes) -> str:
    """Return the largest text/html MIME part from MHTML content."""
    msg = message_from_bytes(mhtml_content)
    largest_html = None
    largest_size = 0

    for part in msg.walk():
        if part.get_content_type() == "text/html":
            payload = part.get_payload(decode=True)
            if payload:
                charset = part.get_content_charset() or "utf-8"
                html = payload.decode(charset, errors="replace")
                # Heuristic: the primary page is usually the largest HTML part.
                if len(html) > largest_size:
                    largest_size = len(html)
                    largest_html = html

    return largest_html or ""


def load_mhtml(source: str) -> bytes:
    """Load raw MHTML bytes from a local path or HTTP(S) URL."""
    if source.startswith("http://") or source.startswith("https://"):
        req = urllib.request.Request(
            source,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()
    else:
        with open(source, "rb") as f:
            return f.read()


def html_to_markdown(html: str) -> str:
    """Convert HTML text to Markdown via MarkItDown's stream API."""
    stream = io.BytesIO(html.encode("utf-8"))
    result = MarkItDown().convert_stream(stream, file_extension=".html")
    return result.text_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert MHTML content from a file or URL into Markdown."
    )
    parser.add_argument("source", help="Path to an MHTML file or URL")
    args = parser.parse_args()

    content = load_mhtml(args.source)
    html = extract_html(content)

    if not html:
        print("No HTML content found in the MHTML source.", file=sys.stderr)
        sys.exit(1)

    markdown = html_to_markdown(html)
    print(markdown)
