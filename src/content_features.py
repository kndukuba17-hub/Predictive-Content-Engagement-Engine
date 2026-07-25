"""Data prep for the UCI Online News Popularity dataset.

Extracted from the notebook so the logic is importable and testable.
"""
from __future__ import annotations
import pandas as pd

DROP_COLUMNS = ["url", "timedelta"]   # non-predictive


def load_and_prepare(csv_path: str):
    """Load the dataset and return (X, y, median_shares).

    Target is binary popularity: 1 if an article's shares are >= the median.
    """
    df = pd.read_csv(csv_path, skipinitialspace=True)
    df = df.drop(columns=DROP_COLUMNS, errors="ignore")
    median = df["shares"].median()
    y = (df["shares"] >= median).astype(int)
    X = df.drop(columns=["shares"])
    return X, y, median
