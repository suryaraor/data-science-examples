# GitHub Deployment Example

Auto-generate and deploy a data analysis report using GitHub Actions.

What you need
- Python
- pandas, matplotlib (install: `pip install pandas matplotlib`)
- A GitHub account (for deployment)
- File: data.csv (already here)

What the data means
- date: date of measurement
- page_views: total page views that day
- unique_visitors: distinct visitors that day

What the script does (generate_report.py)
- Loads website traffic data from data.csv.
- Creates two plots: time series trend and total summary bar chart.
- Generates a nice HTML report with key metrics and embedded charts.
- Saves everything to a `report/` folder.

How to run locally
```bash
python examples/github_deployment/generate_report.py
```
Then open `examples/github_deployment/report/index.html` in your browser.

What you will see
- Console: progress messages.
- Folder: `report/` with index.html, timeseries.png, summary.png.
- Report shows: total/average stats, peak date, and visual charts.

GitHub Actions automation
The workflow file `.github/workflows/run_analysis.yml` does:
- Runs automatically on every push to main/master.
- Can be triggered manually from the Actions tab.
- Optional: runs daily at midnight (uncomment the schedule).
- Installs dependencies, runs the script, saves the report.
- Optionally deploys the HTML report to GitHub Pages.

How to set up GitHub deployment
1. Push this repo to GitHub.
2. Go to Settings → Pages → Source → select "gh-pages" branch.
3. Push a commit to trigger the workflow (Actions tab to monitor).
4. After a minute, visit: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

What you learn
- How to generate an HTML report with Python.
- How to use GitHub Actions for automation.
- How to deploy static content to GitHub Pages.
- How to schedule recurring analysis runs.

Try your own tweaks
- Update data.csv with new rows and push to see auto-regeneration.
- Add more plots (e.g., day-of-week patterns).
- Customize the HTML template styling.
- Add email notifications when metrics cross thresholds.
- Connect to a real data source (API, database) instead of CSV.
