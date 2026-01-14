# Basic Stats Example

This is a first-step data check: read a small table, get quick facts, and draw one simple chart.

What you need
- Python
- pandas, matplotlib (install: `pip install pandas matplotlib`)
- File: data.csv (already here)

What the data means
- city: which city the row belongs to
- temperature_c: average temperature
- sales: units sold

What the script does (analysis.py)
- Loads data.csv.
- Prints: number of rows/columns, column names, missing values, and summary stats.
- Groups by city to show mean/min/max sales.
- Sorts by temperature and adds a 3-point rolling average of sales to smooth the curve.
- Plots temperature_c vs sales and saves a picture.

How to run
```bash
python examples/basic_stats/analysis.py
```

What you will see
- Console text: quick stats, per-city averages, and a rolling-average table.
- Image file: sales_vs_temperature.png (scatter plot saved in this folder).

How to read it
- Higher average temperature pairs with higher sales in this toy data.
- The rolling average column shows a smoother trend than the raw sales column.
- The scatter plot lets you eyeball the relationship; an upward pattern means positive correlation.

Try your own tweaks
- Add another city row to data.csv and rerun.
- Change the rolling window (search for `rolling(window=3` in analysis.py) to see how smoothing changes.
- Color the scatter by city to compare clusters (hint: use matplotlib `c=` or `hue`).
