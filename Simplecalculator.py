# Functions for arithmetic operations
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
# Input
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
# Select operation of your choice
if choice in ['1', '2', '3', '4']:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
else:
    print("Invalid choice. Please select a valid operation.")
