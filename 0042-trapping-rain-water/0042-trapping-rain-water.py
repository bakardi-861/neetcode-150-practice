class Solution:
    def trap(self, h: List[int]) -> int:
        L,R = 0,len(h)-1
        i = 0
        maxL,maxR = h[L],h[R]
        ans = 0
        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(maxL, h[L])
                ans += maxL - h[L]
            else:
                R -= 1
                maxR = max(maxR,h[R])
                ans += maxR - h[R]
        return ans
