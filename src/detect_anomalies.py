import pandas as pd
from sklearn.ensemble import IsolationForest
from utils import get_env, log

def detect_anomalies(df):
    threshold = float(get_env("ANOMALY_THRESHOLD", 15))
    log(f"Detecting anomalies above {threshold}% variation...")

    df = df.sort_values("date")
    df["pct_change"] = df.groupby("service")["total_cost"].pct_change() * 100
    df["is_spike"] = df["pct_change"].abs() > threshold

    # Optional ML detection for complex trends
    model = IsolationForest(contamination=0.05, random_state=42)
    df["ml_anomaly"] = model.fit_predict(df[["total_cost"]])
    df["ml_anomaly"] = df["ml_anomaly"].apply(lambda x: True if x == -1 else False)

    anomalies = df[df["is_spike"] | df["ml_anomaly"]]
    log(f"Detected {len(anomalies)} anomalies.")
    return df, anomalies
