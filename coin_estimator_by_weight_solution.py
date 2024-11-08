#! python3
# a program to calculate the amount of coin wrappers needed, how many of each coin they have and the total value of their money

import pyinputplus as pyip

measurement_system = ["metric", "imperial"]

measurement_choice = pyip.inputMenu(
    measurement_system,
    prompt=f"Choose the corresponding number for grams (metric) or pounds (imperial) ! \n",
    numbered=True,
)

pennies_weight = pyip.inputNum("Please input the weight of your pennies \n")
nickels_weight = pyip.inputNum("Please input the weight of your nickels \n")
dimes_weight = pyip.inputNum("Please input the weight of your dimes \n")
quarters_weight = pyip.inputNum("Please input the weight of your quarters \n")

one_penny_weight_grams = 2.5
one_nickel_weight_grams = 5
one_dime_weight_grams = 2.27
one_quarter_weight_grams = 5.67

one_penny_weight_pounds = 0.0055116
one_nickel_weight_pounds = 0.011023
one_dime_weight_pounds = 0.0050045
one_quarter_weight_pounds = 0.012500

if measurement_choice == "metric":
    amount_of_pennies = round(pennies_weight / one_penny_weight_grams)
    amount_of_nickels = round(nickels_weight / one_nickel_weight_grams)
    amount_of_dimes = round(dimes_weight / one_nickel_weight_grams)
    amount_of_quarters = round(quarters_weight / one_quarter_weight_grams)

elif measurement_choice == "imperial":
    amount_of_pennies = round(pennies_weight / one_penny_weight_pounds)
    amount_of_nickels = round(nickels_weight / one_nickel_weight_pounds)
    amount_of_dimes = round(dimes_weight / one_nickel_weight_pounds)
    amount_of_quarters = round(quarters_weight / one_quarter_weight_pounds)

count_pennies_wrappers = round(amount_of_pennies / 50)
count_nickels_wrappers = round(amount_of_pennies / 50)
count_dimes_wrappers = round(amount_of_dimes / 50)
count_quarters_wrappers = round(amount_of_quarters / 50)

total_money = (
    amount_of_pennies
    + amount_of_nickels * 5
    + amount_of_dimes * 10
    + amount_of_quarters * 25
) / 100

print(
    f"You have {amount_of_pennies} pennies,  {amount_of_nickels} nickels, {amount_of_dimes} dimes and {amount_of_quarters} quarters."
)
print(
    f"You will need {count_pennies_wrappers} penny wrappers, {count_nickels_wrappers} nickels wrappers, {count_dimes_wrappers} dimes wrappers and {count_quarters_wrappers} quarters wrappers"
)
print(f"You have approximately {total_money} dollars!")
