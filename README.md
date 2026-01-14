# data-science-examples
A collection of practical data science examples covering data analysis, machine learning, and visualization using Python.

## Quick start (friendly for beginners)
1) Install Python 3.11+.
2) Open a terminal in this folder.
3) Install the needed libraries:
	```bash
	pip install pandas matplotlib scikit-learn
	```
4) Run an example (see below). Each script prints results and saves a picture in its folder.

## Examples
- [examples/basic_stats](examples/basic_stats): Small weather-and-sales table.
	- What you learn: load a CSV, check for missing data, see averages by city, compute a tiny moving average, and draw a scatter plot (temperature vs sales).
	- Run:
		```bash
		python examples/basic_stats/analysis.py
		```
	- You will see: printed stats plus the plot file `sales_vs_temperature.png` in the same folder.

- [examples/simple_linear_model](examples/simple_linear_model): Simple ad-spend → sales prediction.
	- What you learn: split data into train/test, fit a straight-line model (LinearRegression), read common metrics (MAE, RMSE, R²), and visualize predicted vs actual sales.
	- How to think about it: teach the model with part of the table, check it on the rest, see three scores (MAE/RMSE → lower is better, R² → closer to 1 is better), look at each channel’s weight (how much it moves sales), and view a scatter plot where the dashed line is “perfect predictions.”
	- Run:
		```bash
		python examples/simple_linear_model/train_linear_model.py
		```
	- You will see: printed metrics and coefficients plus the plot file `pred_vs_actual.png` in the same folder.
- [examples/github_deployment](examples/github_deployment): Auto-generate and deploy HTML reports with GitHub Actions.
	- What you learn: create an HTML report from data, automate it with GitHub Actions, and deploy to GitHub Pages.
	- Run:
		```bash
		python examples/github_deployment/generate_report.py
		```
	- You will see: a `report/` folder with an HTML dashboard showing traffic stats and charts. Open `index.html` in your browser.
## Tips if you're new
- If a command is not found, check you are in this folder and Python is installed.
- If imports fail, rerun the install command above.
- Open the CSVs to see the raw data: [examples/basic_stats/data.csv](examples/basic_stats/data.csv) and [examples/simple_linear_model/data.csv](examples/simple_linear_model/data.csv).

More examples (visualization, feature engineering, and beyond) can be added alongside these folders using the same pattern.
