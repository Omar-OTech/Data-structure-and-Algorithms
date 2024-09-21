def vector_affinity(a, b):
    if len(a) == 0 and len(b) == 0:
        return 1.0
    if len(a) == 0 or len(b) == 0:
        return 0.0
    if len(a) > len(b):
        a, b = b, a
    return sum([1 if a[i] == b[i] else 0 for i in range(len(a))]) / len(b)


print(vector_affinity([1,2,3], [1,2,3,4,5]))     # 0.6
print(vector_affinity([1,2,3,4], [1,2,3,5]))     # 0.75
print(vector_affinity([6,6,6,6,6,6], [6]))       # 1.0/6.0
print(vector_affinity([None], [None]))           # 1.0
print(vector_affinity([None], []))               # 0.0
print(vector_affinity([None], [None, None]))     # 0.5
print(vector_affinity([], []))                   # 1.0