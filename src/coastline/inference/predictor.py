"""Batch image-classification prediction."""

from __future__ import annotations

from typing import Any

import numpy as np


class Predictor:
    """Device-aware PyTorch predictor."""

    def __init__(self, model: Any, device: Any) -> None:
        self.model = model.to(device)
        self.device = device
        self.model.eval()

    def predict_loader(self, loader: Any) -> tuple[np.ndarray, np.ndarray]:
        import torch

        labels: list[np.ndarray] = []
        probabilities: list[np.ndarray] = []

        with torch.no_grad():
            for inputs, *_ in loader:
                outputs = self.model(inputs.to(self.device))
                if hasattr(outputs, "logits"):
                    outputs = outputs.logits
                elif isinstance(outputs, tuple):
                    outputs = outputs[0]
                batch_probabilities = torch.softmax(outputs, dim=1)
                probabilities.append(batch_probabilities.cpu().numpy())
                labels.append(batch_probabilities.argmax(dim=1).cpu().numpy())

        return np.concatenate(labels), np.concatenate(probabilities)
