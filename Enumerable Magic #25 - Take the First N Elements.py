def take(arr, n):
    return arr[:n]


print(take([0, 1, 2, 3, 5, 8, 13], 3))  # [0, 1, 2], "should return the first 3 items")
print(take([0, 1, 2, 3, 5, 8, 13], 0))  # [], "should return the first 0 items")
print(take([0, 1, 2, 3, 5, 8, 13], 1))  # [0], "should return the first item")
print(take([0, 1, 2, 3, 5, 8, 13], 5))  # [0, 1, 2, 3, 5], "should return the first 5 items")
print(take([0, 1, 2, 3, 5, 8, 13], 7))  # [0, 1, 2, 3, 5, 8, 13], "should return the first 7 items")
print(take([0, 1, 2, 3, 5, 8, 13], 10))  # [0, 1, 2, 3, 5, 8, 13], "should return the first 10 items")