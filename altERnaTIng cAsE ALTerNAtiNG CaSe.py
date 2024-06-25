def to_alternating_case(string):
# 1st solution
    res = ""
    for i in string:
        if i.isupper():
            res += i.lower()
        else:
            res += i.upper()
    return res


# 2nd solution
    # return string.swapcase()

print(to_alternating_case("hello world"))                               # "HELLO WORLD"
print(to_alternating_case("HELLO WORLD"))                               # "hello world"
print(to_alternating_case("hello WORLD"))                               # "HELLO world"
print(to_alternating_case("HeLLo WoRLD"))                               # "hEllO wOrld"
print(to_alternating_case("12345"))                                     # "12345"
print(to_alternating_case("1a2b3c4d5e"))                                # "1A2B3C4D5E"
print(to_alternating_case("String.prototype.toAlternatingCase"))        # "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
print(to_alternating_case(to_alternating_case("Hello World")))          # "Hello World"