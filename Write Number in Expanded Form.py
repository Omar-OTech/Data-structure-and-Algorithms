def expanded_form(num):
    num = str(num)
    num = num[::-1]
    result = []
    for i in range(len(num)):
        if num[i] != '0':
            result.append(num[i] + '0'*i)
    return ' + '.join(result[::-1])

print(expanded_form(12))          # '10 + 2'
print(expanded_form(42))          # '40 + 2'
print(expanded_form(70304))       # '70000 + 300 + 4'