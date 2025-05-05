# Burned Area Classification in Central Kalimantan Using Sentinel-2 and Random Forest

This project uses Sentinel-2 imagery and a Random Forest classifier to map burned areas in Central Kalimantan, Indonesia, following the 2019 fire season. The workflow involves satellite data preprocessing, training sample preparation, spectral index computation, and supervised classification.

---

## 🔍 Study Area

- **Region**: Pulang Pisau Regency, Central Kalimantan, Indonesia
- **Timeframe**: Post-fire season (September–December 2019)

---

## 🛰️ Data Sources

- **Sentinel-2 L2A imagery** (10 bands, 10–20 m resolution)
- **Labeled training points** manually digitized in QGIS (burn / not burn)
- **Derived indices**: NDVI, NBR

---

## 📁 Directory Structure
data/
│
├── kalimantan-post-fire-images/ # Original Sentinel-2 tiles
├── post_fire_mosaic.tif # Mosaicked composite
├── post_fire_with_indices.tif # Composite + NDVI/NBR
├── burn_training_samples.geojson # Labeled training points (burn / not burn)
├── burned_area_classified.tif # Final classified raster


---

## ⚙️ Workflow Overview

### 1. **Data Preparation**
- Mosaic multiple Sentinel-2 tiles using `rasterio.merge`
- Save as `post_fire_mosaic.tif`

### 2. **Spectral Index Calculation**
- Compute NDVI: `(B8 - B4) / (B8 + B4)`
- Compute NBR: `(B8 - B12) / (B8 + B12)`
- Save all bands and indices into a stacked raster: `post_fire_with_indices.tif`

### 3. **Training Sample Creation**
- Digitize labeled points in QGIS (class = "burn" or "not burn")
- Export to `burn_training_samples.geojson`
- Sample raster values at point locations and build a labeled DataFrame

### 4. **Model Training**
- Use `scikit-learn` RandomForestClassifier
- Train/test split: 80/20
- Evaluate using a confusion matrix and feature importance

### 5. **Inference**
- Apply trained model to the full raster
- Generate classified burn map: `burned_area_classified.tif`

---

## 🧠 Requirements

- Python 3.9+
- `rasterio`, `geopandas`, `scikit-learn`, `numpy`, `matplotlib`, `joblib`, `seaborn`


