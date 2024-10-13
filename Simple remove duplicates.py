def solve(arr):
    res = []
    for i in arr[::-1]:
        if i not in res:
            res.append(i)
    return res[::-1]


print(solve([3,4,4,3,6,3]))       # [4,6,3]
print(solve([1,2,1,2,1,2,3]))     # [1,2,3]
print(solve([1,2,3,4]))           # [1,2,3,4]
print(solve([1,1,4,5,1,2,1]))     # [4,5,2,1]