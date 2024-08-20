def show_sequence(n):
    res = 0
    if n == 0:
        return '0=0'
    elif n < 0:
        return f"{n}<0"
    else:
        for i in range(n + 1):
            res += i
        return '+'.join([str(i) for i in range(n + 1)]) + f" = {res}"
        
        
print(show_sequence(6))    # "0+1+2+3+4+5+6 = 21"),
print(show_sequence(7))    # "0+1+2+3+4+5+6+7 = 28"),
print(show_sequence(-1))   # "-1<0"), 
print(show_sequence(-10))  # "-10<0"),