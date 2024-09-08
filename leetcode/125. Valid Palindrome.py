import re

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
        



# test code
# Example usage:
sol = Solution()

# Example 1
s1 = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s1))  # Output: True

# Example 2
s2 = "race a car"
print(sol.isPalindrome(s2))  # Output: False

# Example 3
s3 = " "
print(sol.isPalindrome(s3))  # Output: True