def remove_char(s):
# 1st solution
    return s[1:-1]

# 2nd solution
    # return s[1: len(s) - 1]

# 3rd solution
    # res = ''
    # for i in range(1, len(s) - 1):
    #     res += s[i]
    # return res

print(remove_char('eloquent'))        # 'loquen'
print(remove_char('country'))          # 'ountr'
print(remove_char('person'))          # 'erso'
print(remove_char('place'),)          # 'lac'
print(remove_char('ok'))              # ''
print(remove_char('ooopsss'))         # 'oopss'