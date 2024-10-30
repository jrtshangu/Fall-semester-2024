
class MyData:
    def __init__(self, name, age):#name of the functions that will be initialized after
        
        self.name = input("What is your name? >: ")
        self.age = int(input("How old are you? >: "))

        
data = MyData(""," ")#calling the function
#printing the input according to the needed function
print("Hello ",data.name) 
print("you are ", data.age)

