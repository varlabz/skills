#!/usr/bin/env -S uvx --with httpx python
"""Fetch a web page and convert it to Markdown."""

import argparse
import asyncio
import os
import sys

import httpx

DEFAULT_BASE_URL = "http://localhost:11235"


async def fetch_markdown(url: str, base_url: str) -> str:
    """Fetch a page via the Crawl4AI /md endpoint and return its markdown."""
    async with httpx.AsyncClient(base_url=base_url, timeout=120.0) as client:
        # --- health check ---
        try:
            resp = await client.get("/health", timeout=10.0)
            resp.raise_for_status()
        except httpx.RequestError:
            print(f"Cannot reach Crawl4AI server at {base_url}", file=sys.stderr)
            sys.exit(1)
        except httpx.HTTPStatusError as e:
            print(
                f"Crawl4AI server health check failed (HTTP {e.response.status_code})",
                file=sys.stderr,
            )
            sys.exit(1)

        # --- fetch markdown ---
        payload = {"url": url, "f": "fit", "q": None, "c": "0"}
        try:
            resp = await client.post("/md", json=payload, timeout=120.0)
            resp.raise_for_status()
        except httpx.TimeoutException:
            print(f"Request timed out while fetching {url}", file=sys.stderr)
            sys.exit(1)
        except httpx.HTTPStatusError as e:
            print(
                f"Crawl4AI server returned HTTP {e.response.status_code}",
                file=sys.stderr,
            )
            if e.response.text:
                print(e.response.text[:500], file=sys.stderr)
            sys.exit(1)
        except httpx.RequestError as e:
            print(f"Request failed: {e}", file=sys.stderr)
            sys.exit(1)

        data = resp.json()
        markdown = data.get("markdown", "")
        if not markdown and data.get("error"):
            print(f"Server error: {data['error']}", file=sys.stderr)
            sys.exit(1)
        return markdown


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch a web page and convert it to Markdown.",
    )
    parser.add_argument("url", help="URL of the web page to fetch")
    parser.add_argument(
        "--server",
        "-s",
        default=os.getenv("CRAWL4AI_URL", DEFAULT_BASE_URL),
        help=f"Server URL (default: {DEFAULT_BASE_URL}, or $CRAWL4AI_URL)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Write markdown to FILE instead of stdout",
        metavar="FILE",
    )
    args = parser.parse_args()

    markdown = asyncio.run(fetch_markdown(args.url, args.server))

    if not markdown:
        print("No markdown content returned for the given URL.", file=sys.stderr)
        return 1

    # Write to file or stdout
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Markdown saved to {args.output}", file=sys.stderr)
    else:
        print(markdown, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
