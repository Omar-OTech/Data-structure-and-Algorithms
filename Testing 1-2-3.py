def number(lines):
    for i in range(len(lines)):
        lines[i] = str(i + 1 ) + ": " + lines[i]
    return lines



print(number([]))                            # []
print((number(["a", "b", "c"])))              # ["1: a", "2: b", "3: c"])