from pathlib import Path
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def load_data(path: Path) -> pd.DataFrame:
    """Load the advertising-style spend dataset."""
    return pd.read_csv(path)


def train_and_evaluate(df: pd.DataFrame) -> Tuple[LinearRegression, Dict[str, float], Dict[str, float], float, pd.Series, np.ndarray]:
    """Fit a basic linear regression and compute metrics."""
    features = ["tv_spend", "radio_spend", "social_spend"]
    X = df[features]
    y = df["sales"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "mae": mean_absolute_error(y_test, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
        "r2": r2_score(y_test, y_pred),
    }
    coefs = dict(zip(features, model.coef_))

    return model, metrics, coefs, model.intercept_, y_test, y_pred


def plot_predictions(y_true: pd.Series, y_pred: np.ndarray, path: Path) -> None:
    """Plot predicted vs actual with an identity line for quick visual check."""
    plt.figure(figsize=(6, 4))
    plt.scatter(y_true, y_pred, alpha=0.75, label="Predicted")

    line_min = min(y_true.min(), y_pred.min())
    line_max = max(y_true.max(), y_pred.max())
    line = np.linspace(line_min, line_max, 100)
    plt.plot(line, line, color="black", linestyle="--", label="Ideal")

    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Linear Regression: Actual vs Predicted")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(path)
    print(f"Saved plot to {path}")


def main() -> None:
    data_path = Path(__file__).parent / "data.csv"
    df = load_data(data_path)

    model, metrics, coefs, intercept, y_true, y_pred = train_and_evaluate(df)

    print("=== Metrics ===")
    for name, value in metrics.items():
        print(f"{name}: {value:.3f}")

    print("\n=== Coefficients ===")
    rounded_coefs = {name: round(float(value), 3) for name, value in coefs.items()}
    print(rounded_coefs)
    print(f"intercept: {intercept:.3f}")

    plot_path = Path(__file__).parent / "pred_vs_actual.png"
    plot_predictions(y_true, y_pred, plot_path)


if __name__ == "__main__":
    main()
