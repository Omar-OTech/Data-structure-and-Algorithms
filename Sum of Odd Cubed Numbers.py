def cube_odd(arr):
    for i in arr:
        if type(i) != int:
            return None
    # Cube odd numbers and sum them
    return sum([i**3 for i in arr if i % 2 != 0])


# Test cases
print(cube_odd([1, 2, 3, 4]))            # 28 (1^3 + 3^3 = 1 + 27 = 28)
print(cube_odd([-3, -2, 2, 3]))          # 0 (-3^3 + 3^3 = -27 + 27 = 0)
print(cube_odd(["a", 12, 9, "z", 42]))   # None (contains non-integer values)
