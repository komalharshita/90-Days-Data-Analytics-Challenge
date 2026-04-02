import pandas as pd
import sqlite3

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "cleaned_data.csv"
DB_FILE = "etl_pipeline.db"
TABLE_NAME = "sales"


# STEP 1: EXTRACT

def extract(file_path):
    print("\n[EXTRACT] Starting data extraction...")
    try:
        df = pd.read_csv(file_path)
        print("[EXTRACT] Data extracted successfully")
        return df
    except Exception as e:
        print("[ERROR] Extraction failed:", e)
        return None


# STEP 2: TRANSFORM

def transform(df):
    print("\n[TRANSFORM] Starting data transformation...")
    
    try:
        # Handle missing values
        df["Age"].fillna(df["Age"].mean(), inplace=True)
        df["Price"].fillna(df["Price"].mean(), inplace=True)

        # Convert data types
        df["Age"] = df["Age"].astype(int)
        df["Price"] = df["Price"].astype(float)

        # Feature Engineering
        df["Revenue"] = df["Price"] * df["Quantity"]

        # Remove duplicates
        df = df.drop_duplicates()

        print("[TRANSFORM] Transformation completed")
        return df

    except Exception as e:
        print("[ERROR] Transformation failed:", e)
        return None


# STEP 3: LOAD

def load(df, output_file, db_file, table_name):
    print("\n[LOAD] Starting data loading...")

    try:
        # Save to CSV
        df.to_csv(output_file, index=False)
        print(f"[LOAD] Data saved to {output_file}")

        # Save to Database
        conn = sqlite3.connect(db_file)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        print(f"[LOAD] Data loaded into database ({table_name})")

    except Exception as e:
        print("[ERROR] Loading failed:", e)


# MAIN PIPELINE

def main():
    print("\n===== ETL PIPELINE STARTED =====")

    # Create sample input file (for practice)
    sample_data = {
        "Customer": ["Alice", "Bob", "Charlie", "David", None],
        "Age": [25, 30, None, 22, 28],
        "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
        "Price": [50000, 20000, None, 50000, 20000],
        "Quantity": [1, 2, 1, 1, None]
    }

    pd.DataFrame(sample_data).to_csv(INPUT_FILE, index=False)

    # Run pipeline
    df = extract(INPUT_FILE)

    OUTPUT_FILE = "90-Days-Data-Analytics-Challenge/day_75/cleaned_data.csv"
    
    if df is not None:
        df_transformed = transform(df)

        if df_transformed is not None:
            load(df_transformed, OUTPUT_FILE, DB_FILE, TABLE_NAME)



    print("\n===== ETL PIPELINE COMPLETED =====")


if __name__ == "__main__":
    main()