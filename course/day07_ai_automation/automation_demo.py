"""
Day 7 — AI Automation
NERP AI Fundamentals

Demonstrates the complete NERP intelligence loop:
  Telemetry  ->  AI Engine  ->  Decision Engine  ->  Automation
"""

import sys
from pathlib import Path

# Allow running this script directly from the course directory.
ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from nerp.ai_engine.anomaly_detector import detect_anomaly, train_anomaly_detector
from nerp.ai_engine.predict import predict_failure
from nerp.ai_engine.train_model import train_prediction_model
from nerp.automation.remediation_actions import execute_action
from nerp.decision_engine.decision_logic import decision_engine

# ---------------------------------------------------------------------------
# 1. Train AI models from the sample dataset
# ---------------------------------------------------------------------------
prediction_model = train_prediction_model()
anomaly_detector = train_anomaly_detector()

# ---------------------------------------------------------------------------
# 2. Telemetry samples to process through the full loop
# ---------------------------------------------------------------------------
SAMPLES = [
    {"cpu": 92, "memory": 85, "latency": 110},
    {"cpu": 45, "memory": 48, "latency": 18},
    {"cpu": 60, "memory": 70, "latency": 40},
]

# ---------------------------------------------------------------------------
# 3. Run the full NERP loop for each sample
# ---------------------------------------------------------------------------
print("=== NERP AI Automation Demo ===\n")

for sample in SAMPLES:
    cpu = sample["cpu"]
    memory = sample["memory"]
    latency = sample["latency"]

    # AI engine
    prediction = predict_failure(prediction_model, cpu=cpu, memory=memory, latency=latency)
    anomaly = detect_anomaly(anomaly_detector, cpu=cpu, memory=memory, latency=latency)

    # Decision engine
    action = decision_engine(prediction=prediction, anomaly_detected=anomaly)

    # Automation layer
    label = "failure risk" if prediction == 1 else "healthy"
    print(f"--- Telemetry: cpu={cpu}, memory={memory}, latency={latency} ---")
    print(f"Prediction      : {prediction} ({label})")
    print(f"Anomaly detected: {anomaly}")
    print(f"Decision        : {action}")
    print("Action:")
    execute_action(action)
    print()
