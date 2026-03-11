
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
