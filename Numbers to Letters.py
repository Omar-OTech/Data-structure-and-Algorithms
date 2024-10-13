def switcher(arr):
    res = ''
    for i in arr:
        if i == '0':
            continue  # Skip '0' as it doesn't correspond to any character
        elif i == '28':
            res += ' '  # '28' corresponds to a space ' '
        elif i == '29':
            res += '?'  # '29' corresponds to a question mark '?'
        elif i == '27':
            res += '!'  # '27' corresponds to an exclamation mark '!'
        else:
            res += chr(27 - int(i) + 96) if 1 <= int(i) <= 26 else ''  # '1' to '26' correspond to 'z' to 'a'
    return res

# Test cases
print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))                    # 'codewars'
print(switcher(['25','7','8','4','14','23','8','25','23','29','16','16','4']))    # 'btswmdsbd?kkw'
print(switcher(['4', '24']))                                                      # 'wc'
print(switcher(['12']))                                                           # 'o'
print(switcher(['12','28','25','21','25','7','11','22','15']))                    # 'o bfbtpel'