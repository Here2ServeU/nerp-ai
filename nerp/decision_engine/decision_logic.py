def decision_engine(prediction: int, anomaly_detected: bool = False) -> str:
    if prediction == 1 and anomaly_detected:
        return "Scale infrastructure and investigate anomaly"
    if prediction == 1:
        return "Scale infrastructure"
    if anomaly_detected:
        return "Investigate anomaly"
    return "System healthy"