import pandas as pd
import os

# ---------- 1. Load or clean ---------------------------------
if os.path.exists("cleaned_output.csv"):
    df = pd.read_csv("cleaned_output.csv")
    print("📂 cleaned_output.csv chargé")
else:
    df = pd.read_csv("Functional Task - OLTP_Subscription.csv")
    df["SubscriptionProgress"] = df["SubscriptionProgress"].str.replace('%', '').astype(float)
    df["SubscriptionStartDate"] = pd.to_datetime(df["SubscriptionStartDate"], errors="coerce")
    df["SubscriptionMonth"] = df["SubscriptionStartDate"].dt.to_period("M")
    df.to_csv("cleaned_output.csv", index=False)
    print("✅ cleaned_output.csv créé")

# ---------- 2. OLAP aggregation -------------------------------
df["IsDiploma"] = df["SubscriptionHasDiploma"].astype(int)
revenue = {"P1": 100, "P2": 150, "Night": 120, "Day": 120}
df["EstimatedRevenue"] = df["ProductSchedule"].map(revenue).fillna(100)
df["IsChurned"] = df["SubscriptionProgress"] < 50

olap = (
    df.groupby(["SubscriptionMonth", "Country", "TrackName"])
      .agg(
          total_subscriptions=("Student", "count"),
          avg_progression=("SubscriptionProgress", "mean"),
          diploma_rate=("IsDiploma", "mean"),
          estimated_revenue=("EstimatedRevenue", "sum"),
          churn_rate=("IsChurned", "mean")
      )
      .reset_index()
)

olap["avg_progression"] = olap["avg_progression"].round(2)
olap["diploma_rate"]   = (olap["diploma_rate"] * 100).round(2)
olap["churn_rate"]     = (olap["churn_rate"]   * 100).round(2)

olap.to_csv("OLAP_Cohort_Analysis.csv", index=False)
print("📊 OLAP_Cohort_Analysis.csv créé")
print(olap.head())
