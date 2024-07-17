def combat(health, damage):
    if health - damage <= 0:
        return 0
    else:
        return health - damage
    
# 2nd solution
#     return max(0, health - damage)

print(combat(100, 5))  #  95
print(combat(83, 16))  #  67
print(combat(20, 30))  #  0