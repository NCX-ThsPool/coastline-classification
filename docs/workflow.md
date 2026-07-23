# Research workflow

## 1. Data acquisition

The source code used Google Earth Engine to download
`COPERNICUS/S2_SR_HARMONIZED` imagery over a 0.1-degree grid. The documented
seasonal window was April 1 to October 31, with a scene cloud threshold below
80 percent and SCL-based masking.

The public refactoring replaces duplicated band-specific scripts with one
`Sentinel2ExportConfig`. Earth Engine project identifiers and local Google Drive
paths are supplied through local configuration.

## 2. Spectral indices

The package implements MNDWI, NDWI, NDVI, EVI, RVI, NDBI, and LTidel.
Twenty-metre SWIR bands should be resampled to the target ten-metre grid before
index calculation. Resampling remains an explicit preprocessing decision rather
than being silently performed inside the formulas.

## 3. Coastline extraction

The extraction path is:

1. Otsu thresholding on valid index pixels.
2. Binary water-mask construction.
3. Connected-component filtering.
4. Optional 2-by-2 structural requirement.
5. Internal-hole filling.
6. Marching-squares subpixel contour extraction.
7. Pixel-to-world coordinate transformation.
8. Vector post-processing in GIS software when necessary.

## 4. Classification datasets

High-resolution data use RGB image tiles and 256-by-256 windows. Mid-resolution
experiments use fourteen-channel feature stacks and 32-by-32 windows. Sampling
utilities support fixed-distance points along LineString and MultiLineString
geometries.

## 5. Model training

The stable research line uses ConvNeXt. High-resolution classification uses RGB
inputs without channel attention. Mid-resolution classification uses a
multi-channel input adapter and prior-initialized learnable channel weighting.

Historical comparison scripts for VGG16, ResNet50, InceptionV3, DenseNet121,
EfficientNet, EVA-02, FasterViT, and SigLIP2 were consolidated conceptually into
a model factory. Model-specific research code remains traceable in the migration
inventory but is not copied verbatim.

## 6. Product generation and evaluation

Point predictions are aggregated to line identifiers by majority vote.
Evaluation includes overall accuracy, Cohen's Kappa, Macro-F1, per-class
precision, recall, F1 and IoU, transition matrices, and classified coastline
length summaries.
