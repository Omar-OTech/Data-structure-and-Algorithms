def make_negative( number ):
# 1st solution
    if number == 0:
        return 0
    elif number < 0:
        return number
    else:
        return number * -1
    
# 2nd solution
    # return abs(number) * -1
    # return -abs(number)



print(make_negative(42)) # -42
print(make_negative(-9)) # -9
print(make_negative(0)) # 0
