# filename: calculator.py

def calculator():
    operation = input("Enter the operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = num1 + num2
        print(f"The result is {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result is {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result is {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Error: Invalid operation!")

if __name__ == "__main__":
    while True:
        calculator()
        continue_calculation = input("Do you want to calculate again? (yes/no): ")
        if continue_calculation.lower() != 'yes':
            break