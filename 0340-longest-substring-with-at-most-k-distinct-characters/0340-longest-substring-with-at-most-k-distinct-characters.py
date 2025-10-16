class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        win = Counter()
        l = 0
        res = 0
        for r in range(len(s)):
            win[s[r]] += 1
            while len(win) > k:
                win[s[l]] -= 1
                if not win[s[l]]: del win[s[l]]
                l += 1
            res = max(res, r-l+1)
        return res
