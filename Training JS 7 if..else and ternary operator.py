def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    else:
        return n * 90



print(sale_hotdogs(0))     #  0
print(sale_hotdogs(1))     #  100
print(sale_hotdogs(2))     #  200
print(sale_hotdogs(3))     #  300
print(sale_hotdogs(4))     #  400
print(sale_hotdogs(5))     #  475
print(sale_hotdogs(9))     #  855
print(sale_hotdogs(10))    #  900
print(sale_hotdogs(11))    #  990
print(sale_hotdogs(100))   #  9000