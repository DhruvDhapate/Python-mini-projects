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


def check_resource(item):
    for i in item:
        if resources[i] < item[i]:
            print(f"Not sufficient {i}")
            return False
    return True


def calculate_resources(item, drink):
    for i in drink:
        resources[i] -= drink[i]
    print(f"Take your drink {item}")


def display_report():
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Money : {wallet}")


def coins():
    total = int(input("Quarters : "))*0.25
    total += int(input("Dimes : "))*0.1
    total += int(input("Nickles : "))*0.05
    total += int(input("Pennies : "))*0.01
    return total


def transaction(cost):
    global payment,wallet
    if payment >= cost:
        payment = round(payment - cost, 2)
        print(f"Your change is {payment}")
        wallet += payment
        return True
    else:
        print("Need to pay more")
        return False


wallet = 0

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        display_report()
    elif choice == "off":
        break
    else:
        drink = MENU[choice]
        if check_resource(drink['ingredients']):
            payment = coins()
            if transaction(payment):
                calculate_resources(choice, drink['ingredients'])
                display_report()
