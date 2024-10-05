def explode(s):
    res = ''
    for i in s:
        res += i * int(i)
    return res



print(explode('312'))              # '333122'
print(explode('102269'))           #'12222666666999999999'
print(explode('0'))                # ''
print(explode('000'))              # ''
print(explode('123'))              # '122333'