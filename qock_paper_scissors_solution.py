#!3 python3
# rock-paper-scissors game

import random
import pyinputplus as pyip

choices = ['rock', 'paper', 'scissors']

player_wins = 0
computer_wins = 0

while True:

    player_choice = pyip.inputMenu(choices, prompt=f"Choose the corresponding number for rock, paper, or scissors! \n", numbered=True)
    print(f'you chose {player_choice}')

    computer_choice = choices[random.randint(0, 2)]
    print(f'computer chose {computer_choice}')

    if player_choice == computer_choice:
        print('Its a tie!')
    elif player_choice == choices[0] and computer_choice == choices[1]:
        computer_wins += 1
        print('The computer wins!')
    elif player_choice == choices[1] and computer_choice == choices[0]:
        player_wins += 1
        print('The player wins!')
    elif player_choice == choices[0] and computer_choice == choices[2]:
        computer_wins += 1
        print('The computer wins!')
    elif player_choice == choices[2] and computer_choice == choices[0]:
        player_wins += 1
        print('The player wins!')
    elif player_choice == choices[1] and computer_choice == choices[2]:
        computer_wins += 1
        print('The computer wins!')
    elif player_choice == choices[2] and computer_choice == choices[1]:
        player_wins += 1
        print('The player wins!')

    user_input = input('Would you like to continue or quit and see results? Press Enter to continue, enter "q" to quit \n')

    if user_input == 'q':
        break
    else:
        continue

print(f'The player won {player_wins} times and the computer won {computer_wins} times! \n Thanks for playing!')