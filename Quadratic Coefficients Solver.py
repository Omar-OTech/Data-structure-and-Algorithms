def quadratic(x1, x2):
    a = 1
    b = -x1 - x2
    c = x1 * x2
    return a, b, c

print(quadratic(0,1))     # (1, -1, 0)
print(quadratic(4,9))     # (1, -13, 36)
print(quadratic(2,6))     # (1, -8, 12)
print(quadratic(-5,-4))   # (1, 9, 20)
