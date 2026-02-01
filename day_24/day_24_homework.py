"""
Day 24 Homework — Pandas Basics
"""

import pandas as pd

df = pd.read_csv("day_24_data.csv")

# 1. Print first 3 rows

print(df.head(3))


# 2. Show only students from Mumbai

print(df[df["city"]== 'Mumbai'])


# 3. Show names and math_score where math_score > 80

print(df[df["math_score"] > 80][["name", "math_score"]])


# 4. Calculate average attendance

print(df["attendance"].mean())


# 5. Find student with highest science_score

print(df[df["science_score"] == df["science_score"].max() ])
