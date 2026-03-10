from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from nerp.ai_engine.anomaly_detector import detect_anomaly, train_anomaly_detector
from nerp.ai_engine.predict import predict_failure
from nerp.ai_engine.train_model import train_prediction_model
from nerp.automation.remediation_actions import execute_action
from nerp.decision_engine.decision_logic import decision_engine


def main() -> None:
    prediction_model = train_prediction_model()
    anomaly_model = train_anomaly_detector()

    telemetry = {"cpu": 92, "memory": 85, "latency": 100}

    prediction = predict_failure(
        prediction_model,
        cpu=telemetry["cpu"],
        memory=telemetry["memory"],
        latency=telemetry["latency"],
    )
    anomaly_detected = detect_anomaly(
        anomaly_model,
        cpu=telemetry["cpu"],
        memory=telemetry["memory"],
        latency=telemetry["latency"],
    )
    action = decision_engine(prediction, anomaly_detected)

    print("NERP Incident Predictor")
    print(f"Telemetry sample: {telemetry}")
    print(f"Model prediction: {prediction}")
    print(f"Anomaly detected: {anomaly_detected}")
    print(f"Decision: {action}")
    execute_action(action)


if __name__ == "__main__":
    main()