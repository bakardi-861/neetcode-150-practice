class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        maxF = 0
        win = defaultdict(int)
        l = 0
        for r in range(len(s)):
            win[s[r]] += 1
            maxF = max(win.values()) # inefficient
            if (r-l+1) - maxF > k:
                win[s[l]] -= 1
                if win[s[l]] == 0:
                    del win[s[l]]
                l += 1
            ans = max(r-l+1,ans)
        return ans
            
           