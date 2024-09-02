def cube_odd(arr):
    # Check if all elements in the list are integers
    if not all(isinstance(x, int) for x in arr):
        return None
    
    # Sum the cubes of odd integers
    return sum(x**3 for x in arr if x % 2 != 0)

# Test cases
print(cube_odd([1, 2, 3, 4]))            # 28 (1^3 + 3^3 = 1 + 27 = 28)
print(cube_odd([-3, -2, 2, 3]))          # 0 (-3^3 + 3^3 = -27 + 27 = 0)
print(cube_odd(["a", 12, 9, "z", 42]))   # None (contains non-integer values)
