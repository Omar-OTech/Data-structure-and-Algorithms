def remove_smallest(numbers):
    if not numbers:
        return []
    new_arr = numbers[:]
    new_arr.remove(min(numbers))
    return new_arr


print(remove_smallest([1, 2, 3, 4, 5]))        # [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]"
print(remove_smallest([5, 3, 2, 1, 4]))        # [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]"
print(remove_smallest([1, 2, 3, 1, 1]))        # [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]"
print(remove_smallest([]))                     # [], "Wrong result for []"