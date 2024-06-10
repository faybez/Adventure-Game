# Nikita Moseichuk - Monster Class
# Class representing a monster in the game.

class Monster:
    def __init__(self, name, hp, attack):
        # Initialization of the monster object with name, health points (hp), and attack power
        self.name = name
        self.hp = hp
        self.attack = attack

    def display_info(self):
        # Method to display information about the monster
        print(f"Monster: {self.name}, HP: {self.hp}, Attack: {self.attack}")  # Printing monster information
