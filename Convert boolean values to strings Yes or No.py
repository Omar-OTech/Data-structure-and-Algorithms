def bool_to_word(boolean):
# 1st solution
    if boolean == True:
        return 'Yes'
    else:
        return 'No'

# 2nd solution
    # return 'Yes' if boolean else 'No'

print(bool_to_word(True))  # 'Yes'
print(bool_to_word(False)) # 'No'