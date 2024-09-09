def reverse(lst):
    empty_list = list()
    for _ in range(len(lst)):
        empty_list.append(lst.pop())
    return empty_list


print(reverse(list([1,2,3]))) # [3,2,1]
print(reverse(list([1,2,3,4]))) # [4,3,2,1]
print(reverse(list([1,None,14,"two"]))) # ["two",14,None,1]