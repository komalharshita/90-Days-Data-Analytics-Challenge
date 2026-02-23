"""
Day 45 — Sampling Theory & Central Limit Theorem
------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt


print("\n--- Creating Population (Skewed Distribution) ---")

# Exponential distribution (skewed)
population = np.random.exponential(scale=50, size=100000)

print("Population Mean:", round(np.mean(population), 2))
print("Population Std Dev:", round(np.std(population), 2))

#taking a sample

print("\n--- Single Sample ---")

sample_size = 30
sample = np.random.choice(population, size=sample_size)

print("Sample Mean:", round(np.mean(sample), 2))
print("Sample Std Dev:", round(np.std(sample), 2))

# sampling distribution

print("\n--- Sampling Distribution ---")

sample_means = []

num_samples = 1000

for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

print("Mean of Sample Means:", round(np.mean(sample_means), 2))
print("Std Dev of Sample Means:", round(np.std(sample_means), 2))


print("\n--- Comparison ---")

print("Population Std Dev:", round(np.std(population), 2))
print("Standard Error (theoretical):",
      round(np.std(population) / np.sqrt(sample_size), 2))

print("Standard Error (empirical):",
      round(np.std(sample_means), 2))

# CLT

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.hist(population, bins=50)
plt.title("Population Distribution (Skewed)")

plt.subplot(1,2,2)
plt.hist(sample_means, bins=30)
plt.title("Sampling Distribution (Nearly Normal)")

plt.tight_layout()
plt.show()



print("\n--- Effect of Sample Size ---")

sample_sizes = [5, 30, 100]

for size in sample_sizes:
    sample_means_temp = []
    
    for _ in range(1000):
        sample = np.random.choice(population, size=size)
        sample_means_temp.append(np.mean(sample))
    
    se = np.std(sample_means_temp)
    print(f"Sample Size: {size} -> Standard Error: {round(se, 2)}")



print("\n===== FINAL INSIGHTS =====")

print("""
1. Even if population is skewed, sample means become normal (CLT).
2. Sampling distribution mean ≈ population mean.
3. Standard Error decreases as sample size increases.
4. Larger samples give more stable estimates.
5. Sampling distribution is the foundation of inference.
""")