def small_enough(array, limit):
# 1st solution
    res = []
    for i in array:
        if i > limit:
            res.append(i)
    if len(res) == 0:
        return True
    else:
        return False

# 2nd solution
    # return max(array) <= limit

print(small_enough([66, 101], 200))                                           # True
print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))              # False
print(small_enough([101, 45, 75, 105, 99, 107], 107))                         # True
print(small_enough([80, 117, 115, 104, 45, 85, 112, 115], 120))               # True
print(small_enough([1, 1, 1, 1, 1, 2], 1))                                    # False
print(small_enough([78, 33, 22, 44, 88, 9, 6], 87))                           # False
print(small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))                          # True
print(small_enough([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 12))     # True
