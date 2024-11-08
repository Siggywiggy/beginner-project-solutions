#! python3

import pyinputplus as pyip

while True:

    nickel_pennies = 5
    dime_pennies = 10
    quarter_pennies = 25
    nickels = 0
    dimes = 0
    quarters = 0
    pennies = 0

    item_price = pyip.inputFloat("Please enter the price of the item: \n")
    client_money = pyip.inputFloat(
        "Please enter how much money did the customer give you: \n"
    )

    if client_money < item_price:
        print(
            f"The customer gave too little money. Ask for at least {round((item_price - client_money), 2)}$ more!"
        )
        continue

    pennies = int((client_money - item_price) * 100)

    # check if you can get quarters out of the penny total
    if pennies >= quarter_pennies:
        quarters += int(pennies / quarter_pennies)
        pennies -= quarter_pennies * quarters

    # check if you can get dimes out of the remaining penny total
    if pennies >= dime_pennies:
        dimes += int(pennies / dime_pennies)
        pennies -= dime_pennies * dimes

    # check if you can get nickels out of the remaining penny total
    if pennies >= nickel_pennies:
        nickels += int(pennies / nickel_pennies)
        pennies -= nickel_pennies * nickels

    print(
        f"You need to return {quarters} quarters, {dimes} dimes, {nickels} nickels and {pennies} pennies"
    )
