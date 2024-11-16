def insert_dash(num):
    num = str(num)
    res = ''
    for i in range(len(num)):
        if int(num[i]) % 2 != 0 and i != len(num) - 1 and int(num[i + 1]) % 2 != 0:
            res += num[i] + '-'
        else:
            res += num[i]
    return res


print(insert_dash(454793))      # '4547-9-3')
print(insert_dash(123456))      # '123456')
print(insert_dash(1003567))     # '1003-567')
print(insert_dash(24680))       # '24680')
print(insert_dash(13579))       # '1-3-5-7-9')