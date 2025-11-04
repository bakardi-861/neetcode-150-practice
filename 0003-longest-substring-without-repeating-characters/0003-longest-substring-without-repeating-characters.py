class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = Counter()
        l = 0
        longest = 0
        for r in range(len(s)):
            win[s[r]] += 1
            while win[s[r]] > 1:
                win[s[l]] -= 1
                if win[s[l]] == 0:
                    del win[s[l]]
                l += 1
            
            longest = max(longest,r-l+1)
        return longest