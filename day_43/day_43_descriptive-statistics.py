import pandas as pd
import numpy as np

# creating a sample book sales data

data = {
    "book_id": range(1,11),
    "rating":[4.6,4.2,4.7,4.4,4,3,3.3,4.9,3.5,3.1],
    "price": [18.88, 11.05, 11.99, 13.62, 11.37, 25.00, 14.50, 9.99, 16.00, 12.75],
    "reviews_count": [145747, 395512, 116101, 472618, 51520, 80000, 120000, 60000, 250000, 300000]
}

df = pd.DataFrame(data)

print("Initial Dataset: \n")
print(df.head())

# helper functions 

def describe_col(series):
    """
    Returns key descriptive statistics for a numeric columns
    """
    return {
        "mean": round(series.mean(), 2),
        "median":round(series.median(), 2),
        "mode": series.mode().values,
        "variance": round(series.var(), 2),
        "stddev": round(series.std(), 2),
        "min": series.min(),
        "max": series.max()
    }

# mean, median and mode analysis

print("\n----- Rating statistics -----")
rating_stats = describe_col(df["rating"])
print(rating_stats)

print("\nInterpretation:")
print("Mean rating represents overall average satisfaction.")
print("Median shows the central tendency without outlier influence.")

# variance and standard deviation

print("\n----- Price spread analysis -----")
price_stats = describe_col(df["price"])
print(price_stats)

print("\nInterpretation:")
print("Standard deviation tells how much prices vary from the average.")
print("Higher std_dev means more pricing volatility.")

# skewness check 

print("\n ----- Reviews distribution -----")

mean_reviews = df["reviews_count"].mean()
median_reviews = df["reviews_count"].median()

print("Mean reviews:", round(mean_reviews, 2))
print("Median reviews:", round(median_reviews, 2))

if mean_reviews > median_reviews:
    print("Distribution appears right-skewed (large outliers pulling mean up).")
elif mean_reviews < median_reviews:
    print("Distribution appears left-skewed.")
else:
    print("Distribution appears symmetric.")