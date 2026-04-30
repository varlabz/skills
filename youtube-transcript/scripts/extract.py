#!/usr/bin/env -S uvx --with yt-dlp python 
"""Extract YouTube transcripts."""

import argparse
import os
import re
import sys
import tempfile
import time
from typing import Tuple
from yt_dlp import YoutubeDL 


def clean_vtt(text: str) -> str:
    """Strip VTT markup and metadata, removing duplicate consecutive lines."""
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("WEBVTT"):
            continue
        if stripped.startswith("NOTE"):
            continue
        if "-->" in stripped:
            continue
        # Skip header lines like "Kind: captions", "Language: en"
        if re.match(r"^(Kind|Language|Voice|CSS):", stripped):
            continue
        line = re.sub(r"<[^>]+>", "", line).strip()
        if line and (not lines or lines[-1] != line):
            lines.append(line)
    return "\n".join(lines)


def _parse_input(value: str) -> Tuple[str, str]:
    """Extract video ID and canonical URL from a YouTube URL or ID."""
    patterns = [
        r"v=([a-zA-Z0-9_-]{6,})",
        r"youtu\.be/([a-zA-Z0-9_-]{6,})",
    ]
    for pat in patterns:
        match = re.search(pat, value)
        if match:
            video_id = match.group(1)
            return video_id, f"https://www.youtube.com/watch?v={video_id}"
    if re.fullmatch(r"[a-zA-Z0-9_-]{6,}", value):
        return value, f"https://www.youtube.com/watch?v={value}"
    raise RuntimeError("Could not parse video id from input")


def _format_info(info: dict) -> str:
    """Format video info dict into a string."""
    lines = []
    for key in ("title", "description", "channel", "upload_date", "duration", "view_count", "like_count", "channel_id", "channel_url", "tags", "categories", "license", "creator", "release_year", "average_rating", "comment_count", "age_limit", "webpage_url"):
        value = info.get(key)
        if value is None:
            continue
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        lines.append(f"{key}: {value}")
    lines.append("\n")
    return "\n".join(lines)


def _resolve_lang(info: dict, lang: str) -> str:
    """Resolve 'auto' to the video's detected source language.

    yt-dlp detects the source language and stores it in info['language'].
    Auto-generated captions exist in info['automatic_captions'] under
    the key 'ab' (a sentinel, not a real language code). Using 'ab'
    as subtitleslangs causes YouTube to return HTTP 429 because it
    tries to translate to Abkhazian which has no captions.
    """
    if lang != "auto":
        return lang
    # Use yt-dlp's detected source language (e.g. 'en')
    detected = info.get("language")
    if detected:
        return detected
    raise RuntimeError("No subtitles available for this video")


def extract_transcript(url: str, lang: str, raw: bool = False) -> Tuple[dict, str]:
    """Extract transcript from a YouTube video using the yt-dlp Python module.

    Performs a single extract_info call to get both video metadata and
    subtitle availability, then downloads the requested subtitles.

    Args:
        url: YouTube video URL.
        lang: Language code (e.g. 'en', 'de') or 'auto'.
        raw: If True, return raw VTT instead of cleaned text.

    Returns:
        Tuple of (info dict, cleaned transcript text or raw VTT).

    Raises:
        RuntimeError: If yt-dlp is not installed or no transcript is found.
    """

    # Single extract_info call to get metadata + subtitle info
    opts = {
        "skip_download": True,
        "quiet": True,
        "no_warnings": True,
    }
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)

    # Resolve 'auto' to the actual source language
    selected = _resolve_lang(info, lang)

    # Download subtitles
    with tempfile.TemporaryDirectory() as tmpdir:
        sub_opts = {
            "skip_download": True,
            "writeautomaticsub": True,
            "writesubtitles": True,
            "subtitleslangs": [selected],
            "subtitlesformat": "vtt",
            "outtmpl": os.path.join(tmpdir, "%(id)s.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "progress_hooks": [],
        }
        # Redirect actual file descriptors to suppress yt-dlp progress output
        devnull_fd = os.open(os.devnull, os.O_WRONLY)
        old_out_fd = os.dup(1)
        old_err_fd = os.dup(2)
        os.dup2(devnull_fd, 1)
        os.dup2(devnull_fd, 2)
        os.close(devnull_fd)

        try:
            time.sleep(2)  # Be polite to YouTube API between calls
            with YoutubeDL(sub_opts) as ydl:
                ydl.download([url])
        finally:
            os.dup2(old_out_fd, 1)
            os.dup2(old_err_fd, 2)
            os.close(old_out_fd)
            os.close(old_err_fd)

        vtt_files = [p for p in os.listdir(tmpdir) if p.endswith(".vtt")]
        if not vtt_files:
            raise RuntimeError("yt-dlp module did not produce a .vtt file")

        vtt_path = os.path.join(tmpdir, vtt_files[0])
        with open(vtt_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
            text = raw_text if raw else clean_vtt(raw_text)
            return info, text


def main() -> int:
    """CLI entry point for yt-dlp module transcript extraction."""
    parser = argparse.ArgumentParser(
        description="Extract YouTube transcript using yt-dlp Python module."
    )
    parser.add_argument("input", help="YouTube URL or video ID")
    parser.add_argument(
        "--lang",
        default="auto",
        help="Transcript language code (e.g. en, de) or 'auto'",
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Print raw VTT transcript without cleaning",
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Print video info (title, description, etc.)",
    )
    args = parser.parse_args()

    try:
        video_id, url = _parse_input(args.input)
    except Exception as exc:
        sys.stderr.write(f"Failed to parse input '{args.input}': {exc}\n")
        return 1

    try:
        info, text = extract_transcript(url, args.lang, raw=args.raw)
        if args.info:
            print(_format_info(info))
            print("script:")
        print(text)
        return 0
    except Exception as exc:
        sys.stderr.write(f"Failed to extract transcript for '{args.input}': {exc}\n")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
