MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_machine_on = True
quarters_value = 0.25
dimes_value = 0.10
nickels_value = 0.05
pennies_value = 0.01

water_remaining = resources["water"]
milk_remaining = resources["milk"]
coffee_remaining = resources["coffee"]
money_in_machine = 0


def is_resource_enough():
    is_enough = True
    if water_remaining < MENU[answer]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        is_enough = False
    if coffee_remaining < MENU[answer]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        is_enough = False
    if answer != "espresso" and milk_remaining < MENU[answer]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        is_enough = False
    return is_enough


def process_coins():
    """Returns true if the money is enough or else returns false"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    total = quarters_value * quarters + dimes_value * dimes + nickels_value * nickels + pennies_value * \
            pennies
    return total


def make_coffee(total):
    if total_money >= MENU[answer]["cost"]:
        global money_in_machine, water_remaining, coffee_remaining, milk_remaining
        money_in_machine += MENU[answer]["cost"]
        water_remaining -= MENU[answer]["ingredients"]["water"]
        coffee_remaining -= MENU[answer]["ingredients"]["coffee"]
        if answer != "espresso":
            milk_remaining -= MENU[answer]["ingredients"]["milk"]
        change = round(total_money - MENU[answer]["cost"], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {answer} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


while is_machine_on:
    making_coffee = True
    answer = input("What would you like? (espresso/latte/cappuccino):").lower()
    if answer == "off":
        is_machine_on = False
    elif answer == "report":
        print(f"Water: {water_remaining}ml\nMilk: {milk_remaining}ml\nCoffee: {coffee_remaining}g\nMoney: "
              f"${money_in_machine}")
    elif answer in ("latte", "espresso", "cappuccino"):
        making_coffee = is_resource_enough()
        if making_coffee:
            total_money = process_coins()
            make_coffee(total_money)
