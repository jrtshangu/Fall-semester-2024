#practicing functions

def my_data(names, age, phone):
    names = input("What is your full name? \n>: ")
    age = input("How old are you? \n>: ")
    phone = input("What is your phone number? \n>: ")

    data = f"Your information:\nFull name: {names}\nAge: {age}\nPhone number: {int(phone)}"
    print(data)
    if int(age) >= 30:
        status = input("Are you married? (yes/no)\n >:")
        if status.lower() == "yes":
            print("Hey, you are good now!! Congratulations")
        elif status.lower() == "no":

            print("Consider getting married now!")





my_data(" ", " ", " ")



