def wave(people):
    res = []
    for i in range(len(people)):
        if people[i] != " ":
            res.append(people[:i] + people[i].upper() + people[i+1:])
    return res


print(wave("hello"))    # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave("codewars")) # ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
print(wave(""))         # []
print(wave("two words"))# ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
print(wave(" gap "))     # [" Gap ", " gAp ", " gaP "]
print(wave("a       b    "))# ["A       b    ", "a       B    "]
print(wave("this is a few words")) # ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"]