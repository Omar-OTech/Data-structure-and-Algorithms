def persistence(n):
    count = 0
    while n >= 10:
        n = eval('*'.join(str(n)))
        count += 1
    return count
    


print(persistence(39))     # 3
print(persistence(4))      # 0
print(persistence(25))     # 2
print(persistence(999))    # 4