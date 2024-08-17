def mango(quantity, price):
    return price * (quantity - quantity // 3)

print(mango(2, 3))   # 6
print(mango(9, 5))   # 30
print(mango(5, 3))   # 15
print(mango(10, 5))  # 30
print(mango(3, 3))   # 36