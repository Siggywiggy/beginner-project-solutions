#! python3
# a program for single player blackjack game

import random
import pyinputplus as pyip


class Deck:
    def __init__(self):
        # initiate the default state of deck of cards
        # one card of every value in a suite

        self.clubs_card_stack = {
            "Ace of clubs": 1,
            "Two of clubs": 2,
            "Three of clubs": 3,
            "Four of clubs": 4,
            "Five of clubs": 5,
            "Six of clubs": 6,
            "Seven of clubs": 7,
            "Eight of clubs": 8,
            "Nine of clubs": 9,
            "Ten of clubs": 10,
            "Jack of clubs": 10,
            "Queen of clubs": 10,
            "King of clubs": 10,
        }
        self.diamonds_card_stack = {
            "Ace of diamonds": 1,
            "Two of diamonds": 2,
            "Three of diamonds": 3,
            "Four of diamonds": 4,
            "Five of diamonds": 5,
            "Six of diamonds": 6,
            "Seven of diamonds": 7,
            "Eight of diamonds": 8,
            "Nine of diamonds": 9,
            "Ten of diamonds": 10,
            "Jack of diamonds": 10,
            "Queen of diamonds": 10,
            "King of diamonds": 10,
        }
        self.hearts_card_stack = {
            "Ace of hearts": 1,
            "Two of hearts": 2,
            "Three of hearts": 3,
            "Four of hearts": 4,
            "Five of hearts": 5,
            "Six of hearts": 6,
            "Seven of hearts": 7,
            "Eight of hearts": 8,
            "Nine of hearts": 9,
            "Ten of hearts": 10,
            "Jack of hearts": 10,
            "Queen of hearts": 10,
            "King of hearts": 10,
        }
        self.spades_card_stack = {
            "Ace of spades": 1,
            "Two of spades": 2,
            "Three of spades": 3,
            "Four of spades": 4,
            "Five of spades": 5,
            "Six of spades": 6,
            "Seven of spades": 7,
            "Eight of spades": 8,
            "Nine of spades": 9,
            "Ten of spades": 10,
            "Jack of spades": 10,
            "Queen of spades": 10,
            "King of spades": 10,
        }
        self.stacks = [
            self.clubs_card_stack,
            self.diamonds_card_stack,
            self.hearts_card_stack,
            self.spades_card_stack,
        ]

    def __repr__(self):
        return "A deck with {amount} of cards".format(
            amount=(
                    len(self.clubs_card_stack)
                    + (len(self.diamonds_card_stack))
                    + len(self.hearts_card_stack)
                    + len(self.spades_card_stack)
            )
        )

    def pick_random_card(self):
        # firstly select a random suite
        random_suite = random.choice(self.stacks)
        # create a list of existing cards in the suite
        list_of_cards = [card for card in random_suite.keys()]
        # choose a random card and get its value from dict
        random_card = random.choice(list_of_cards)
        card_value = random_suite[random_card]
        # delete the card from the dictionary as it is being drawn
        print(f"You got {random_card} from the deck")
        del random_suite[random_card]

        return random_card, card_value


class Player:
    def __init__(self):
        self.round_score = 0
        self.cards = list()

    def __repr__(self):
        return "The player has {points} points.".format(points=self.round_score)

    def add_card(self, card, value):
        self.round_score += value
        self.cards.append(card)

    def check_score(self):
        if self.round_score == 21:
            return True
        elif self.round_score > 21:
            return False
        else:
            return self.round_score

    def check_hand(self):
        print(
            f'You are holding {", ".join(self.cards)} and you have {self.round_score} points!'
        )


rounds = 1
game_score = 100

while rounds < 6:
    print(f"Currently on round {rounds}!")
    print(f"You have {game_score} points total!")
    # instantiate player instance
    player_1 = Player()
    # instantiate deck of cards instance
    deck_of_cards = Deck()
    # player gets the first two cards from the deck at the start of a round
    card, value = deck_of_cards.pick_random_card()
    player_1.add_card(card, value)
    card, value = deck_of_cards.pick_random_card()
    player_1.add_card(card, value)
    # player sees his hand
    player_1.check_hand()
    # player choices loop
    while True:
        if player_1.check_score() == False:
            print(
                f"You just went bust! Perhaps taking a bit more calculated risks would be wiser..."
            )
            game_score -= 21
            rounds += 1
            break
        elif player_1.check_score() == True:
            print(f"You scored a perfect 21!")
            rounds += 1
            break

        player_input = pyip.inputMenu(
            ["Draw card", "End round"], prompt="Choose your action:\n", lettered=True
        )

        if player_input == "End round":
            game_score -= 21 - player_1.check_score()
            rounds += 1
            break
        elif player_input == "Draw card":
            card, value = deck_of_cards.pick_random_card()
            player_1.add_card(card, value)
            player_1.check_hand()
            continue

print(f"You finished the game with {game_score} points!")
