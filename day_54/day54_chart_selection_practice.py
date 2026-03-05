import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

n = 120

department = np.random.choice(
    ["Engineering", "Marketing", "Finance", "HR"],
    n
)

experience = np.random.randint(1, 12, n)

salary = experience * 6000 + np.random.normal(20000, 5000, n)

performance_score = np.random.normal(75, 10, n)

data = pd.DataFrame({
    "Department": department,
    "Experience": experience,
    "Salary": salary,
    "Performance Score": performance_score
})

print(data.head())



avg_salary = data.groupby("Department")["Salary"].mean()

fig, ax = plt.subplots(figsize = (8,5))

ax.bar(avg_salary.index, avg_salary.values)
ax.set_title("Average Salary per Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")

plt.show()


# engineering shows the highest average salary due to higher technical skill requirments


sorted_data = data.sort_values("Experience")
fig, ax = plt.subplots(figsize = (8,5))

ax.plot(sorted_data["Experience"], sorted_data["Salary"], marker = 'o')

ax.set_title("Salary growth with experience")
ax.set_xlabel("years of experience")
ax.set_ylabel("salary")

plt.show()


# salary generally increases with experience 



plt.figure(figsize=(8,5))

sns.boxplot(x= "Department", y= "Salary", data = data)

plt.title("Salary distribution by department")
plt.xlabel("department")
plt.ylabel("salary")

plt.show()

# some departments show wider salary changes



plt.figure(figsize=(8,5))

sns.violinplot(x= "Department", y =  "Performance Score", data = data)

plt.title("Performance Score distribution by department")
plt.xlabel("department")
plt.ylabel("performance_score")

plt.show()

# this plot shows how perfermance scores are distributed, highlighting where most employess
#  fall within a range