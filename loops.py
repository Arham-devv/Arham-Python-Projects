# loops.py
# This file explains loops in Python

# for loop example
print("For Loop Example:")
for i in range(1, 6):
    print("Number:", i)

# while loop example
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Loop with condition
print("\nEven Numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# Loops are used to repeat tasks efficiently