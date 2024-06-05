def digitize(n):
# 1st solution
    res = []
    for i in str(n):
        res.append(int(i))
    return res[::-1]


# 2nd solution
    # return [int(i) for i in reversed(str(n))]



print(digitize(35231))                 # [1,3,2,5,3]
print(digitize(0))                     # [0]
print(digitize(23582357))              # [7,5,3,2,8,5,3,2]
print(digitize(984764738))             # [8,3,7,4,6,7,4,8,9]
print(digitize(45762893920))           # [0,2,9,3,9,8,2,6,7,5,4]
print(digitize(548702838394))          # [4,9,3,8,3,8,2,0,7,8,4,5]