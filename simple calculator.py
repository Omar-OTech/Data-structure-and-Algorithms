def calculator(x,y,op):
    if type(x) != int or type(y) != int:
        return 'unknown value'
    elif op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return 'unknown value'

print(calculator(6, 2, '+'))      # 8
print(calculator(4, 3, '-'))      # 1
print(calculator(5, 5, '*'))      # 25
print(calculator(5, 4, '/'))      # 1.25
print(calculator(6, 2, '&'))      # "unknown value"