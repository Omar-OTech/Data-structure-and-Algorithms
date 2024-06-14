def count(s):
    res = {}
    for j in s:
        if j in res:
            res[j] += 1
        else:
            res[j] = 1
    return res

print(count('aba'))          # {'a': 2, 'b': 1}
print(count(''))             # {}
print(count('aa'))           # {'a' : 2}
print(count('aabb'))         # {'b' : 2, 'a' : 2}