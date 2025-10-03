class Solution:
    def isPalindrome(self, s: str) -> bool:
        # skip all non alpha characters
        l,r = 0,len(s)-1
        while l <= r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > -1 and not s[r].isalnum():
                r -= 1
            
            if l <= r and s[r].lower() != s[l].lower():
                return False

            l += 1
            r -= 1
        return True