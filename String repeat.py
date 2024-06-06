def repeat_str(repeat, string):
# 1st solution
    res = ''
    for i in range(repeat):
        res += string
    return res

# 2nd solution
    # return repeat * string

print(repeat_str(4, 'a'))         # 'aaaa')
print(repeat_str(3, 'hello '))    # 'hello hello hello ')
print(repeat_str(2, 'abc'))       # 'abcabc')