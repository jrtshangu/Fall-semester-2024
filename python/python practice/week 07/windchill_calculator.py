speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

temp = int(input("What is the temperature?\n>: "))
value_choice = input("Fahrenheit or Celcius (F/C)\n>: ")

if value_choice.lower() == "f":
    
    for number in speed:
        convert = (number * 9/5) + 32
        convert_fahrenheit =  convert / number ** 0.16 
        message = f"At the temperature of {float(temp)}F, and the wind peed of {number} mph, the windchill is {convert_fahrenheit:.2f}F"
        print(message)

        
        
        
    
elif value_choice.lower() == "c":
    for number in speed:
        
        convert_celcius =  temp / number ** 0.16 
        message = f"At the temperature of {float(temp)}F, and the wind peed of {number} mph, the windchill is {convert_celcius:.2f}F"
        print(message)
    
    

    
