class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0
        profit = 0
        while l < r and r < len(prices):
            if prices[r] < prices[l]:
                min_price = prices[r]
                l = r
            else:
              profit = prices[r] - prices[l]
            max_profit = max(profit,max_profit)
            r += 1
        return max_profit