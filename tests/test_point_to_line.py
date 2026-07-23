import pandas as pd

from coastline.inference.point_to_line import majority_label_by_group


def test_majority_label() -> None:
    frame = pd.DataFrame(
        {
            "line_id": [1, 1, 1, 2],
            "predicted_label": [0, 0, 3, 4],
        }
    )
    result = majority_label_by_group(
        frame,
        group_column="line_id",
        label_column="predicted_label",
    )
    labels = dict(zip(result["line_id"], result["predicted_label"]))
    assert labels == {1: 0, 2: 4}
