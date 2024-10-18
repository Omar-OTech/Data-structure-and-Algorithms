def name_value(my_list):
    res = []
    for i in range(len(my_list)):
        value = 0
        for letter in my_list[i].replace(' ', ''):
            if letter.isalpha(): 
                value += ord(letter) - 96
        res.append(value * (i + 1))
    return res


print(name_value(["codewars","abc","xyz"]))             # [88,12,225]
print(name_value(["abc abc","abc abc","abc","abc"]))    # [12,24,18,24]