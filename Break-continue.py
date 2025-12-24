# Break Example
# Commit: "Demonstrate usage of break in a loop"

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num == 4:
        print("Breaking the loop at", num)
        break  # Stop the loop when num is 4
    print("Current number:", num)

# Continue Example
# Commit: "Demonstrate usage of continue in a loop"

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print("Skipping even number:", num)
        continue  # Skip this iteration if number is even
    print("Odd number:", num)