def tidyNumber(n):
    sorted_n = sorted(str(n))
    return str(n) == ''.join(sorted_n)


print(tidyNumber(12))      # True
print(tidyNumber(102))     # False
print(tidyNumber(9672))    # False
print(tidyNumber(2789))    # True