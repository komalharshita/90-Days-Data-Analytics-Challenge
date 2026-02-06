import pandas as pd

df = pd.read_csv("day_29/day_29_students_dirty.csv")

# 1. Count missing values per column

df.isna().sum()


# 2. Calculate missing value percentages

(df.isna().mean()*100).round(2)


# 3. Impute missing values using appropriate strategies

df["age"] = df["age"].fillna(df["age"].median())
df["math_score"] = df["math_score"].fillna(df["math_score"].mean())
df["attendance"] = df["attendance"].fillna(df["attendance"].median())
df["city"] = df["city"].fillna(df["city"].mode()[0])


# 4. Verify dataset has no missing values

df.isna().sum()


# 5. Save cleaned dataset

df.to_csv("day_29/cleaned_students.csv", index = False)