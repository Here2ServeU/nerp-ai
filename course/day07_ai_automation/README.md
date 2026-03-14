# AI Fundamentals in 7 Days
## Day 7 — AI Automation

**Created by Emmanuel Naweji, 2026**

Welcome to **Day 7** — the final lesson of the *AI Fundamentals in 7 Days* learning journey.

Over the past six days we have built every layer of the NERP intelligence loop:

- Day 1: Environment setup
- Day 2: What Artificial Intelligence really is
- Day 3: Datasets and features
- Day 4: Training your first machine learning model
- Day 5: Model evaluation and accuracy
- Day 6: AI Decision Engine

Today we complete the loop by executing **automated remediation actions**.

---

# The Full NERP Loop

```
Telemetry  →  AI Engine  →  Decision Engine  →  Automation
```

| Layer | Responsibility |
|-------|---------------|
| Data pipeline | Load and structure telemetry |
| AI engine | Predict failure risk and detect anomalies |
| Decision engine | Map AI signals to operational actions |
| Automation | Execute safe responses |

---

# What is Automation in NERP?

Automation is the final layer. It receives a decision from the decision engine and executes the corresponding action.

Examples of actions:

| Action | Description |
|--------|-------------|
| Scale infrastructure | Increase compute capacity in response to failure risk |
| Investigate anomaly | Collect logs and telemetry for unusual behavior |
| No action | System is healthy — monitor only |

In this beginner course, all automation actions are **safe placeholder outputs** that print what a real system would do.

This lets you understand the flow without making changes to real infrastructure.

---

# Why Placeholder Automation?

Real automation actions such as scaling Kubernetes clusters or triggering incident workflows carry risk.

In production, automation is typically:

- **Gated by approval workflows** for destructive actions
- **Rate-limited** to prevent runaway scaling
- **Logged and audited** for every execution
- **Tested in staging environments** before production

For learning purposes, we simulate these actions safely with print statements.

---

# Project Structure

Your complete project now looks like this:

```
nerp-ai/
├── .venv/
├── datasets/
│   └── system_metrics.csv
├── train_model.py          (Day 4)
├── evaluate_model.py       (Day 5)
├── decision_engine.py      (Day 6)
├── automation_demo.py      (Day 7 — new)
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

# Step 2: Run the Automation Demo

```sh
python automation_demo.py
```

---

# Understanding the Output

Example output:

```
=== NERP AI Automation Demo ===

--- Telemetry: cpu=92, memory=85, latency=110 ---
Prediction      : 1 (failure risk)
Anomaly detected: True
Decision        : Scale infrastructure and investigate anomaly
Action:
  Scaling Kubernetes cluster
  kubectl scale deployment api --replicas=6
  Opening anomaly investigation workflow
  Collect logs, traces, and recent deploy information

--- Telemetry: cpu=45, memory=48, latency=18 ---
Prediction      : 0 (healthy)
Anomaly detected: False
Decision        : System healthy
Action:
  No scaling needed

--- Telemetry: cpu=60, memory=70, latency=40 ---
Prediction      : 0 (healthy)
Anomaly detected: True
Decision        : Investigate anomaly
Action:
  Opening anomaly investigation workflow
  Collect logs, traces, and recent deploy information
```

Each section shows the complete NERP loop in action:

1. Raw telemetry input
2. AI prediction
3. Anomaly detection result
4. Operational decision
5. Executed action

---

# The Complete NERP Intelligence Loop

This is the end-to-end flow you have now built piece by piece:

```
datasets/system_metrics_sample.csv
    ↓
nerp/data_pipeline/data_loader.py   (load telemetry)
    ↓
nerp/ai_engine/train_model.py       (train prediction model)
nerp/ai_engine/anomaly_detector.py  (train anomaly detector)
    ↓
nerp/ai_engine/predict.py           (predict failure risk)
nerp/ai_engine/anomaly_detector.py  (detect anomalies)
    ↓
nerp/decision_engine/decision_logic.py  (map signals to decisions)
    ↓
