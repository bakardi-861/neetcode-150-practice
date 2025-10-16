class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # greedy: smallest 2 chocolates <= money or return original money if no solution
        # [1,2,1] money = 2
        # [1,1] money = 1 ans = 1 (no sol)
        # sort and return 2 pointers i and i + 1 that are less than money? -> O(nlogn)
        n = len(prices)
        prices.sort()
        cost = prices[0] + prices[1]
        if cost <= money:
            return money - cost
        return money