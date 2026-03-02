# ==========================================================
# Topic: jointplot() & pairplot()
# ==========================================================

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


np.random.seed(42)

n = 100

marketing_spend = np.random.normal(10000, 2000, n)
website_traffic = marketing_spend * 4 + np.random.normal(0, 5000, n)
conversion_rate = np.random.normal(5, 1, n)
sales = marketing_spend * 2 + website_traffic * 0.05 + np.random.normal(0, 5000, n)

region = np.random.choice(["North", "South", "East", "West"], n)

data = pd.DataFrame({
    "Marketing Spend": marketing_spend,
    "Website Traffic": website_traffic,
    "Conversion Rate": conversion_rate,
    "Sales": sales,
    "Region": region
})

print(data.head())


sns.set_theme(style="whitegrid")

# jointplot

sns.jointplot(
    x="Marketing Spend",
    y="Sales",
    data=data,
    kind="reg"
)

plt.show()

# strong correlation
# Regression line slopes upward,
# indicating higher marketing spend leads to higher sales.
# Relationship appears moderately strong.



# jointplot


sns.jointplot(
    x="Website Traffic",
    y="Sales",
    data= data,
    kind="scatter"
)

plt.show()


# Positive trend visible but slightly more scattered.
# Traffic contributes to sales but may not be sole driver.



# pairplot

numerical_data = data.drop(columns=["Region"])

sns.pairplot(numerical_data)

plt.show()


# Marketing Spend and Website Traffic show strong correlation.
# Sales is positively correlated with both.
# Conversion Rate appears weakly related to other variables.




# pairplot with hue

sns.pairplot(
    data=data[["Marketing Spend", "Sales", "Website Traffic", "Region"]],
    hue="Region"
)

plt.show()


# Regions show overlapping clusters.
# No strong separation by region,
# suggesting performance is not region-dependent in this dataset.



"""

1. Jointplot is useful because it shows both scatter and
   distribution with optional regression line in one view.

2. Pairplot is not ideal when dataset has too many columns,
   as it becomes cluttered and unreadable.

3. Upward regression line indicates positive correlation.

4. Outliers can pull regression line and distort correlation,
    leading to misleading conclusions.

5. Business decision:
   Increasing marketing budget may drive higher sales,
   but cost-benefit analysis is required.

"""