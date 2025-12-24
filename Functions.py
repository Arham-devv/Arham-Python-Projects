# Functions 
# Commit: "Add simple function to greet user"

def greet():
    """Function to print a greeting message"""
    print("Hello! Welcome to Python functions.")

greet()  # Call the function

#Function with Arguments 
# Commit: "Add function with arguments to greet user by name"

def greet_user(name):
    """Function to greet user by their name"""
    print(f"Hello, {name}! Welcome to Python functions.")

greet_user("Arham")  # Pass name as argument

# Function with Return Value 
# Commit: "Add function that calculates sum and returns result"

def add_numbers(a, b):
    """Return the sum of two numbers"""
    return a + b

result = add_numbers(5, 7)
print("Sum is:", result)