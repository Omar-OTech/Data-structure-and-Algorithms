def pythagorean_triple(integers):
    integers.sort()
    return integers[0]**2 + integers[1]**2 == integers[2]**2

# second solution
    # a, b, c = sorted(integers)
    # return a**2 + b**2 == c**2



print(pythagorean_triple([3,4,5]))   # True, "Returned solution incorrect - [3,4,5] can form a Pythagorean Triple: 3**2 + 4**2 == 5**2")
print(pythagorean_triple([5,3,4]))   # True, "Returned solution incorrect - [5,3,4] can form a Pythagorean Triple: 3**2 + 4**2 == 5**2")
print(pythagorean_triple([13,12,5]))   # True, "Returned solution incorrect - [13,12,5] can form a Pythagorean Triple: 5**2 + 12**2 == 13**2")
print(pythagorean_triple([100,3,999]))   # False, "Returned solution incorrect - there is no way to form a Pythagorean Triple using [100,3,999]")