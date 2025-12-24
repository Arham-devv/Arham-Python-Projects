# Docstrings 
# Commit: "Add docstring examples to document functions and improve code readability"

def greet_user(name):
    """
    This function greets the user by their name.

    Parameters:
    name (str): The name of the user

    Returns:
    None
    """
    print(f"Hello, {name}! Welcome to Python.")

greet_user("Arham")


def add_numbers(a, b):
    """
    This function takes two numbers and returns their sum.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Sum of a and b
    """
    return a + b

result = add_numbers(5, 7)
print("Sum is:", result)


def introduce():
    """
    This function introduces the purpose of docstrings.

    Docstrings are used to:
    - Explain what a function does
    - Describe parameters and return values
    - Help other developers understand the code
    """
    print("Docstrings help document your code clearly.")

introduce()
