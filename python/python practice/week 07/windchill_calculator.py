speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

temp = int(input("What is the temperature?\n>: "))
value_choice = input("Fahrenheit or Celcius (F/C)\n>: ")

def statement(celcius, fahrenheit):
    if value_choice.lower() == "f":
        for number in speed:
            convert_fahrenheit =  34.74 + 0.6215 * temp - 35.75 * number**0.16 + 0.4275 * temp * number**0.16
            fahrenheit = f"At the temperature of {float(temp)}F, and the wind peed of {number} mph, the windchill is {convert_fahrenheit:.2f}F"
            print(fahrenheit)  
                   
    elif value_choice.lower() == "c":
        for number in speed:
            convert_celcius = number  * 9 / 5 + 32 
            celcius = f"At the temperature of {float(temp)}F, and the wind peed of {number} mph, the windchill is {convert_celcius:.2f}F"
            print(celcius)
    

statement(" ", " ")

    
