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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

profit = 0
turned_on = True

def print_resources():
    for res,qty in resources.items():
        if res == "coffee":
            measurement = "g"
        else:
            measurement = "ml"
        print(f"{res.title()}: {qty}{measurement}")
    print(f"Money: ${profit}")

def process_coins():
    total_inserted = 0
    for coin, value in coins.items():
        current_coin = input(f"How many {coin}?: ")
        if not current_coin:
            current_coin = 0
        total_inserted += int(current_coin) * coins[coin]
    return round(total_inserted, 2)

def main_process(coffee_type):
    print(f"You selected {coffee_type}")
    for res, qty in resources.items():
        if res in MENU[coffee_type]['ingredients']:
            if qty < MENU[coffee_type]['ingredients'][res]:
                print(f"Sorry, there's not enough {res}. [Available: {qty}]/[Needed: {MENU[coffee_type]['ingredients'][res]}]")
                return 0
    coffee_cost = MENU[coffee_type]['cost']
    print(f"That will be ${coffee_cost}")
    total_inserted = process_coins()
    print(f"You inserted ${total_inserted}")
    if total_inserted < coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return 0
    else:
        print("You can buy the coffee :)")
        if total_inserted > coffee_cost:
            refund = total_inserted - coffee_cost
            print(f"Here's {round(refund, 2)} in change.")
        global profit
        profit += coffee_cost
        make_coffee(coffee_type)

def make_coffee(coffee_selected):
    print(f"Making {coffee_selected}...")
    for res, qty in resources.items():
        if res in MENU[coffee_selected]['ingredients']:
            resources[res] -= MENU[coffee_selected]['ingredients'][res]
    print(f"Here's your {coffee_selected}. Enjoy!")

while turned_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        print_resources()
        continue

    if user_input == "off":
        turned_on = False
        break

    if user_input in MENU:
        main_process(user_input)
    else:
        print("Not valid")
