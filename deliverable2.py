apple = " Apple 2$ "
grape = " Grape 1$ "
orange = " Orange 3$ "
total_cost = 0
fruit = [apple, grape, orange]
apple_count = 0
grape_count = 0
orange_count = 0
name = input("What is your name? ")

"""
The code below uses a while true loop. This loop breaks when anything other y is inputed to would you want another fruit
The reason it does this is the != opperand is not equal to, therefore when the input is not why the loop moves on and 
breaks. If that was not there the loop would run indefinitely. The if statements are simple setting the user input equal
to one of the options each option selects the appropriate costs and has a counter to count how many are bought. 
"""
while True:


    print(f"Welcome {name}. Which fruit would you like to buy today?")
    print(f"1.) {fruit[0]}")
    print(f"2.) {fruit[1]}")
    print(f"3.) {fruit[2]}")
    fruit_choice = int(input("> "))

    # Process the chosen fruit
    if fruit_choice == 1:
        fruit_buy = "apple"
        cost = 2
        apple_count += 1
    elif fruit_choice == 2:
        fruit_buy = "grape"
        cost = 1
        grape_count += 1
    elif fruit_choice == 3:
        fruit_buy = "orange"
        cost = 3
        orange_count += 1
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

    total_cost += cost

    another_fruit = input("Would you like to buy another piece of fruit? (y/n)\n> ")
    if another_fruit.lower() != 'y':
        break

"""
Below is a simple the subtotal is equal to the cost before calculation. Then the tax would be the subtotal multiplied
by the sales tax rate. Adding the two values gives you the correct total cost. 
"""
sub_total = total_cost
tax = sub_total * .05
total_cost = sub_total + tax
print(f"Order for {name}")
print(f"{apple_count} Apple(s) at $2 apiece")
print(f"{grape_count} Grape(s) at $1 apiece")
print(f"{orange_count} Orange(s) at $3 apiece")

print(f"Sub Total: ${sub_total}")
print(f"5% Tax: ${tax}")
print(f"Total: ${total_cost}")