class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #  0123456
        # "abcabc"
        #       r
        #     l
        # win = {a:1,b:1,c:1}
        # # if win == chars # keys == "abc"
        #     ans += 1 + ((len(s)-1) - r)
        #     ans = 10

        
        win = defaultdict(int)
        l = 0
        ans = 0
        chars = set(["a","b","c"])
        for r in range(len(s)):
            win[s[r]] += 1
            while set(win.keys()) == chars:
                ans += 1 + ((len(s)-1) - r)
                win[s[l]] -= 1
                if win[s[l]] == 0:
                    del win[s[l]]
                l += 1
        return ans


