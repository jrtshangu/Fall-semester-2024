grade= int(input("Please enter your Grade >: "))

if grade >= 60:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C") 
    elif grade >= 60:
        print("D")
   
    else:
        print("F")
else:
    print("F")
