# AI Fundamentals in 7 Days
## Day 5 — Model Evaluation and Accuracy

**Created by Emmanuel Naweji, 2026**

Welcome to **Day 5** of the *AI Fundamentals in 7 Days* learning journey.

In **Day 1**, we prepared our development environment.
In **Day 2**, we discussed what Artificial Intelligence is and how machines learn from data.
In **Day 3**, we explored features and datasets.
In **Day 4**, we trained our first machine learning model.

Today we ask the most important question:

**How do we know if our model is actually good?**

This lesson covers **model evaluation** — the process of measuring how accurately a model makes predictions.

---

# Why Evaluation Matters

Training a model is only half the work.

A model that performs well on training data but fails on new data is not useful.

We must evaluate the model on data it has never seen before.

This is called **testing on unseen data**.

---

# Train / Test Split

The standard approach is to split the dataset into two parts:

| Split | Purpose |
|-------|---------|
| Training set | The model learns patterns from this data |
| Test set | The model is evaluated on this data |

A typical split is:

- **80%** training
- **20%** testing

The model never sees the test set during training. This gives an honest measure of real-world performance.

---

# Key Evaluation Metrics

## Accuracy

Accuracy measures the percentage of correct predictions.

$$\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} \times 100$$

Example: 9 correct out of 10 predictions = 90% accuracy.

## Precision

Precision measures how many predicted positives were actually positive.

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

## Recall

Recall measures how many actual positives the model correctly identified.

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

## F1 Score

F1 is the balance between precision and recall.

$$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

# Cross-Validation

A single train/test split can be misleading if the split is lucky or unlucky.

**Cross-validation** solves this by splitting the data multiple times and averaging the results.

The most common method is **k-Fold Cross-Validation**:

1. Split data into k equal parts (folds)
2. Train on k-1 folds, test on the remaining fold
3. Repeat k times, each time using a different fold as the test set
4. Average the scores

This gives a more reliable measure of model performance.

---

# Project Structure

Your project should now look like this:

```
nerp-ai/
├── .venv/
├── datasets/
│   └── system_metrics.csv
├── train_model.py        (Day 4)
├── evaluate_model.py     (Day 5 — new)
└── README.md
```

---

# Step 1: Activate Your Virtual Environment

```sh
source .venv/bin/activate
```

Windows:

```sh
.venv\Scripts\activate
```

---

# Step 2: Install Required Libraries

```sh
pip install pandas scikit-learn
```

---

# Step 3: Run the Evaluation Script

```sh
python evaluate_model.py
```

---

# Understanding the Output

Example output:

```
Dataset shape: (10, 4)

Training samples : 8
Testing  samples : 2

Accuracy: 1.00

Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         1
           1       1.00      1.00      1.00         1

Cross-Validation Scores: [1. 0.5 1. 1. 1.]
Mean CV Accuracy       : 0.90
```

| Term | Meaning |
|------|---------|
| Accuracy | Overall percentage of correct predictions |
| Precision | How often positive predictions are correct |
| Recall | How often actual positives are found |
| F1 Score | Balanced measure of precision and recall |
| CV Mean | Average accuracy across multiple splits |

---

# How This Connects to NERP

In the **NERP platform**, model evaluation is critical before deploying any AI component.

A model that incorrectly predicts failures as normal could miss real incidents.

A model that flags too many false alarms causes alert fatigue.

Evaluation metrics help balance these trade-offs and ensure the model is reliable before it drives automation.

---

# Script Walkthrough — `evaluate_model.py`

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, train_test_split
```

`import pandas as pd` — loads pandas for reading and managing the dataset.

`from sklearn.ensemble import RandomForestClassifier` — imports the Random Forest model. A Random Forest trains many Decision Trees and combines their votes for a more reliable prediction than a single tree.

`from sklearn.metrics import accuracy_score, classification_report` — imports two evaluation tools from scikit-learn:
- `accuracy_score` computes the percentage of correct predictions.
- `classification_report` prints precision, recall, and F1 score for each class.

`from sklearn.model_selection import cross_val_score, train_test_split` — imports two data-splitting utilities:
- `train_test_split` divides the dataset into a training portion and a test portion.
- `cross_val_score` runs k-fold cross-validation and returns a score for each fold.

---

```python
DATA_PATH = "../../datasets/system_metrics_sample.csv"
data = pd.read_csv(DATA_PATH)
print(f"Dataset shape: {data.shape}\n")
```

`DATA_PATH` — the path to the dataset file relative to this script's location.

`pd.read_csv(DATA_PATH)` — loads the CSV into a DataFrame.

`data.shape` — returns `(rows, columns)`. Printing it before splitting confirms the dataset loaded correctly.

---

```python
FEATURE_COLUMNS = ["cpu", "memory", "latency"]
TARGET_COLUMN = "failure"

X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]
```

`X` — the feature matrix containing the three input columns.

`y` — the label vector the model will learn to predict.

---

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

`train_test_split(X, y, test_size=0.2, random_state=42)` — randomly splits the data into training and test sets.

| Parameter | Meaning |
|-----------|---------|
| `test_size=0.2` | Reserve 20% of rows for testing; use 80% for training |
| `random_state=42` | Fix the random seed so the split is the same every run |

The function returns four objects: training features, test features, training labels, and test labels.

---

```python
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
```

`RandomForestClassifier(random_state=42)` — creates an untrained Random Forest.

`model.fit(X_train, y_train)` — trains the model using only the training data. The test data is kept hidden at this stage.

---

```python
y_pred = model.predict(X_test)
```

`model.predict(X_test)` — applies the trained model to the test features and returns the predicted labels. These predictions will be compared against the real labels in `y_test`.

---

```python
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}\n")
```

`accuracy_score(y_test, y_pred)` — counts how many predictions match the real labels and divides by the total.

`{accuracy:.2f}` — formats the number to two decimal places (e.g. `0.90` for 90% accuracy).

---

```python
print("Classification Report:")
print(classification_report(y_test, y_pred))
```

`classification_report(y_test, y_pred)` — produces a formatted table with precision, recall, and F1 score for each class label, plus weighted averages. This gives a more complete picture than accuracy alone.

---

```python
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Accuracy       : {cv_scores.mean():.2f}")
```

`cross_val_score(model, X, y, cv=5)` — runs 5-fold cross-validation. It splits the full dataset into 5 equal parts, trains on 4 and tests on 1, repeating 5 times so every row is tested exactly once. Returns an array of 5 accuracy scores.

`cv_scores.mean()` — averages the 5 fold scores into a single reliability estimate.

---

# Deactivate the Virtual Environment

```sh
deactivate
```

---

# Assignment

Complete the following:

1. Run `evaluate_model.py`
2. Note the accuracy, precision, recall, and F1 scores
3. Experiment with removing a feature column and observe how accuracy changes
4. Try changing `test_size` from 0.2 to 0.4 and note the difference

---

# Next Lesson

**Day 6: AI Decision Engine**

In the next lesson you will learn:

- How to turn model predictions into operational decisions
- How deterministic decision logic works
- How NERP maps AI signals to actions

See you in **Day 6**.

---

## Install dependencies for a specific course day

```bash
cd course/day05_model_evaluation
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
