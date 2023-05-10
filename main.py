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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def did_you_pay(payment, drink):
    if payment <= MENU[drink]["cost"]:
        return False
    else:
        return True


def insert_coins():
    print("Please insert coins.")
    quarters = .25 * int(input("how many quarters?: "))
    dimes = .1 * int(input("how many dimes?: "))
    nickles = .05 * int(input("how many nickles?: "))
    pennies = .01 * int(input("how many pennies?: "))
    payment = quarters + dimes + nickles + pennies
    return payment


def have_resources(drink):
    message_string = ""
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            message_string += f"Sorry there is not enough {ingredient}\n"
    if message_string == "":
        return True, "all good"
    else:
        return False, message_string[:-1]


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    if choice.lower() in ["espresso", "latte", "cappuccino"]:
        if have_resources(choice)[0]:
            total = insert_coins()
            if did_you_pay(total, choice):
                print(f"Here is ${round(total-MENU[choice]['cost'], 2)} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
                profit += MENU[choice]['cost']
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                try:
                    resources['milk'] -= MENU[choice]['ingredients']['milk']
                except KeyError:
                    pass

            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(have_resources(choice)[1])


# TODO: 1. Print a report of all the coffee machine resources
# TODO: 2. Check resources sufficient to make drink order.
# TODO: 3.
# TODO: 4.
