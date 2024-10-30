def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return None



# Test code
print(quadrant(1, 2))             # 1
print(quadrant(-1, 2))            # 2
print(quadrant(-1, -2))           # 3
print(quadrant(1, -2))            # 4
print(quadrant(0, 2))             # None
print(quadrant(0, 0))             # None
print(quadrant(1, 0))             # None
print(quadrant(3, 5))             # 1
print(quadrant(-10, 100))         # 2
print(quadrant(-1, -9))           # 3
print(quadrant(19, -56))          # 4