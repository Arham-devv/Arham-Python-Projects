# Sets and Set Methods 
# Commit: "Add set examples and common set methods with explanations"

# Creating a set
numbers = {1, 2, 3, 4, 5}
print("Original Set:", numbers)

# 1. add() - Add an element to the set
numbers.add(6)
print("After add:", numbers)

# 2. update() - Add multiple elements
numbers.update([7, 8])
print("After update:", numbers)

# 3. remove() - Remove an element (error if not found)
numbers.remove(3)
print("After remove:", numbers)

# 4. discard() - Remove element safely (no error if not found)
numbers.discard(10)
print("After discard (no error):", numbers)

# 5. pop() - Remove a random element
removed_element = numbers.pop()
print("Removed element using pop:", removed_element)
print("After pop:", numbers)

# 6. union() - Combine two sets
even_numbers = {2, 4, 6, 8}
union_set = numbers.union(even_numbers)
print("Union of sets:", union_set)

# 7. intersection() - Common elements between sets
intersection_set = numbers.intersection(even_numbers)
print("Intersection of sets:", intersection_set)
