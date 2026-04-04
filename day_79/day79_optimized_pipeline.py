import pandas as pd
import sqlite3
from datetime import datetime

CONFIG = {
    "input_file": "sales_raw.csv",
    "output_file": "output/sales_cleaned.csv",
    "db_file": "sales_opt.db",
    "table": "sales_cleaned"
}

def extract(path):
    df = pd.read_csv(path)
    return df

def transform(df):
    df = df.drop_duplicates()
    df["price"].fillna(df["price"].median(), inplace=True)
    df["quantity"].fillna(1, inplace=True)
    df["revenue"] = df["price"] * df["quantity"]
    df["processed_at"] = datetime.now()
    return df

def validate(df):
    if not df["order_id"].is_unique:
        return False
    if df["price"].isnull().any():
        return False
    if (df["price"] < 0).any():
        return False
    return True

def load(df, config):
    df.to_csv(config["output_file"], index=False)
    conn = sqlite3.connect(config["db_file"])
    df.to_sql(config["table"], conn, if_exists="replace", index=False)

def log(msg):
    print(f"[LOG] {msg}")

def main():
    log("Pipeline started")

    sample_data = {
        "order_id": [101, 102, 103, 104, 104],
        "product": ["A", "B", "C", "A", "A"],
        "price": [100, 200, None, 150, 150],
        "quantity": [1, 2, 1, None, None]
    }

    pd.DataFrame(sample_data).to_csv(CONFIG["input_file"], index=False)

    df = extract(CONFIG["input_file"])
    log("Data extracted")

    df = transform(df)
    log("Data transformed")

    if validate(df):
        load(df, CONFIG)
        log("Data loaded")
    else:
        log("Validation failed")

    log("Pipeline completed")

if __name__ == "__main__":
    main()