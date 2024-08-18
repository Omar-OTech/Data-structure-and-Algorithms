def find_difference(a, b):
# 1st solution
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])

# 2nd solution
    # return abs(prod(a) - prod(b))

print(find_difference([3, 2, 5], [1, 4, 4]))      # 14, "{0} should equal 14".format(find_difference([3, 2, 5], [1, 4, 4])))
print(find_difference([9, 7, 2], [5, 2, 2]))      # 106, "{0} should equal 106".format(find_difference([9, 7, 2], [5, 2, 2])))