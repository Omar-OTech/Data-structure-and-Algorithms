import math

def square_area(A):
    radius = (2 * A) / math.pi
    side_length = radius
    area = side_length ** 2
    return round(area, 2)

print(square_area(2))          # 1.62
print(square_area(0))          # 0
print(square_area(14.05))      # 80
print(square_area(1))          # 0.41
print(square_area(100))        # 4052.85