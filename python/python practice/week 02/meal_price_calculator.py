#Prompt message
print("Please enter the following: ")

#Getting inputs from the user
ch_meal = float(input("What is the price of a child's meal? >: " ))
ad_meal = float(input("What is the price of an adult's meal? >: "))
num_children = int(input("How many children ar there? >: "))
num_adult = int(input("How many adults are there? >: "))

#printing subtotal
subtotal = ch_meal * num_children + ad_meal * num_adult
print(f"Subtotal: $ {subtotal:.2f}")

#the sales tax rate
tax_rate = float(input("What is the sales tax rate? >: "))
sales_tax =  subtotal * tax_rate / 100
total = subtotal + sales_tax

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: $ {total:.2f}")

#payment amount
payment_amount = float(input("What is the payment amount? >: "))
change = f"Change: $ {payment_amount - total:.2f}"
print(change)