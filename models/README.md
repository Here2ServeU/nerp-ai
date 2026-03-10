# Models

This directory stores beginner-friendly serialized model artifacts used by the demos:

- `prediction_model.pkl`: Random Forest classifier for failure-risk prediction.
- `anomaly_detector.pkl`: Isolation Forest model for anomaly detection.

You can regenerate both files at any time:

```bash
/Users/emmanuelnaweji/.pyenv/versions/3.11.4/bin/python -m nerp.ai_engine.train_model
/Users/emmanuelnaweji/.pyenv/versions/3.11.4/bin/python -m nerp.ai_engine.anomaly_detector
```