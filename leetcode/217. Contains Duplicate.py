from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Test cases
nums = [1, 2, 3, 1]
s = Solution()
print(s.containsDuplicate(nums))  # True

nums = [1, 2, 3, 4]
s = Solution()
print(s.containsDuplicate(nums))  # False