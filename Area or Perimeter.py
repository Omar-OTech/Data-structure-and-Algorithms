def area_or_perimeter(l , w):
# 1st solution
    if l == w:
        return l * w
    else:
        return 2 * (l + w)

# 2nd solution
    # return l * w if l == w else 2 * (l + w)

print(area_or_perimeter(4, 4))    # 16
print(area_or_perimeter(6, 10))   # 32