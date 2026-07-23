from coastline.evaluation.classification import evaluate_classification


def test_perfect_classification() -> None:
    report = evaluate_classification([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
    assert report.accuracy == 1.0
    assert report.kappa == 1.0
    assert report.macro_f1 == 1.0
