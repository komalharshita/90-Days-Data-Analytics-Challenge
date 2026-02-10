import pandas as pd

df = pd.read_csv("day_33/day_33_event_registrations_dirty.csv")

# 1. Parse registration_date using pd.to_datetime (handle invalid dates)

df["registration_date"] = pd.to_datetime(
    df["registration_date"], errors = "coerce"
)


# 2. Create year, month, and day columns

df["year"] = df["registration_date"].dt.year
df["month"] = df["registration_date"].dt.month
df["day"] = df["registration_date"].dt.day


# 3. Clean event_name (strip, lowercase, remove special chars)

df["event_name"] = (
    df["event_name"]
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z\s]", "", regex = True)
    .str.replace(r"\s+", "", regex = True)
)


# 4. Clean city names (strip, lowercase, remove non-letters)

df["city"] = (
    df["city"]
    .str.strip()
    .str.lower()
    .str.replace(r"[^a-z]", "", regex = True)
)


# 5. Count registrations per city

registrations_per_city = (
    df.groupby("city", dropna=False)
      .size()
      .reset_index(name="registrations")
)
registrations_per_city



# 6. Save cleaned dataset

df.to_csv("day_33/day_33_event_registrations_clean.csv", index=False)

