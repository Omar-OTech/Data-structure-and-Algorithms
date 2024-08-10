def nearest_sq(n):
    return round(n ** 0.5) ** 2


print(nearest_sq(1))           # 1
print(nearest_sq(2))           # 1
print(nearest_sq(10))          # 9
print(nearest_sq(111))         # 121
print(nearest_sq(9999))        # 10000