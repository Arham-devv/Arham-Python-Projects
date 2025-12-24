# Tuples and Tuple Operations Example
# Commit: "Add tuple examples and common tuple operations in Python"

# Creating a tuple
fruits = ("apple", "banana", "cherry", "apple", "date")
print("Original Tuple:", fruits)

# 1. Accessing elements (indexing)
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# 2. Slicing a tuple
print("Sliced tuple (1 to 3):", fruits[1:4])

# 3. count() - Count occurrences of an element
print("Count of 'apple':", fruits.count("apple"))

# 4. index() - Find index of an element
print("Index of 'cherry':", fruits.index("cherry"))

# 5. Length of tuple
print("Length of tuple:", len(fruits))

# 6. Looping through a tuple
print("Looping through tuple:")
for fruit in fruits:
    print(fruit)

# 7. Tuple concatenation
more_fruits = ("mango", "orange")
combined_tuple = fruits + more_fruits
print("Combined Tuple:", combined_tuple)
