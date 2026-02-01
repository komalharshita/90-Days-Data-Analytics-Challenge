"""
Day 23 Homework - Error handling, CSV scripts, regex, debugging

Solve the problems below. Use built-in libraries only.
"""

# 1. Safe CSV reader
# Write a function safe_read_scores(path) that reads a CSV with header name,city,age,score
# It should return (total_score, count) for valid numeric score rows.
# - Use try/except to handle FileNotFoundError and ValueError on rows.
# - Skip rows with invalid data but continue processing.
# - Do not use pandas.

def safe_read_scores(path):
    total = 0
    count = 0

    try:
        with open(path, "r") as f:
            next(f)
            for line in f:
                try:
                    parts = line.strip().split(",")
                    score = int(parts[3])
                    total += score
                    count += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File not found")

    return total, count



# 2. Merge CSVs into merged.csv
# Write a function merge_customers_purchases(cust_path, pur_path, out_path)
# - cust_path: CSV with columns customer_id,name,...
# - pur_path: CSV with columns purchase_id,customer_id,product,category,amount,purchase_date
# - out_path: write a CSV with header: purchase_id,customer_name,product,amount
# - If customer_id not found, write 'UNKNOWN' as customer_name
# - Use try/except for file operations.

def merge_customers_purchases(cust_path, pur_path, out_path):
    customers = {}

    try:
        with open(cust_path, "r") as f:
            next(f)
            for line in f:
                parts = line.strip().split(",")
                customers[parts[0]] = parts[1]
    except FileNotFoundError:
        print("Customer file missing")

    try:
        with open(pur_path, "r") as p, open(out_path, "w") as out:
            next(p)
            out.write("purchase_id,customer_name,product,amount\n")

            for line in p:
                parts = line.strip().split(",")
                pid = parts[0]
                cid = parts[1]
                product = parts[2]
                amount = parts[4]

                name = customers.get(cid, "UNKNOWN")
                out.write(f"{pid},{name},{product},{amount}\n")

    except FileNotFoundError:
        print("Purchases file missing")




# 3. Regex cleaning
# Write a function clean_price(s) that accepts price strings like 'Rs. 1,299', '₹499', '700'
# and returns integer cents/rupees (e.g., 1299, 499, 700).
# Use re module. Handle edge cases gracefully (return 0 for empty or None).

import re

def clean_price(s):
    if not s:
        return 0

    num = re.sub(r'\D', '', s)
    if num == "":
        return 0
    return int(num)




# 4. Debugging task
# Deliberately create a function buggy_average(numbers) that sometimes raises an exception for an empty list.
# Then write a wrapper function safe_average(numbers) that calls buggy_average and uses try/except to return 0 on error.
# Add docstrings to both functions.


def buggy_average(numbers):
    return sum(numbers) / len(numbers)


def safe_average(numbers):
    try:
        return buggy_average(numbers)
    except ZeroDivisionError:
        return 0
