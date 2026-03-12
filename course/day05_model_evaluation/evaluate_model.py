"""
Day 5 — Model Evaluation and Accuracy
NERP AI Fundamentals

Measures how well the prediction model performs on unseen data
using accuracy, a classification report, and cross-validation.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, train_test_split

# ---------------------------------------------------------------------------
# 1. Load dataset
# ---------------------------------------------------------------------------
DATA_PATH = "../../datasets/system_metrics_sample.csv"

data = pd.read_csv(DATA_PATH)
print(f"Dataset shape: {data.shape}\n")

# ---------------------------------------------------------------------------
# 2. Define features and label
# ---------------------------------------------------------------------------
FEATURE_COLUMNS = ["cpu", "memory", "latency"]
TARGET_COLUMN = "failure"

X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]

# ---------------------------------------------------------------------------
# 3. Split into training and test sets (80 / 20)
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples : {len(X_train)}")
print(f"Testing  samples : {len(X_test)}\n")

# ---------------------------------------------------------------------------
# 4. Train the model on the training set
# ---------------------------------------------------------------------------
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ---------------------------------------------------------------------------
# 5. Evaluate on the test set
# ---------------------------------------------------------------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------------------------------------------------------
# 6. Cross-validation for a more reliable estimate
# ---------------------------------------------------------------------------
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Accuracy       : {cv_scores.mean():.2f}")
