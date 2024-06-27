def make_upper_case(s):
# 1t solution
    return s.upper()

# 2nd solution
    # return ''.join(i.capitalize() for i in s)

# 3rd solution
    # split_word = list(s)
    # for i in range(len(split_word)):
    #     if ord(split_word[i]) >= 97 and ord(split_word[i]) <= 122:
    #         split_word[i] = chr(ord(split_word[i]) - 32)
    # return ''.join(split_word)

print(make_upper_case("hello"))          # "HELLO"