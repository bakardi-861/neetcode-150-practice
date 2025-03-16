class Solution:
    def makePalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        ops = 0
        while l <= r:
            if s[l] != s[r]:
                if ops < 2: # must perform at least one op
                    ops += 1
                    # simulate s[l] == s[r]
                else:
                    return False
            l += 1
            r -= 1
        return True