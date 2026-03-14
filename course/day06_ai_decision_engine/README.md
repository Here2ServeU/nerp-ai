# AI Fundamentals in 7 Days
## Day 6 — AI Decision Engine

**Created by Emmanuel Naweji, 2026**

Welcome to **Day 6** of the *AI Fundamentals in 7 Days* learning journey.

In the previous lessons we covered:

- Day 1: Environment setup
- Day 2: What Artificial Intelligence really is
- Day 3: Datasets and features
- Day 4: Training your first machine learning model
- Day 5: Model evaluation and accuracy

Today we connect AI predictions to **operational decisions**.

---

# The Problem with Raw Predictions

A machine learning model produces a **signal**, not a decision.

Examples of raw signals:

- `failure = 1` (the model predicts a failure)
- `anomaly = True` (the anomaly detector flags unusual behavior)

Raw signals tell you something is wrong. They do not tell you what to do.

This is where the **Decision Engine** comes in.

---

# What is a Decision Engine?

A **Decision Engine** translates AI signals into clear, deterministic actions.

It answers the question:

> Given this model output, what should the system do?

Decision logic is intentionally explicit and rule-based. This makes automation safe, auditable, and predictable.

---

# Decision Logic in NERP

The NERP decision engine combines two signals:

| Signal | Source |
|--------|--------|
| `prediction` | The prediction model (1 = failure risk, 0 = healthy) |
| `anomaly_detected` | The anomaly detector (True = unusual behavior) |

Decision table:

| Prediction | Anomaly Detected | Action |
|------------|-----------------|--------|
| 1 | True | Scale infrastructure and investigate anomaly |
| 1 | False | Scale infrastructure |
| 0 | True | Investigate anomaly |
| 0 | False | System healthy |

---

# Project Structure

Your project should now look like this:

```
nerp-ai/
├── .venv/
├── datasets/
│   └── system_metrics.csv
├── train_model.py          (Day 4)
├── evaluate_model.py       (Day 5)
├── decision_engine.py      (Day 6 — new)
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

# Step 2: Run the Decision Engine Script

```sh
python decision_engine.py
```

---

# Understanding the Output

Example output:

```
--- Sample 1: cpu=92, memory=85, latency=110 ---
Prediction      : 1 (failure risk)
Anomaly detected: True
Decision        : Scale infrastructure and investigate anomaly

--- Sample 2: cpu=45, memory=48, latency=18 ---
Prediction      : 0 (healthy)
Anomaly detected: False
Decision        : System healthy

