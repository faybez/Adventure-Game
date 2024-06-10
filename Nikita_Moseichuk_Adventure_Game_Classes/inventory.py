# Nikita Moseichuk - Inventory Class
# Represents the player's inventory in the game.

class Inventory:
    def __init__(self):
        # Initialize the inventory with an empty list of items
        self.items = []

    def add_item(self, item):
        # Method to add an item to the inventory
        self.items.append(item)  # Append the item to the list of items in the inventory
        print(f"{item} added to inventory.")  # Print a message indicating the item was added

    def remove_item(self, item):
        # Method to remove an item from the inventory
        if item in self.items:  # Check if the item is in the inventory
            self.items.remove(item)  # Remove the item from the list of items
            print(f"{item} removed from inventory.")  # Print a message indicating the item was removed
        else:
            print(f"{item} not found in inventory.")  # Print a message indicating the item was not found

    def list_items(self):
        # Method to list all items in the inventory
        return self.items  # Return the list of items in the inventory


# Nikita Moseichuk - Coin Class
# Represents a coin object in the game.

class Coin:
    def __init__(self):
        # Initialize the coin object with an amount of 0
        self.amount = 0

    def add(self, amount):
        # Method to add coins to the coin object
        self.amount += amount  # Add the specified amount to the current amount of coins
        print(f"Received {amount} coins.")  # Print a message indicating the amount of coins received

    def remove(self, amount):
        # Method to remove coins from the coin object
        if self.amount >= amount:  # Check if there are enough coins to remove
            self.amount -= amount  # Subtract the specified amount from the current amount of coins
            print(f"Spent {amount} coins.")  # Print a message indicating the amount of coins spent
            return True  # Return True indicating successful removal of coins
        else:
            print("Not enough coins.")  # Print a message indicating there are not enough coins
            return False  # Return False indicating unsuccessful removal of coins
