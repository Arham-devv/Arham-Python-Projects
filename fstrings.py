# f-Strings Example
# Commit: "Add f-strings examples to format strings in a clean and readable way"

# Variables
name = "Arham"
age = 18
language = "Python"

# 1. Basic f-string usage
print(f"My name is {name} and I am {age} years old.")

# 2. Using f-string with expressions
print(f"Next year, I will be {age + 1} years old.")

# 3. Using f-string with multiple variables
print(f"I am learning {language} programming.")

# 4. f-string with numbers and calculations
a = 10
b = 5
print(f"Sum of {a} and {b} is {a + b}")

# 5. f-string inside a function
def introduce(user, skill):
    return f"My name is {user} and my main skill is {skill}."

print(introduce("Arham", "Python"))
