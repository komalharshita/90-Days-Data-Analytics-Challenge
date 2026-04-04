import pandas as pd
import sqlite3
from datetime import datetime

INPUT = "transactions_raw.csv"
DB = "transactions.db"

def extract_task():
    data = {
        "txn_id": [1, 2, 3, 4],
        "user": ["U1", "U2", "U3", "U4"],
        "amount": [500, None, 700, 800]
    }
    pd.DataFrame(data).to_csv(INPUT, index=False)
    df = pd.read_csv(INPUT)
    print("Extract task done")
    return df

def transform_task(df):
    df["amount"].fillna(df["amount"].mean(), inplace=True)
    df["processed_at"] = datetime.now()
    print("Transform task done")
    return df

def validate_task(df):
    if df["amount"].isnull().any():
        print("Validation failed")
        return False
    print("Validation passed")
    return True

def load_task(df):
    conn = sqlite3.connect(DB)
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    print("Load task done")

def run_dag():
    print("\n--- DAG STARTED ---")

    df = extract_task()

    df = transform_task(df)

    if validate_task(df):
        load_task(df)

    print("--- DAG COMPLETED ---")

if __name__ == "__main__":
    run_dag()