"""Pexels API utilities for video search and download."""

import os
import requests

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")


class PexelsVideoNotFoundError(Exception):
    """Exception raised when no suitable Pexels video is found."""


def search_pexels_video(query="calm", orientation="portrait", duration=30):
    """Search for videos on Pexels API."""
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "orientation": orientation, "per_page": 5}
    res = requests.get(
        "https://api.pexels.com/videos/search",
        headers=headers,
        params=params,
        timeout=90,
    )
    res.raise_for_status()
    data = res.json()

    for video in data.get("videos", []):
        # Try to find a clip close to desired duration
        if video.get("duration", 0) >= duration:
            return video["video_files"][0]["link"]  # Usually MP4

    raise PexelsVideoNotFoundError("No suitable Pexels video found.")


def download_video(url, filename="pexels_video.mp4"):
    """Download video from URL and save to file."""
    print(f"📥 Downloading Pexels video:\n{url}")
    video = requests.get(url, timeout=90)
    with open(filename, "wb") as f:
        f.write(video.content)
    print(f"✅ Saved video to {filename}")
