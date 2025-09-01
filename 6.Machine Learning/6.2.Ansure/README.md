# Gender Classification Using Anthropometric Data

This project predicts gender based on anthropometric measurements (height and weight) using a custom K-Nearest Neighbors (KNN) algorithm.

## Project Overview
- Load male and female anthropometric datasets.
- Merge datasets into a single dataframe.
- Convert units: weight to kg, height to cm.
- Encode gender numerically (Female=0, Male=1).
- Visualize male & female distribution using scatter plots.
- Train a custom KNN classifier and predict gender.

## Required Libraries
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from knn import KNN # Custom KNN class

How to Run

1. Open the project in Jupyter Notebook or any Python IDE.


2. Ensure the following CSV files are in the project folder:

ANSUR_II_FEMALE_Public.csv

ANSUR_II_MALE_Public.csv


