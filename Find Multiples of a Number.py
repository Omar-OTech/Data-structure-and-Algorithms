def find_multiples(integer, limit):
    res = []
    for i in range(integer, limit + 1, integer):
        res.append(i)
    return res

print(find_multiples(5, 25))           # [5, 10, 15, 20, 25]
print(find_multiples(1, 2))            # [1, 2]