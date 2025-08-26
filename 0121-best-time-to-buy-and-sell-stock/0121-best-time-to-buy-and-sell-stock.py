class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_price=0
        for current in prices:
            if current < min_price:
                min_price=current
            elif current-min_price> max_price:
                max_price= current-min_price
        return max_price   
            

        # profit = prices[r] - prices[l]
        # shrink window when profit is negative
        # otherwise, store max profit
        # return max