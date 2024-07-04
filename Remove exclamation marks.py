def remove_exclamation_marks(s):
# 1st solution
    res = ""
    for i in s:
        if i != "!":
            res += i
    return res

# 2nd solution
    # return s.replace("!", "")

print(remove_exclamation_marks("Hello World!"))      # "Hello World"
print(remove_exclamation_marks("Hello World!!!"))    # "Hello World"
print(remove_exclamation_marks("Hi! Hello!"))        # "Hi Hello"
print(remove_exclamation_marks(""))                  # ""
print(remove_exclamation_marks("Oh, no!!!"))         # "Oh, no"