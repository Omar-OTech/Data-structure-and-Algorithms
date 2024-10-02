def sort_by_bit(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))

# Test cases
a = [3, 8, 3, 6, 5, 7, 9, 1]
sort_by_bit(a)
print(a)  # Expected: [1, 8, 3, 3, 5, 6, 9, 7]

b = [9, 4, 5, 3, 5, 7, 2, 56, 8, 2, 6, 8, 0]
sort_by_bit(b)
print(b)  # Expected: [0, 2, 2, 4, 8, 8, 3, 5, 5, 6, 9, 7, 56]
