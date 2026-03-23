import pandas as pd

data = {
    "Ads_Spend": [10, 20, 30, 40, 50, 60, 70, 80],
    "Discount": [5, 10, 15, 20, 25, 30, 35, 40],
    "Website_Visits": [100, 200, 300, 400, 500, 600, 700, 800],
    "Sales": [15, 25, 40, 50, 65, 75, 90, 100]
}

df = pd.DataFrame(data)

print(df)

# correlation matrix

print("\nCorrelation Matrix:\n")
print(df.corr())

# heatmap visualization

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

X = df[["Ads_Spend", "Discount", "Website_Visits"]]
y = df["Sales"]

# train linear regression

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)

print("\nCoefficients:", model.coef_)

# check multicollinearity

from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns

vif_data["VIF"] = [
    variance_inflation_factor(X.values, i)
    for i in range(len(X.columns))
]

print("\nVIF:\n", vif_data)

# feature selection

X_selected = df[["Ads_Spend", "Discount"]]  # removed Website_Visits

model2 = LinearRegression()
model2.fit(X_selected, y)

print("\nNew Coefficients:", model2.coef_)

print("\nOld Model Coefficients:", model.coef_)
print("New Model Coefficients:", model2.coef_)

# lasso for feature selection

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

print("\nLasso Coefficients:", lasso.coef_)



"""
Insights:

1. All features (Ads_Spend, Discount, Website_Visits) are perfectly correlated (correlation ≈ 1),
   indicating severe multicollinearity in the dataset.

2. VIF values are infinite (inf), confirming extreme multicollinearity and redundancy among features.

3. Due to multicollinearity, the original model coefficients are very small and unstable,
   making interpretation unreliable.

4. After removing Website_Visits, the new model coefficients became more meaningful and interpretable.

5. Ads_Spend (~0.99) has a stronger impact on Sales compared to Discount (~0.49).

6. The simplified model is more stable and easier to interpret, while maintaining similar predictive power.

7. Lasso regression automatically reduced the Discount coefficient to zero, effectively performing feature selection.

8. Lasso retained Ads_Spend as the most important feature, confirming its strong influence on Sales.

9. The convergence warning in Lasso suggests that scaling or tuning alpha may improve model performance.

10. Feature selection is crucial to remove redundancy, improve model stability, and enhance interpretability.
"""