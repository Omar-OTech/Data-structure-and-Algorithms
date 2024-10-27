def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])


# 2nd solution
    # s = s.split(' ')                                                    # split the string into a list of words
    # s = s[::-1]
    # s = ' '.join(s)                                                     # join the list of words into a string
    # res = ""
    # for c in s:
    #     if c.islower():
    #         res += c.upper()
    #     elif c.isupper():
    #         res += c.lower()
    #         res = res + c
    # return res


print(string_transformer("Example string"))                             # "STRING eXAMPLE"
print(string_transformer("Example Input"))                              # "iNPUT eXAMPLE"
print(string_transformer("To be OR not to be That is the Question"))    # "qUESTION THE IS tHAT BE TO NOT or BE tO"
print(string_transformer(""))                                           # ""
print(string_transformer("You Know When  THAT  Hotline Bling"))         # "bLING hOTLINE  that  wHEN kNOW yOU"
print(string_transformer(" A b C d E f G "))                            # " g F e D c B a "