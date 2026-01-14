from pathlib import Path
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for CI environments


def load_data(path: Path) -> pd.DataFrame:
    """Load the website traffic data."""
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def create_plots(df: pd.DataFrame, output_dir: Path) -> dict:
    """Generate and save plots, return their paths."""
    output_dir.mkdir(exist_ok=True)
    plots = {}
    
    # Time series plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["date"], df["page_views"], marker='o', label="Page views", linewidth=2)
    ax.plot(df["date"], df["unique_visitors"], marker='s', label="Unique visitors", linewidth=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    ax.set_title("Website Traffic Over Time")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    timeseries_path = output_dir / "timeseries.png"
    plt.savefig(timeseries_path)
    plt.close()
    plots["timeseries"] = timeseries_path
    
    # Summary bar chart
    summary = df[["page_views", "unique_visitors"]].sum()
    fig, ax = plt.subplots(figsize=(6, 4))
    summary.plot(kind='bar', ax=ax, color=['steelblue', 'coral'])
    ax.set_ylabel("Total Count")
    ax.set_title("Total Traffic Summary")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    
    summary_path = output_dir / "summary.png"
    plt.savefig(summary_path)
    plt.close()
    plots["summary"] = summary_path
    
    return plots


def generate_html_report(df: pd.DataFrame, plots: dict, output_path: Path) -> None:
    """Create an HTML report with stats and embedded plots."""
    stats = {
        "Total Page Views": df["page_views"].sum(),
        "Total Unique Visitors": df["unique_visitors"].sum(),
        "Average Daily Page Views": round(df["page_views"].mean(), 1),
        "Average Daily Visitors": round(df["unique_visitors"].mean(), 1),
        "Peak Page Views": df["page_views"].max(),
        "Peak Date": df.loc[df["page_views"].idxmax(), "date"].strftime("%Y-%m-%d")
    }
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Traffic Analysis Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
                background: #f5f5f5;
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            .stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin: 20px 0;
            }}
            .stat-card {{
                background: #ecf0f1;
                padding: 15px;
                border-radius: 5px;
                border-left: 4px solid #3498db;
            }}
            .stat-label {{
                font-size: 0.9em;
                color: #7f8c8d;
                margin-bottom: 5px;
            }}
            .stat-value {{
                font-size: 1.5em;
                font-weight: bold;
                color: #2c3e50;
            }}
            .plot {{
                margin: 30px 0;
                text-align: center;
            }}
            .plot img {{
                max-width: 100%;
                border-radius: 5px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .footer {{
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #ecf0f1;
                text-align: center;
                color: #95a5a6;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Website Traffic Analysis Report</h1>
            <p>Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            
            <h2>Key Metrics</h2>
            <div class="stats">
    """
    
    for label, value in stats.items():
        formatted_value = f"{value:,}" if isinstance(value, (int, float)) else value
        html += f"""
                <div class="stat-card">
                    <div class="stat-label">{label}</div>
                    <div class="stat-value">{formatted_value}</div>
                </div>
        """
    
    html += """
            </div>
            
            <h2>Traffic Trends</h2>
            <div class="plot">
                <img src="timeseries.png" alt="Traffic over time">
            </div>
            
            <h2>Summary</h2>
            <div class="plot">
                <img src="summary.png" alt="Total traffic summary">
            </div>
            
            <div class="footer">
                <p>Auto-generated report from data-science-examples</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    output_path.write_text(html, encoding='utf-8')
    print(f"Report saved to {output_path}")


def main() -> None:
    base_dir = Path(__file__).parent
    data_path = base_dir / "data.csv"
    output_dir = base_dir / "report"
    
    print("Loading data...")
    df = load_data(data_path)
    
    print("Creating plots...")
    plots = create_plots(df, output_dir)
    
    print("Generating HTML report...")
    report_path = output_dir / "index.html"
    generate_html_report(df, plots, report_path)
    
    print(f"\n✅ Report generated successfully!")
    print(f"Open {report_path} in your browser to view.")


if __name__ == "__main__":
    main()
