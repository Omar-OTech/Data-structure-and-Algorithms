def xor(a,b):
# 1st solution
    return a != b

# 2nd solution
    # return a ^ b

# 3rd solution
    # return a is not b

# 4th solution
    # if a == True and b == True:
    #     return False
    # elif a == True or b == True:
    #     return True

print(xor(False, False))   # False, "False xor False == False"
print(xor(True, False))    # True, "True xor False == True"
print(xor(False, True))    # True, "False xor True == True"
print(xor(True, True))     # False, "True xor True == False"