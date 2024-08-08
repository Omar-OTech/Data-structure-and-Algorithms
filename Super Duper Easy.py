def problem(a):
# 1st solution
    if type(a) == int or type(a) == float:
        return a * 50 + 6
    else:
        return 'Error'

# 2nd solution
    return a * 50 + 6 if type(a) == int or type(0) == float else 'Error'


print(problem("hello"))    # "Error"
print(problem(1))          # 56
