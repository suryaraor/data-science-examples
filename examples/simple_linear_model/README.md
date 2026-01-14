# Simple Linear Model Example

Goal: Predict sales from ad spend (TV, radio, social) with a basic linear regression and understand its quality.

Data
- File: data.csv
- Columns: tv_spend, radio_spend, social_spend (floats), sales (float target)

What the script does (train_linear_model.py)
- Load the dataset.
- Split rows into train (learn) and test (check) sets.
- Fit sklearn LinearRegression on train data.
- Predict sales on the test set.
- Report metrics: MAE, RMSE (lower is better), R² (closer to 1 is better).
- Show learned coefficients per channel and the intercept.
- Plot predicted vs actual sales with a dashed identity line (perfect predictions).

Run it
```bash
python examples/simple_linear_model/train_linear_model.py
```

Outputs
- Console: metrics, coefficients, intercept.
- File: pred_vs_actual.png (scatter of predicted vs actual with ideal line).

How to read the results
- MAE/RMSE: average error size; smaller means better predictions.
- R²: fraction of sales variation explained; nearer to 1 means a stronger fit.
- Coefficients: how much each channel moves sales; negative means spending there reduces predicted sales (in this tiny sample).
- Plot: points near the dashed line are good predictions; wide scatter means the model is limited.

Try this next
- Change test_size in train_test_split to see how it affects metrics.
- Remove one feature (e.g., social_spend) to test its impact.
- Add synthetic noise to sales to see metrics drop.
- Swap LinearRegression for Ridge or Lasso to compare coefficients.
