def is_uppercase(inp):
# 1st solution
    return not any(char.islower() for char in inp)

# 2nd solution
    # return inp == inp.upper()


print("c")                   #  False
print("C")                   #  True
print("hello I AM DONALD")   #  False
print("HELLO I AM DONALD")   #  True
print("$%&")                 #  True