#importing the random module
import random as rm

#number range
secret_range = rm.randint(1, 100)
magic_number = secret_range

#getting user input
user_magic_number = int(input("What is your magic number? >: "))
guess_number = int(input("What is your guess number? "))

while guess_number == magic_number:
    print("You guessed it!")

    if user_magic_number < magic_number:
        print("Low")
        
        guess_number = int(input("What is your guess number? "))
    elif user_magic_number > magic_number:
        print("Higher")
        
        guess_number = int(input("What is your guess number? "))