# Nikita Moseichuk - Player Class
# Represents the player character in the game.

from inventory import Inventory  # Import the Inventory class

class Player:
    def __init__(self, name, inventory=None):
        # Initialize the player with a name, an optional inventory, and starting position
        self.name = name
        self.inventory = inventory if inventory is not None else Inventory()  # Assign the provided inventory or create a new one
        self.position = (0, 0)  # Start the player at position (0, 0)

    def move(self, direction):
        # Method to move the player in the specified direction
        x, y = self.position
        if direction == "up" and y > 0:
            self.position = (x, y - 1)  # Move the player up
        elif direction == "down" and y < 9:
            self.position = (x, y + 1)  # Move the player down
        elif direction == "left" and x > 0:
            self.position = (x - 1, y)  # Move the player left
        elif direction == "right" and x < 9:
            self.position = (x + 1, y)  # Move the player right
        else:
            print("Move not allowed.")
        return self.position  # Return the new position after the move