import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

np.random.seed(42)

# generating data 
marketing_spend = np.random.normal(10000, 2000, 100)
website_traffic = np.random.normal(50000, 10000, 100)

sales = 5 + 0.003 * marketing_spend + 0.0002 * website_traffic + np.random.normal(0, 5, 100)

data = pd.DataFrame({
    "Marketing_Spend": marketing_spend,
    "Website_Traffic": website_traffic,
    "Sales": sales
})

# linear regression model
X = data[["Marketing_Spend", "Website_Traffic"]]
X = sm.add_constant(X)   # adds intercept
y = data["Sales"]

model = sm.OLS(y, X).fit()

print("\n--- REGRESSION SUMMARY ---")
print(model.summary())

# r squared interpretation
r_squared = model.rsquared
print(f"\nR-squared: {r_squared:.4f}")

# residual analysis
residuals = model.resid
fitted = model.fittedvalues

plt.figure()
plt.scatter(fitted, residuals)
plt.axhline(y=0)
plt.title("Residual Plot")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.show()

plt.figure()
plt.hist(residuals, bins=20)
plt.title("Residual Distribution")
plt.show()

print("\nFile Execution Completed Successfully ✅")