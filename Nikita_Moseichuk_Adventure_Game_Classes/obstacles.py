# Nikita Moseichuk - Obstacle Class
# Represents an obstacle on the game map.

class Obstacle:
    def __init__(self, name, position):
        # Initialize the obstacle with a name and position
        self.name = name
        self.position = position

    def __str__(self):
        # Method to return a string representation of the obstacle
        return f"{self.name} at {self.position}"  # Returns the name and position of the obstacle as a string


# Chest Class (Inherits from Obstacle)
# Represents a chest obstacle on the game map.

class Chest(Obstacle):
    def __init__(self, position):
        # Initialize the chest with a position
        super().__init__("Chest", position)  # Call the superclass constructor with the name "Chest"

# MonsterObstacle Class (Inherits from Obstacle)
# Represents a monster obstacle on the game map.

class MonsterObstacle(Obstacle):
    def __init__(self, monster_type, position):
        # Initialize the monster obstacle with a monster type and position
        super().__init__(monster_type, position)  # Call the superclass constructor with the provided monster type
