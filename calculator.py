"""
Command-line calculator with user-friendly prompts and robust error handling.

This module asks the user for two numbers and an arithmetic operator,
performs the calculation, and displays the result in a clear format.

Functions:
- print_header(): Prints a decorative header for the program.
- prompt_number(prompt): Repeatedly prompts until a valid float is entered.
- prompt_operator(prompt): Repeatedly prompts until a supported operator is entered.
- format_num(n): Nicely formats floats for display.
- calculate(a, op, b): Performs the arithmetic operation with error checks.
- main(): Main program loop that ties everything together.
"""

import sys

def print_header():
    """Display a pleasant, framed header when the program starts.

    No parameters.
    Prints a multi-line decorative heading to STDOUT.
    """
    print("\n" + "="*48)
    print("        Simple & Pleasant Command Line Calculator")
    print("="*48 + "\n")

def prompt_number(prompt):
    """Prompt the user for a numeric value.

    - prompt: string shown to the user.
    Returns:
    - float value parsed from user input.

    Keeps asking until the user provides a valid floating-point number.
    Displays an error message on invalid input.
    """
    while True:
        s = input(prompt).strip()            # raw string from user
        try:
            return float(s)                  # convert to float and return
        except ValueError:
            # Inform the user and loop again for valid numeric input
            print("\n[Error] That is not a valid number. Please enter digits like 12, -3.5, or 2.0\n")

def prompt_operator(prompt):
    """Prompt the user for an arithmetic operator.

    - prompt: string shown to the user.
    Returns:
    - operator string chosen by the user (one of the supported set).

    Keeps asking until the operator is one of the supported symbols.
    """
    valid = {"+", "-", "*", "/", "%", "^"}   # supported operators
    while True:
        op = input(prompt).strip()           # raw operator input
        if op in valid:
            return op
        # Notify the user about valid choices and re-prompt
        print(f"\n[Error] Invalid operator. Choose one of: {' '.join(sorted(valid))}\n")

def format_num(n):
    """Format numeric values for display.

    - n: numeric value (float or int)
    Returns:
    - string representation using up to 10 significant digits, trimmed of trailing zeros.
    """
    s = f"{n:.10g}"
    return s

def calculate(a, op, b):
    """Perform the requested arithmetic operation with safety checks.

    Parameters:
    - a: first operand (float)
    - op: operator string (one of '+', '-', '*', '/', '%', '^')
    - b: second operand (float)

    Returns:
    - numeric result of applying op to a and b.

    Raises:
    - ZeroDivisionError for division or modulo by zero.
    - ValueError for unsupported operations.
    - OverflowError will propagate if exponentiation or operations overflow.
    """
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                raise ZeroDivisionError("division by zero")
            return a / b
        if op == "%":
            if b == 0:
                raise ZeroDivisionError("modulo by zero")
            return a % b
        if op == "^":
            return a ** b
        # If we reach here, the operation was not supported
        raise ValueError("unsupported operation")
    except OverflowError:
        # Allow caller to handle overflow specifically
        raise

def main():
    """Main interactive loop.

    Repeatedly:
    - prompt for first number (a)
    - prompt for operator (op)
    - prompt for second number (b)
    - compute and display result
    Handles user-triggered KeyboardInterrupt at top-level.
    """
    print_header()
    while True:
        # Get the first operand from the user
        a = prompt_number("Enter the first number: ")

        # Get the operator from the user
        op = prompt_operator("Enter an operation (+ - * / % ^): ")

        # Get the second operand from the user
        b = prompt_number("Enter the second number: ")

        try:
            # Attempt computation and handle possible arithmetic errors
            result = calculate(a, op, b)
        except ZeroDivisionError as e:
            # Clear, user-friendly math error message; loop back to start
            print(f"\n[Math Error] {e}. Try again.\n")
            continue
        except OverflowError:
            # Inform user about numeric overflow and prompt again
            print("\n[Error] Calculation overflowed. Try smaller numbers.\n")
            continue
        except Exception as e:
            # Generic catch-all for unexpected errors; show message and retry
            print(f"\n[Error] {e}\n")
            continue

        # Nicely formatted output block showing the expression and result
        print("\n" + "-"*48)
        print(f"  {format_num(a)}  {op}  {format_num(b)}  =  {format_num(result)}")
        print("-"*48 + "\n")

        # Ask whether the user wants another calculation
        again = input("Perform another calculation? (y/N): ").strip().lower()
        if again != "y":
            # Exit message and break loop to end program
            print("\nGoodbye.\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully with a friendly message
        print("\n\nInterrupted. Goodbye.\n")
        sys.exit(0)