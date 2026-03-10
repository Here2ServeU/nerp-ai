from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from nerp.data_pipeline.data_loader import load_fintech_transactions


def classify_transaction_risk(velocity_score: float, geo_risk: float, device_risk: float) -> str:
    weighted_score = velocity_score * 0.5 + geo_risk * 100 * 0.25 + device_risk * 100 * 0.25
    if weighted_score >= 70:
        return "High risk"
    if weighted_score >= 40:
        return "Medium risk"
    return "Low risk"


def main() -> None:
    transactions = load_fintech_transactions()
    print("Fintech Risk Monitor")

    for _, row in transactions.iterrows():
        risk = classify_transaction_risk(row["velocity_score"], row["geo_risk"], row["device_risk"])
        print(
            f"{row['transaction_id']}: amount=${row['amount']:.2f}, "
            f"fraud_flag={row['fraud_flag']}, classified_risk={risk}"
        )


if __name__ == "__main__":
    main()