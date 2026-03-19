import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sleep_Hours": [8, 7, 7, 6, 6, 5, 5, 4],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 85]
}

df = pd.DataFrame(data)

print(df)

X = df[["Study_Hours", "Sleep_Hours"]]
y = df["Marks"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Without Scaling:")
print("MAE:", mae)
print("RMSE:", rmse)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)

y_pred_scaled = model_scaled.predict(X_test_scaled)

mae_scaled = mean_absolute_error(y_test, y_pred_scaled)
rmse_scaled = np.sqrt(mean_squared_error(y_test, y_pred_scaled))

print("\nWith Scaling:")
print("MAE:", mae_scaled)
print("RMSE:", rmse_scaled)

print("\nComparison:")
print("MAE Improvement:", mae - mae_scaled)
print("RMSE Improvement:", rmse - rmse_scaled)

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred, label="Without Scaling")
plt.scatter(y_test, y_pred_scaled, label="With Scaling")

plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Model Comparison")

plt.legend()
plt.show()

"""
Insights: 

# Insights:

- The model achieved almost zero error (MAE ≈ 0, RMSE ≈ 0), indicating a perfect fit.
- This happens because the dataset follows a clear linear pattern, so linear regression fits it exactly.
- Feature scaling did not improve performance because Linear Regression is not sensitive to feature scaling.
- The slight negative "improvement" is due to floating-point precision errors, not actual performance degradation.
- Both models (with and without scaling) perform equally well on this dataset.
- Study Hours has a strong positive impact on marks, while Sleep Hours has a smaller or indirect effect.
- The model predictions are almost identical to actual values, indicating excellent model accuracy.
"""