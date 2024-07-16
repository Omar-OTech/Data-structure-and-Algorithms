def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None

    diamond_str = ""
    mid = n // 2

    for i in range(n):
        stars = n - abs(mid - i) * 2
        spaces = abs(mid - i)
        diamond_str += ' ' * spaces + '*' * stars + '\n'

    return diamond_str


print(diamond(1))    #  "*\n"
print(diamond(2))    #  None
print(diamond(3))    #  expected
print(diamond(5))    #  "  *\n ***\n*****\n ***\n  *\n"
print(diamond(0))    #  None
print(diamond(-3))   #  None