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
    print(f"{choice} costs ${menu[choice]}")
    menu_choice = menu_lookup[choice]
else:
    print("Sorry, we dont sell that.")
