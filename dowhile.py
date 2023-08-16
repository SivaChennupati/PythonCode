# Example of a "do-while" loop in Python
while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == "exit":
        break
    else:
        print("You entered a   :", user_input)
