# conditions.py
# This file explains conditional statements in Python

# Taking input from user
age = int(input("Enter your age: "))

# if condition
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# elif example
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

# Conditions help in decision making in real-world applications