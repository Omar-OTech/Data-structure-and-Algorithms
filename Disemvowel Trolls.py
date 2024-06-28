def disemvowel(string):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    res = ""
    for i in string:
        if i not in vowel:
            res += i
    return res




print(disemvowel("This website is for losers LOL!"))                                    # "Ths wbst s fr lsrs LL!", 'Incorrect answer for input="This website is for losers LOL!"\n'
print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))    # "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd", 'Incorrect answer for input="No offense but,\nYour writing is among the worst I\'ve ever read"\n'
print(disemvowel("What are you, a communist?"))                                         # "Wht r y,  cmmnst?", 'Incorrect answer for input="What are you, a communist?"\n'