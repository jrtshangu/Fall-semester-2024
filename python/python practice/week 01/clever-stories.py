#prompt message
print("Please enter the following: ")

#getting inputs from the user
adj=input("Adjective >: ")
anim= input("Animal >: ")
verb= input("Verb >: ")
exc= input("Exclamation >: ")
verbTwo= input("Verb >: ")
verbThree= input("Verb >: ")

#creating a story
story= f"""The other day, I was really in trouble. It all started when I saw a very {adj} {anim} {verb} down the hallway. "{exc.capitalize()}!" I yelled. But all I could think to do was to {verbTwo} over and over. Miraculously, that caused it to stop, but not before it tried to {verbThree} right in front of my family."""

#displaying the result
print("--------------------------------------------------------------------------------------")
print("Your story is:\n ")
print(story)


