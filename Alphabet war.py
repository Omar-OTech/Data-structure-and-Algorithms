def alphabet_war(fight):
    left_side = {"s": 1, "b": 2, "p": 3, "w": 4}
    right_side = {"z": 1, "d": 2, "q": 3, "m": 4}
    
    left_score = 0
    right_score = 0
    
    for i in fight:
        if i in left_side:
            left_score += left_side[i]
        elif i in right_side:
            right_score += right_side[i]
    
    if left_score > right_score:
        return "Left side wins!"
    elif left_score < right_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"


print(alphabet_war("z"))            # "Right side wins!"
print(alphabet_war("zdqmwpbs"))     # "Let's fight again!"
print(alphabet_war("wq"))           # "Left side wins!"
print(alphabet_war("zzzzs"))        # "Right side wins!"
print(alphabet_war("wwwwww"))       # "Left side wins!"