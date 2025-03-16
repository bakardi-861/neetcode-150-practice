class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}
        def isValid(l,r,k):
            # RECURSION + MEMO
            if (l,r,k) in memo:
                return memo[(l,r,k)]

            while l < r: # bc we need 2 characters to choose to remove
                if s[l] != s[r]:
                    if k > 0:
                        # choose one character to remove on either side
                        memo[(l,r,k)] = isValid(l+1,r,k-1) or isValid(l,r-1,k-1)
                    else: # k == 0, so can't remove anymore characters
                        memo[(l,r,k)] = False
                    return memo[(l,r,k)]
                l += 1
                r -= 1
            return True

        return isValid(0,len(s)-1,k)
