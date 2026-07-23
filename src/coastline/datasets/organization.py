"""Image-dataset organization helpers."""

from __future__ import annotations

import shutil
from pathlib import Path

import pandas as pd

from coastline.utils.filesystem import ensure_directory


def organize_images_by_label(
    table: pd.DataFrame,
    *,
    uid_column: str,
    label_column: str,
    source_directory: str | Path,
    output_directory: str | Path,
    suffix: str = ".jpg",
    copy: bool = True,
) -> dict[str, int]:
    """Copy or move UID-named images into one directory per label."""
    source = Path(source_directory)
    output = ensure_directory(output_directory)
    counts: dict[str, int] = {}

    for row in table.itertuples(index=False):
        uid = str(getattr(row, uid_column))
        label = str(getattr(row, label_column))
        source_path = source / f"{uid}{suffix}"
        if not source_path.is_file():
            continue

        label_directory = ensure_directory(output / label)
        destination = label_directory / source_path.name
        if copy:
            shutil.copy2(source_path, destination)
        else:
            shutil.move(str(source_path), destination)
        counts[label] = counts.get(label, 0) + 1

    return counts
