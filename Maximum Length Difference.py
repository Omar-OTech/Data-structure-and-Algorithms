def mxdiflg(a1, a2):
# 1st solution
    if len(a1) == 0 or len(a2) == 0:
        return -1
    else:
        return max([abs(len(x) - len(y)) for x in a1 for y in a2])

# 2nd solution
    # if not a1 or not a2: return -1
    
    # max_a1 = max([len(x) for x in a1])
    # min_a1 = min([len(x) for x in a1])
    
    # max_a2 = max([len(x) for x in a2])
    # min_a2 = min([len(x) for x in a2])
    
    # return max(max_a1 - min_a2, max_a2 - min_a1)


s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))   # 13)
s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
s2 = ["bbbaaayddqbbrrrv"]
print(mxdiflg(s1, s2))   # 10)
s2 = []
s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))   # -1) 