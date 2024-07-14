def two_sum(numbers, target):
# 1st solution
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target:
    #             return ( i, j ) or (j, i)

    #   numbers            target   valid results
print(two_sum([1 ,2, 3],            4))    #  ((0,2), (2,0)
print(two_sum([1234,5678,9012], 14690))    # ((1,2), (2,1)
print(two_sum([2, 2, 3],            4))    # ((0,1), (1,0)
