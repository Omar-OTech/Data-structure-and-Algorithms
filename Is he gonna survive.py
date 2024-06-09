def hero(bullets, dragons):
# 1st solution
    return True if bullets >= dragons * 2 else False

# 2nd solution
    # return dragons <= bullets / 2


print(hero(10, 5))          # True
print(hero(7, 4))           # False
print(hero(4, 5))           # False
print(hero(100, 40))        # True
print(hero(1500, 751))      # False 
print(hero(0, 1))           # False
print(hero(10, 10))         # False
