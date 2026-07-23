import numpy as np

from coastline.indices.spectral import mndwi, ndbi, ndvi, ndwi


def test_normalized_indices_are_finite() -> None:
    green = np.array([[1.0, 0.0]], dtype=np.float32)
    nir = np.array([[0.0, 0.0]], dtype=np.float32)
    swir = np.array([[0.5, 0.0]], dtype=np.float32)

    for result in (
        ndwi(green, nir),
        mndwi(green, swir),
        ndvi(nir, green),
        ndbi(swir, nir),
    ):
        assert np.isfinite(result).all()
