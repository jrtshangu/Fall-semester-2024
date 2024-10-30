prompt = "Please enter the items of the shopping list\n(Type 'Quit' to finish)"
print(prompt)

item = ""
items = []

#getting inputs while looping through
while item.lower() != "quit":
    
    item = input("Item >: ")
    if item.lower() != "quit":

        items.append(item)

print()
print("The shopping list is:")    
for it in items:
    print(it)

print()
#printing shopping list with indexes
print("The shopping list with indexes:")
for it_with_indexes in range(len(items)):
    shopping_list = items[it_with_indexes]
    print(f"{it_with_indexes}. {shopping_list}")

print() #blank line
#working on the modification of the list
checking_index = input("Which item would you like to change? >: ") 
items.pop(int(checking_index))
new_item = input("What is the new item? >: ")
items.append(new_item)
print()
#printing the new list
print("The shopping list with new index is:")
for new_list in range(len(items)):
    new_shopping_list = items[new_list]
    print(f"{new_list}. {new_shopping_list}")