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

while is_machine_on:
    making_coffee = True
    answer = input("What would you like? (espresso/latte/cappuccino):").lower()
    if answer == "off":
        is_machine_on = False
    elif answer == "report":
        print(f"Water: {water_remaining}ml\nMilk: {milk_remaining}ml\nCoffee: {coffee_remaining}g\nMoney: "
              f"${money_in_machine}")
    elif answer in ("latte", "espresso", "cappuccino"):
        if water_remaining < MENU[answer]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            making_coffee = False

        if coffee_remaining < MENU[answer]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            making_coffee = False
        if answer != "espresso" and milk_remaining < MENU[answer]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            making_coffee = False
        if making_coffee:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))

            total_money = quarters_value * quarters + dimes_value * dimes + nickels_value * nickels + pennies_value * pennies
            if total_money >= MENU[answer]["cost"]:
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



