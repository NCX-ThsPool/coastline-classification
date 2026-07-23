"""Minimal reusable supervised image-classification trainer."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from coastline.utils.filesystem import ensure_directory


@dataclass(frozen=True)
class EpochResult:
    loss: float
    accuracy: float


class Trainer:
    """Train and validate a PyTorch classifier with best-checkpoint saving."""

    def __init__(self, model: Any, optimizer: Any, criterion: Any, device: Any) -> None:
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device
        self.model.to(device)

    def _run_epoch(self, loader: Any, training: bool) -> EpochResult:
        import torch

        self.model.train(training)
        loss_total = 0.0
        correct = 0
        samples = 0

        context = torch.enable_grad() if training else torch.no_grad()
        with context:
            for inputs, labels in loader:
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)

                if training:
                    self.optimizer.zero_grad(set_to_none=True)

                outputs = self.model(inputs)
                if hasattr(outputs, "logits"):
                    outputs = outputs.logits
                elif isinstance(outputs, tuple):
                    outputs = outputs[0]

                loss = self.criterion(outputs, labels)
                if training:
                    loss.backward()
                    self.optimizer.step()

                batch_size = labels.shape[0]
                loss_total += float(loss.item()) * batch_size
                correct += int((outputs.argmax(dim=1) == labels).sum().item())
                samples += batch_size

        return EpochResult(
            loss=loss_total / max(samples, 1),
            accuracy=correct / max(samples, 1),
        )

    def fit(
        self,
        train_loader: Any,
        validation_loader: Any,
        *,
        epochs: int,
        output_directory: str | Path,
    ) -> list[dict[str, float]]:
        import torch

        output = ensure_directory(output_directory)
        history: list[dict[str, float]] = []
        best_accuracy = -1.0

        for epoch in range(1, epochs + 1):
            train_result = self._run_epoch(train_loader, training=True)
            validation_result = self._run_epoch(validation_loader, training=False)

            record = {
                "epoch": float(epoch),
                "train_loss": train_result.loss,
                "train_accuracy": train_result.accuracy,
                "validation_loss": validation_result.loss,
                "validation_accuracy": validation_result.accuracy,
            }
            history.append(record)

            if validation_result.accuracy > best_accuracy:
                best_accuracy = validation_result.accuracy
                torch.save(self.model.state_dict(), output / "best_model.pth")

        return history
