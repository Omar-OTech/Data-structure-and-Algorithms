class solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# test cases
nums = [2,7,11,15]
target = 9
sol = solution()
print(sol.twoSum(nums, target))        # [0, 1]

nums = [3,2,4]
target = 6
sol = solution()
print(sol.twoSum(nums, target))        # [1, 2]

nums = [3,3]
target = 6
sol = solution()
print(sol.twoSum(nums, target))        # [0, 1]

nums = [3,2,3]
target = 6
sol = solution()
print(sol.twoSum(nums, target))        # [0, 2]
