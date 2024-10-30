#prompts
prompt = "Welcome to the Shopping Cart Program!"
prompt_two = "Please select one of the following: "
menu = """
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit
"""

prompt_question = " "
action = " "
item = " "
items = [ ]

price_of_item = " "
item_prices = [ ]
#while loop
while prompt_question.lower() != "quit":
    print()
    print(prompt)
    print(prompt_two)
    print(menu)
    prompt_question = input("Enter here >: ")
#Adding items through 1 selection
    if prompt_question == "1" and action.lower() != "quit":
        item = input("What item would you like to add?\n>: ")
        price_of_item = input(f"What is the price of {item}?\n>: ")
        items.append(item)
        item_prices.append(float(price_of_item))

#viewing the shopping cart
    elif prompt_question == "2":
        print()
        for item_display in range(len(items)):
            shopping_list = items[item_display]
            price_display = item_prices[item_display]
            #print(f"{item_display}. {shopping_list}")
            item_display += 1

            print("Your Shopping Cart:")
            print(f"{item_display}. {shopping_list} - ${price_display}")
            

#removing from the shopping cart
    if prompt_question == "3":
        print()
        item_removal = int(input("Which item would you like to remove?\n>: "))
        
        if item_removal in range(len(items)):
            items.pop(item_removal)
            item_prices.pop(item_removal)
            print()
            #displaying the new shopping cart
            for item_display in range(len(items)):
                shopping_list = items[item_display]
                price_display = item_prices[item_display]
                
                print()
                print(f"Number {item_removal} removed!\n{item_display}. {shopping_list} - ${price_display}")
                
            

        elif item_removal not in range(len(items)):
            print("Sorry, that not a valid item")
            
        
            
    #comparing the input from the existing list
    

#using the sum() builtin funcion
    elif prompt_question == "4":
        print()
        sum_me = sum(item_prices)
        print(f"The total price of the items in the shopping cart is ${sum_me:.2f}")

#quiting the shopping cart
    elif prompt_question == "5":
        print("You chose to quit!")
        break

print("Goodbye!")
print()    