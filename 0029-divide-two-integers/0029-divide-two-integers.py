class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #O (logn) time, O(1) space - optimal solution
        # O(n) time, O(1) space - repeatedly subtract until dividend < divisor.
        d = abs(dividend)
        dv = abs(divisor)
        count = 0
        
        while d >= dv:
            tmp = dv
            multiplier = 1
            while d >= tmp:
                d -= tmp
                count += multiplier

                multiplier += multiplier
                tmp += tmp

        if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
            count = -count
        
        return min(2147483647, max(-2147483648,count))