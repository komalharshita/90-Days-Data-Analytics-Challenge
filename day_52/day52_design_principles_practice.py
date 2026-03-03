# ==========================================================
# Goal: Improve bad charts into professional ones
# ==========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(42)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = np.random.randint(20000, 50000, size=6)
marketing = np.random.randint(10000, 25000, size=6)

data = pd.DataFrame({
    "Month": months,
    "Sales": sales,
    "Marketing Spend": marketing
})

print(data)


# bad chart

plt.figure()

plt.plot(data["Month"], data["Sales"],
         color="yellow",
         linewidth=1)

plt.title("Sales")
plt.show()

# Problems in bad chart:
# 1. Yellow line has low contrast on white background.
# 2. Title is vague ("Sales") — no context or time range.
# 3. No axis labels or units.
# 4. Thin line makes trend unclear.
# 5. No grid for readability.
# 6. Default small figure size.
# 7. No markers to highlight data points.


plt.rcParams.update({'font.size': 12})

fig, ax = plt.subplots(figsize= (9,5))

ax.plot(data["Month"], data["Sales"], color="blue", linewidth=3, marker= 'o')

ax.set_title("Monthly Sales trend")
ax.set_xlabel("Months")
ax.set_ylabel("Sales(Rs)")

ax.grid(True, linestyle = '--', alpha= 0.6)

plt.show()


# Sales show moderate fluctuation across months.
# The clearer line and markers make trend changes easy to see.


# Colorblind 

sns.color_palette("colorblind")

fig, ax = plt.subplots(figsize = (9,5))

ax.plot(data["Month"], data["Sales"],
        linewidth=3,
        marker='o',
        label="Sales")
ax.plot(data["Month"], data["Marketing Spend"],
        linewidth=3,
        marker='s',
        label="Marketing Spend")

ax.set_title("Marketing Spend vs Sales (Colorblind-Friendly)")
ax.set_xlabel("Month")
ax.set_ylabel("Amount(Rs)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)

plt.show()

# Months with higher marketing spend generally align
# with higher sales values, indicating positive association.


fig, ax = plt.subplots(figsize= (9,5))

ax.plot(data["Month"], data["Sales"], linewidth = 3, marker = 'o')

ax.plot(data["Month"], data["Sales"], linewidth= 3, marker = 'o')

# Optional cleanup ideas:
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_title("Monthly sales overview")
ax.set_xlabel("Month")
ax.set_ylabel("Sales(Rs)")

ax.grid(True, linestyle="--", alpha=0.4)

plt.show()
