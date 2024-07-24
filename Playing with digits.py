def dig_pow(n, p):
    res = 0
    for j in str(n):
        res += int(j) ** p
        p += 1
        if res % n == 0:
            return res // n
    return -1



print(dig_pow(89, 1))      # 1
print(dig_pow(92, 1))      # -1
print(dig_pow(46288, 3))   # 51
print(dig_pow(41, 5))      # 25
print(dig_pow(114, 3))     # 9
print(dig_pow(8, 3))       # 64