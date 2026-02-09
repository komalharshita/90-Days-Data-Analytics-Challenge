import pandas as pd
import numpy as np

df = pd.read_csv("day_32/day_32_logistics_shipments.csv")

# 1. Parse dispatch_time and delivery_time to datetime

df["dispatch_time"] = pd.to_datetime(df["dispatch_time"])
df["delivery_time"] = pd.to_datetime((df["delivery_time"]))


# 2. Create delivery_duration_min

df["dispatch_time"] = pd.to_datetime(df["dispatch_time"])
df["delivery_time"] = pd.to_datetime(df["delivery_time"])
df.dtypes

df["delivery_duration_min"] = (
    df["delivery_time"] - df["dispatch_time"]
).dt.total_seconds() / 60


# 3. Create dispatch_hour and is_weekend

df["dispatch_hour"] = df["dispatch_time"].dt.hour
df["is_weekend"] = df["dispatch_time"].dt.weekday >= 5


# 4. Create speed_kmph

df["delivery_hours"] = df["delivery_duration_min"] / 60
df["speed_kmph"] = df["distance_km"] / df["delivery_hours"]


# 5. Create distance_bucket

df["distance_bucket"] = pd.cut(
    df["distance_km"],
    bins=[0, 15, 30, np.inf],
    labels=["Short", "Medium", "Long"]
)


# 6. Create is_delayed flag

df["is_delayed"] = df["delivery_status"] == "Delayed"



# 7. Add data quality assertions

assert (df["delivery_duration_min"] >= 0).all()
assert (df["distance_km"] > 0).all()
assert (df["speed_kmph"] < 120).all()


# 8. Save final dataset as day_32_logistics_features.csv

df.to_csv("day_32/day_32_logistics_features.csv", index=False)


