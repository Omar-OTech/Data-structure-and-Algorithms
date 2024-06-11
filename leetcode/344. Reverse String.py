class Solution(object):
    def reverseString(self, s):
# 1st solution
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# 2nd solution
        # for i in range(len(s) // 2):
        #     s[i], s[~i] = s[~i], s[i]

# 3rd solution
        # return s.reverse()



sol = Solution()
s1 = ["h", "e", "l", "l", "o"]
sol.reverseString(s1)
print(s1)  # Output should be: ["o", "l", "l", "e", "h"]
s2 = ["H", "a", "n", "n", "a", "h"]
sol.reverseString(s2)
print(s2)  # Output should be: ["h", "a", "n", "n", "a", "H"]
s3 = ["c", "h", "a", "l", "l", "e", "n", "g", "e", "r"]
sol.reverseString(s3)
print(s3)  # Output should be: ["r", "a", "m", "o"]
