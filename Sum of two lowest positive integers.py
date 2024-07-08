def sum_two_smallest_numbers(numbers):
# 1st solution
    return sum(sorted(numbers)[:2])


# 2nd solution
    # numbers.sort()
    # return numbers[0] + numbers[1]


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))    #   13
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))   #   19
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))  #   30