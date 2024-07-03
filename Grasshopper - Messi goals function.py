def goals(laLiga, copaDelRey, championsLeague):
    res = laLiga + copaDelRey + championsLeague
    return res

# 2nd solution
    # return sum([laLiga, copaDelRey, championsLeague])

# 3rd solution
def goals(*args):
    return sum(args)


print(goals(0, 0, 0))       # 0
print(goals(1, 2, 3))       # 6
print(goals(43, 10, 5))     # 58
print(goals(5, 10, 2))      # 17