def sum_of_minimums(numbers):
# 1st solution
    res = 0
    for i in numbers:
        res += min(i)
    return res

# 2nd solution
    # return sum(map(min, numbers))

print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))             #9
print(sum_of_minimums([ [11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7]]))   #76