"""Day 22 Homework - Python Basics

Solve the problems below inside this file. Do NOT include any print statements other than what's asked.
Keep functions small and use docstrings.
"""

# Section 1: Variables & Types
# 1. Create variables: student_name (str), student_age (int), gpa (float).
#    Then create a new variable `gpa_percent` which converts gpa (out of 10) to percentage (out of 100).
#    e.g., gpa 8.0 -> gpa_percent 80.0

student_name = "komal"
student_age = 19
gpa = 9.09

gpa_percent = gpa*10
print(gpa_percent)

# Section 2: Control Flow
# 2. Write a function grade(marks) that returns:
#    'A' if marks >= 90, 'B' if marks >= 75, 'C' if marks >= 50, else 'F'.
#    Use docstring for the function.

def grade(marks):
    """
    Docstring for calculating grade
    """
    if marks >= 90:
        return 'A'
    elif marks >=75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'F'

# Section 3: Loops
# 3. Given a list numbers = [12, 5, 8, 130, 44], write code to create a new list greater_than_10 containing only numbers > 10.
#    Implement this once using a for loop and once using list comprehension (two separate functions).

numbers = [12,5,8,130,44]
greater_than_10 = [n for n in numbers if n> 10]
print(greater_than_10)

# Section 4: Functions
# 4. Write a function calculate_average(numbers) that returns the average. Handle empty list by returning 0.

def calculate_average(numbers):
    """
    Returns the average of a list of numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)



# Section 5: Lists & Dictionaries
# 5. Given a list of dictionaries customers = [{'name':'A','age':20}, {'name':'B','age':25}], write a function extract_names(customers)
#    that returns ['A', 'B']

customers = [{'name':'A','age':20}, {'name':'B','age':25}]

def extract_names(customers):
    """
    Extracts names from a list of customer dictionaries.
    """
    names = []
    for customer in customers:
        names.append(customer["name"])
    return names


# Section 6: File I/O (CSV)
# 6. Read a CSV file named 'sample_sales.csv' placed in the same folder. The CSV has header: product,amount
#    Write a function read_sales_and_total(path) that returns the total amount (sum of amounts) as int.
#    (Hint: use open() and split(), convert amounts from string to int)


def read(path):
    total = 0
    with open(path, "r") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(",")
            score = int(parts[3])  
            total += score
    return total

file_path = "day_22\day_22_simple_data.csv"
read(file_path)