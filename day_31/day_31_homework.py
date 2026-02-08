import pandas as pd

df = pd.read_csv("day_31/day_31_iot_logs_dirty.csv")


# 1. Identify duplicate rows

df[df.duplicated()]


# 2. Identify duplicates using business keys

df[df.duplicated(subset = ["device_id", "event_type", "event_time"])]


# 3. Remove duplicates keeping the latest record

df = df.drop_duplicates(
    subset = ["device_id", "event_type", "event_time"],
    keep = "last"
)


# 4. Parse event_time to datetime

df["event_time"] = pd.to_datetime(
    df["event_time"],
    errors = "coerce"
)


# 5. Extract date and hour

df["event_date"] = df["event_time"].dt.date
df["event_hour"] = df["event_time"].dt.hour


# 6. Save cleaned dataset

df.to_csv("day_31/day_31_iot_logs_clean.csv")
