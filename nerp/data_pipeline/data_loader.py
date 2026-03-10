from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[2]
DATASETS_DIR = ROOT_DIR / "datasets"
MODELS_DIR = ROOT_DIR / "models"

SYSTEM_METRICS_DATASET = DATASETS_DIR / "system_metrics_sample.csv"
FINTECH_TRANSACTIONS_DATASET = DATASETS_DIR / "fintech_transactions_sample.csv"
INCIDENT_LOGS_DATASET = DATASETS_DIR / "incident_logs_sample.csv"


def load_csv_dataset(csv_path: str | Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def load_system_metrics(csv_path: str | Path | None = None) -> pd.DataFrame:
    return load_csv_dataset(csv_path or SYSTEM_METRICS_DATASET)


def load_fintech_transactions(csv_path: str | Path | None = None) -> pd.DataFrame:
    return load_csv_dataset(csv_path or FINTECH_TRANSACTIONS_DATASET)


def load_incident_logs(csv_path: str | Path | None = None) -> pd.DataFrame:
    return load_csv_dataset(csv_path or INCIDENT_LOGS_DATASET)