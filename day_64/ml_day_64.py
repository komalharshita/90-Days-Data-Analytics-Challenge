import pandas as pd

# Creating dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 85]
}

df = pd.DataFrame(data)

print(df)

X = df[["Study_Hours"]]   # independent variable
y = df["Marks"]           # dependent variable

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X_train:\n", X_train)
print("X_test:\n", X_test)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("Actual:", y_test.values)

print("Slope (Coefficient):", model.coef_)
print("Intercept:", model.intercept_)

import matplotlib.pyplot as plt

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.legend()
plt.show()


"""
Insights: 

- there is a strong positive relationship between study hours and marks 
- for every 1 hour increase in study time, marks increase by approximately 7
- if a student studies 0 hours, the predicted marks would be around 27.6
- the predicted values are very close to actual values, indicating a good model
- the mode has small precision errors, showing high accuracy
- increasing study hours has a significant impact on performance
"""