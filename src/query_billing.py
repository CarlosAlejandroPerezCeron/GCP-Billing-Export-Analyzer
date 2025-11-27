from google.cloud import bigquery
import pandas as pd
from utils import get_env, log

def fetch_billing_data():
    client = bigquery.Client(project=get_env("GCP_PROJECT_ID"))

    dataset = get_env("BQ_DATASET")
    table = get_env("BQ_TABLE")

    query = f"""
    SELECT
      service.description AS service,
      project.id AS project_id,
      DATE(usage_start_time) AS date,
      SUM(cost) AS total_cost
    FROM `{get_env("GCP_PROJECT_ID")}.{dataset}.{table}`
    WHERE cost > 0
    GROUP BY service, project_id, date
    ORDER BY date DESC
    """

    log("Executing BigQuery billing export query...")
    df = client.query(query).to_dataframe()
    log(f"Fetched {len(df)} rows from BigQuery.")
    return df

if __name__ == "__main__":
    print(fetch_billing_data().head())
