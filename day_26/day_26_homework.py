"""
Day 26 Homework — CSV Join & Output Writing
"""

# 1. Create dictionary from customers CSV

customers = {}
with open("day_26/day_26_customers.csv", "r") as f:
    next(f)
    for line in f:
        parts = line.strip().split(",")
        customers[parts[0]] = (parts[1], parts[2])


print(customers)


# 2. Read orders CSV, clean price column, and print customer name with item

with open("day_26/day_26_orders.csv", "r") as f:
    next(f)
    for line in f:
        parts = line.strip().split(",")
        cid = parts[1]
        item = parts[2]
        price = int(parts[3].replace("Rs.", ""))

        name,city = customers.get(cid, ("UNKNOWN", "UNKNOWN"))
        print(name, item, price)

    
# 3. Write a function merge_and_save(cust_path, order_path, out_path) that writes merged CSV with columns: order_id,name,city,item,price
# 4. Handle missing customers using 'UNKNOWN'
# 5. Add try/except for file handling


def merge_and_save(cust_path, order_path, out_path):
    customers = {}

    try:
        with open("cust_path", "r") as f:
            next(f)
            for line in f:
                parts = line.strip().split(",")
                customers[parts[0]] = (parts[1], parts[2])

        with open(order_path, "r") as o, open(out_path, "w") as out:
            next(o)
            out.write("order_id,name,city,item,price\n")

            for line in o:
                parts = line.strip().split(",")
                oid = parts[0]
                cid = parts[1]
                item = parts[2]
                price = parts[3].replace("Rs.", "")

                name, city = customers.get(cid, ("UNKNOWN", "UNKNOWN"))

                out.write(f"{oid},{name},{city},{item},{price}\n")

    except FileNotFoundError:
        print("One of the files not found")



