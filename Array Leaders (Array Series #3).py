def array_leaders(numbers):
    res = []
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i+1:]):
            res.append(numbers[i])
    return res



print(array_leaders([1,2,3,4,0]))        # [4]
print(array_leaders([16,17,4,3,5,2]))    # [17,5,2]
print(array_leaders([-1,-29,-26,-2]))    # [-1]
print(array_leaders([-36,-12,-27]))      # [-36,-12]
print(array_leaders([5,2]))              # [5,2]
print(array_leaders([0,-1,-29,3,2]))     # [0,-1,3,2]