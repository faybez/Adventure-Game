# Nikita Moseichuk - Adventure Game
#The Python script creates a text-based adventure game where players navigate a grid-based map, encountering obstacles like monsters and chests. 
#They can interact with these objects, collect items, and use inventory items like health potions and coins. The game progresses through levels, 
#with players needing keys to unlock doors and advance. The script manages game logic, player input, and map generation.

# Importing necessary modules
import random
from player import Player
from map import Map
from obstacles import Obstacle, Chest, MonsterObstacle
from inventory import Inventory, Coin

# Function to initialize a level in the game
def initialize_level():
    # Creating a new game map
    game_map = Map(10, 10)
    
    # Creating a player with an inventory and setting initial health
    player = Player("Hero", Inventory())
    coins = Coin()
    player_health = 3

    # Adding initial obstacles and items to the map
    obstacle = Obstacle("Rock", (4, 4))
    game_map.add_obstacle(obstacle)
    game_map.add_inventory_item("Health Potion", (2, 2))
    player.inventory.add_item("Health Potion")

    # Adding monsters to the map
    for _ in range(5):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        monster_obstacle = MonsterObstacle("E", (x, y))
        game_map.add_obstacle(monster_obstacle)

    # Adding chests to the map
    for _ in range(3):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        chest = Chest((x, y))
        game_map.add_obstacle(chest)

    # Adding a key chest to the map
    key_chest_position = (random.randint(0, 9), random.randint(0, 9))
    key_chest = Chest(key_chest_position)
    game_map.add_obstacle(key_chest)
    game_map.key_chest_position = key_chest_position

    # Adding a door to the map
    game_map.add_door((9, 9))

    return game_map, player, coins, player_health

# Function to display the game rules
def display_rules():
    print("Welcome to the Adventure Game!")
    print("Rules:")
    print("1. Use commands to navigate the map and interact with objects.")
    print("2. Commands include 'move up', 'move down', 'move left', 'move right', 'inventory', 'use <item>', 'quit'.")
    print("3. Encounter monsters ('E') and choose to 'fight' or 'flee'. Defeat monsters to earn coins.")
    print("4. Find and open chests ('C') to discover items. Some chests may contain a key needed to progress.")
    print("5. Find and use 'Health Potion' to restore health.")
    print("6. Use 'Gold Coin' to receive 100 coins and 'Silver Coin' to receive 50 coins.")
    print("7. Beware of traps ('I') which may either grant you 50 coins or rob you of 1 heart.")
    print("8. Reach the door ('🚪') with the key to progress to the next level.")
    print("Type 'start' to begin your adventure!")

# Main function to run the game
def main():
    # Displaying game rules and waiting for the user to start
    display_rules()
    command = input("Enter 'start' to begin: ").strip().lower()
    while command != 'start':
        command = input("Invalid command. Please enter 'start' to begin: ").strip().lower()

    # Initializing game parameters for the first level
    max_health = 3
    game_map, player, coins, player_health = initialize_level()
    has_key = False

    # Main game loop
    while True:
        # Displaying player health and map
        print("❤️" * player_health)
        game_map.update_player_position(player.position)
        game_map.display_map()

        # Taking input command from the player
        command = input("Enter a command (move up/down/left/right, inventory, use <item>, quit): ").strip().lower()

        # Handling different commands
        if command.startswith("move "):
            _, direction = command.split(maxsplit=1)
            if direction in ["up", "down", "left", "right"]:
                new_position = player.move(direction)
                if new_position is not None:
                    print(f"Moved to {new_position}")
                    encountered, tile = game_map.check_tile(new_position)
                    if encountered:
                        # Handling encounters with different tiles
                        if tile == "E":
                            print("You encountered a monster! Type 'fight' to engage or 'flee' to retreat.")
                            sub_command = input("Enter command: ").strip().lower()
                            if sub_command == "fight":
                                if random.choice([True, False]):
                                    print("You defeated the monster!")
                                    coins.add(50)
                                    game_map.remove_obstacle(new_position)  # Remove the monster from the map
                                else:
                                    print("You were defeated by the monster!")
                                    player_health -= 1
                                    if player_health <= 0:
                                        print("Game Over")
                                        return
                            elif sub_command == "flee":
                                print("You retreated from the monster.")
                                player.move("down")  # Move player back to previous position
                            else:
                                print("Invalid command. You retreated.")
                        elif tile == "C":
                            print("You found a chest! Type 'open' to open it.")
                            sub_command = input("Enter command: ").strip().lower()
                            if sub_command == "open":
                                if new_position == game_map.key_chest_position:
                                    print("You found the key!")
                                    has_key = True
                                else:
                                    if coins.remove(50):
                                        print("You opened the chest and found a treasure!")
                                        item = game_map.generate_random_item()
                                        player.inventory.add_item(item)
                                    else:
                                        print("Not enough coins to open the chest.")
                                game_map.remove_obstacle(new_position)  # Remove the chest from the map
                            else:
                                print("Invalid command. You moved away from the chest.")
                        elif tile == "I":
                            if random.choice([True, False]):
                                print("You were robbed and lost 1 heart!")
                                player_health -= 1
                                if player_health <= 0:
                                    print("Game Over")
                                    return
                            else:
                                print("You found 50 coins!")
                                coins.add(50)
                            game_map.remove_obstacle(new_position)  # Remove the item from the map
                        elif tile == "🚪":
                            if has_key:
                                print("You unlocked the door and progressed to the next level!")
                                game_map, player, coins, player_health = initialize_level()
                                has_key = False
                            else:
                                print("You need a key to unlock this door.")
                    else:
                        player.position = new_position
        elif command == "inventory":
            items = player.inventory.list_items()
            print("Inventory:", items)
            print("Coins:", coins.amount)
        elif command.startswith("use "):
            _, item = command.split(maxsplit=1)
            if item.lower() == "health potion":
                if "Health Potion" in player.inventory.items:
                    player_health = min(player_health + 3, max_health)
                    player.inventory.remove_item("Health Potion")
                    print("Health potion used. Current health:", player_health)
                else:
                    print("No health potions left.")
            elif item.lower() == "gold coin":
                if "Gold Coin" in player.inventory.items:
                    coins.add(100)
                    player.inventory.remove_item("Gold Coin")
                    print("Gold coin used. 100 coins added.")
                else:
                    print("No gold coins left.")
            elif item.lower() == "silver coin":
                if "Silver Coin" in player.inventory.items:
                    coins.add(50)
                    player.inventory.remove_item("Silver Coin")
                    print("Silver coin used. 50 coins added.")
                else:
                    print("No silver coins left.")
            else:
                player.inventory.remove_item(item)
        elif command == "quit":
            print("Quitting the game.")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()

