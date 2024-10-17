def jumping_number(number):
    num_str = str(number)
    for i in range(len(num_str) - 1):
        if abs(int(num_str[i]) - int(num_str[i + 1])) != 1:
            return "Not!!"
    return "Jumping!!"


print(jumping_number(1))            # "Jumping!!"
print(jumping_number(7))            # "Jumping!!"
print(jumping_number(9))            # "Jumping!!"
print(jumping_number(23))           # "Jumping!!"
print(jumping_number(32))           # "Jumping!!"
print(jumping_number(79))           # "Not!!"
print(jumping_number(98))           # "Jumping!!"
print(jumping_number(8987))         # "Jumping!!"
print(jumping_number(4343456))      # "Jumping!!"
print(jumping_number(98789876))     # "Jumping!!"
print(jumping_number(987654322))    # "Not!!"