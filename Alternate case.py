def alternate_case(s):
# 1st solution
    res = ''
    for i in range(len(s)):
        if s[i].isupper():
            res += s[i].lower()
        else:
            res += s[i].upper()
    return res

# 2nd solution
    # return s.swapcase()

print(alternate_case("ABC"))                               # "abc"
print(alternate_case(""))                                  # ""
print(alternate_case(" "))                                 # " "
print(alternate_case("Hello World"))                       # "hELLO wORLD"
print(alternate_case("cODEwARS"))                          # "CodeWars"
print(alternate_case("i LIKE MAKING KATAS VERY MUCH"))     # "I like making katas very much"