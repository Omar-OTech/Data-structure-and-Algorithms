def set_alarm(employed, vacation):
# 1st solution
    if employed == True and vacation == False:
        return True
    else:
        return False

# 2nd solution
    # return employed and not vacation

print(set_alarm(True, True))      # False, "Fails when input is True, True"
print(set_alarm(False, True))     # False, "Fails when input is False, True"
print(set_alarm(False, False))    # False, "Fails when input is False, False"
print(set_alarm(True, False))     # True, "Fails when input is True, False"