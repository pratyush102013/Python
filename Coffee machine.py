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
money = 0

choice1 = input("Do you want coffee? Type yes or no\n").lower()
if choice1 == "yes":
    want_coffee = True
else:
    want_coffee = False

while want_coffee == True:
    choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if choice == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g")
        print(f"Money: {money}$")
        continue

    if "water" in MENU[choice]["ingredients"] and resources["water"] < MENU[choice]["ingredients"]["water"]:
        print(f"sorry there is not enough water for this {choice}")
        continue
    if "coffee" in MENU[choice]["ingredients"] and resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print(f"sorry there is not enough coffee for this {choice}")
        continue
    if "milk" in MENU[choice]["ingredients"] and resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print(f"sorry there is not enough milk for this {choice}")
        continue

    match choice:
        case "espresso":
            resources["water"] = resources["water"]-MENU[choice]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
            print("Please insert coins")
            quarters = int(input("How many quarters?\n"))
            dimes = int(input("How many dimes?\n"))
            nickels = int(input("How many nickels?\n"))
            pennies = int(input("How many pennies?\n"))
            quarters = (quarters*0.25)
            dimes = (dimes*0.10)
            nickels = (nickels*0.05)
            pennies = (pennies*0.01)
            total = (quarters+dimes+nickels+pennies)
            change = round(total-(MENU[choice]["cost"]), 2)
            if total >= (MENU["espresso"]["cost"]):
                money += MENU[choice]["cost"]
                print(f"Here is {change}$ in change")
                print("Here is your drink enjoy")
            else:
                print("Sorry you did not have enough money. Money refunded")
                continue
            choice1 = input("Do you want coffee? Type yes or no").lower()
            if choice1 == "yes":
                want_coffee = True
        case "latte":
            resources["water"] = resources["water"]-MENU[choice]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
            print("Please insert coins")
            quarters = int(input("How many quarters?\n"))
            dimes = int(input("How many dimes?\n"))
            nickels = int(input("How many nickels?\n"))
            pennies = int(input("How many pennies?\n"))
            quarters = (quarters*0.25)
            dimes = (dimes*0.10)
            nickels = (nickels*0.05)
            pennies = (pennies*0.01)
            total = (quarters+dimes+nickels+pennies)
            change = round(total-(MENU[choice]["cost"]), 2)
            if total >= (MENU["latte"]["cost"]):
                money += MENU[choice]["cost"]
                print(f"Here is {change}$ in change")
                print("Here is your drink enjoy")
            else:
                print("Sorry you did not have enough money. Money refunded")
                continue
            choice1 = input("Do you want coffee? Type yes or no").lower()
            if choice1 == "yes":
                want_coffee = True
        case "cappuccino":
            resources["water"] = resources["water"]-MENU[choice]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
            print("Please insert coins")
            quarters = int(input("How many quarters?\n"))
            dimes = int(input("How many dimes?\n"))
            nickels = int(input("How many nickels?\n"))
            pennies = int(input("How many pennies?\n"))
            quarters = (quarters*0.25)
            dimes = (dimes*0.10)
            nickels = (nickels*0.05)
            pennies = (pennies*0.01)
            total = (quarters+dimes+nickels+pennies)
            change = round(total-(MENU[choice]["cost"]), 2)
            if total >= (MENU["cappuccino"]["cost"]):
                money += MENU[choice]["cost"]
                print(f"Here is {change}$ in change")
                print("Here is your drink enjoy")
            else:
                print("Sorry you did not have enough money. Money refunded")
                continue
            choice1 = input("Do you want coffee? Type yes or no").lower()
            if choice1 == "yes":
                want_coffee = True
        case _:
            print("You have a typo please try again")
