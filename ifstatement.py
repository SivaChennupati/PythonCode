# Example 1: Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else statement
age = int(input("Please enter your age:    "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 3: if-elif-else statement
score = int(input("Please enter your Score:    "))
if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("Below C grade")

# Example 4: Nested if statements
num = int(input("Please enter any number:    "))
if num % 2 == 0:
    print("Enetered number " + str(num) +" is Even number")
    if num > 10:
        print("Even number greater than 10")
else:
    print("Enetered number " + str(num) +"  is Odd number")
