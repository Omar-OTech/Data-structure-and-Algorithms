class Solution(object):
    def romanToInt(self, s):
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        i = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dict[s[i]] < dict[s[i + 1]]:
                result -= dict[s[i]]
            else:
                result += dict[s[i]]
        return result

# test code
s = Solution()
print(s.romanToInt("III")) # 3
print(s.romanToInt("IV")) # 4
print(s.romanToInt("IX")) # 9
print(s.romanToInt("LVIII")) # 58
