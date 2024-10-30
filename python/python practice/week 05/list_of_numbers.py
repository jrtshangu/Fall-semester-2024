prompt = "Enter a list of numbers, type 0 when finished"
print(prompt)

number = " "
list_of_number = []
while number != 0:
    number = int(input("Enter number >: "))
    if number != 0:
        list_of_number.append(number)


#summing all together
sum = 0
for number in list_of_number:
    sum += number

print(f"The sum is: {sum}")
#average
average = mean(list_of_number)
print("The average is: ",average)
#largest number
