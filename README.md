# NERP AI Foundations

NERP AI Foundations is a beginner-friendly learning project for understanding the core reliability intelligence loop.

## Core Loop

Telemetry -> AI Model -> Decision -> Automation

The repository is organized as a small course. It combines reference notes, daily lesson material, notebooks, sample datasets, reusable Python modules, and demo scripts that show how a simple NERP pipeline can be assembled from raw telemetry to remediation.

## Learning Outcomes

By the end of the material in this repository, you should be able to:

1. Explain the NERP architecture at a beginner level.
2. Load and explore operational datasets with Python and pandas.
3. Train a basic prediction model for failure risk.
4. Detect unusual system behavior with anomaly detection.
5. Map model output to deterministic operational decisions.
6. Execute safe placeholder remediation actions from software.

## Repository Layout


```text
nerp-ai/
├── docs/                 Reference reading for concepts and architecture
├── course/               Day-by-day teaching materials
├── notebooks/            Guided hands-on labs
├── datasets/             Sample CSV datasets for system, fintech, and incidents
├── models/               Saved model artifacts and notes
├── nerp/                 Reusable Python modules for the NERP pipeline
├── demos/                End-to-end demos built from the shared modules
└── diagrams/             Architecture and pipeline images
```

## Core Python Modules

- `nerp/data_pipeline/data_loader.py`: dataset discovery and CSV loading helpers.
- `nerp/ai_engine/train_model.py`: trains and saves the prediction model.
- `nerp/ai_engine/predict.py`: loads a trained model and predicts risk.
- `nerp/ai_engine/anomaly_detector.py`: trains and runs anomaly detection.
- `nerp/decision_engine/decision_logic.py`: converts model output into actions.
- `nerp/automation/remediation_actions.py`: executes safe placeholder remediation commands.

## Quick Start

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the incident predictor demo:

```bash
python demos/nerp_incident_predictor/demo_script.py
```

Run the fintech risk monitor demo:

```bash
python demos/fintech_risk_monitor/demo_script.py
```

Generate model artifacts:

```bash
python -m nerp.ai_engine.train_model
python -m nerp.ai_engine.anomaly_detector
```

Install dependencies for a specific course day:

```bash
cd course/day07_ai_automation
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Using the Notebooks

The notebooks are designed to be completed in order:

1. `notebooks/01_python_basics.ipynb`
2. `notebooks/02_data_exploration.ipynb`
3. `notebooks/03_first_ml_model.ipynb`
4. `notebooks/04_anomaly_detection.ipynb`
5. `notebooks/05_prediction_demo.ipynb`

To use them in VS Code:

1. Install the dependencies from `requirements.txt`.
2. Open the repository root in VS Code.
3. Open a notebook from the `notebooks/` folder.
4. Select a Python kernel that has the project dependencies installed.
5. Run the cells from top to bottom.

The early notebooks focus on Python and data exploration. The later notebooks move into model training, anomaly detection, and the full prediction flow.

If a notebook imports project modules such as `nerp.ai_engine`, make sure the notebook is being run with the repository opened as the workspace root so the local package can be resolved correctly.

## Day-by-Day Path

Day 1 starts with environment setup so you can install dependencies, understand the repository layout, and see how the folders connect.

Day 2 introduces the AI foundation terms you need for the rest of the week, including features, labels, training, and prediction.

Day 3 moves into data and features, where you inspect the datasets and decide what information should feed the models.

Day 4 uses that data understanding to train the first machine learning model and generate predictions from telemetry.

Day 5 focuses on model evaluation so you can measure prediction quality with accuracy, classification metrics, and cross-validation.

Day 6 turns those AI signals into deterministic operational decisions through the decision engine.

Day 7 completes the loop by executing safe automation actions and presenting the full NERP flow from telemetry to remediation.

To move through the material smoothly, read the matching note in `docs/`, complete the lesson in `course/`, work through the related notebook, then inspect the corresponding Python module in `nerp/`.

## Notes

- The automation layer uses safe print-based placeholders instead of real infrastructure changes.
- The sample model files under `models/` are beginner-friendly artifacts that can be regenerated from the training modules.
- The diagrams are placeholder visuals for teaching structure and can be replaced with richer assets later.

## Author

Emmanuel Naweji, 2026
