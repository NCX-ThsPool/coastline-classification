"""Dataset validation functions."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def find_missing_uid_files(
    uids: Iterable[str | int],
    directory: str | Path,
    suffix: str,
) -> list[str]:
    """Return UIDs whose expected files are absent."""
    root = Path(directory)
    return [
        str(uid)
        for uid in uids
        if not (root / f"{uid}{suffix}").is_file()
    ]
