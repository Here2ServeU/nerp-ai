# NERP AI Architecture

The teaching architecture in this repository uses a clear linear flow:

```text
datasets/system_metrics_sample.csv
        -> nerp/data_pipeline/data_loader.py
        -> nerp/ai_engine/train_model.py
        -> nerp/ai_engine/predict.py
        -> nerp/decision_engine/decision_logic.py
        -> nerp/automation/remediation_actions.py
```

## Layer Responsibilities

- Data pipeline: loads CSV datasets from the repository.
- AI engine: trains a prediction model and anomaly detector.
- Decision engine: translates model signals into an operational action.
- Automation: performs safe placeholder responses.
- Demos: wire everything together in a narrative-friendly way.

## Design Principles

- Keep modules small.
- Prefer readable names over abstract patterns.
- Make each layer testable in isolation.
- Use safe placeholder actions instead of real infrastructure changes.

That structure makes it easier for beginners to understand what each layer contributes to the overall NERP loop.
