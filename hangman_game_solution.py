#! python 3
# a program to play hangman
from hangman_game_ascii import hangman_pics
import time
from random import randint
import pyinputplus as pyip


def get_word():
    # open and import a dictionary from a .txt file
    dict_file = open("hangman_game_dictionary.txt")
    dict_words = dict_file.readlines()
    dict_file.close()
    # randomly choose a word
    secret_word = dict_words[randint(0, len(dict_words))].rstrip("\n").upper()
    return secret_word


def check_win(secret_word, hidden_word):
    # check if the player has guessed the word
    if secret_word == "".join(hidden_word):
        return True
    else:
        return False


def check_loss(wrong_answers):
    if wrong_answers > 5:
        return True
    else:
        return False


def game_loop(secret_word):
    wrong_answers = 0
    hidden_word = ["_" for letter in secret_word]
    # main game loop
    while True:
        # keep track of wrong answers with a variable wrong_answers
        # generate the hidden word list/graphic

        # draw the first hangman ASCII graphic
        print(hangman_pics[wrong_answers])
        # draw the hidden word
        print(" ".join(hidden_word))
        # player input
        player_guess = pyip.inputRegex(
            r"^[a-zA-Z]$",
            prompt="Guess a single letter or leave empty if you want to give up: \n",
            blank=True,
        ).upper()
        # if the player doesnt pick a letter defaults to loss
        if player_guess == "":
            print(hangman_pics[5])
            print("You gave up and you were hanged!")
            time.sleep(0.5)
            break
        # find the letter indices
        letter_indices = [
            index for (index, item) in enumerate(secret_word) if item == player_guess
        ]
        # check if the player guessed any letter correctly
        if not letter_indices:
            wrong_answers += 1
            print("You guessed wrong! You are one step closer to the hangmans noose!")
            time.sleep(0.5)
        else:
            print(f"You guessed {len(letter_indices)} letters!")
            for index in letter_indices:
                hidden_word[index] = player_guess
            time.sleep(0.5)

        if check_loss(wrong_answers) == True:
            print("You were hanged!")
            print(hangman_pics[wrong_answers])
            print(f"The correct word was {secret_word}")
            time.sleep(0.5)
            break
        elif check_win(secret_word, hidden_word) == True:
            print(secret_word)
            print("You have escaped the hangmans noose!\nFor this time...")
            time.sleep(0.5)
            break
        else:
            continue


# main game loop
while True:
    play_game = pyip.inputMenu(
        ["Yes", "No"], prompt="Do you want to play the Hangman game?\n", lettered=True
    )
    if play_game == "Yes":
        print(
            "Welcome to the gallows!\nYou can escape the noose if you guess the word correctly."
        )

        secret_word = get_word()
        game_loop(secret_word)
    elif play_game == "No":
        print("The gallows await.. for the next time...")
        print(hangman_pics[0])
        break
