class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l = 0
        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            max_p = max(max_p, profit)
        return max_p

        # prices = [2,1,2,1,0,1,2]
        #                   l
        #                       r
        # profit = 2
        # max_p = 2
