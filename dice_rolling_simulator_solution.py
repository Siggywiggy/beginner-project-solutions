#! python3
# a program to roll dice

# https://stackoverflow.com/questions/15884075/tkinter-in-a-virtualenv

from random import randint
import pyinputplus as pyip

while True:

    dice_sides = pyip.inputInt(prompt="Please enter the sides of desired dice\n", min=3)

    rolls = pyip.inputInt(
        prompt="Please enter how many times should the dice be rolled\n", min=1
    )
    # keep statistics of each roll in a dictionary
    roll_statistics = dict()

    for r in range(0, rolls):
        dice_roll = randint(1, dice_sides)
        if str(dice_roll) in roll_statistics.keys():
            roll_statistics[str(dice_roll)] += 1
        else:
            roll_statistics.setdefault(str(dice_roll), 1)

    for key, value in roll_statistics.items():
        print(
            f"Dice side {key} was rolled {value} times, this is {round((value / rolls) * 100, 2)} % of the total"
        )

    continue_rolling = pyip.inputYesNo(
        prompt="Do you wish to continue rolling? Yes/No?"
    )

    if continue_rolling == "yes":
        continue
    else:
        break
