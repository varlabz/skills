#!/usr/bin/env python3
"""Extract HTML from an MHTML file or URL pointing to an MHTML resource."""

import argparse
import sys
import urllib.request
from email import message_from_bytes, message_from_string


def extract_html(mhtml_content: bytes) -> str:
    """Return the largest HTML part from MHTML content."""
    msg = message_from_bytes(mhtml_content)
    largest_html = None
    largest_size = 0

    for part in msg.walk():
        if part.get_content_type() == "text/html":
            payload = part.get_payload(decode=True)
            if payload:
                charset = part.get_content_charset() or "utf-8"
                html = payload.decode(charset, errors="replace")
                if len(html) > largest_size:
                    largest_size = len(html)
                    largest_html = html

    return largest_html or ""


def load_mhtml(source: str) -> bytes:
    """Load MHTML content from a file path or URL."""
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract HTML from an MHTML file or URL."
    )
    parser.add_argument("source", help="Path to an MHTML file or URL")
    args = parser.parse_args()

    content = load_mhtml(args.source)
    html = extract_html(content)

    if not html:
        print("No HTML content found in the MHTML source.", file=sys.stderr)
        sys.exit(1)

    print(html)
