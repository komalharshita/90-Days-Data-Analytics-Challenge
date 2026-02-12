import pandas as pd
import numpy as np

df = pd.read_csv("day_35/day_35_learning_platform_dirty.csv")

# 1. Inspect category inconsistencies

print(df["course_category"].value_counts())
print(df["subscription_type"].value_counts())


# 2. Standardize course_category and subscription_type

df["course_category"] = (
    df["course_category"]
    .str.strip()
    .str.lower()
)

df["subscription_type"] = (
    df["subscription_type"]
    .str.strip()
    .str.lower()
)

df["course_category"] = df["course_category"].replace({
    "ds": "data science",
    "data science": "data science",
    "web dev": "web development",
    "web development": "web development",
    "ai": "ai"
})

df["subscription_type"] = df["subscription_type"].replace({
    "paid": "paid",
    "free": "free",
    "trial": "trial"
})


# 3. Handle invalid ages and completion_rate values

df.loc[(df["age"] < 18) | (df["age"] > 30), "age"] = np.nan
df.loc[(df["completion_rate"] < 0) | (df["completion_rate"] > 1), "completion_rate"] = np.nan


# 4. Apply conditional cleaning rules

df.loc[df["hours_spent"] == 0, "completion_rate"] = 0


# 5. Prepare final dataset for EDA

final_df = df[
    ["user_id", "course_category", "subscription_type", "age", "hours_spent", "completion_rate"]
]


# 6. Save as day_35_learning_platform_clean.csv

final_df.to_csv("day_35/cleaned_csv.csv", index = False)
