def to_binary(n):
# 1st solution
    return int(bin(n)[2:])

# 2nd solution
    # return int(f'{n:b}')


print(to_binary(1))    # 1
print(to_binary(2))    # 10
print(to_binary(3))    # 11
print(to_binary(5))    # 101