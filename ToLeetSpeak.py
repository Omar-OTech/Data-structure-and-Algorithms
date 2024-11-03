def to_leet_speak(str):
    dict = {
    'A' : '@',
    'B' : '8',
    'C' : '(',
    'D' : 'D',
    'E' : '3',
    'F' : 'F',
    'G' : '6',
    'H' : '#',
    'I' : '!',
    'J' : 'J',
    'K' : 'K',
    'L' : '1',
    'M' : 'M',
    'N' : 'N',
    'O' : '0',
    'P' : 'P',
    'Q' : 'Q',
    'R' : 'R',
    'S' : '$',
    'T' : '7',
    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X',
    'Y' : 'Y',
    'Z' : '2'
    }

    for i in dict:
        str = str.replace(i, dict[i])
    return str

# 2nd solution
    # return str.translate(str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72"))

print(to_leet_speak("LEET"))                                          # "1337"
print(to_leet_speak("CODEWARS"))                                      # "0D3W@R$"
print(to_leet_speak("HELLO WORLD"))                                   # "#3110 W0R1D"
print(to_leet_speak("LOREM IPSUM DOLOR SIT AMET"))                    # "10R3M !P$UM D010R $!7 @M37"
print(to_leet_speak("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))   # "7#3 QU!(K 8R0WN F0X JUMP$ 0V3R 7#3 1@2Y D06"