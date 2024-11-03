# # Function to perform addition
# def add(a, b):
#     return a + b

# # Function to perform subtraction
# def subtract(a, b):
#     return a - b

# # Function to perform multiplication
# def multiply(a, b):
#     return a * b

# # Function to perform division
# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b

# Main calculator function
def calculator():
    # Ask the user to input their expression
    expression = input("Enter your sum value (e.g., 5 + 6): ")
    
    # Split the expression into parts: number1, operator, number2
    parts = expression.split()
    
    if len(parts) != 3:
        print("Error: Please enter a valid expression (e.g., 5 + 6)")
        return
    
    num1= int(parts[0])  # First number
    operator = parts[1]     # Operator (+, -, *, /)
    num2 = int(parts[2])  # Second number

    num1, operator, num2 = parts #better than the above code, divides all the parts of spilited stings into the 3 variables
    num1 = int(num1)
    num2 = int(num2)
    
    # Check the operator and call the corresponding function
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero!")
        result = num1 / num2
    else:
        result = "Error: Invalid operator!"
    
    # Display the result
    print(f"The result of {expression} is: {result}")

# Run the calculator
calculator()
