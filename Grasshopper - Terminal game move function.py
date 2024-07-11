def move(position, roll):
    return ( roll * 2 ) + position 

print(move(0, 4))  #  8
print(move(3, 6))  #  15
print(move(2, 5))  #  12