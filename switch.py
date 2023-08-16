def case_add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 + num2

def case_subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 - num2

def case_multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1 * num2

def case_divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."

def case_default():
    return "Invalid option."

switch_dict = {
    "add": case_add,
    "subtract": case_subtract,
    "multiply": case_multiply,
    "divide": case_divide
}

print("Available operations:")
print("add, subtract, multiply, divide")

user_input = input("Enter the operation: ")

selected_case = switch_dict.get(user_input, case_default)
result = selected_case()

print("Result:", result)
