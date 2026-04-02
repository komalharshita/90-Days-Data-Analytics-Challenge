import pandas as pd

print("\n--- STEP 1: CREATING DATA SOURCES ---")

# Customers dataset
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 28]
})

# Orders dataset
orders = pd.DataFrame({
    "CustomerID": [1, 2, 2, 3, 5],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Price": [50000, 20000, 15000, 50000, 20000],
    "Quantity": [1, 2, 1, 1, 3]
})

print("\nCustomers Data:")
print(customers)

print("\nOrders Data:")
print(orders)


print("\n--- STEP 2: MERGING DATA ---")

merged_df = pd.merge(customers, orders, on="CustomerID", how="left")

print("\nMerged Data:")
print(merged_df)


print("\n--- STEP 3: CLEANING AFTER MERGE ---")

# Fill missing values
merged_df["Product"].fillna("Unknown", inplace=True)
merged_df["Price"].fillna(0, inplace=True)
merged_df["Quantity"].fillna(0, inplace=True)

print("\nCleaned Merged Data:")
print(merged_df)


print("\n--- STEP 4: FEATURE ENGINEERING ---")

merged_df["Revenue"] = merged_df["Price"] * merged_df["Quantity"]

print("\nWith Revenue Column:")
print(merged_df)


print("\n--- STEP 5: GROUPING ---")

revenue_by_customer = merged_df.groupby("Name")["Revenue"].sum()

print("\nRevenue by Customer:")
print(revenue_by_customer)


print("\n--- STEP 6: CONCATENATION ---")

# Simulate another month of orders
orders_month2 = pd.DataFrame({
    "CustomerID": [1, 3, 4],
    "Product": ["Tablet", "Phone", "Laptop"],
    "Price": [15000, 20000, 50000],
    "Quantity": [2, 1, 1]
})

all_orders = pd.concat([orders, orders_month2])

print("\nAll Orders Combined:")
print(all_orders)


print("\n--- STEP 7: FINAL DATASET ---")

final_df = pd.merge(customers, all_orders, on="CustomerID", how="left")
final_df["Revenue"] = final_df["Price"] * final_df["Quantity"]

print("\nFinal Dataset:")
print(final_df)


print("\n--- STEP 8: SAVE OUTPUT ---")

final_df.to_csv("90-Days-Data-Analytics-Challenge/day_76/final_multisource_data.csv", index=False)

print("\nData saved as final_multisource_data.csv")

print("\n--- MULTI-SOURCE ETL COMPLETED ---")