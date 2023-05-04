import os
import time

from machine_data import logo, prompt, wrong_input, out_resource, not_enough_resources_logo, payment_logo, final_coffee, \
    MENU
from machine_resources import resources


def min_resource_check(resources):
    """Check if the machine has minimum resources for any drink"""

    if resources["water"] < 50 or resources["coffee"] < 18:
        return True
    else:
        return False


def drink_resource_check(resources, ingredients, drink):
    """Check if the machine has enough resources for a specific drink"""

    less_water = ""
    less_milk = ""
    less_coffee = ""
    less_resources = False

    if resources["water"] < ingredients["water"]:
        less_water = "water"
        less_resources = True
    if resources["milk"] < ingredients["milk"]:
        less_milk = "milk"
        less_resources = True
    if resources["coffee"] < ingredients["coffee"]:
        less_coffee = "coffee"
        less_resources = True

    if less_resources:
        os.system('cls')
        print(not_enough_resources_logo)
        print(f"not enough {less_water} {less_milk} {less_coffee} for {drink}")
        time.sleep(2)
        return True


def create_drink(ingredients, resources, cost):
    """deduct the resources after successfull payment"""

    water = resources["water"] - ingredients["water"]
    milk = resources["milk"] - ingredients["milk"]
    coffee = resources["coffee"] - ingredients["coffee"]
    money = resources["money"] + cost
    updated_resources = {
        "water": water,
        "milk": milk,
        "coffee": coffee,
        "money": money,
    }

    file = open('machine_resources.py', 'w')
    file.write(f"resources = {updated_resources}")
    file.close()

    return updated_resources


avail_prompt_input = ["espresso", "latte", "cappuccino", "report", "off"]  # All correct possible inputs to the prompt

while True:

    print(logo)
    out_of_resources = min_resource_check(resources)

    if out_of_resources:
        break

    prompt_input = input(prompt).lower()

    # Check if we obtain the right input

    while prompt_input not in avail_prompt_input:
        os.system('cls')
        print(wrong_input)
        time.sleep(2)  # Wait for two seconds and proceed
        os.system('cls')
        print(logo)
        prompt_input = input(prompt).lower()

    # perform tasks

    if prompt_input == "off":  # turn off the app and coffee machine
        exit()

    elif prompt_input == "report":  # Print the available resources left in a coffee machine
        os.system('cls')
        print("Resources:\n\n\tWater:  " + str(resources["water"]) + "ml")
        print("\tMilk:   " + str(resources["milk"]) + "ml")
        print("\tCoffee: " + str(resources["coffee"]) + "g")
        print("\tMoney:  $" + str(resources["money"]))
        print("\n\n\t\tthis will disappear in 10 seconds...")
        time.sleep(10)
        os.system('cls')
        continue

    drink = prompt_input
    drink_disc = MENU[drink]
    drink_ingredients = drink_disc["ingredients"]
    drink_cost = drink_disc["cost"]
    not_enough_resources = drink_resource_check(resources, drink_ingredients, drink)

    # Check if resources are enough for selected drink

    if not_enough_resources:
        continue  # Go back to start if not enough resources

    # If enough resources then go to payment area

    while True:

        os.system('cls')
        print(payment_logo)
        print(f"Your drink: {drink}\ntotal cost: ${drink_cost}")
        quarters = input("no. of quarters: ")
        dimes = input("no. of dimes: ")
        nickles = input("no. of nickels: ")
        pennies = input("no. of pennies: ")

        # Check if the input for payment is valid

        if not quarters.isnumeric() or not dimes.isnumeric() or not nickles.isnumeric() or not pennies.isnumeric():
            os.system('cls')
            print(wrong_input)
            time.sleep(2)
            continue

        quarters = int(quarters)
        dimes = int(dimes)
        nickles = int(nickles)
        pennies = int(pennies)
        amount_paid = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

        # Check if the money is enough

        if amount_paid < drink_cost:  # Refund money and cancel order if amount paid is less than the actual cost
            print(f"Sorry that is not enough money.\nMoney refunded: {amount_paid}")
            time.sleep(3)
            os.system('cls')
            break

        # update resources and collect money for drinks

        resources = create_drink(drink_ingredients, resources, drink_cost)
        os.system('cls')

        print(f"\n\tYour drink:  {drink}")
        print(f"\tDrink cost:  ${drink_cost}")

        if amount_paid > drink_cost:  # Return the extra money
            return_money = round(amount_paid - drink_cost, 2)
            print(f"\tYour change: ${return_money}")

        time.sleep(10)
        os.system('cls')
        print(final_coffee)
        print(f"\nHere is your {drink}. Enjoy!...")
        time.sleep(10)
        os.system('cls')
        break

# exit the machine if resources not enough for any drink and exit automatically after 10 sec.

os.system('cls')
print(out_resource)
print("the machine will turn off automatically in 10 seconds...")
time.sleep(10)
