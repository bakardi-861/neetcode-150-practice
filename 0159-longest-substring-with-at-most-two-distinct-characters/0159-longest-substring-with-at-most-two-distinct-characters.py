class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        win = Counter()
        l = 0
        longest = 0
        size = 0
        for r in range(len(s)):
            win[s[r]] += 1
            size += 1
            while len(win) > 2:
                win[s[l]] -= 1
                if not win[s[l]]:
                    del win[s[l]]
                l += 1
                size -= 1
            longest = max(longest,size)
        return longest
            