# Lists Basics Example
# Commit: "Add basic list creation and access example"

fruits = ["apple", "banana", "cherry", "date"]
print("Fruits List:", fruits)

# Access elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Lists Methods Example
# Commit: "Add examples of common list methods in Python"

fruits = ["apple", "banana", "cherry"]

# 1. append() - Add an element at the end
fruits.append("date")
print("After append:", fruits)

# 2. insert() - Add element at specific position
fruits.insert(1, "blueberry")
print("After insert:", fruits)

# 3. remove() - Remove a specific element
fruits.remove("banana")
print("After remove:", fruits)

# 4. pop() - Remove element by index (default last)
fruits.pop()
print("After pop:", fruits)

# 5. sort() - Sort the list
fruits.sort()
print("After sort:", fruits)

# 6. reverse() - Reverse the list
fruits.reverse()
print("After reverse:", fruits)

# 7. count() - Count occurrences of an element
print("Count of 'apple':", fruits.count("apple"))
