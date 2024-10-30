#Prompt message
message = "You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?"
print(message)

#getting answer from the user
answer = " "

#prompt messages based on the inputs
match_choice = """
    You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?
"""
flash = """
    You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?
"""
#checking on the user's answers
#conditions based on the match choice
while answer != "quit":
    answer_two = input("Enter your answer here >: ")

    if answer.lower() == "match":
        print(match_choice)
        
    elif answer_two.lower() == "hide":
        print("What if you get burned by the fire? You are putting your life into danger")
        
    elif answer_two.lower() == "run":
        print("What if you got attacked by the bear? And I am sure that you are not strong enough to fight the bear")

#conditions based on the flashlight choices
    elif answer.lower() == "flashlight":
        print(flash)
        answer_three = input("Enter your answer here >: ")

        if answer_three.lower() == "look":
            print("You might be attacked and waste your time ")
        if answer_three.lower() == "follow":
            print("It is better to follow the path and you should also be careful ")
        else:
            print("You are in danger still")