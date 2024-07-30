def sum_digits(number):
    res = 0
    for i in str(abs(number)):
        res += int(i)
    return res


print(sum_digits(10))              # 1
print(sum_digits(99))              # 18
print(sum_digits(-32))             # 5
print(sum_digits(1234567890))      # 45
print(sum_digits(0))               # 0
print(sum_digits(666))             # 18
print(sum_digits(100000002))       # 3
print(sum_digits(800000009))       # 17