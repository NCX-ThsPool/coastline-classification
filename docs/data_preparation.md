# Data preparation

No nationwide raster or vector dataset is distributed in this repository.

Recommended local layout:

```text
data/
├── raw/
│   ├── sentinel2/
│   ├── google_imagery/
│   ├── dem/
│   ├── grids/
│   └── boundaries/
├── external/
│   └── reference_products/
├── interim/
│   ├── indices/
│   ├── water_masks/
│   ├── extracted_coastlines/
│   └── image_tiles/
└── processed/
    ├── training_samples/
    ├── validation_samples/
    └── coastline_products/
```

The original research referenced OSM coastlines, SRTM DEM, administrative
boundaries, GCL_FCS30, GCTD100, and other coastline products. Users must obtain
each source under its own license and document the version, acquisition date,
spatial reference, and processing history.

A local path configuration should be copied from
`configs/paths.example.yaml` to `configs/paths.local.yaml`. The local file is
ignored by Git.
