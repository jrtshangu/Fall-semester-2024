#with open("life-expectancy.csv") as my_data:
    #for sort_data in my_data:
        #removing blank lines
        #clear_data = sort_data.strip()
        #checking on the stripping
        #print(clear_data)

my_data = open("life-expectancy.csv")

for sort_data in my_data:
    #clearing the lines
    clean_data = sort_data.strip()
    #checking the action to be done successfully
    #print(clean_data)
    #separating the data
    separating_data = clean_data.split(",")
    #checking on the splitting
    #print(separating_data)
    #print("Data successfully split")

    #assigning indexes
    entity = separating_data[0]
    code = separating_data[1]
    year = separating_data[2]
    life_expectancy = separating_data[3]
    sorted_data = f"Entity {entity} (Code: {code}), Year: {year} - Life expectancy: {life_expectancy}"
    #checking on the data if they are correctly displayed
    #print(sorted_data)

    #getting an input from the user
year_of_interest = input("Enter the year of interest: ")
mini_so_far = -1
largest_so_far = 0

    # printing the largest
for number in life_expectancy:
    if number > largest_so_far:
        number_largest = largest_so_far

print(f"The overall max life expectancy is: {float(number_largest):.2f} from {entity} in {year}")

    # printing the lowest
for number_two in life_expectancy:
    if number_two < mini_so_far:
        number_two = mini_so_far
print(f"The overall min life expectancy is: {float(number_two):.2f} from {entity} in {year}")


my_data.close()