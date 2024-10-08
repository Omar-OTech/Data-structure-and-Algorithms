# Defining the Player class with a 'name' attribute
class Player:
    def __init__(self, name):
        self.name = name

# Duck Duck Goose function
def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name  # Access 'name' from Player object

# Example names and creating Player instances
ex_names = ["a", "b", "c", "d", "c", "e", "f", "g", "h", "z"]
players = list(map((lambda x: Player(x)), ex_names))

# Test cases
print(duck_duck_goose(players, 10))  # "z"
print(duck_duck_goose(players, 20))  # "z"
print(duck_duck_goose(players, 30))  # "z"
print(duck_duck_goose(players, 18))  # "g"
print(duck_duck_goose(players, 28))  # "g"
print(duck_duck_goose(players, 12))  # "b"
print(duck_duck_goose(players, 2))   # "b"
print(duck_duck_goose(players, 7))   # "f"