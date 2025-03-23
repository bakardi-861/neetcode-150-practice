class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x+1
        while l < r:
            mid = (r+l+1)//2
            sqr_mid = mid ** 2
            if sqr_mid <= x:
                l = mid
            else:
                r = mid-1
        return l