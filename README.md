# data-science-examples
A collection of practical data science examples covering data analysis, machine learning, and visualization using Python.

## Structure
- [examples/basic_stats](examples/basic_stats): Descriptive statistics starter with a tiny CSV and Matplotlib scatter plot.
	- Purpose: show an end-to-end mini workflow—load CSV, profile, group by city, compute a rolling average, and plot temperature vs sales.
- [examples/simple_linear_model](examples/simple_linear_model): Train/test split with scikit-learn LinearRegression on a small advertising-style dataset, plus a predicted-vs-actual plot.
	- Purpose: minimal ML example—fit, evaluate (MAE/RMSE/R²), inspect coefficients, and visualize predictions.

## Getting started
1) Install dependencies (consider a virtualenv):
	```bash
	pip install pandas matplotlib scikit-learn
	```
2) Run the basic stats example from the repo root:
	```bash
	python examples/basic_stats/analysis.py
	```
3) Run the simple linear model:
	```bash
	python examples/simple_linear_model/train_linear_model.py
	```
4) Outputs:
	- `basic_stats`: console stats plus `examples/basic_stats/sales_vs_temperature.png` scatter plot.
	- `simple_linear_model`: metrics (MAE/RMSE/R²), coefficients, and `examples/simple_linear_model/pred_vs_actual.png` predicted-vs-actual plot.

More examples (ML, visualization, feature engineering) can be added alongside `basic_stats/` following the same pattern.
