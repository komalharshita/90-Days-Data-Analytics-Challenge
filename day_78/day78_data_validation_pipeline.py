import pandas as pd
import sqlite3
from datetime import datetime

INPUT_FILE = "orders_raw.csv"
OUTPUT_FILE = "orders_cleaned.csv"
DB_FILE = "orders.db"
TABLE_NAME = "orders_cleaned"

def extract(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print("Extraction error:", e)
        return None

def transform(df):
    try:
        df["price"].fillna(df["price"].mean(), inplace=True)
        df["quantity"].fillna(1, inplace=True)
        df = df.drop_duplicates()
        df["revenue"] = df["price"] * df["quantity"]
        df["timestamp"] = datetime.now()
        return df
    except Exception as e:
        print("Transformation error:", e)
        return None

def validate(df):
    try:
        assert df["order_id"].is_unique
        assert df["price"].notnull().all()
        assert df["quantity"].notnull().all()
        assert (df["price"] >= 0).all()
        assert (df["quantity"] > 0).all()
        assert df["revenue"].notnull().all()
        print("Validation passed")
        return True
    except AssertionError as e:
        print("Validation failed")
        return False

def load(df):
    try:
        df.to_csv(OUTPUT_FILE, index=False)
        conn = sqlite3.connect(DB_FILE)
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
        print("Data loaded successfully")
    except Exception as e:
        print("Loading error:", e)

def main():
    print("\n--- ETL PIPELINE WITH VALIDATION ---")

    sample_data = {
        "order_id": [1, 2, 3, 4, 4],
        "customer": ["A", "B", "C", "D", "D"],
        "price": [1000, 2000, None, 1500, 1500],
        "quantity": [1, 2, 1, None, None]
    }

    pd.DataFrame(sample_data).to_csv(INPUT_FILE, index=False)

    df = extract(INPUT_FILE)

    if df is not None:
        df = transform(df)

        if df is not None:
            is_valid = validate(df)

            if is_valid:
                load(df)
            else:
                print("Pipeline stopped due to validation failure")

    print("\n--- PIPELINE COMPLETED ---")

if __name__ == "__main__":
    main()