def to_jaden_case(string):
# 1st solution
    res = ''
    setence = string.split()
    for word in setence:
        res += word.capitalize() + ' '
    return res[:-1]


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))    # "How Can Mirrors Be Real If Our Eyes Aren't Real")
print(to_jaden_case("The moment that truth is organized it becomes a lie"))  # "The Moment That Truth Is Organized It Becomes A Lie")