class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l,r,k):
            while l <= r:
                if s[l] != s[r]:
                    if k > 0:
                        return isValid(l+1,r,0) or isValid(l,r-1,0)
                    else:
                        return False
                l += 1
                r -= 1
            return True
        
        return isValid(0,len(s)-1,1)