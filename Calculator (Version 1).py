# # while True:
# #     number_1 = int(input("please enter the first number: "))
# #     number_2 = int(input("please enter the second number: "))
# #     symbol = input("please enter a operator: ")
    
# #     if symbol == "+":
# #         print(f"your result is {number_1 + number_2}")
# #     elif symbol == "-":
# #         print(f"your result is {number_1 - number_2}")
# #     elif symbol == "/":
# #         print(f"your result is {number_1 / number_2}")
# #     elif symbol == "*":
# #         print(f"your result is {number_1 * number_2}")

# #     play_again = input("do you want to calculate again?: ").upper()

# #     if play_again == "NO":
# #         print("okay bye👋👋")
# #         break
# #     elif play_again == "YES":
# #         pass


# running = True

# while running:
#     number_1 = int(input("please enter the first number: "))
#     number_2 = int(input("please enter the second number: "))
#     symbol = input("please enter a operator: ")
    
#     if symbol == "+":
#         print(f"your result is {number_1 + number_2}")
#     elif symbol == "-":
#         print(f"your result is {number_1 - number_2}")
#     elif symbol == "/":
#         print(f"your result is {number_1 / number_2}")
#     elif symbol == "*":
#         print(f"your result is {number_1 * number_2}")

#     if input("do you want to calculate again?: ").lower() != "yes":
#         print("okay bye👋👋")
#         running = False



















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


# Ask the user to input their expression
expression = input("Enter your sum value (e.g., 5 + 6): ")
    
# Split the expression into parts: number1, operator, number2
parts = expression.split()
    
# if len(parts) != 3:
#     print("Error: Please enter a valid expression (e.g., 5 + 6)")
    
    
num1 = int(parts[0])  # First number
operator = parts[1]     # Operator (+, -, *, /)
num2 = int(parts[2])  # Second number


print (num1, num2)
# # Check the operator and call the corresponding function
# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     if num2 == 0:
#         print("can't divide by zero")
#     try:    
#         result = num1 / num2
#     except:
#         print("can't divide by zero")
# else:
#     result = "Error: Invalid operator!"
    
# # Display the result
# print(f"The result of {expression} is: {result}")
