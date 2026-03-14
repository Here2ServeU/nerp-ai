
# NERP AI Fundamentals
## Day 4 — Training Your First Machine Learning Model

Welcome to **Day 4** of the NERP AI Fundamentals series.

In the previous lessons we built the foundation for understanding Artificial Intelligence.

Day 1: Environment setup  
Day 2: What Artificial Intelligence really is  
Day 3: Datasets and features  

Today we take the next step:

**Training your first Machine Learning model.**

---

# Objective

In this lesson you will:

- Load a dataset
- Train a simple machine learning model
- Make a prediction using system metrics

This example simulates a simplified concept used in the **NERP platform (Naweji Enterprise Reliability Platform)**.

NERP analyzes infrastructure signals such as:

- CPU usage
- memory usage
- system logs
- network activity

AI models learn patterns from this data to detect potential system risks.

---

# Project Structure

Your project should now look like this:

```
nerp-ai/
├── .venv/
├── datasets/
│   └── system_metrics.csv
├── train_model.py
└── README.md
```

---

# Step 1: Activate Your Python Virtual Environment

Move to your project directory.

```
cd nerp-ai
```

Activate the virtual environment.

### Windows

```
.venv\Scripts\activate
```

### Linux or macOS

```
source .venv/bin/activate
```

You should see something like:

```
(.venv)
```

This means the virtual environment is active.

---

# Step 2: Install Machine Learning Libraries

Install required packages.

```
pip install pandas scikit-learn
```

Explanation:

| Library | Purpose |
|------|------|
| pandas | Data analysis and dataset loading |
| scikit-learn | Machine learning models |

---

# Step 3: Verify the Dataset

Check that the dataset exists:

```
datasets/system_metrics.csv
```

Example dataset:

```
cpu_usage,memory_usage,system_status
45,60,normal
50,65,normal
70,70,normal
85,75,warning
90,80,warning
95,85,failure
98,90,failure
```

Explanation:

| Column | Meaning |
|------|------|
| cpu_usage | CPU percentage |
| memory_usage | Memory percentage |
| system_status | Health state of the system |

---

# Step 4: Create the Training Script

Create a new file:

```
train_model.py
```

Add the following code:

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("datasets/system_metrics.csv")

# Features
X = data[["cpu_usage", "memory_usage"]]

# Target label
y = data["system_status"]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Test prediction
prediction = model.predict([[92, 85]])

print("Prediction:", prediction)
```

---

# Step 5: Run the Model

Run the script from your terminal.

```
python train_model.py
```

Example output:

```
Prediction: ['warning']
```

This means the model predicts that the system metrics indicate a **warning state**.

---

# What Just Happened?

The machine learning model:

1. Loaded the dataset
2. Learned patterns from system metrics
3. Predicted the system state for new data

Even though this dataset is small, the concept is the same for large systems.

In production environments, AI models analyze millions of telemetry events to detect anomalies.

---

# How This Connects to NERP

The **NERP platform** will eventually analyze real infrastructure signals such as:

- Kubernetes metrics
- cloud infrastructure telemetry
- application logs
- financial transaction patterns
- healthcare system events

Machine learning models will detect patterns and identify risks before failures occur.

This enables **predictive reliability engineering**.

---

# Troubleshooting

### pandas not installed

```
pip install pandas
```

### scikit-learn not installed

```
pip install scikit-learn
```

### Dataset file not found

Verify the file exists:

```
datasets/system_metrics.csv
```

---

# Script Walkthrough — `train_model.py`

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
```

`import pandas as pd` — loads pandas for reading and handling the dataset.

`from sklearn.tree import DecisionTreeClassifier` — imports the Decision Tree model from scikit-learn. A Decision Tree learns rules by splitting data based on feature thresholds, similar to a flowchart of yes/no questions.

---

```python
DATA_PATH = "../../datasets/system_metrics_sample.csv"
data = pd.read_csv(DATA_PATH)
```

`DATA_PATH` — the relative path to the dataset file.

`pd.read_csv(DATA_PATH)` — reads the CSV file into a pandas DataFrame. Each row is a system snapshot. Each column is a feature or the label.

---

```python
print("Dataset Preview:")
print(data)
```

Prints the full dataset so you can verify it loaded correctly before training.

---

```python
FEATURE_COLUMNS = ["cpu", "memory", "latency"]
TARGET_COLUMN = "failure"

X = data[FEATURE_COLUMNS]
y = data[TARGET_COLUMN]
```

`FEATURE_COLUMNS` — the three columns the model will use as inputs.

`TARGET_COLUMN` — the column the model will learn to predict.

`X` — the feature matrix. By convention, `X` is uppercase because it is a 2D table (matrix).

`y` — the label vector. By convention, `y` is lowercase because it is a 1D list (vector).

---

```python
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
```

`DecisionTreeClassifier(random_state=42)` — creates a new, untrained Decision Tree model. `random_state=42` fixes the random seed so results are reproducible every time you run the script.

`model.fit(X, y)` — trains the model. It reads every row in `X` alongside the matching label in `y` and learns which feature combinations predict each outcome.

---

```python
print("Model trained successfully.\n")
```

Prints a confirmation message after training completes.

---

```python
sample = pd.DataFrame([{"cpu": 92, "memory": 85, "latency": 110}])
prediction = model.predict(sample[FEATURE_COLUMNS])
```

`pd.DataFrame([{...}])` — creates a single-row DataFrame representing a new telemetry reading. Wrapping it in a list and DataFrame ensures it matches the format expected by `model.predict`.

`model.predict(sample[FEATURE_COLUMNS])` — asks the trained model to classify the new sample. It returns an array of predicted labels.

---

```python
label = "failure risk" if prediction[0] == 1 else "healthy"
print(f"Sample  : cpu=92, memory=85, latency=110")
print(f"Prediction: {prediction[0]} ({label})")
```

`prediction[0]` — takes the first (and only) prediction from the returned array.

The `if/else` expression maps the numeric output back to a human-readable string.

`print(...)` — displays the input sample and prediction together so the result is easy to read.

---

# Cleanup (Optional)

Deactivate the virtual environment.

```
deactivate
```

---

# Next Lesson

**Day 5: Model Evaluation and Accuracy**

In the next lesson you will learn:

- how to measure model accuracy
- how to validate machine learning models
- how to improve predictions

NERP AI Fundamentals continues on Day 5. See you then!

---

## Install dependencies for a specific course day

```bash
cd course/day04_machine_learning_model
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```


