def _all(seq, fun):
    return all(fun(x) for x in seq)

def greater_than_9(x):
    return x > 9

def less_than_9(x):
    return x < 9

print(_all((1, 2, 3, 4, 5), greater_than_9)) # False
print(_all((1, 2, 3, 4, 5), less_than_9))    # True