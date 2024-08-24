def adjacent_element_product(array):
# 1st solution
    res = []
    for i in range(len(array) - 1):
        res.append(array[i] * array[i + 1])
    return max(res)

# 2nd solution
    # return max(a * b for a, b in zip(array, array[1:]))



print(adjacent_element_product([5, 8]))                                          #  40
print(adjacent_element_product([1, 2, 3]))                                       #  6
print(adjacent_element_product([1, 5, 10, 9]))                                   #  90
print(adjacent_element_product([4, 12, 3, 1, 5]))                                #  48
print(adjacent_element_product([5, 1, 2, 3, 1, 4]))                              #  6
print(adjacent_element_product([3, 6, -2, -5, 7, 3]))                            #  21
print(adjacent_element_product([9, 5, 10, 2, 24, -1, -48]))                      #  50
print(adjacent_element_product([5, 6, -4, 2, 3, 2, -23]))                        #  30
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))         #  -14
print(adjacent_element_product([5, 1, 2, 3, 1, 4]))                              #  6
print(adjacent_element_product([1, 0, 1, 0, 1000]))                              #  0
print(adjacent_element_product([1, 2, 3, 0]))                                    #  6