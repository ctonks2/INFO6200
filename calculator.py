"""Simple Command-Line Calculator
that performs basic arithmetic operations: +, -, *, /
Error handling for non-numeric input and division by zero is included.
Steps: 1. Prompt user for first number
       2. Prompt user for operation
       3. Prompt user for second number
       4. Perform calculation and display result"""

## create prompt to user to enter a number, include error handling for non-numeric input and division by zero
from logging import root

## core calculator function asking for first number, operation, second number.
## num 1 = first user number, operation = arithmetic operation, num2 = second user number
## float used to allow for decimals
def calculator():
    
    try:
        num1 = float(input("First number: "))
    except ValueError:
        print("That is not a number, please enter a number.")
        return

    operation = input("Enter an arithmetic operation (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        print("That is not a valid operation. Please use +, -, *, or /.")
        return

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    #basic if-else for calculation
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2

        print(f"{num1} {operation} {num2} is: {result}")
    
    #catch division by zero error    
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return

#Main loop: keep running calculations until the user says they are done.
def main():
    while True:
        calculator()
        again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the main function which loops the calculator
if __name__ == "__main__":
    main()
    