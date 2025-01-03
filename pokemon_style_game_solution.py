#! python3
# a pokemon style game - player and computer both have 3 moves

import random
import pyinputplus as pyip


# player Class
class Player:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def __repr__(self):
        return "Player {name}, with current health of {health} points".format(
            name=self.name, health=self.health
        )

    def cast_stab(self):
        stab_damage = random.randint(18, 25)
        print(f"{self.name} stabbed for {stab_damage} points!")
        return stab_damage

    def cast_fireball(self):
        fireball_damage = random.randint(10, 35)
        print(f"{self.name} cast Fireball for {fireball_damage} points!")
        return fireball_damage

    def cast_heal(self):
        health_amount = random.randint(18, 25)
        self.health += health_amount
        if self.health > 100:
            self.health = 100
        print(
            "{name} healed himself for {points} points of health, current health is now {hp}!".format(
                name=self.name, points=health_amount, hp=self.health
            )
        )

    def take_damage(self, damage, spell):
        self.health -= damage
        # prevent from health dropping to negative
        if self.health < 0:
            self.health = 0
        print(
            f"{self.name} took {damage} points of damage from {spell}, his current health is now {self.health}!"
        )

    def check_health(self):
        if self.health <= 0:
            return False

    def choose_move(self):
        move_choice = pyip.inputMenu(
            ["Stab", "Cast a fireball", "Cast a heal"],
            prompt="Choose a spell:\n",
            numbered=True,
        )
        if move_choice == "Stab":
            return self.cast_stab(), "Stab!"
        if move_choice == "Cast a fireball":
            return self.cast_fireball(), "Fireball!"
        if move_choice == "Cast a heal":
            return self.cast_heal(), "Heal!"


class Computer_player(Player):
    def __init__(self):
        self.name = "Grand Necromancer Kraz'hul"
        self.health = 100

    def computer_choose_move(self):
        # when sub 35 health increasing chance to cast heal
        if self.health < 35:
            # 3-6 are all heal spells so 50% chance to cast heal
            spell_cast = random.randint(1, 6)
        # if health is nearly full no need to cast heal so only choices 1-2 (Stab and Fireball)
        elif self.health <= 90:
            spell_cast = random.randint(1, 2)
        # if health is between 35 and 90 points all 3 spells are available
        else:
            spell_cast = random.randint(1, 3)

        if spell_cast == 1:
            # print(f"{self.name} cast Stab!")
            return self.cast_stab(), "Stab!"
        elif spell_cast == 2:
            # print(f"{self.name} cast Fireball!")
            return self.cast_fireball(), "Fireball!"
        elif spell_cast >= 3:
            # print(f"{self.name} cast Heal!")
            return self.cast_heal(), "Heal!"


player_name = pyip.inputStr(prompt="Please enter your name: \n")

Player_1 = Player(player_name)
Enemy = Computer_player()

# main game loop
while True:

    # player moves
    damage, spell = Player_1.choose_move()
    # if the spell chosen was a heal dont need to pass the damage and spell to the Enemy
    if spell == "Heal!":
        pass
    else:
        Enemy.take_damage(damage, spell)
        # check if enemy health was reduced to 0
        if Enemy.check_health() == False:
            print(f"{Enemy.name} has lost to {Player_1.name}! Game over!")
            break

    # enemy moves
    damage, spell = Enemy.computer_choose_move()
    # if the spell chosen was a heal dont need to pass the damage and spell to the player
    if spell == "Heal!":
        pass
    else:
        Player_1.take_damage(damage, spell)
        # check if player health is reduced to 0
        if Player_1.check_health() == False:
            print(f"{Player_1.name} has lost to {Enemy.name}! Game over!")
            break
