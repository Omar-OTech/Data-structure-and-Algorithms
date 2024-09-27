def calc(x):
    total1 = ''.join(str(ord(i)) for i in x)
    total2 = total1.replace('7', '1')
    sum_total1 = sum(int(i) for i in total1)
    sum_total2 = sum(int(i) for i in total2)
    return sum_total1 - sum_total2


print(calc('abcdef'))             # 6
print(calc('ifkhchlhfd'))         # 6
print(calc('aaaaaddddr'))         # 30
print(calc('jfmgklf8hglbe'))      # 6
print(calc('jaam'))               # 12