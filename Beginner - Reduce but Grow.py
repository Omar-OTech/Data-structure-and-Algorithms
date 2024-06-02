def grow(arr):
    res = 1
    for i in arr:
        res *= i
    return res



print(grow([1, 2, 3])) # 6
print(grow([4, 1, 1, 1, 4])) # 16
print(grow([2, 2, 2, 2, 2, 2])) # 64
print(grow([1, 2, 3, 4])) # 24
print(grow([1, 2, 3, 4, 5])) # 120
print(grow([10])) # 10
print(grow([1, 1, 1, 1])) # 1