def duplicate_encode(word):
    word = word.lower()
    res = ''
    for i in word:
        if word.count(i) > 1:
            res += ")"
        else:
            res += "("
    return res



print(duplicate_encode("din"))       # "((("
print(duplicate_encode("recede"))    # "()()()"
print(duplicate_encode("Success"))   # ")())())","should ignore case"
print(duplicate_encode("(( @"))      # "))(("