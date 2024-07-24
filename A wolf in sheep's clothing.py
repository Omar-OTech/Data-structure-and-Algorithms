def warn_the_sheep(queue):
    res = 0
    for i in range(len(queue)):
        if queue[-1] == "wolf":
            return "Pls go away and stop eating my sheep"
        elif queue[i] == "wolf":
            res = len(queue) - i - 1
    return f"Oi! Sheep number {res}! You are about to be eaten by a wolf!"

# 2nd solution
    # queue.reverse()
    # wolfnum = queue.index('wolf')
    # if wolfnum == 0:
    #     return 'Pls go away and stop eating my sheep'
    # return f'Oi! Sheep number {wolfnum}! You are about to be eaten by a wolf!'


print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))  # 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))           # 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))           # 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'wolf', 'sheep']))                                               # 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'sheep', 'wolf']))                                               # 'Pls go away and stop eating my sheep')
