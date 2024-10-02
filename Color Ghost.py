class Ghost(object):
    res = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = Ghost.res[random.randint(0, 3)]
import random

# Test Cases
ghosts = [Ghost().color for _ in range(100)]
print(ghosts.count("white") >= 1)
print(ghosts.count("yellow") >= 1)
print(ghosts.count("purple") >= 1)
print(ghosts.count("red") >= 1)