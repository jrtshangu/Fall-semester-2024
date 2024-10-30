
#opening the file
with open("my_data.csv") as my_data:
    #printing the data
    for lines in my_data:
        cleaning_data = lines.strip()
        print()
    #splitting data and parsing them accordingly
        separate = cleaning_data.split(",")
        entity = separate[0]
        code = separate[1]
        year = separate[2]
        life_expectancy = separate[3]

        data = f"Entity {entity} (Code: {code}), Year: {year} - Life expectancy: {life_expectancy:.3f}"
    
        #print(data)

        

    #user inputs
    year_of_interest = int(input("Enter the year of interest: "))
    
    #finding the min and max numbers
    mini_so_far = -1
    largest_so_far = 0

    #printing the largest
    for number in life_expectancy:
        if largest_so_far > 0:
            number = largest_so_far

    print(f"The overall max life expectancy is: {float(largest_so_far):.2f} from {entity} in {year}")
    
    #printing the lowest
    for number_two in life_expectancy:
        if mini_so_far < number:
            number_two = mini_so_far
    print(f"The overall min life expectancy is: {float(number_two):.2f} from {entity} in {year}")

