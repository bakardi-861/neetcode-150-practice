class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        return self.climb_Stairs(0, n)

    @cache
    def climb_Stairs(self, i: int, n: int) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)