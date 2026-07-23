# Platform-specific dependencies

## ArcGIS Pro / ArcPy

Some historical scripts used ArcPy for projection, line-to-polygon conversion,
feature creation, field updates, and in-memory geoprocessing. ArcPy is not
installable from PyPI and is therefore not listed as a package dependency.

## QGIS Python

Historical Google imagery export scripts used `qgis.core` and the QGIS
processing framework. They must run inside a compatible QGIS Python environment.
The public package does not automatically access Google imagery and does not
embed tile credentials.

## Google Earth Engine

Install the `gee` optional dependency and authenticate separately. The project
ID must be supplied through `EE_PROJECT` or local YAML configuration.
