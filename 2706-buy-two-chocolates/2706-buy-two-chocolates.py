class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minimum = min(prices[0],prices[1]) # find min of first two
        second = max(prices[0],prices[1]) # second is the second min, so choose the other one of the first two

        for i in range(2,len(prices)):
            if prices[i] < minimum:
                second = minimum
                minimum = prices[i]
            elif prices[i] < second:
                second = prices[i]

        min_cost = minimum + second

        if min_cost <= money:
            return money - min_cost
        return money