def case_one():
    return "This is case 1"

def case_two():
    return "This is case 2"

def case_default():
    return "This is the default case"

switch_dict = {
    "option1": case_one,
    "option2": case_two
}

user_input = input("Enter an option: ")

selected_case = switch_dict.get(user_input, case_default)
result = selected_case()

print(result)
