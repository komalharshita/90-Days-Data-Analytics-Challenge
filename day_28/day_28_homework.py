# Day 28 Homework — Advanced Python Foundations

from collections import Counter, defaultdict
from datetime import datetime

rows = []
with open("day_28/day_28_stationary.csv", "r") as f:
    next(f)
    for line in f:
        rows.append(line.strip().split(","))



# 1. Dict comprehension mapping item_name to price

sorted_by_stock = sorted(rows, key=lambda r: int(r[4]), reverse=True)
sorted_by_stock


# 2. Sort items by stock descending

sort_by_price = sorted(rows, key = lambda r: int(r[3]), reverse = True)
sort_by_price[:3]


# 3. Use Counter to find most common category

from collections import Counter

most_common = Counter([r[2] for r in rows]).most_common(1)
most_common


# 4. Group items by category using defaultdict

from collections import defaultdict

grouped = defaultdict(list)

for r in rows:
    grouped[r[2]].append(r[1])

grouped



# 5. Generator yielding items with stock < 200

def low_stock(rows):
    for r in rows:
        if int(r[4]) < 200:
            yield r[1]

list(low_stock(rows))



# 6. Parse last_restock dates and find items restocked > 10 days ago

from datetime import datetime

today = datetime.today()

for r in rows:
    restock = datetime.strptime(r[5], "%Y-%m-%d")
    if (today - restock).days > 10:
        print(r[1])
