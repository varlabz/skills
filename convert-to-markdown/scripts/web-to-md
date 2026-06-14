#!/usr/bin/env -S uvx --with httpx python
"""Fetch a web page and convert it to Markdown."""

import argparse
import asyncio
import os
import sys
from pathlib import Path

import httpx

BASE = "http://localhost:11235"


def bail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


async def fetch(url, server):
    async with httpx.AsyncClient(base_url=server, timeout=120.0) as c:
        r = await c.get("/health", timeout=10.0)
        r.raise_for_status()
        r = await c.post(
            "/md", json={"url": url, "f": "fit", "q": None, "c": "0"}, timeout=120.0
        )
        r.raise_for_status()
        d = r.json()
        md = d.get("markdown", "")
        if not md and d.get("error"):
            bail(f"Server error: {d['error']}")
        return md


def main():
    p = argparse.ArgumentParser(
        description="Fetch a web page and convert it to Markdown."
    )
    p.add_argument("url")
    p.add_argument(
        "-s",
        "--server",
        default=os.getenv("CRAWL4AI_URL", BASE),
        help=f"Server URL (default: {BASE}, or $CRAWL4AI_URL)",
    )
    p.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        help="Write markdown to FILE instead of stdout",
    )
    a = p.parse_args()
    md = asyncio.run(fetch(a.url, a.server))
    if not md:
        bail("No markdown content returned for the given URL.")
    if a.output:
        Path(a.output).write_text(md, encoding="utf-8")
        print(f"Markdown saved to {a.output}", file=sys.stderr)
    else:
        print(md, end="")


if __name__ == "__main__":
    raise SystemExit(main())
