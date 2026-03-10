from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier

from nerp.data_pipeline.data_loader import MODELS_DIR, load_system_metrics


PREDICTION_MODEL_PATH = MODELS_DIR / "prediction_model.pkl"
FEATURE_COLUMNS = ["cpu", "memory", "latency"]
TARGET_COLUMN = "failure"


def train_prediction_model(dataset_path: str | Path | None = None) -> RandomForestClassifier:
    data = load_system_metrics(dataset_path)

    features = data[FEATURE_COLUMNS]
    target = data[TARGET_COLUMN]

    model = RandomForestClassifier(random_state=42)
    model.fit(features, target)
    return model


def save_prediction_model(output_path: str | Path = PREDICTION_MODEL_PATH) -> Path:
    model = train_prediction_model()
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_file)
    return output_file


if __name__ == "__main__":
    saved_path = save_prediction_model()
    print(f"Saved prediction model to {saved_path}")