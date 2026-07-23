from __future__ import annotations

import argparse
from pathlib import Path

from coastline.utils.config import load_config

def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the high-resolution training configuration.")
    parser.add_argument("--config", required=True)
    arguments = parser.parse_args()
    config = load_config(arguments.config)

    model = config["model"]
    data = config["data"]
    print(
        "High-resolution training configuration loaded:",
        f"model={model['name']}",
        f"channels={data['input_channels']}",
        f"image_size={data['image_size']}",
    )
    print("Dataset-specific DataLoader construction is intentionally left to the data adapter.")


if __name__ == "__main__":
    main()
