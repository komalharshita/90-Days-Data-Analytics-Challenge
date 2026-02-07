import pandas as pd
import numpy as np

df = pd.read_csv("day_30/day_30_orders_dirty.csv")

# 1. Detect outliers using IQR

Q1 = df["order_amount"].quantile(0.25)
Q3 = df["order_amount"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df[(df["order_amount"] < lower) | (df["order_amount"] > upper)]



# 2. Detect outliers using Z-score

z = (df["quantity"] - df["quantity"].mean()) / df["quantity"].std()
df[z.abs() > 3]



# 3. Handle outliers

df["order_amount"] = df["order_amount"].clip(lower, upper)



# 4. Optimize data types

df["city"] = df["city"].astype("category")
df["order_id"] = pd.to_numeric(df["order_id"], downcast="integer")
df["quantity"] = pd.to_numeric(df["quantity"], downcast="integer")


# 5. Save cleaned data

df.to_csv("day_30/day_30_orders_clean.csv", index=False)

