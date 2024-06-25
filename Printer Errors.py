def printer_error(s):
    length = len(s)
    error = 0
    for i in s:
        if i not in "abcdefghijklm":
            error += 1
    return f"{error}/{length}"


s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))                 # "3/56"
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))                 # "6/60"
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
print(printer_error(s))                 # "11/65"