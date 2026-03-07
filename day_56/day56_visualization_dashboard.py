# imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style = "whitegrid")

df = pd.read_csv("day_56\order_history_kaggle_data.csv")

print(df.head())
print(df.info())


# data cleaning

df["Order Placed At"] = pd.to_datetime(df["Order Placed At"])
df["Order Date"] = df["Order Placed At"].dt.date
df = df.dropna(subset = ["Total", "City", "Distance", "Rating"])

# dashboard

fig, ax = plt.subplots(2,2, figsize = (14,10))


#charts

orders_per_day = df.groupby("Order Date").size()
ax[0,0].plot(orders_per_day.index, orders_per_day.values)
ax[0,0].set_title("Orders trend over time")
ax[0,0].set_xlabel("Date")
ax[0,0].set_ylabel("Number of orders")


orders_city = df["Subzone"].value_counts().head(5)
ax[0,1].bar(orders_city.index, orders_city.values)
ax[0,1].set_title("Top subzones by orders")
ax[0,1].set_xlabel("Subzone")
ax[0,1].set_ylabel("Number of orders")
ax[0,0].tick_params(axis='x', rotation=45)


sns.boxplot(
    y = df["Total"], 
    ax= ax[1,0]
)
ax[1,0].set_title("Order value distribution")
ax[1,0].set_ylabel("Order Total")


ax[1,1].scatter(df["Distance"], df["Total"], alpha = 0.5)
ax[1,1].set_title("Distance vs Order Value")
ax[1,1].set_xlabel("Distance")
ax[1,1].set_ylabel("Order total")

plt.tight_layout()

# export 

plt.savefig(
    "food_delivery_dashboard.png", 
    dpi = 300, 
    bbox_inches = "tight"
)

plt.show()


"""
Insights 


"""