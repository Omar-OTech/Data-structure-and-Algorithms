class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit



# test code
s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 5
print(s.maxProfit([7,6,4,3,1])) # 0
print(s.maxProfit([1,2])) # 1
print(s.maxProfit([2,1,2,0,1])) # 1
print(s.maxProfit([2,4,1])) # 2
print(s.maxProfit([3,2,6,5,0,3])) # 4
print(s.maxProfit([1,4,2])) # 3
print(s.maxProfit([3,3,5,0,0,3,1,4])) # 4