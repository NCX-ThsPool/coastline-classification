"""Training-time metric accumulation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RunningAverage:
    total: float = 0.0
    count: int = 0

    def update(self, value: float, count: int = 1) -> None:
        self.total += value * count
        self.count += count

    @property
    def average(self) -> float:
        return self.total / self.count if self.count else 0.0
