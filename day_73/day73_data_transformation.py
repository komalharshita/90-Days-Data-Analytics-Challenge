import pandas as pd
import numpy as np

print("\n--- STEP 1: RAW DATA ---")

data = {
    "Customer": ["Alice", "Bob", "Charlie", "Alice", None],
    "Age": [25, None, 35, 25, 40],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Price": [50000, 20000, None, 50000, 20000],
    "Quantity": [1, 2, 1, 1, None]
}

df = pd.DataFrame(data)

print(df)

print("\n--- STEP 2: HANDLING MISSING VALUES ---")

df_clean = df.dropna()

print("\nAfter dropping missing values:")
print(df_clean)

print("\n--- STEP 3: REMOVE DUPLICATES ---")

df_clean = df_clean.drop_duplicates()

print("\nAfter removing duplicates:")
print(df_clean)

print("\n--- STEP 4: DATA TYPE CONVERSION ---")

df_clean["Age"] = df_clean["Age"].astype(int)
df_clean["Price"] = df_clean["Price"].astype(float)

print(df_clean.dtypes)

print("\n--- STEP 5: FEATURE ENGINEERING ---")

# Create Revenue column
df_clean["Revenue"] = df_clean["Price"] * df_clean["Quantity"]

# Create Age Group column
df_clean["Age_Group"] = df_clean["Age"].apply(
    lambda x: "Young" if x < 30 else "Adult"
)

print(df_clean)

print("\n--- STEP 6: FILTERING ---")

high_revenue = df_clean[df_clean["Revenue"] > 30000]

print("\nHigh Revenue Records:")
print(high_revenue)


print("\n--- STEP 7: SORTING ---")

sorted_df = df_clean.sort_values(by="Revenue", ascending=False)

print(sorted_df)


print("\n--- STEP 8: GROUPING ---")

grouped = df_clean.groupby("Product")["Revenue"].sum()

print("\nRevenue by Product:")
print(grouped)

print("\n--- STEP 9: SAVE DATA ---")

df_clean.to_csv("day_73/transformed_data.csv", index=False)

print("\nData saved as transformed_data.csv")

print("\n--- DATA TRANSFORMATION COMPLETED ---")