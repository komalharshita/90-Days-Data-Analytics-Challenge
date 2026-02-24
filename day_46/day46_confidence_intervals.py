import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# sample data

spend = np.random.normal(loc=4500, scale = 400, size = 50)

n = len(spend)
sample_mean = np.mean(spend)
sample_std = np.std(spend, ddof=1)

print("\n--- Sample Statistics ---")
print(f"Sample size: {n}")
print(f"Sample mean: {sample_mean:.2f}")
print(f"Sample std dev: {sample_std:.2f}")

# manual 95% CI

confidence_level = 0.95
alpha = 1- confidence_level

t_critical = stats.t.ppf(1-alpha/2, df= n-1)
standard_error = sample_std/ np.sqrt(n)
moe = t_critical * standard_error

lower = sample_mean - moe
upper = sample_mean + moe

print("\n--- 95% CONFIDENCE INTERVAL ---")
print(f"T Critical Value: {t_critical:.4f}")
print(f"Standard Error: {standard_error:.4f}")
print(f"Margin of Error: {moe:.2f}")
print(f"Confidence Interval: ({lower:.2f}, {upper:.2f})")


print("\n--- BUSINESS INTERPRETATION ---")
print("We are 95% confident that the true average customer spend lies within the calculated interval.")
print("Larger samples produce narrower intervals, meaning more precise estimates.")
print("\nFile Execution Completed Successfully ✅")