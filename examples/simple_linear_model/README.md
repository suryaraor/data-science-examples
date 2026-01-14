# Simple Linear Model Example

Predict sales from ad spend (TV, radio, social) using a straight-line model, then judge how good it is.

What you need
- Python
- pandas, matplotlib, scikit-learn (install: `pip install pandas matplotlib scikit-learn`)
- File: data.csv (already here)

What the data means
- tv_spend, radio_spend, social_spend: money spent on each channel
- sales: the sales that followed (this is what we predict)

What the script does (train_linear_model.py)
- Loads data.csv.
- Splits rows into train (to learn) and test (to check).
- Fits LinearRegression on the train set.
- Predicts sales on the test set.
- Reports three scores: MAE and RMSE (lower is better), R² (closer to 1 is better).
- Prints the weight for each channel and the intercept (baseline sales).
- Draws predicted vs actual sales with a dashed line showing “perfect” predictions.

How to run
```bash
python examples/simple_linear_model/train_linear_model.py
```

What you will see
- Console text: metrics, channel weights (coefficients), and intercept.
- Image file: pred_vs_actual.png (saved in this folder).

How to read it
- MAE/RMSE: typical size of the prediction error; smaller is better.
- R²: how much of the sales variation the model explains; closer to 1 is better.
- Coefficients: how much each channel moves predicted sales; a negative value means that channel lowers the prediction in this toy sample.
- Plot: points near the dashed line are good predictions; a wide scatter means the model is limited.

Try your own tweaks
- Change test_size in train_test_split to see how scores change.
- Drop a feature (e.g., remove social_spend) and rerun to see its importance.
- Add a new feature column (e.g., billboard_spend) and fit again.
- Replace LinearRegression with Ridge or Lasso to compare the coefficients.
