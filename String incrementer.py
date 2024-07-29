def increment_string(strng):
# 1st solution
    if strng and strng[-1].isdigit():
        num = ''
        for i in range(len(strng) - 1, -1, -1):
            if strng[i].isdigit():
                num = strng[i] + num
            else:
                break
        return strng[:len(strng)-len(num)] + str(int(num) + 1).zfill(len(num))
    else:
        return strng + '1'

# 2nd solution
#     stripped = strng.rstrip('0123456789')
#     num = strng[len(stripped):]
#     if num == "": return strng + "1"
#     return stripped + str(int(num) + 1).zfill(len(num))

print(increment_string("foo"))         # "foo1"
print(increment_string("foobar001"))   # "foobar002"
print(increment_string("foobar1"))     # "foobar2"
print(increment_string("foobar00"))    # "foobar01"
print(increment_string("foobar99"))    # "foobar100"
print(increment_string("foobar099"))   # "foobar100"
print(increment_string("fo99obar99"))  # "fo99obar100"
print(increment_string(""))            # "1"
