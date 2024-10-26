def balanced_num(number):
    num_str = str(number)
    l = len(num_str)
    if l == 1:
        return "Balanced"
    # Find the middle index
    if l % 2 == 0:
        mid_right = l // 2
        mid_left = mid_right - 1
    else:
        mid_left = l // 2
        mid_right = mid_left
# Calculate the sum of the left part and right part
    left_sum = sum(int(num_str[i]) for i in range(mid_left))
    right_sum = sum(int(num_str[i]) for i in range(mid_right + 1, l))
    
    return "Balanced" if left_sum == right_sum else "Not Balanced"


print(balanced_num(7))          #  "Balanced"
print(balanced_num(959))        #  "Balanced"
print(balanced_num(13))         #  "Balanced"
print(balanced_num(432))        #  "Not Balanced"
print(balanced_num(424))        #  "Balanced"
print(balanced_num(1024))       #  "Not Balanced"
print(balanced_num(66545))      #  "Not Balanced"
print(balanced_num(295591))     #  "Not Balanced"
print(balanced_num(1230987))    #  "Not Balanced"
print(balanced_num(56239814))   #  "Balanced"