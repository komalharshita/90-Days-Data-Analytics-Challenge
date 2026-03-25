import pandas as pd

# ------------------------------
# STEP 1: EXTRACT
# ------------------------------
print("\n--- STEP 1: EXTRACT ---")

data = {
    "Customer": ["Alice", "Bob", "Charlie", None, "Eve"],
    "Age": [25, 30, None, 22, 29],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", None],
    "Price": [50000, 20000, 15000, None, 30000],
    "Quantity": [1, 2, 1, 1, None]
}

df = pd.DataFrame(data)

print("\nRaw Data:")
print(df)


# ------------------------------
# STEP 2: TRANSFORM
# ------------------------------
print("\n--- STEP 2: TRANSFORM ---")

# 1. Handle missing values
print("\nHandling missing values...")
df_clean = df.dropna()

# 2. Create new column (Feature Engineering)
print("Creating Revenue column...")
df_clean["Revenue"] = df_clean["Price"] * df_clean["Quantity"]

# 3. Convert data types
print("Converting data types...")
df_clean["Age"] = df_clean["Age"].astype(int)

# 4. Remove duplicates (if any)
df_clean = df_clean.drop_duplicates()

print("\nCleaned Data:")
print(df_clean)


# ------------------------------
# STEP 3: LOAD
# ------------------------------
print("\n--- STEP 3: LOAD ---")

# Save cleaned data to CSV
output_file = "day_71/cleaned_sales_data.csv"
df_clean.to_csv(output_file, index=False)

print(f"\nData successfully saved to {output_file}")


print("\n--- ETL PIPELINE COMPLETED SUCCESSFULLY ---")