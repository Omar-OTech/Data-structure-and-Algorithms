# def isPP(n):
#     for i in range(2, int(n**0.5)+1):
#         power = 2
#         while i**power <= n:
#             if i**power == n:
#                 return [i, power]
#             power += 1
#     return None

# 2nd solution
def isPP(n):
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i**j > n:
                break
            elif i**j == n:
                return [i, j]
    return None

print(isPP(4))    # [2,2], "4 = 2^2"
print(isPP(9))    # [3,2], "9 = 3^2"
print(isPP(5))    # None, "5 isn't a perfect power"
