class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AAAA"
        #  l
        #     r
        #  win = {"A":4}
        #  minF = 4
        #  k = 2
        # longest = 2
        
        win = Counter()
        l = 0
        longest = 0
        min_f = float("inf")
        max_f = -float("inf")
        for r in range(len(s)):
            win[s[r]] += 1
            max_f = max(max_f,win[s[r]])
            if (r-l+1) - max_f > k:
                win[s[l]] -= 1
                l += 1
            longest = max(longest,r-l+1)
        return longest

