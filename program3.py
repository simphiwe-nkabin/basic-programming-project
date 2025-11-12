# program3.py
# A program that adds two numbers input by the user

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

# Convert input to numbers (int or float)
try:
    first_number = float(first_number)
    second_number = float(second_number)
    total = first_number + second_number
    print(f"The sum is {total}")
except ValueError:
    print("Please enter valid numbers.")
