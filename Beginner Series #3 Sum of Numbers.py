def get_sum(a,b):
    if a == b:
        return a
    low = min(a, b)
    high = max(a, b)
    return sum(range(low, high + 1))



print(get_sum(0, 1))    # 1
print(get_sum(0, -1))   # -1