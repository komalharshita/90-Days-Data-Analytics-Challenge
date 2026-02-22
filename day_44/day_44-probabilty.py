"""
Day 44 — Probability Foundations Practice
------------------------------------------
"""

# ============================================
# 1️⃣ Imports
# ============================================

import numpy as np


# ============================================
# 2️⃣ Basic Probability Example
# ============================================

print("\n--- Basic Probability ---")

# Rolling a fair die
total_outcomes = 6
favorable_outcomes = 1

probability = favorable_outcomes / total_outcomes

print(f"Probability of rolling a 3: {probability}")


# ============================================
# 3️⃣ Discrete Random Variable Simulation
# ============================================

print("\n--- Discrete Random Variable: Coin Flip ---")

# Simulate 1000 coin flips (0 = Tail, 1 = Head)
coin_flips = np.random.choice([0, 1], size=1000)

# Empirical probability of heads
empirical_prob_heads = coin_flips.mean()

print(f"Empirical Probability of Heads: {round(empirical_prob_heads, 3)}")


# ============================================
# 4️⃣ Continuous Random Variable Simulation
# ============================================

print("\n--- Continuous Random Variable: Normal Distribution ---")

# Simulate 1000 heights (mean=170, std=10)
heights = np.random.normal(loc=170, scale=10, size=1000)

print(f"Mean Height: {round(np.mean(heights), 2)}")
print(f"Standard Deviation of Height: {round(np.std(heights), 2)}")

# Probability that height > 180 (empirical)
prob_height_above_180 = np.mean(heights > 180)
print(f"Probability Height > 180 cm: {round(prob_height_above_180, 3)}")


# ============================================
# 5️⃣ Expected Value (Discrete)
# ============================================

print("\n--- Expected Value (Discrete Example) ---")

# Fair die expected value
values = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.array([1/6] * 6)

expected_value = np.sum(values * probabilities)

print(f"Expected Value of Fair Die: {expected_value}")


# ============================================
# 6️⃣ Variance of Random Variable
# ============================================

print("\n--- Variance of Die ---")

mean_die = expected_value
variance = np.sum((values - mean_die) ** 2 * probabilities)

print(f"Variance of Die: {round(variance, 2)}")
print(f"Standard Deviation of Die: {round(np.sqrt(variance), 2)}")


# ============================================
# 7️⃣ Law of Large Numbers Demonstration
# ============================================

print("\n--- Law of Large Numbers ---")

sample_sizes = [10, 100, 1000, 10000]

for size in sample_sizes:
    flips = np.random.choice([0, 1], size=size)
    mean_flips = flips.mean()
    print(f"Sample Size: {size} -> Mean: {round(mean_flips, 3)}")

print("\nNotice how mean approaches 0.5 as sample size increases.")


# ============================================
# 8️⃣ Final Summary
# ============================================

print("\n===== FINAL SUMMARY =====")

print("""
1. Probability ranges from 0 to 1.
2. Discrete variables take countable values.
3. Continuous variables take infinite values.
4. Expected value is long-run average.
5. Larger samples produce more stable estimates.
""")