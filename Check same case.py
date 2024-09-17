def same_case(a, b):
    lower_case = {'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'y', 'v', 'w', 'x', 'y', 'z'}
    upper_case = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T', 'Y', 'V', 'W', 'X', 'Y', 'Z'}
    if a in lower_case and b in lower_case:
        return 1
    elif a in upper_case and b in upper_case:
        return 1
    elif a in lower_case and b in upper_case:
        return 0
    elif a in upper_case and b in lower_case:
        return 0
    else:
        return -1
    
# 2nd solution
# def same_case(a, b):
#     if a.islower() and b.islower():
#         return 1
#     elif a.isupper() and b.isupper():
#         return 1
#     elif a.islower() and b.isupper():
#         return 0
#     elif a.isupper() and b.islower():
#         return 0
#     else:
#         return -1


print(same_case('C', 'B'))     # 1
print(same_case('b', 'a'))     # 1
print(same_case('d', 'd'))     # 1
print(same_case('A', 's'))     # 0
print(same_case('c', 'B'))     # 0
print(same_case('b', 'Z'))     # 0
print(same_case('\t', 'Z'))    # -1
print(same_case('H', ':'))     # -1