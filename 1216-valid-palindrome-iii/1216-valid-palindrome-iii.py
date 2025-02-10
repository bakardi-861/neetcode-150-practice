class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}
        def isValid(l,r,k):
            if (l,r,k) in memo:
                return memo[(l,r,k)]

            while l <= r: 
                if s[l] != s[r]:
                    if not k:
                        memo[(l,r,k)] = False
                    else:
                        memo[(l,r,k)] = isValid(l+1,r,k-1) or isValid(l,r-1,k-1)
                    return memo[(l,r,k)]
                
                l += 1
                r -= 1
            return True

        return isValid(0,len(s)-1,k)