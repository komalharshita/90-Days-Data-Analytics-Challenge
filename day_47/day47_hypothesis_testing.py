import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

# simulated delivery times

delivery_time = np.random.normal(loc=32, scale=5, size=40)
n= len(delivery_time)

sample_mean= np.mean(delivery_time)
sample_std = np.std(delivery_time)

print("\n--- SAMPLE STATISTICS ---")
print(f"Sample Size: {n}")
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Std Dev: {sample_std:.2f}")

# hypothesized mean 

mu_0 = 30

# manual t statistic

standard_error = sample_std/ np.sqrt(n)
t_stats = (sample_mean - mu_0) / standard_error

dof = n-1

p_value_m = 2*(1-stats.t.cdf(abs(t_stats), dof))

print("\n--- MANUAL T-TEST ---")
print(f"T-statistic: {t_stats:.4f}")
print(f"P-value: {p_value_m:.4f}")

if p_value_m < 0.05:
    print("Decision: Reject Null Hypothesis")
else:
    print("Decision: Fail to Reject Null Hypothesis")

# using scipy 

t_stat, p_value = stats.ttest_1samp(delivery_time, mu_0)

print("\n--- SCIPY T-TEST ---")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

#visualizing rejection region 

x = np.linspace(-4, 4, 1000)
y = stats.t.pdf(x, dof)

plt.figure()
plt.plot(x, y)
plt.axvline(x=t_stats)
plt.title("T Distribution with Test Statistic")
plt.xlabel("t value")
plt.ylabel("Density")
plt.show()


print("\n--- BUSINESS INTERPRETATION ---")

if p_value < 0.05:
    print("There is statistically significant evidence that average delivery time differs from 30 minutes.")
else:
    print("There is not enough statistical evidence to conclude delivery time differs from 30 minutes.")

print("\nFile Execution Completed Successfully ✅")