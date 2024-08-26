class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        res = []
        for i in set(arr):
            res.append(arr.count(i))
        res.sort()
        for i in range(len(res)):
            if k >= res[i]:
                k -= res[i]
                res[i] = 0
            else:
                res[i] -= k
                k = 0
        return len([i for i in res if i > 0])
    
# Test Cases
sol = Solution()
print(sol.findLeastNumOfUniqueInts([5,5,4], 1))        # 1
print(sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))        # 2
print(sol.findLeastNumOfUniqueInts([1], 1))        # 0
print(sol.findLeastNumOfUniqueInts([1,2,3], 3))        # 0
print(sol.findLeastNumOfUniqueInts([1,2,3], 2))        # 1
print(sol.findLeastNumOfUniqueInts([1,2,3], 1))        # 2
print(sol.findLeastNumOfUniqueInts([1,2,3], 0))        # 3
print(sol.findLeastNumOfUniqueInts([1,2,3,4,5], 5))        # 0