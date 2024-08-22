def likes(names):
    res = ''
    if len(names) == 0:
        res = 'no one likes this'
    elif len(names) == 1:
        res = names[0] + ' likes this'
    elif len(names) == 2:
        res = names[0] + ' and ' + names[1] + ' like this'
    elif len(names) == 3:
        res = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        res = names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'
    return res


print(likes([]))                                     # 'no one likes this'
print(likes(['Peter']))                              # 'Peter likes this'
print(likes(['Jacob', 'Alex']))                      # 'Jacob and Alex like this'
print(likes(['Max', 'John', 'Mark']))                # 'Max, John and Mark like this'
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))       # 'Alex, Jacob and 2 others like this'