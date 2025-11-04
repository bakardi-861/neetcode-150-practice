class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in win:
                win.remove(s[l])
                l += 1
                
            win.add(s[r])
            
            longest = max(longest,r-l+1)
        return longest