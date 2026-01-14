# data-science-examples
A collection of practical data science examples covering data analysis, machine learning, and visualization using Python.

## Structure
- [examples/basic_stats](examples/basic_stats): Descriptive statistics starter with a tiny CSV and Matplotlib scatter plot.
	- Purpose: show an end-to-end mini workflow—load CSV, profile, group by city, compute a rolling average, and plot temperature vs sales.

## Getting started
1) Install dependencies (consider a virtualenv):
	```bash
	pip install pandas matplotlib
	```
2) Run the basic stats example from the repo root:
	```bash
	python examples/basic_stats/analysis.py
	```
3) Outputs:
	- Console: shape, missing values, summary stats, per-city averages, and a 3-point moving average.
	- File: `examples/basic_stats/sales_vs_temperature.png` scatter plot.

More examples (ML, visualization, feature engineering) can be added alongside `basic_stats/` following the same pattern.
