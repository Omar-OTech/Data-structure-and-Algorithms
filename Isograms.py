def is_isogram(string):
# 1st solution
    res = string.lower()
    for i in res:
        if res.count(i) > 1:
            return False
    return True

# 2nd solution
    # res = set(string.lower())
    # if len(res) == len(string):
    #     return True
    # return False


print(is_isogram("Dermatoglyphics")) # True 
print(is_isogram("isogram"))         # True
print(is_isogram("aba"))             # False, "same chars may not be adjacent"
print(is_isogram("moOse"))           # False, "same chars may not be same case"
print(is_isogram("isIsogram"))       # False
print(is_isogram(""))                # True, "an empty string is a valid isogram"