--- Sample 3: cpu=60, memory=70, latency=40 ---
Prediction      : 0 (healthy)
Anomaly detected: True
Decision        : Investigate anomaly
```

Each sample shows:

1. The input telemetry
2. The model prediction
3. Whether an anomaly was detected
4. The resulting decision

---

# Why Deterministic Decision Logic?

Deterministic logic means: **the same inputs always produce the same output**.

This is intentional.

In operational systems, decision logic must be:

- **Auditable** — you can explain exactly why an action was taken
- **Predictable** — operators can anticipate system behavior
- **Safe** — unexpected outputs cannot trigger destructive actions

AI models introduce probabilistic uncertainty. The decision engine eliminates that uncertainty by mapping outputs to fixed, well-defined actions.

---

# How This Connects to NERP

In the full NERP loop, the decision engine sits between:

```
AI Engine  →  Decision Engine  →  Automation Layer
```

The AI engine produces signals.
The decision engine maps signals to actions.
The automation layer executes those actions.

---

# Script Walkthrough — `decision_engine.py`

```python
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
```

`import sys` — provides access to the Python interpreter's path list.

`from pathlib import Path` — imports `Path`, a modern Python class for working with filesystem paths in a cross-platform way.

`Path(__file__).resolve()` — returns the absolute path of this script file.

`.parents[2]` — navigates two directory levels up (from `day06_ai_decision_engine/` → `course/` → the project root).

`sys.path.insert(0, str(ROOT_DIR))` — adds the project root to Python's module search path so that `import nerp.ai_engine...` works when running the script directly from this folder.

---

```python
from nerp.ai_engine.anomaly_detector import detect_anomaly, train_anomaly_detector
from nerp.ai_engine.predict import predict_failure
from nerp.ai_engine.train_model import train_prediction_model
from nerp.decision_engine.decision_logic import decision_engine
```

Each line imports a specific function from the shared `nerp` package:

| Import | Purpose |
|--------|---------|
| `train_anomaly_detector` | Trains the Isolation Forest anomaly detector on the dataset |
| `detect_anomaly` | Runs the trained detector on a single telemetry sample |
| `train_prediction_model` | Trains the Random Forest failure-risk classifier |
| `predict_failure` | Runs the trained classifier on a single sample |
| `decision_engine` | Maps prediction + anomaly signals to a named action string |

---

```python
prediction_model = train_prediction_model()
anomaly_detector = train_anomaly_detector()
```

`train_prediction_model()` — trains a Random Forest classifier on the system metrics dataset and returns the fitted model object.

`train_anomaly_detector()` — trains an Isolation Forest detector on the same dataset and returns the fitted detector object.

Both models are trained once here and then reused for every sample below.

---

```python
SAMPLES = [
    {"cpu": 92, "memory": 85, "latency": 110},
    {"cpu": 45, "memory": 48, "latency": 18},
    {"cpu": 60, "memory": 70, "latency": 40},
]
```

`SAMPLES` — a list of three dictionaries, each representing a telemetry snapshot with CPU percentage, memory percentage, and latency in milliseconds.

The first sample represents a stressed system. The second is a healthy system. The third is a borderline case.

---

```python
for i, sample in enumerate(SAMPLES, start=1):
    cpu = sample["cpu"]
    memory = sample["memory"]
    latency = sample["latency"]
```

`enumerate(SAMPLES, start=1)` — iterates over the samples list while also providing a counter `i` starting at 1. This makes it easy to label each output block.

`sample["cpu"]`, `sample["memory"]`, `sample["latency"]` — unpacks the three values from the dictionary into individual variables.

---

```python
    prediction = predict_failure(prediction_model, cpu=cpu, memory=memory, latency=latency)
    anomaly = detect_anomaly(anomaly_detector, cpu=cpu, memory=memory, latency=latency)
    action = decision_engine(prediction=prediction, anomaly_detected=anomaly)
```

`predict_failure(...)` — passes the telemetry values to the trained classifier and returns `1` (failure risk) or `0` (healthy).

`detect_anomaly(...)` — passes the same telemetry to the anomaly detector. Returns `True` if the sample is flagged as unusual, `False` otherwise.

`decision_engine(prediction=prediction, anomaly_detected=anomaly)` — takes both signals and returns the matching action string from the decision table.

---

```python
    label = "failure risk" if prediction == 1 else "healthy"
    print(f"--- Sample {i}: cpu={cpu}, memory={memory}, latency={latency} ---")
    print(f"Prediction      : {prediction} ({label})")
    print(f"Anomaly detected: {anomaly}")
    print(f"Decision        : {action}")
    print()
```

`"failure risk" if prediction == 1 else "healthy"` — a one-line conditional expression that converts the numeric prediction to a readable label.

The four `print` statements display the sample inputs, AI outputs, and final decision as a structured block. The trailing `print()` adds a blank line between samples for readability.

---

# Deactivate the Virtual Environment

```sh
deactivate
```

---

# Assignment

Complete the following:

1. Run `decision_engine.py` and observe the output for all three samples
2. Add a fourth sample with `cpu=80, memory=75, latency=85` and predict the decision

---

# Next Lesson

**Day 7: AI Automation**

In the final lesson you will learn:

- How to execute remediation actions from software
- How the full NERP loop connects end to end
- How to present the complete pipeline in a demo

See you in **Day 7**.

---

## Install dependencies for a specific course day

```bash
cd course/day06_ai_decision_engine
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
