"""
Day 3 — Features and Datasets
NERP AI Fundamentals

Loads the system metrics dataset, inspects its structure,
and prints a summary of features and label distribution.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------------------------
DATA_PATH = "../../datasets/system_metrics_sample.csv"

data = pd.read_csv(DATA_PATH)

# ---------------------------------------------------------------------------
# 2. Preview the data
# ---------------------------------------------------------------------------
print("Dataset Preview:")
print(data)
print()

# ---------------------------------------------------------------------------
# 3. Dataset shape (rows, columns)
# ---------------------------------------------------------------------------
print(f"Rows   : {data.shape[0]}")
print(f"Columns: {data.shape[1]}")
print()

# ---------------------------------------------------------------------------
# 4. Feature columns and label
# ---------------------------------------------------------------------------
FEATURE_COLUMNS = ["cpu", "memory", "latency"]
TARGET_COLUMN = "failure"

print(f"Features : {FEATURE_COLUMNS}")
print(f"Label    : {TARGET_COLUMN}")
print()

# ---------------------------------------------------------------------------
# 5. Basic statistics for each feature
# ---------------------------------------------------------------------------
print("Feature Statistics:")
print(data[FEATURE_COLUMNS].describe())
print()

# ---------------------------------------------------------------------------
# 6. Label distribution
# ---------------------------------------------------------------------------
print("Label Distribution:")
print(data[TARGET_COLUMN].value_counts().rename({0: "healthy (0)", 1: "failure (1)"}))
