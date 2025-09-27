class Solution:
    def mySqrt(self, x: int) -> int:
        # search range from 1-x, implicitly sorted

        # 1,2,3,4,5 ,6,7,8,9
        # m
        # l
        #   r

        l,r = 0,x+1 # +1 to include x since x could be a sqrt of itself
        while l < r:
            mid = (r+l+1) // 2
            if mid * mid > x:
                r = mid - 1
            else:
                l = mid
        return l