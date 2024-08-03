def get_even_numbers(arr):
# 1st solution
    res = []
    for i in arr:
        if i % 2 == 0:
            res.append(i)
    return res

# 2nd solution
    # even_num = lambda x: x % 2 == 0
    # return list(filter(even_num, arr))

print(get_even_numbers([2,4,5,6]))       # [2,4,6], "Returned list is incorrect"
print(get_even_numbers([]))              # [], "Returned list is incorrect"
print(get_even_numbers([1]))             # [], "Returned list is incorrect"
print(get_even_numbers([1,2]))           # [2], "Returned list is incorrect"
print(get_even_numbers([1,2,3,4,5]))     # [2,4], "Returned list is incorrect"
print(get_even_numbers([2,4,6,8]))       # [2,4,6,8], "Returned list is incorrect"