def square_digits(num):
    splited = [int(i) for i in str(num)]
    res = ''
    for i in splited:
        res += str(i ** 2)
    return int(res)








print(square_digits(9119))  # 811181
print(square_digits(0))     # 0