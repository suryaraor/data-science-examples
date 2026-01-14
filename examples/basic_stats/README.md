# Basic Stats Example

Goal: Explore a tiny weather-and-sales table, compute quick stats, and plot sales vs temperature.

Data
- File: data.csv
- Columns: city (category), temperature_c (float), sales (integer)

What the script does (analysis.py)
- Load the CSV into a pandas DataFrame.
- Print shape, columns, missing-value counts, and summary statistics.
- Group by city to show mean/min/max sales.
- Sort by temperature and add a 3-point rolling average for sales.
- Plot a scatter chart of temperature_c vs sales and save it.

Run it
```bash
python examples/basic_stats/analysis.py
```

Outputs
- Console: profiling info, per-city stats, rolling average table.
- File: sales_vs_temperature.png (scatter plot).

How to read the results
- Summary stats: look for reasonable min/max and whether std is large (data spread).
- Grouped stats: which city has higher average sales.
- Rolling average: smooths sales as temperature increases.
- Plot: upward trend suggests warmer temps correlate with higher sales.

Try this next
- Add another city row to data.csv and rerun.
- Change the rolling window size in analysis.py (sales_ma3) to see how smoothing changes.
- Color the scatter by city to compare clusters.
