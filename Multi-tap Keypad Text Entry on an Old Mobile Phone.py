def presses(phrase):
    buttons = ["1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7", "TUV8", "WXYZ9", "*", " 0", "#"]
    total = 0
    for char in phrase.upper():
        for button in buttons:
            if char in button:
                total += button.index(char) + 1
    return total


print(presses("LOL"))        # 9
print(presses("HOW R U"))    # 13