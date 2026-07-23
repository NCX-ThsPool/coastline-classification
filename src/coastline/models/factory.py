"""Unified model construction."""

from __future__ import annotations

from typing import Any


SUPPORTED_MODELS = {
    "convnext_tiny",
    "resnet50",
    "densenet121",
    "efficientnet_b0",
    "inception_v3",
    "vgg16",
}


def _replace_first_convolution(model: Any, input_channels: int) -> None:
    """Replace a common first convolution while retaining output dimensions."""
    import torch.nn as nn

    candidates = (
        ("features", 0, 0),
        ("conv1",),
    )

    for candidate in candidates:
        try:
            if len(candidate) == 3:
                block = getattr(model, candidate[0])[candidate[1]][candidate[2]]
                replacement = nn.Conv2d(
                    input_channels,
                    block.out_channels,
                    kernel_size=block.kernel_size,
                    stride=block.stride,
                    padding=block.padding,
                    bias=block.bias is not None,
                )
                getattr(model, candidate[0])[candidate[1]][candidate[2]] = replacement
                return
            block = getattr(model, candidate[0])
            replacement = nn.Conv2d(
                input_channels,
                block.out_channels,
                kernel_size=block.kernel_size,
                stride=block.stride,
                padding=block.padding,
                bias=block.bias is not None,
            )
            setattr(model, candidate[0], replacement)
            return
        except (AttributeError, IndexError, TypeError):
            continue

    raise ValueError("Could not locate the model's first convolution.")


def create_model(
    name: str,
    *,
    num_classes: int = 5,
    input_channels: int = 3,
    pretrained: bool = True,
):
    """Create a torchvision classifier with a configurable input channel count."""
    try:
        import torch.nn as nn
        from torchvision import models
    except ImportError as exc:
        raise RuntimeError("Model creation requires the 'ml' optional dependencies.") from exc

    normalized = name.lower()
    if normalized not in SUPPORTED_MODELS:
        raise ValueError(f"Unsupported model: {name}")

    weights = "DEFAULT" if pretrained else None

    if normalized == "convnext_tiny":
        model = models.convnext_tiny(weights=weights)
        model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
    elif normalized == "resnet50":
        model = models.resnet50(weights=weights)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif normalized == "densenet121":
        model = models.densenet121(weights=weights)
        model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    elif normalized == "efficientnet_b0":
        model = models.efficientnet_b0(weights=weights)
        model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
    elif normalized == "inception_v3":
        model = models.inception_v3(weights=weights, aux_logits=True)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    else:
        model = models.vgg16(weights=weights)
        model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)

    if input_channels != 3:
        _replace_first_convolution(model, input_channels)

    return model
