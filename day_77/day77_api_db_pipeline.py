import pandas as pd
import requests
import sqlite3

# config
API_URL = "https://dummyjson.com/users"
DB_FILE = "company_v2.db"

# setup database
conn = sqlite3.connect(DB_FILE)

departments = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "department": ["HR", "IT", "Finance", "Marketing", "Sales"]
})

departments.to_sql("departments", conn, if_exists="replace", index=False)

# extract API
response = requests.get(API_URL)
data = response.json()["users"]
df_api = pd.DataFrame(data)

# select & rename
df_api = df_api[["id", "firstName", "lastName", "email", "address"]]
df_api.rename(columns={"id": "user_id"}, inplace=True)

# extract nested field
df_api["city"] = df_api["address"].apply(lambda x: x["city"])

# combine names
df_api["full_name"] = df_api["firstName"] + " " + df_api["lastName"]

df_api = df_api[["user_id", "full_name", "email", "city"]]

# extract DB
df_db = pd.read_sql("SELECT * FROM departments", conn)

# merge
df = pd.merge(df_api, df_db, on="user_id", how="left")

# transform
df["department"].fillna("Unknown", inplace=True)
df["email_domain"] = df["email"].apply(lambda x: x.split("@")[1])

# load
df.to_csv("90-Days-Data-Analytics-Challenge/day_77/final_users_v2.csv", index=False)
df.to_sql("90-Days-Data-Analytics-Challenge/day_77/final_users", conn, if_exists="replace", index=False)

# validate
df_check = pd.read_sql("SELECT * FROM final_users", conn)
print(df_check.head())