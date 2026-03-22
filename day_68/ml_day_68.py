import numpy as np
import pandas as pd

np.random.seed(42)

# Generate data
X = np.random.rand(50, 1) * 10
y = 3 * X.squeeze() + 5 + np.random.randn(50) * 2  # noise added

df = pd.DataFrame({"Feature": X.squeeze(), "Target": y})

print(df.head())

# train test split 

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# linear regression 

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

from sklearn.metrics import mean_squared_error
import numpy as np

rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))

print("Linear Regression RMSE:", rmse_lr)

# cross validation

from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(lr, X, y, cv=5, scoring='neg_mean_squared_error')

rmse_cv = np.sqrt(-cv_scores)

print("Cross Validation RMSE:", rmse_cv)
print("Average CV RMSE:", rmse_cv.mean())

# ridge regression 

from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

y_pred_ridge = ridge.predict(X_test)

rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))

print("\nRidge RMSE:", rmse_ridge)

# lasso regression 

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

y_pred_lasso = lasso.predict(X_test)

rmse_lasso = np.sqrt(mean_squared_error(y_test, y_pred_lasso))

print("Lasso RMSE:", rmse_lasso)

# compare coeffeiccents 

print("\nCoefficients Comparison:")
print("Linear:", lr.coef_)
print("Ridge:", ridge.coef_)
print("Lasso:", lasso.coef_)


import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, label="Actual")
plt.scatter(X_test, y_pred_lr, label="Linear")
plt.scatter(X_test, y_pred_ridge, label="Ridge")
plt.scatter(X_test, y_pred_lasso, label="Lasso")

plt.legend()
plt.title("Model Comparison")
plt.show()


# Insights:

# 1. Linear Regression RMSE is approximately 1.78, indicating good model performance with low prediction error.

# 2. Cross-validation RMSE values range between ~1.43 and ~2.56, showing some variation across different data splits.

# 3. The average cross-validation RMSE (~1.85) is slightly higher than test RMSE, indicating mild overfitting but overall good generalization.

# 4. Ridge Regression RMSE (~1.79) is very close to Linear Regression, showing that regularization did not significantly improve performance.

# 5. Lasso Regression RMSE (~1.79) is also similar, indicating that the dataset is simple and does not require strong regularization.

# 6. Coefficients decreased slightly from Linear → Ridge → Lasso (2.94 → 2.93 → 2.93), confirming that regularization shrinks coefficients.

# 7. Since there is only one feature, Lasso could not eliminate any feature, but still reduced coefficient magnitude slightly.

# 8. The model captures the underlying relationship well (approximately y ≈ 3x + 5), even with noise present.

# 9. Cross-validation provides a more reliable estimate of model performance compared to a single train-test split.

# 10. Regularization is more beneficial in complex datasets, while in this simple dataset, all models perform similarly.