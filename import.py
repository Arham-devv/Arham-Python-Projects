"""
 Python Modules & dir() Functions
"""

# Importing built-in modules
import math
import random

# Using dir() to explore module contents
print("Functions and attributes in math module:")
print(dir(math))

print("\nFunctions and attributes in random module:")
print(dir(random))

# Using some functions from math module
num = 25
print("\nSquare root of", num, "is:", math.sqrt(num))
print("Power (2^3):", math.pow(2, 3))

# Using some functions from random module
print("\nRandom number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(["Python", "C++", "Java"]))
