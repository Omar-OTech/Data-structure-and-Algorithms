class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
# test code
s = Solution()
print(s.isPowerOfTwo(1)) # True
print(s.isPowerOfTwo(3)) # False
print(s.isPowerOfTwo(16)) # True
print(s.isPowerOfTwo(218)) # False
print(s.isPowerOfTwo(0)) # False
print(s.isPowerOfTwo(1024)) # True
print(s.isPowerOfTwo(1023)) # False
print(s.isPowerOfTwo(1025)) # False
print(s.isPowerOfTwo(1073741824)) # True
print(s.isPowerOfTwo(1073741823)) # False
print(s.isPowerOfTwo(1073741825)) # False