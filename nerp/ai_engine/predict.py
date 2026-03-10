from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from nerp.ai_engine.train_model import FEATURE_COLUMNS, PREDICTION_MODEL_PATH, train_prediction_model


def load_prediction_model(model_path: str | Path = PREDICTION_MODEL_PATH) -> RandomForestClassifier:
    model_file = Path(model_path)
    if model_file.exists() and model_file.stat().st_size > 0:
        return joblib.load(model_file)
    return train_prediction_model()


def predict_failure(model: RandomForestClassifier, cpu: int, memory: int, latency: int) -> int:
    sample = pd.DataFrame([
        {"cpu": cpu, "memory": memory, "latency": latency}
    ])
    prediction = model.predict(sample[FEATURE_COLUMNS])
    return int(prediction[0])


if __name__ == "__main__":
    trained_model = load_prediction_model()
    result = predict_failure(trained_model, cpu=92, memory=85, latency=100)
    print(f"Prediction: [{result}]")