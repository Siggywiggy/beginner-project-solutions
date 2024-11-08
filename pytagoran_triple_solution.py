#! python3
# a program to check if the triangle input by the user is a right angle triangle

# c2 = a2 + b2


import pyinputplus as pyip

while True:
    print('Please enter the length of sides of your triangle.')

    side_1 = pyip.inputNum("Please enter first side:")
    side_2 = pyip.inputNum("Please enter second side:")
    side_3 = pyip.inputNum("Please enter third side:")

    if side_1 ** 2 + side_2 ** 2 == side_3 ** 2:
        print(f'{side_1}, {side_2}, {side_3} is a pytagorean triple!')
    elif side_1 ** 2 + side_3 ** 2 == side_2 ** 2:
        print(f'{side_1}, {side_2}, {side_3} is a pytagorean triple!')
    elif side_2 ** 2 + side_3 ** 2 == side_1 ** 2:
        print(f'{side_1}, {side_2}, {side_3} is a pytagorean triple!')
    else:
        print('Its not a pytagorean triple!')

    print('Would you like to continue or quit? Press Enter to continue, enter "q" to quit')

    user_input = input()

    if user_input == 'q':
        break
    else:
        continue


