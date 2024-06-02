def invert(lst):
# 1st solution
    return [i * -1 for i in lst]

# 2nd solution
    # res = []
    # for i in lst:
    #     res.append(i * -1)
    # return res

print(invert([1,2,3,4,5]))    # [-1,-2,-3,-4,-5]
print(invert([1,-2,3,-4,5]))  # [-1,2,-3,4,-5]
print(invert([]))             # []
