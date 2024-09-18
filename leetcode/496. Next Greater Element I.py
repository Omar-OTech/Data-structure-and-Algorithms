class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []
        
        # Traverse through nums2 to build the next greater mapping
        for num in nums2:
            # Pop from the stack and map the next greater element
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # If there are elements left in the stack, they have no next greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Return the result for nums1 by looking up the values in the next_greater dictionary
        return [next_greater[num] for num in nums1]


# Instantiate the Solution class
solution = Solution()

# Test Case 1:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
expected_output = [-1, 3, -1]
output = solution.nextGreaterElement(nums1, nums2)
assert output == expected_output, f"Test Case 1 Failed: Expected {expected_output}, but got {output}"

# Test Case 2:
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
expected_output = [3, -1]
output = solution.nextGreaterElement(nums1, nums2)
assert output == expected_output, f"Test Case 2 Failed: Expected {expected_output}, but got {output}"

# Test Case 3: (Edge Case with only one element)
nums1 = [1]
nums2 = [1]
expected_output = [-1]
output = solution.nextGreaterElement(nums1, nums2)
assert output == expected_output, f"Test Case 3 Failed: Expected {expected_output}, but got {output}"

# Test Case 5: (Every number has a next greater element)
nums1 = [2, 3]
nums2 = [1, 2, 3, 4]
expected_output = [3, 4]
output = solution.nextGreaterElement(nums1, nums2)
assert output == expected_output, f"Test Case 5 Failed: Expected {expected_output}, but got {output}"

print("All test cases passed!")
