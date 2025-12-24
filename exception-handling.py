# Exception Handling 
# "Add exception handling examples to handle runtime errors safely"

# 1. Basic try-except
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result is: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
finally:
    print("It always Excecute")


# 2. try-except-else
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Age must be a number.")
else:
    print(f"Your age is {age}")



# 3. Catching multiple exceptions together
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except (IndexError, TypeError):
    print("Error: Invalid index or type issue.")
