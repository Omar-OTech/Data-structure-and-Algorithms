def spacify(string):
    return ''.join([i + ' ' for i in string])[:-1]

# 2nd solution
    # return ' '.join(string)


print(spacify("hello world"))     # "h e l l o   w o r l d"
print(spacify("12345"))           # "1 2 3 4 5"
print(spacify("Pippi"))           # "P i p p i"
print(spacify("a"))               # "a"
print(spacify(""))                # ""