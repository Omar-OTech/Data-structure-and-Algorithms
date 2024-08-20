def merge_arrays(arr1, arr2):
    res = []
    for i in arr1:
        if i not in res:
            res.append(i)
    for i in arr2:
        if i not in res:
            res.append(i)
    return sorted(res)

# 2nd solution
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))


print(merge_arrays([1,2,3,4], [5,6,7,8]))                     # [1,2,3,4,5,6,7,8])
print(merge_arrays([1,3,5,7,9], [10,8,6,4,2]))                # [1,2,3,4,5,6,7,8,9,10])
print(merge_arrays([1,3,5,7,9,11,12], [1,2,3,4,5,10,12]))     # [1,2,3,4,5,7,9,10,11,12])