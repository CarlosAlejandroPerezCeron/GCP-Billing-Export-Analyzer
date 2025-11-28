from query_billing import fetch_billing_data
from detect_anomalies import detect_anomalies
from export_reports import export_reports
from utils import log

def main():
    log("=== GCP Billing Export Analyzer ===")

    df = fetch_billing_data()
    df, anomalies = detect_anomalies(df)
    export_reports(df, anomalies)

    log("Pipeline completed successfully.")

if __name__ == "__main__":
    main()