def min_value(digits):
    sorted_digits = sorted(set(digits))
    return int(''.join(map(str, sorted_digits)))



print(min_value([1, 3, 1]))        # 13
print(min_value([4, 7, 5, 7]))     # 457
print(min_value([4, 8, 1, 4]))     # 148