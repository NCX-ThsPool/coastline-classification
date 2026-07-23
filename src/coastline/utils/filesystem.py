"""Filesystem helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def ensure_directory(path: str | Path) -> Path:
    """Create a directory if necessary and return it as a Path."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def iter_files(
    directory: str | Path,
    suffixes: Iterable[str],
    recursive: bool = False,
) -> list[Path]:
    """Return deterministically sorted files whose suffix matches."""
    root = Path(directory)
    normalized = {suffix.lower() for suffix in suffixes}
    iterator = root.rglob("*") if recursive else root.glob("*")
    return sorted(
        path for path in iterator
        if path.is_file() and path.suffix.lower() in normalized
    )
