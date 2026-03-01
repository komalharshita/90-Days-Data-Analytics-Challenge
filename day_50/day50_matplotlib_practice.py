# ==========================================================
# Topic: Line Charts & Bar Charts
# ==========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate Synthetic Business Dataset

np.random.seed(42)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

marketing_spend = np.random.randint(8000, 15000, size=6)
website_traffic = np.random.randint(40000, 80000, size=6)
sales = marketing_spend * 2 + np.random.randint(5000, 10000, size=6)

data = pd.DataFrame({
    "Month": months,
    "Marketing Spend": marketing_spend,
    "Website Traffic": website_traffic,
    "Sales": sales
})

print(data)

# line chart

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(data["Month"], data["Sales"],
        marker='o',
        linestyle='-',
        linewidth=2)

ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (₹)")
ax.grid(True)

plt.show()

"""
Insights: 

1. sales show a generally increasing trend

2. february is the month with the highest sales

"""

# bar chart==========================================================

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(data["Month"], data["Marketing Spend"])

ax.set_title("Marketing Spend by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Marketing Spend (₹)")

plt.xticks(rotation=45)

plt.show()

"""
Insights: 

1. the highest marketing spend was in the month february followed by march and april

2. the lowest as in the month january

"""

# multi line chart

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(data["Month"], data["Marketing Spend"],
        marker='o',
        label="Marketing Spend")

ax.plot(data["Month"], data["Sales"],
        marker='s',
        label="Sales")

ax.set_title("Marketing Spend vs Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Amount (₹)")
ax.legend()
ax.grid(True)

plt.show()


"""
Insights: 

1. sales generally increase when marketing spend increases

2. there is a strong relation between them

"""

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(data["Month"], data["Sales"],
        marker='o',
        linewidth=2)

ax.set_title("Monthly Sales Trend (Export Version)")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (₹)")
ax.grid(True)

plt.savefig("day_50/day50_sales_chart.png",
            dpi=300,
            bbox_inches='tight')

plt.close()
