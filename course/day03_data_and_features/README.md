
# AI Fundamentals in 7 Days
## Day 3 — Features and Datasets

**Created by Emmanuel Naweji, 2026**

Welcome to **Day 3** of the *AI Fundamentals in 7 Days* learning journey.

In this course we explore the foundations of Artificial Intelligence while gradually building components of the **Naweji Enterprise Reliability Platform (NERP)**.

In **Day 1**, we prepared our development environment.
In **Day 2**, we discussed what Artificial Intelligence is and how machines learn patterns from data.

Today we go deeper into the foundations of machine learning.

Today’s topic is **features and datasets**.

Understanding these two ideas is one of the most important skills in Artificial Intelligence.

---

# What is a Dataset?

A **dataset** is a structured collection of examples used to train or evaluate machine learning models.

Each row in a dataset represents an observation or event.

Example dataset:

```
cpu_usage,memory_usage,system_status
45,60,normal
50,65,normal
90,80,warning
95,85,failure
```

Each row represents a snapshot of system behavior.

---

# What is a Feature?

A **feature** is a measurable property used by a machine learning model.

Examples of features:

- cpu_usage
- memory_usage

These features describe the system.

The model studies these features to learn patterns.

---

# What is a Label?

The **label** is the value we want the model to predict.

In this dataset:

`system_status` is the label.

Possible values:

- normal
- warning
- failure

---

# Creating a Dataset

Create a dataset directory.

```cmd
mkdir datasets
```

Create the dataset file.

```cmd
touch datasets/system_metrics.csv
```

Example dataset:

```
cpu_usage,memory_usage,system_status
45,60,normal
50,65,normal
70,70,normal
85,75,warning
90,80,warning
95,85,failure
98,90,failure
```

---

# Loading Data with Python

Create a Python script.

```cmd
touch load_dataset.py
```

Add this code:

```python
import pandas as pd

dataset = pd.read_csv("datasets/system_metrics.csv")

print("Dataset Preview:")
print(dataset)
```

Run the script:

```cmd
python load_dataset.py
```

If everything is correct, the dataset will appear in your terminal.

---

# Why This Matters

Every AI system begins with:

1. Collecting data
2. Structuring datasets
3. Identifying features and labels
4. Training models

In the **NERP platform**, datasets could come from:

- cloud infrastructure metrics
- application logs
- financial transactions
- healthcare monitoring systems

---

# Deactivate the Virtual Environment

When you are finished working, deactivate the virtual environment to
return to your system's default Python environment.

```sh
deactivate
```

---

# Script Walkthrough — `load_dataset.py`

```python
import pandas as pd
```

`import pandas as pd` — loads the pandas library under the alias `pd`. Every pandas operation in this script uses the `pd.` prefix.

---

```python
DATA_PATH = "../../datasets/system_metrics_sample.csv"
```

`DATA_PATH` — stores the relative file path to the dataset as a constant. Two `../` steps navigate up from the current day folder to the project root, then into `datasets/`. Using a named constant makes the path easy to update in one place.

---

```python
data = pd.read_csv(DATA_PATH)
```

`pd.read_csv(DATA_PATH)` — reads the CSV file at `DATA_PATH` and returns a pandas DataFrame. Each row in the file becomes a row in the DataFrame and each column header becomes a column name.

---

```python
print("Dataset Preview:")
print(data)
```

`print("Dataset Preview:")` — prints a descriptive label before the table output.

`print(data)` — prints the entire DataFrame, showing all rows and columns.

---

```python
print(f"Rows   : {data.shape[0]}")
print(f"Columns: {data.shape[1]}")
```

`data.shape` — returns a tuple `(rows, columns)` describing the size of the DataFrame.

`data.shape[0]` — the number of rows (observations).

`data.shape[1]` — the number of columns (features + label).

The `f"...{...}"` syntax is an f-string, which embeds a variable's value directly inside a string.

---

```python
FEATURE_COLUMNS = ["cpu", "memory", "latency"]
TARGET_COLUMN = "failure"
```

`FEATURE_COLUMNS` — a list of the column names that will be used as inputs to the model. These are the measurable properties that describe each system snapshot.

`TARGET_COLUMN` — the column the model will learn to predict. A value of `1` means failure risk and `0` means healthy.

Naming these as constants at the top makes the script easier to read and modify.

---

```python
print(f"Features : {FEATURE_COLUMNS}")
print(f"Label    : {TARGET_COLUMN}")
```

Prints the feature list and label name to the terminal so you can confirm the column selection at a glance.

---

```python
print("Feature Statistics:")
print(data[FEATURE_COLUMNS].describe())
```

`data[FEATURE_COLUMNS]` — selects only the feature columns from the DataFrame, excluding the label.

`.describe()` — computes summary statistics for each column: count, mean, standard deviation, minimum, maximum, and quartile values. This gives a quick overview of the data distribution.

---

```python
print("Label Distribution:")
print(data[TARGET_COLUMN].value_counts().rename({0: "healthy (0)", 1: "failure (1)"}))
```

`data[TARGET_COLUMN]` — selects only the label column.

`.value_counts()` — counts how many times each unique value appears. This tells you how many healthy versus failure examples are in the dataset.

`.rename({0: "healthy (0)", 1: "failure (1)"})` — replaces the numeric labels `0` and `1` with readable names in the output.

---

# Assignment

Complete the following:

1. Create the datasets folder
2. Create the `system_metrics.csv` dataset
3. Create the `load_dataset.py` script
4. Run the script

Your dataset will then be ready for machine learning.

---

# Next Lesson

In **Day 4**, we will build our **first machine learning model**.

This is where **data becomes intelligence**.

---

## Install dependencies for a specific course day

```bash
cd course/day03_data_and_features
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