nerp/automation/remediation_actions.py  (execute actions)
```

---

# How This Scales to Real Systems

In a production reliability platform, this loop would:

- Ingest real-time metrics from Kubernetes, cloud providers, and application monitors
- Run models continuously against live telemetry streams
- Trigger approved automation workflows in response to confirmed risks
- Log every decision and action for compliance and audit

The architecture you have learned here is the same conceptual foundation used in production Site Reliability Engineering (SRE) platforms.

---

# Script Walkthrough — `automation_demo.py`

```python
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
```

`Path(__file__).resolve().parents[2]` — resolves the absolute location of this script and steps two directories up to reach the project root. This allows the `nerp` package to be found regardless of where the script is launched from.

`sys.path.insert(0, str(ROOT_DIR))` — prepends the project root to Python's module search list so `import nerp...` succeeds.

---

```python
from nerp.ai_engine.anomaly_detector import detect_anomaly, train_anomaly_detector
from nerp.ai_engine.predict import predict_failure
from nerp.ai_engine.train_model import train_prediction_model
from nerp.automation.remediation_actions import execute_action
from nerp.decision_engine.decision_logic import decision_engine
```

This block imports one function from each NERP layer:

| Import | Layer | Purpose |
|--------|-------|---------|
| `train_prediction_model` | AI engine | Trains the failure-risk classifier |
| `train_anomaly_detector` | AI engine | Trains the anomaly detector |
| `predict_failure` | AI engine | Predicts failure risk for one sample |
| `detect_anomaly` | AI engine | Detects anomalies for one sample |
| `decision_engine` | Decision engine | Maps AI signals to a named action |
| `execute_action` | Automation | Executes the action (prints placeholder commands) |

---

```python
prediction_model = train_prediction_model()
anomaly_detector = train_anomaly_detector()
```

Both models are trained once before the loop. Training inside the loop would be wasteful because the dataset is the same for every sample.

---

```python
SAMPLES = [
    {"cpu": 92, "memory": 85, "latency": 110},
    {"cpu": 45, "memory": 48, "latency": 18},
    {"cpu": 60, "memory": 70, "latency": 40},
]
```

`SAMPLES` — three telemetry snapshots covering a stressed system, a healthy system, and a borderline case. This lets you see all four possible decision outcomes in a single run.

---

```python
print("=== NERP AI Automation Demo ===\n")
```

Prints a header line before the loop output so the demo output has a clear starting point.

---

```python
for sample in SAMPLES:
    cpu = sample["cpu"]
    memory = sample["memory"]
    latency = sample["latency"]
```

Iterates over each sample dictionary and unpacks the three telemetry values into named variables.

---

```python
    prediction = predict_failure(prediction_model, cpu=cpu, memory=memory, latency=latency)
    anomaly = detect_anomaly(anomaly_detector, cpu=cpu, memory=memory, latency=latency)
```

**AI layer** — both models receive the same telemetry values and independently produce their signals:
- `prediction` is `1` (failure risk) or `0` (healthy).
- `anomaly` is `True` (unusual pattern detected) or `False`.

---

```python
    action = decision_engine(prediction=prediction, anomaly_detected=anomaly)
```

**Decision layer** — the two signals are passed to the decision engine, which returns one of four possible action strings based on the lookup table defined in `nerp/decision_engine/decision_logic.py`.

---

```python
    label = "failure risk" if prediction == 1 else "healthy"
    print(f"--- Telemetry: cpu={cpu}, memory={memory}, latency={latency} ---")
    print(f"Prediction      : {prediction} ({label})")
    print(f"Anomaly detected: {anomaly}")
    print(f"Decision        : {action}")
    print("Action:")
    execute_action(action)
    print()
```

Prints the full state for this sample: raw inputs, AI outputs, and decision.

`execute_action(action)` — **automation layer** — receives the action string and selects the matching remediation function. In this beginner implementation the functions print the commands that a real system would execute, keeping the demo safe to run without real infrastructure.

`print()` — adds a blank line between samples to improve readability.

---

# Deactivate the Virtual Environment

```sh
deactivate
```

---

# Assignment

Complete the following:

1. Run `automation_demo.py` and observe the full loop output
2. Add a fourth telemetry sample and observe which action is triggered
3. Describe in your own words how each of the seven days connects to the final demo

---

# Congratulations

You have completed the **AI Fundamentals in 7 Days** course.

Over seven days you:

1. Set up a Python AI development environment
2. Learned what Artificial Intelligence and Machine Learning are
3. Created and loaded structured datasets
4. Trained your first machine learning model
5. Evaluated model accuracy with real metrics
6. Built a deterministic decision engine
7. Executed safe automated remediation actions

You have built a complete, working AI pipeline from telemetry to automation.

**Author: Emmanuel Naweji, 2026**

---

## Install dependencies for a specific course day

```bash
cd course/day07_ai_automation
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
