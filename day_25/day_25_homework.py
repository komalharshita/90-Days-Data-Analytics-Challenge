"""
Day 25 Homework — Strings, Loops, Functions
"""

# Load CSV manually and store rows

# 1. Clean price column and store numeric prices

rows = []

with open("day_25/day_25_cafe_orders.csv", "r") as f:
    next(f)
    for line in f:
        rows.append(line.strip())

prices = []
for row in rows:
    parts = row.split(",")
    price = int(parts[4].replace("Rs.", "").strip())
    prices.append(price)

prices



# 2. Print all orders from Pune

for row in rows:
    parts = row.split(",")
    if parts[2] == "Pune":
        print(parts)



# 3. Write a function highest_price(rows) that returns the highest order price

def highest_price(rows):
    max_price = 0
    for row in rows:
        parts = row.split(",")
        price = int(parts[4].replace("Rs.", "").strip())
        if price > max_price:
            max_price = price
    return max_price

highest_price(rows)



# 4. Write a function count_orders_by_item(rows, item_name)

def count_orders_by_item(rows, item_name):
    count = 0
    for row in rows:
        parts = row.split(",")
        if parts[3] == item_name:
            count += 1
    return count

count_orders_by_item(rows, "Latte")



# 5. Write cleaned output to a new CSV file named cleaned_orders.csv

with open("cleaned_orders.csv", "w") as out:
    out.write("order_id,customer_name,city,item,price\n")

    for row in rows:
        parts = row.split(",")
        price = parts[4].replace("Rs.", "").strip()
        out.write(f"{parts[0]},{parts[1]},{parts[2]},{parts[3]},{price}\n")


