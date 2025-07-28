def calculator():
    print("🧮 Welcome to the Basic Calculator 🧮\n")

    try:
        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Get user input for operation
        operation = input("Enter the operation (+, -, *, /): ").strip()

        # Perform the operation
        if operation == '+':
            result = num1 + num2
            print(f"\n✅ Result: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"\n✅ Result: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"\n✅ Result: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"\n✅ Result: {num1} / {num2} = {result}")
            else:
                print("\n⚠️ Error: Division by zero is not allowed.")
        else:
            print("\n⚠️ Invalid operation. Please use +, -, *, or /.")
    
    except ValueError:
        print("\n⚠️ Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    calculator()
