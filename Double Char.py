def double_char(s):
    res = ''
    for i in range(len(s)):
        res += s[i] * 2
    return res


print(double_char("String"))         #"SSttrriinngg"
print(double_char("Hello World"))    #"HHeelllloo  WWoorrlldd"
print(double_char("1234!_ "))        #"11223344!!__  "