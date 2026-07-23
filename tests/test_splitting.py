import pandas as pd

from coastline.datasets.splitting import stratified_split


def test_stratified_split_preserves_all_rows() -> None:
    frame = pd.DataFrame(
        {
            "id": range(100),
            "label": [index % 5 for index in range(100)],
        }
    )
    split = stratified_split(
        frame,
        "label",
        validation_fraction=0.2,
        test_fraction=0.1,
    )
    assert len(split.train) + len(split.validation) + len(split.test) == len(frame)
    assert set(split.train["label"]) == {0, 1, 2, 3, 4}
