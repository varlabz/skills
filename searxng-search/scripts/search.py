#!/usr/bin/env python3
"""Search a local SearXNG instance and output results."""

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_URL = "http://localhost:8080"

SEARXNG_CATEGORIES = [
    "general",
    "images",
    "videos",
    "news",
    "map",
    "music",
    "it",
    "science",
    "files",
    "social media",
]


def search(query, engine="general", max_results=10, language="en-US",
           safesearch=0, time_range=None, base_url=None):
    """Perform a search and return parsed results."""
    base_url = base_url or os.environ.get("SEARXNG_URL", DEFAULT_URL)

    params = {
        "q": query,
        "format": "json",
        "engines": engine,
        "language": language,
        "safesearch": str(safesearch),
        "pageno": "1",
    }
    if time_range:
        params["time_range"] = time_range

    url = f"{base_url.rstrip('/')}/search?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "local-searxng-skill/1.0"})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        print(f"Error: Could not reach SearXNG at {base_url}", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: SearXNG returned invalid JSON", file=sys.stderr)
        sys.exit(1)

    results = data.get("results", [])
    return results[:max_results]


def format_text(results, query):
    """Format results as a numbered text list."""
    if not results:
        print(f"No results found for: {query}")
        return

    print(f"Search results for: {query}\n")
    for i, r in enumerate(results, 1):
        title = r.get("title", "Untitled")
        url = r.get("url", "")
        snippet = r.get("content", "")
        engine = r.get("engine", "")
        print(f"{i}. {title}")
        print(f"   {url}")
        if snippet:
            print(f"   {snippet[:200]}")
        if engine:
            print(f"   Source: {engine}")
        print()


def format_json(results):
    """Format results as JSON."""
    output = []
    for r in results:
        output.append({
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "engine": r.get("engine", ""),
            "score": r.get("score", 0),
            "content": r.get("content", ""),
            "img_src": r.get("img_src", ""),
        })
    print(json.dumps(output, indent=2, ensure_ascii=False))


def main():
    cat_help = f"SearXNG category: {', '.join(SEARXNG_CATEGORIES)}"
    parser = argparse.ArgumentParser(
        description="Search a local SearXNG instance",
        epilog="Set SEARXNG_URL environment variable to override the default instance URL."
    )
    parser.add_argument("query", nargs="+", help="Search query")
    parser.add_argument("--engine", "-e", default="general",
                        choices=SEARXNG_CATEGORIES,
                        help=cat_help)
    parser.add_argument("--max-results", "-n", type=int, default=10,
                        help="Maximum results to return")
    parser.add_argument("--language", "-l", default="en-US",
                        help="Language code (e.g. en-US, zh-CN)")
    parser.add_argument("--safesearch", "-s", type=int, default=0,
                        choices=[0, 1, 2],
                        help="Safe search: 0=off, 1=moderate, 2=strict")
    parser.add_argument("--time-range", "-t", default=None,
                        choices=["day", "week", "month", "year"],
                        help="Filter by time range")
    parser.add_argument("--format", "-f", default="json",
                        choices=["text", "json"],
                        help="Output format")
    parser.add_argument("--url", default=None,
                        help="SearXNG instance URL (overrides SEARXNG_URL env)")
    args = parser.parse_args()

    query = " ".join(args.query)
    results = search(
        query=query,
        engine=args.engine,
        max_results=args.max_results,
        language=args.language,
        safesearch=args.safesearch,
        time_range=args.time_range,
        base_url=args.url,
    )

    if args.format == "json":
        format_json(results)
    else:
        format_text(results, query)


if __name__ == "__main__":
    main()
