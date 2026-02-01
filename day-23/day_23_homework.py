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

# 2. Merge CSVs into merged.csv
# Write a function merge_customers_purchases(cust_path, pur_path, out_path)
# - cust_path: CSV with columns customer_id,name,...
# - pur_path: CSV with columns purchase_id,customer_id,product,category,amount,purchase_date
# - out_path: write a CSV with header: purchase_id,customer_name,product,amount
# - If customer_id not found, write 'UNKNOWN' as customer_name
# - Use try/except for file operations.

# 3. Regex cleaning
# Write a function clean_price(s) that accepts price strings like 'Rs. 1,299', '₹499', '700'
# and returns integer cents/rupees (e.g., 1299, 499, 700).
# Use re module. Handle edge cases gracefully (return 0 for empty or None).

# 4. Debugging task
# Deliberately create a function buggy_average(numbers) that sometimes raises an exception for an empty list.
# Then write a wrapper function safe_average(numbers) that calls buggy_average and uses try/except to return 0 on error.
# Add docstrings to both functions.
