# Nikita Moseichuk - Map Class
# Class representing the game map.

import random  # Importing the random module for generating random values

from obstacles import Chest, MonsterObstacle, Obstacle  # Importing obstacle classes from another module

class Map:
    def __init__(self, width, height):
        # Initialization of the map object with specified width and height
        self.width = width
        self.height = height
        self.tiles = [[" " for _ in range(width)] for _ in range(height)]  # Creating a 2D array to represent tiles on the map
        self.start = (0, 0)  # Player's starting position
        self.end = (width - 1, height - 1)  # End position (door)
        self.obstacles = []  # List of obstacles on the map
        self.inventory_items = []  # List of items in the inventory
        self.player_position = self.start  # Current player position
        self.monsters = ["E"]  # List of monsters on the map
        self.door_position = None  # Door position on the map
        self.key_chest_position = None  # Position of the chest with the key on the map

    def add_obstacle(self, obstacle):
        # Adding an obstacle to the map
        self.obstacles.append(obstacle)
        x, y = obstacle.position
        if isinstance(obstacle, Chest):
            self.tiles[y][x] = "C"  # Setting the chest symbol on the map
        elif isinstance(obstacle, MonsterObstacle):
            self.tiles[y][x] = "E"  # Setting the monster symbol on the map
        elif isinstance(obstacle, Obstacle):
            self.tiles[y][x] = "🧱"  # Setting the wall symbol on the map
        else:
            print("Unknown obstacle type")

    def add_inventory_item(self, item, position):
        # Adding an item to the inventory on the map
        self.inventory_items.append((item, position))
        x, y = position
        self.tiles[y][x] = "I"  # Setting the item symbol on the map

    def add_door(self, position):
        # Adding a door to the map
        self.door_position = position
        x, y = position
        self.tiles[y][x] = "🚪"  # Setting the door symbol on the map

    def update_player_position(self, position):
        # Updating the player's position on the map
        self.player_position = position

    def display_map(self):
        # Displaying the map with the current state
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.player_position:
                    print("👺", end=" ")  # Displaying the player symbol at its current position
                else:
                    print(self.tiles[y][x], end=" ")  # Displaying the symbol on the map
            print()

    def check_tile(self, position):
        # Checking the type of tile at the specified position
        x, y = position
        tile = self.tiles[y][x]
        if tile in self.monsters:
            print(f"Encountered monster at {position}")  # Message about encountering a monster
            return True, "E"  # Returning encounter flag and object type (monster)
        elif tile == "C":
            print(f"Encountered chest at {position}")  # Message about encountering a chest
            return True, "C"  # Returning encounter flag and object type (chest)
        elif tile == "🚪":
            print(f"Encountered door at {position}")  # Message about encountering a door
            return True, "🚪"  # Returning encounter flag and object type (door)
        elif tile == "I":
            print(f"Encountered inventory item at {position}")  # Message about encountering an inventory item
            return True, "I"  # Returning encounter flag and object type (item)
        elif tile == "🧱":
            print(f"Encountered wall at {position}")  # Message about encountering a wall
            return True, "🧱"  # Returning encounter flag and object type (wall)
        else:
            return False, None  # Returning no encounter flag and None type

    def remove_obstacle(self, position):
        # Removing an obstacle from the map
        x, y = position
        self.tiles[y][x] = " "  # Clearing the tile
        self.obstacles = [obs for obs in self.obstacles if obs.position != position]  # Removing the obstacle from the list

    def generate_random_item(self):
        # Generating a random item
        return random.choice(["Gold Coin", "Silver Coin", "Health Potion"])  # Returning a random choice from the list
