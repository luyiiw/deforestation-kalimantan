# burn_classify.py

import numpy as np
import rasterio
from sklearn.externals import joblib  # or from joblib import load
from sklearn.ensemble import RandomForestClassifier

# Load trained model
rf = joblib.load("rf_model.pkl")

# Load raster
with rasterio.open("data/post_fire_with_indices.tif") as src:
    data = src.read()
    profile = src.profile
    rows, cols = data.shape[1], data.shape[2]

# Reshape and clean
X = data.reshape((data.shape[0], -1)).T
X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

# Predict
y_pred = rf.predict(X)
classified = y_pred.reshape((rows, cols))

# Save
profile.update(count=1, dtype='uint8')
with rasterio.open("data/burned_area_classified.tif", "w", **profile) as dst:
    dst.write(classified.astype("uint8"), 1)

print("Classification complete.")
