
def get_number_from_string(st):
    return int(''.join([i for i in st if i.isdigit()]))


print(get_number_from_string("1",))                                                    # 1
print(get_number_from_string("123",))                                                  # 123
print(get_number_from_string("this is number: 7",))                                    # 7
print(get_number_from_string("$100 000 000",))                                         # 100000000
print(get_number_from_string("hell5o wor6ld",))                                        # 56
print(get_number_from_string("one1 two2 three3 four4 five5",))                         # 12345