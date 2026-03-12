"""
Day 4 — Training Your First Machine Learning Model
NERP AI Fundamentals

Loads the system metrics dataset, trains a Decision Tree classifier,
and makes a prediction on a new telemetry sample.
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# ---------------------------------------------------------------------------
# 1. Load dataset
# ---------------------------------------------------------------------------
DATA_PATH = "../../datasets/system_metrics_sample.csv"

data = pd.read_csv(DATA_PATH)

print("Dataset Preview:")
print(data)
print()

# ---------------------------------------------------------------------------
# 2. Define features and label
# ---------------------------------------------------------------------------
FEATURE_COLUMNS = ["cpu", "memory", "latency"]
TARGET_COLUMN = "failure"

X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]

# ---------------------------------------------------------------------------
# 3. Create and train the model
# ---------------------------------------------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

print("Model trained successfully.\n")

# ---------------------------------------------------------------------------
# 4. Make a prediction on a new telemetry sample
# ---------------------------------------------------------------------------
# cpu=92, memory=85, latency=110 — high-stress system metrics
sample = pd.DataFrame([{"cpu": 92, "memory": 85, "latency": 110}])
prediction = model.predict(sample[FEATURE_COLUMNS])

label = "failure risk" if prediction[0] == 1 else "healthy"
print(f"Sample  : cpu=92, memory=85, latency=110")
print(f"Prediction: {prediction[0]} ({label})")
