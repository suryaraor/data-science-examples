import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load the CSV data into a DataFrame."""
    df = pd.read_csv(path)
    return df


def basic_profile(df: pd.DataFrame) -> None:
    """Print quick facts about the dataset."""
    print("Rows, Columns:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Missing values per column:\n", df.isna().sum())
    print("\nSummary stats:\n", df.describe())


def group_and_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Return grouped stats and a moving average series."""
    grouped = df.groupby("city")["sales"].agg(["mean", "min", "max"]).sort_values("mean", ascending=False)
    df_sorted = df.sort_values("temperature_c")
    df_sorted["sales_ma3"] = df_sorted["sales"].rolling(window=3, min_periods=1).mean()
    return grouped, df_sorted


def plot_relationship(df: pd.DataFrame, path: str) -> None:
    """Create a scatter plot of temperature vs sales."""
    plt.figure(figsize=(6, 4))
    plt.scatter(df["temperature_c"], df["sales"], alpha=0.7)
    plt.title("Sales vs Temperature")
    plt.xlabel("Temperature (C)")
    plt.ylabel("Sales")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(path)
    print(f"Saved plot to {path}")


def main() -> None:
    df = load_data("data.csv")

    print("=== Basic profile ===")
    basic_profile(df)

    grouped, df_with_ma = group_and_trend(df)
    print("\n=== Avg sales by city ===")
    print(grouped)

    print("\n=== Sales with moving average (sorted by temperature) ===")
    print(df_with_ma[["city", "temperature_c", "sales", "sales_ma3"]])

    plot_relationship(df, "sales_vs_temperature.png")


if __name__ == "__main__":
    main()
