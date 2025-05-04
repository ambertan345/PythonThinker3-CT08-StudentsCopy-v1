# Question 1
# You are given a dictionary representing a restaurant menu.
# Each key is a food item (string), and 
# each value is the price of the item (float).

# Your tasks are:
# 1. Loop through the dictionary to print out the food items they sell.
# 2. Ask the customer what they want to buy.
# 3. Check if the item exists in the menu. 
#    - If it exists, print: " costs $"
#    - If it does not exist, print: "Sorry, we don't sell that."

# Example Output:
# Menu:
# Pizza
# Burger
# Pasta
# ...
# What would you like to buy? Pasta
# Pasta costs $6.9
###########################################
# Task: Complete the code below
menu = {
    "Pizza": 8.5,
    "Burger": 5.0,
    "Pasta": 6.9,
    "Fries": 3.5,
    "Salad": 4.0,
    "Sushi": 10.5,
    "Steak": 12.0,
    "Taco": 4.2,
    "Curry": 7.3,
    "Soup": 3.9
}

# Part 1: LOOP THROUGH THE MENU AND PRINT ITEMS
# Part 2: ASK THE USER WHAT THEY WANT TO BUY
# Part 3: CHECK IF ITEM EXISTS AND PRINT THE PRICE

# Write your code here, add more space as required

# 1.
print("Menu:")
for food in menu:
    print(food)

# 2.
choice = input("What do you want to buy?").strip().lower()

# 3.
menu_lookup = {food.lower(): food for food in menu}
if choice in menu_lookup:
    menu_choice = menu_lookup[choice]
    print(f"{choice} costs ${menu[menu_choice]}")
    
else:
    print("Sorry, we dont sell that.")

# Question 2
# You are given a dictionary called customer_spending, 
# which contains the names of customers (as keys) and 
# the total amount they spent in a month (as values).

# Your tasks are:
# 1. Identify customers who spent more than $1000.
#    - Add them to a dictionary called vip.
#    - Print a message for each VIP customer:
#      "Hi , you are now a VIP! Congratulations!"

# 2. Identify customers who spent less than or equal to $1000.
#    - Add them to a dictionary called non_vip.
#    - Print a message for each non-VIP customer indicating 
#      how much more they need to spend:
#      "Hi , spend $ more to become a VIP member!"

# Example Output:
# Hi Bob, you are now a VIP! Congratulations!
# Hi Charlie, spend $500 more to become a VIP member!

# Task: Complete the code below

customer_spending = {
    "Alice": 950, "Bob": 1200, "Charlie": 500, 
    "Diana": 1800, "Ethan": 2200, "Fiona": 700, 
    "John": 685, "Hor Kee": 1389, "Siew Ling": 235, 
    "Matt": 452, "Kristen": 985, "Johnson": 785, 
    "Charles": 2352, "Tommy": 741, "Laura": 689 }

# Part 1: 
# Loop through the customer_spending dictionary
# add vip customers to vip dictionary
# add non vip customers to non_vip dictionary

# Write your code here, add more space as required
vip = {}
non_vip = {}
for customer, amount in customer_spending.items():
    if amount > 1000:
        vip[customer] = amount
    else:
        non_vip[customer] = amount
    
###################################################
# Part 2: 
# Loop through the vip dictionary 
# Print "Hi [name], you are now a VIP! Congratulations!"

# Write your code here, add more space as required

for customer, amount in vip.items():
    print(f"Hi {customer}, You are now a vip! Congratulations!")




###################################################

# Part 3: 
# Loop through non_vip dictionary        
# Print "Hi [name], spend $XXX more to become a VIP member!"

# Write your code here, add more space as required

for customer, amount in non_vip.items():
    amount_needed = 1001 - amount
    print(f"Hi {customer}, spend ${amount_needed} more to become a vip member!")