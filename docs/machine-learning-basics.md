# Machine Learning Basics

Machine learning helps software learn patterns from historical data instead of relying only on fixed rules.

## Supervised Learning

Supervised learning uses labeled examples. In this repository:

- Features: `cpu`, `memory`, and `latency`
- Label: `failure`

The prediction model learns which combinations of metrics usually point to a risky state.

## Unsupervised Learning

Unsupervised learning looks for patterns without labeled outcomes. The anomaly detector in this project uses Isolation Forest to identify unusual telemetry patterns.

## Typical Workflow

1. Load and clean data.
2. Select features.
3. Train a model.
4. Test with new samples.
5. Use the result in a decision workflow.

## Practical Reminder

Models do not make business decisions by themselves. They produce signals. A decision engine should still make the final action understandable and deterministic.
