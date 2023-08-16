# Writing to a file

# Reading from a file  which is the current path
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
