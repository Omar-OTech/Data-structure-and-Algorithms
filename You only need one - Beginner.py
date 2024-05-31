def check(seq, elem):
# 1st solution
    for i in seq:
        if i == elem:
            return True
    return False

# 2nd solution
    # return elem in seq



print(True, ([66, 101], 66)) # True
print(False, ([78, 117, 110, 99, 104, 117, 107, 115], 8)) # False
print(True, ([101, 45, 75, 105, 99, 107], 107)) # True
print(True, ([80, 117, 115, 104, 45, 85, 112, 115], 45)) # True
print(True, (['t', 'e', 's', 't'], 'e')) # True
print(False, (["what", "a", "great", "kata"], "kat")) # False
print(True, ([66, "codewars", 11, "alex loves pushups"], "alex loves pushups")) # True
print(False, (["come", "on", 110, "2500", 10, '!', 7, 15], "Come")) # False
print(True, (["when's", "the", "next", "Katathon?", 9, 7], "Katathon?")) # True
print(False, ([8, 7, 5, "bored", "of", "writing", "tests", 115], 45)) # False
print(True, (["anyone", "want", "to", "hire", "me?"], "me?")) # True