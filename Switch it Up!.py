def switch_it_up(number):
# 1st solution
    dict = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}
    for key, value in dict.items():
        if value == number:
            return key
        
# 2nd solution
    # return ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][number]


print(switch_it_up(0))    # "Zero"
print(switch_it_up(9))    # "Nine"