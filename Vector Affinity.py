def vector_affinity(a, b):
    if not a and not b:
        return 1.0
    
    max_length = max(len(a), len(b))
    matches = sum(1 for i, j in zip(a, b) if i == j)
    
    return matches / max_length


print(vector_affinity([1,2,3], [1,2,3,4,5]))     # 0.6
print(vector_affinity([1,2,3,4], [1,2,3,5]))     # 0.75
print(vector_affinity([6,6,6,6,6,6], [6]))       # 1.0/6.0
print(vector_affinity([None], [None]))           # 1.0
print(vector_affinity([None], []))               # 0.0
print(vector_affinity([None], [None, None]))     # 0.5
print(vector_affinity([], []))                   # 1.0