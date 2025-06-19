class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "ABAB"
        #  l
        #     r
        #  win = {"A":2,"B":2}
        #  minF = 2
        #  k = 2
        
        win = Counter()
        l = 0
        longest = 0
        min_f = 0
        for r in range(len(s)):
            win[s[r]] += 1
            # get minimum frequency
            min_f = min(win.values())
            while min_f > k:
                win[s[l]] -= 1
                l += 1
                # update min
                min_f = min(win.values())
            if min_f <= k:
                longest = max(longest,r-l+1)
        return longest

