import pandas as pd
import sqlite3

print("\n--- STEP 1: EXTRACT ---")

data = {
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, None, 28],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Price": [50000, 20000, 15000, 50000, None],
    "Quantity": [1, 2, 1, 1, 3]
}

df = pd.DataFrame(data)

print("\nRaw Data:")
print(df)

print("\n--- STEP 2: TRANSFORM ---")

# Handle missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Price"].fillna(df["Price"].mean(), inplace=True)

# Convert data types
df["Age"] = df["Age"].astype(int)
df["Price"] = df["Price"].astype(float)

# Feature Engineering
df["Revenue"] = df["Price"] * df["Quantity"]

print("\nCleaned Data:")
print(df)

print("\n--- STEP 3: LOAD TO CSV ---")

csv_file = "cleaned_data.csv"
df.to_csv(csv_file, index=False)

print(f"Data saved to {csv_file}")

print("\n--- STEP 4: LOAD TO EXCEL ---")

excel_file = "cleaned_data.xlsx"
df.to_excel(excel_file, index=False)

print(f"Data saved to {excel_file}")


print("\n--- STEP 5: LOAD TO DATABASE ---")

conn = sqlite3.connect("sales_data.db")

# Load data into table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded into SQLite database (table: sales)")

print("\n--- STEP 6: READ FROM DATABASE ---")

df_db = pd.read_sql("SELECT * FROM sales", conn)

print("\nData from Database:")
print(df_db)

print("\n--- STEP 7: VALIDATION ---")

print("\nShape:", df_db.shape)
print("\nColumns:", df_db.columns.tolist())
print("\nData Types:\n", df_db.dtypes)

print("\n--- STEP 8: APPEND DATA ---")

new_data = pd.DataFrame({
    "Customer": ["Frank"],
    "Age": [32],
    "Product": ["Tablet"],
    "Price": [18000],
    "Quantity": [2],
    "Revenue": [36000]
})

new_data.to_sql("sales", conn, if_exists="append", index=False)

print("New data appended to database")


df_updated = pd.read_sql("SELECT * FROM sales", conn)
print("\nUpdated Database:")
print(df_updated)

print("\n--- DATA LOADING COMPLETED SUCCESSFULLY ---")