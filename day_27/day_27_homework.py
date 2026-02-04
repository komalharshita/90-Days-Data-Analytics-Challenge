import re

# STEP 1 — Read CSV and create rows list
rows = []

with open("day_27/messy_data.csv", "r") as f:
    next(f)
    for line in f:
        rows.append(line.strip().strip('"'))


# STEP 2 — Function to clean each row
def clean_row(row):
    parts = row.split(",")

    name = parts[0].strip()
    city = re.sub(r'[^A-Za-z]', '', parts[1])
    price = int(re.sub(r'\D', '', parts[2]))
    order_id = re.findall(r'ORD\d+', parts[3])

    return name, city, price, order_id


# STEP 3 — Use map()
cleaned_rows = list(map(clean_row, rows))
print(cleaned_rows)


# STEP 4 — Use filter()
costly_orders = list(filter(lambda r: clean_row(r)[2] > 1500, rows))
print(costly_orders)


# STEP 5 — Write cleaned CSV
with open("cleaned_orders.csv", "w") as out:
    out.write("name,city,price,order_id\n")

    for r in rows:
        name, city, price, order_id = clean_row(r)
        out.write(f"{name},{city},{price},{order_id}\n")


# STEP 6 — Enumerate
for i, r in enumerate(rows, start=1):
    print(i, clean_row(r))
