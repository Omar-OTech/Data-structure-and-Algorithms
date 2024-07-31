def cube_checker(volume, side):
    if volume < 0 or side < 0:
        return False
    return volume == side ** 3



# Examples
print(cube_checker(56.3, 3))        # False
print(cube_checker(125, 5))          # True
print(cube_checker(-125, 5))         # False
print(cube_checker(125, -5))         # False
print(cube_checker(0, 0))            # True
print(cube_checker(0, 1))            # False
print(cube_checker(1, 1))            # True
print(cube_checker(1, 0))            # False

