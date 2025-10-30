class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one,two = cost[1],cost[0]

        for i in range(2,n):
            curr = cost[i] + min(one,two)
            two,one = one,curr
        return min(one,two)