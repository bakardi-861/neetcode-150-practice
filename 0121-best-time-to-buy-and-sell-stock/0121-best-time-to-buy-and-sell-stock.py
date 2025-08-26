class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [7,1,5,3,6,4]
        #             l
        #                     r
        # profit = 3
        # max = 5

        l = 0
        max_profit = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]

            if profit < 0:
                l = r
            max_profit = max(profit,max_profit)
        return max_profit
            

        # profit = prices[r] - prices[l]
        # shrink window when profit is negative
        # otherwise, store max profit
        # return max