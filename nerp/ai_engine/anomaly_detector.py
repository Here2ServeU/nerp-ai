from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest

from nerp.ai_engine.train_model import FEATURE_COLUMNS
from nerp.data_pipeline.data_loader import MODELS_DIR, load_system_metrics


ANOMALY_MODEL_PATH = MODELS_DIR / "anomaly_detector.pkl"


def train_anomaly_detector(dataset_path: str | Path | None = None) -> IsolationForest:
    data = load_system_metrics(dataset_path)
    detector = IsolationForest(contamination=0.2, random_state=42)
    detector.fit(data[FEATURE_COLUMNS])
    return detector


def save_anomaly_detector(output_path: str | Path = ANOMALY_MODEL_PATH) -> Path:
    detector = train_anomaly_detector()
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(detector, output_file)
    return output_file


def detect_anomaly(detector: IsolationForest, cpu: int, memory: int, latency: int) -> bool:
    sample = pd.DataFrame([
        {"cpu": cpu, "memory": memory, "latency": latency}
    ])
    result = detector.predict(sample[FEATURE_COLUMNS])
    return int(result[0]) == -1


if __name__ == "__main__":
    saved_path = save_anomaly_detector()
    print(f"Saved anomaly detector to {saved_path}")