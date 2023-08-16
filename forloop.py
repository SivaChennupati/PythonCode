
# Example 1: Simple while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Example 2: Using a while loop with user input
secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess and Please enter a secret number:    "))
    if guess < secret_number:
        print("Guessed value is too low!")
    elif guess > secret_number:
        print(" Guessed value is Too high!")
    else:
        print("Congratulations! You guessed correctly!")
        break  # Exit the loop when the correct guess is made
