def choose_case_example(option):
    options = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected"
    }

    result = options.get(option, "Invalid option")
    print(result)


user_option = int(input("Enter an option (1, 2, or 3): "))
choose_case_example(user_option)
