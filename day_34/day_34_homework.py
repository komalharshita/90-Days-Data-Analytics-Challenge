import pandas as pd

df = pd.read_csv("day_34/day_34_student_assessments_dirty.csv")

# 1. Inspect data

print(df.shape)
print(df.isna().sum())



# 2. Assert age between 18 and 30

assert df["age"].notna().all()
assert df["age"].between(18, 30).all()


# 3. Assert math_score between 0 and 100

assert df["math_score"].notna().all()
assert df["math_score"].between(0, 100).all()


# 4. Assert attendance_pct between 0 and 100

assert df["attendance_pct"].notna().all()
assert df["attendance_pct"].between(0, 100).all()


# 5. Assert student_id uniqueness

assert df["student_id"].is_unique


# 6. Print success message if all checks pass

print("Data quality checks passed")
