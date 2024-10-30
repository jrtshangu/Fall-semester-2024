#Prompt message
print("Please enter the following information: ")
#getting input from the user

fName= input("First name >: ")
lName= input("Last name >: ")
email= input("Email Address >: ")
phoneNumber= int(input("Phone Number >: "))
jobTitle= input("Job Title >: ")
iNum= int(input("ID Number >: "))

print("Data successfully received!")
#gathering information
#print("Preparing your data...") #fixing bugs

lNameCaps= lName.upper() #converting the last name
data=f"""{lNameCaps}, {fName.capitalize()}\n{jobTitle.capitalize()}\nID: {iNum}
    \n{email}\n{phoneNumber}"""


#displaying the data
#print("Printing your data...") #fixing bugs
lines= "---------------------------------------"
print(lines)
print(data)
print(lines)

#print("Data successfully printed!") #fixing bugs


