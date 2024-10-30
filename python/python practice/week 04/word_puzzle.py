#welcome message
prompt = "Wecome to the word guessing game!\n(enter 'Quit' if you want to quit)"


hint = "_ _ _ _ _ _" 
hint_two = "T_ m_ _"
hint_three = "T_ _p_e"

print(prompt)
print()
print(f"Your hint: {hint}")

question = " "#question

#using loops to tract the inputs
while question.lower() != "quit":
    question = input("What is your guess? >: ")

    #tracking the number of attempts
    for x in range(0,6):
        if x == 3 and question != "temple":
            print(f"This is your {x} attempt")
            print(" ")
            

        #elif x == 5 or question.lower() == "temple":
            #print(f"It took you {x} attempts")
            #print(" ")

    #controling inputs
    if len(question) > 6: #tracking the number of letters from the user input
        print("Sorry, the guess must have the same number of letters as the secret word")

    #secret word
    elif question.lower() == "temple":
        print("You guessed it!")

        #checking whether the user would like to continue playing the game
        check = input("Would you like to continue? (y/n)")
        if check.lower() == "y":
            print(f"Hint: {hint}")
        else:
            print("You chose to quit!")
            break
    
    elif question.lower() != "temple" and "e" in question:
        print("Wrong!")
        print("Hint: ",hint_two)
        
    elif "m" or "p" in question:
        print("You are almost there")
        print("Hint: ",hint_three)

    
        

    
#print(len(hint)) #checking the length of the hint
#once the user enters Quit
print("You just quit!")