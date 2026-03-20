import pandas as pd 

import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Sleep_Hours": [8, 7, 7, 6, 6, 5, 5, 4],
    "Pass": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print(df)

# define features and target 
X = df[["Study_Hours", "Sleep_Hours"]]
y = df["Pass"]


# train test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# apply scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# train logistic regression

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train_scaled, y_train)

# predictions 

y_pred = model.predict(X_test_scaled)

print("Predictions:", y_pred)
print("Actual:", y_test.values)

# confusion matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:\n", cm)

# evaluation metrics 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nMetrics:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

y_prob = model.predict_proba(X_test_scaled)

print("\nProbabilities:\n", y_prob)

print("\nCoefficients:", model.coef_)
print("Intercept:", model.intercept_)



# Insights:
# 1. The model predicts whether a student will pass based on study and sleep hours.
# 2. Higher study hours increase the probability of passing.
# 3. Sleep hours has (positive/negative) impact on passing.
# 4. Accuracy of the model is __ indicating (good/moderate/poor) performance.
# 5. Precision shows that when model predicts pass, it is correct __% of the time.
# 6. Recall shows that model detects __% of actual passing students.
# 7. The model performs well/poorly due to __.