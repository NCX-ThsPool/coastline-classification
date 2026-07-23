"""Logging configuration."""

from __future__ import annotations

import logging
from pathlib import Path


def configure_logging(
    level: int = logging.INFO,
    log_file: str | Path | None = None,
) -> logging.Logger:
    """Configure a package logger without duplicating handlers."""
    logger = logging.getLogger("coastline")
    logger.setLevel(level)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

        if log_file is not None:
            target = Path(log_file)
            target.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(target, encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
