class Solution:
    def makePalindrome(self, s: str) -> bool:
        # when we have a mismatch, count ops. if count exceeds 2, return false.
        # be able to explain why this works
        l,r = 0,len(s)-1
        count = 0
        while l <= r:
            if s[l] != s[r]:
                count += 1
            if count > 2:
                return False
            l += 1
            r -= 1
        return True