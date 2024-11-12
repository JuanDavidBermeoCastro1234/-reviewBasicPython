# Ask for two numbers and the operation to perform
number = float(input("Enter the first numeric value: "))
number2 = float(input("Enter the second numeric value: "))

# Ask for the operation to perform
operation = input("Select a mathematical operation (+, -, *, /): ")

# Use 'match' to select the operation
match operation:
    case "+":
        result = number + number2
        print(f"The result of the addition is: {result}")
    case "-":
        result = number - number2
        print(f"The result of the subtraction is: {result}")
    case "*":
        result = number * number2
        print(f"The result of the multiplication is: {result}")
    case "/":
        if number2 != 0:  # Check if division by zero
            result = number / number2
            print(f"The result of the division is: {result}")
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Invalid operation. Please enter a valid operation (+, -, *, /).")