"""Prior-initialized channel weighting for multi-channel coastline classification."""

from __future__ import annotations


def normalize_prior(prior: list[float]) -> list[float]:
    """Normalize positive prior values to a mean of one."""
    if not prior:
        raise ValueError("prior cannot be empty")
    if any(value < 0 for value in prior):
        raise ValueError("prior values cannot be negative")
    mean = sum(prior) / len(prior)
    if mean == 0:
        return [1.0 for _ in prior]
    return [value / mean for value in prior]


class PriorChannelWeighting:
    """Factory wrapper that delays PyTorch import until instantiated."""

    def __new__(cls, prior: list[float], learnable: bool = True):
        try:
            import torch
            import torch.nn as nn
        except ImportError as exc:
            raise RuntimeError("Channel attention requires the 'ml' dependencies.") from exc

        normalized = torch.tensor(normalize_prior(prior), dtype=torch.float32)

        class _Module(nn.Module):
            def __init__(self) -> None:
                super().__init__()
                self.register_buffer("prior", normalized)
                self.correction = nn.Parameter(torch.zeros_like(normalized), requires_grad=learnable)

            def forward(self, inputs):
                weights = self.prior + self.correction
                return inputs * weights.view(1, -1, 1, 1)

        return _Module()
