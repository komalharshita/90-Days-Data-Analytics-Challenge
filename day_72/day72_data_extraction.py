import pandas as pd
import requests

print("\n--- STEP 1: CSV EXTRACTION ---")

csv_data = {
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 28]
}

df_csv = pd.DataFrame(csv_data)
df_csv.to_csv("customers.csv", index=False)

# Read CSV
df_csv = pd.read_csv("customers.csv")

print("\nCSV Data:")
print(df_csv)
print("Shape:", df_csv.shape)
print("Columns:", df_csv.columns.tolist())

print("\n--- STEP 2: EXCEL EXTRACTION ---")

# Create Excel file
df_csv.to_excel("customers.xlsx", index=False)

# Read Excel
df_excel = pd.read_excel("customers.xlsx")

print("\nExcel Data:")
print(df_excel)

print("\n--- STEP 3: API EXTRACTION ---")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

# Check if request successful
if response.status_code == 200:
    data = response.json()
    df_api = pd.DataFrame(data)
    
    print("\nAPI Data:")
    print(df_api.head())
else:
    print("Failed to fetch API data")

print("\n--- STEP 4: JSON HANDLING ---")

# Extract city from nested 'address'
df_api["City"] = df_api["address"].apply(lambda x: x["city"])

print("\nExtracted City Column:")
print(df_api[["name", "City"]])

print("\n--- STEP 5: COMBINING DATA ---")

# Just showing both datasets together
print("\nCSV Data Preview:")
print(df_csv.head())

print("\nAPI Data Preview:")
print(df_api[["name", "email", "City"]].head())

print("\n--- STEP 6: DATA VALIDATION ---")

print("CSV Info:")
print(df_csv.info())

print("\nAPI Info:")
print(df_api.info())

print("\n--- DATA EXTRACTION COMPLETED SUCCESSFULLY ---")