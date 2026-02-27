import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

# independent t-test

groupA = np.random.normal(30,5,40)
groupB = np.random.normal(27,5,40)
meanA = np.mean(groupA)
meanB = np.mean(groupB)

print("\n--- INDEPENDENT T-TEST ---")
print(f"Mean Group A: {meanA:.2f}")
print(f"Mean Group B: {meanB:.2f}")

t_stat, p_value = stats.ttest_ind(groupA, groupB)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Statistically significant difference between groups.")
else:
    print("No statistically significant difference.")

# cohens d effect size 

pooled_std = np.sqrt(((np.std(groupA, ddof = 1)**2 ) + (np.std(groupB, ddof=1)**2 ))/ 2)
cohens_d = (meanA - meanB) / pooled_std
print(f"Cohen's d: {cohens_d:.4f}")

# anova

regionA = np.random.normal(20000, 2000, 30)
regionB = np.random.normal(22000, 2000, 30)
regionC = np.random.normal(21000, 2000, 30)

print("\n--- ANOVA TEST ---")

f_stat, p_anova = stats.f_oneway(regionA, regionB, regionC)

print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {p_anova:.4f}")

if p_anova < 0.05:
    print("At least one region mean is different.")
else:
    print("No significant difference among regions.")

plt.figure()
plt.boxplot([groupA, groupB])
plt.title("Group comparison - A vs B")
plt.xticks([1,2], ["groupA", "groupB"])
plt.show()


# -------------------------------
# PRACTICAL INTERPRETATION
# -------------------------------

print("\n--- PRACTICAL INTERPRETATION ---")
print("Even if p-value < 0.05, always check effect size.")
print("Small statistical difference may not be business meaningful.")
print("\nFile Execution Completed Successfully ✅")
