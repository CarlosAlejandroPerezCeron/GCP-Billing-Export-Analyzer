import os
import matplotlib.pyplot as plt
from utils import get_env, log

def export_reports(df, anomalies):
    output_dir = get_env("OUTPUT_DIR", "./reports")
    os.makedirs(output_dir, exist_ok=True)

    df.to_csv(os.path.join(output_dir, "daily_costs.csv"), index=False)
    anomalies.to_csv(os.path.join(output_dir, "anomalies.csv"), index=False)

    plt.figure(figsize=(12,6))
    plt.plot(df["date"], df["total_cost"], label="Cost")
    plt.scatter(anomalies["date"], anomalies["total_cost"], color="red", label="Anomalies")
    plt.title("GCP Cost Anomalies Over Time")
    plt.xlabel("Date")
    plt.ylabel("USD")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "anomalies_chart.png"))
    log("Reports and chart exported successfully.")
