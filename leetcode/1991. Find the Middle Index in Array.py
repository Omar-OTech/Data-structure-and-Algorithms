class Solution(object):
    def findMiddleIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1






# test code
s = Solution()
print(s.findMiddleIndex([2,3,-1,8,4])) # 3
print(s.findMiddleIndex([1,-1,4])) # 2
print(s.findMiddleIndex([2,5])) # -1
print(s.findMiddleIndex([1])) # 0
