import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(42)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = np.random.randint(30000, 70000, 6)

orders = np.random.randint(400, 900, 6)

customer_rating = np.random.uniform(3.8, 4.9, 6)

data = pd.DataFrame({
    "Month": months,
    "Sales": sales,
    "Orders": orders,
    "Customer Rating": customer_rating
})

print(data)


fig, ax = plt.subplots(figsize = (8,5))

ax.plot(data["Month"], data["Sales"], marker = 'o', linewidth = 2)

ax.set_title("Month sales trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

# Find peak value
peak_sales = data["Sales"].max()
peak_month = data.loc[data["Sales"].idxmax(), "Month"]

ax.annotate("Peak Sales", xy= (peak_month, peak_sales), 
            xytext= (peak_month, peak_sales + 5000), 
            arrowprops= dict(facecolor = 'black'))

plt.show()

# march has the highest no. of sales followed by january and june


fig, ax = plt.subplots(figsize=(8,5))

ax.bar(data["Month"],
       data["Orders"])

ax.set_title("Monthly Orders")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Orders")

plt.show()

# march shows the highest number of orders 



fig, ax = plt.subplots(2,2, figsize = (10, 8))

# Panel 1 – Sales Trend
ax[0,0].plot(data["Month"],
             data["Sales"],
             marker='o')

ax[0,0].set_title("Sales Trend")


# Panel 2 – Orders Comparison
ax[0,1].bar(data["Month"],
            data["Orders"])

ax[0,1].set_title("Orders by Month")


# Panel 3 – Customer Rating Trend
ax[1,0].plot(data["Month"],
             data["Customer Rating"],
             marker='s')

ax[1,0].set_title("Customer Rating Trend")


# Panel 4 – Orders vs Sales Relationship
ax[1,1].scatter(data["Orders"],
                data["Sales"])

ax[1,1].set_title("Orders vs Sales")

plt.tight_layout()

plt.show()
