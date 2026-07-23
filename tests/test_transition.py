import pandas as pd

from coastline.evaluation.transition import transition_matrix


def test_transition_matrix_shape() -> None:
    frame = pd.DataFrame({"before": [0, 0, 1], "after": [0, 1, 1]})
    result = transition_matrix(
        frame,
        from_column="before",
        to_column="after",
        labels=[0, 1, 2, 3, 4],
    )
    assert result.shape == (5, 5)
    assert result.loc[0, 1] == 1
