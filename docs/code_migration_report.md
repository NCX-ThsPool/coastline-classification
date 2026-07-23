# Code migration report

## Source reviewed

The migration inventory covers **469 Python files** extracted
from the supplied merged source archive. The complete source was used as a
functional reference, but was not copied into the public repository.

## Classification summary

### By functional domain

- `datasets`: 40
- `download`: 33
- `evaluation`: 54
- `extraction`: 7
- `indices`: 8
- `inference`: 68
- `models`: 15
- `training`: 112
- `utils`: 132

### By disposition

- `ARCHIVE`: 165
- `MERGE`: 34
- `REWRITE`: 270

Definitions:

- `REWRITE`: the script represents useful functionality and informed a clean
  implementation.
- `MERGE`: the script is a versioned variant whose behavior belongs in a single
  configurable implementation.
- `ARCHIVE`: the path or filename identifies it as archived, temporary, draft,
  test, or failed experimental code. It remains traceable but is not public
  package code.

## Consolidation decisions

1. Band-specific Earth Engine scripts were represented by one export
   configuration and collection builder.
2. Seven coastal indices were implemented as tested numerical functions.
3. Otsu, morphology, hole filling, and subpixel contour extraction were split
   into independent modules.
4. Dataset scripts were reorganized by sampling, splitting, organization, and
   validation responsibilities.
5. Repeated model-specific training loops were represented by a model factory
   and one reusable trainer.
6. Repeated inference scripts were represented by a generic predictor and
   point-to-line aggregation.
7. Paper tables and plots were separated from reusable metric and transition
   calculations.
8. ArcPy and QGIS operations were documented as optional platform workflows
   rather than pretending they are portable PyPI dependencies.

## Important limitation

A clean public repository cannot reproduce the full national products without
the original imagery, interpreted labels, reference products, coordinate-system
decisions, and trained weights. Those artifacts were not supplied as distributable
inputs and are intentionally not fabricated.
