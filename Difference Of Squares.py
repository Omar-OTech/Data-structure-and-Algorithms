def difference_of_squares(n):
    return sum(range(1, n+1)) ** 2 - sum([i ** 2 for i in range(1, n+1)])



print(difference_of_squares(5))      # 170, "For n = 5"
print(difference_of_squares(10))     # 2640, "For n = 10"
print(difference_of_squares(100))    # 25164150, "For n = 100"