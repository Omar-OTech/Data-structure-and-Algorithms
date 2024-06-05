def square_sum(numbers):
    return sum(num ** 2 for num in numbers)

print(square_sum([1,2]))            # 5
print(square_sum([0, 3, 4, 5]))     # 50
print(square_sum([]))               # 0
print(square_sum([-1,-2]))          # 5
print(square_sum([-1,0,1]))         # 2