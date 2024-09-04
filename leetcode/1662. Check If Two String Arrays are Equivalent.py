class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)
    

# test code
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(Solution().arrayStringsAreEqual(word1, word2)) # True
word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(Solution().arrayStringsAreEqual(word1, word2)) # False
word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(Solution().arrayStringsAreEqual(word1, word2)) # True
word1 = ["abc", "d", "defg"]
word2 = ["abcddef"]
print(Solution().arrayStringsAreEqual(word1, word2)) # False
word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(Solution().arrayStringsAreEqual(word1, word2)) # True